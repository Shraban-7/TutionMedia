from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import ListView, CreateView

from tuition.models import Country, Class
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, MemberShipForm
from .models import UserProfile, Membership

UserModel = get_user_model()


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ownerprofile')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registrations/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('/')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('registrations/accounts.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[send_email])
            email.send()
            messages.success(request, 'successfully crated account')
            messages.info(request, 'Activate your account from your provided mail')
            return redirect('login')
    else:
        form = SignUpForm
    return render(request, 'registrations/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'your account is activated now')
        return redirect('login')
    else:
        messages.warning(request, 'activation link is invalid')
        return redirect('signup')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, 'password successfully change')
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registrations/change_password.html', {'form': form})


def user_profile(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None
    if request.method == 'POST':
        if instance:
            form = UserProfileForm(request.POST, request.FILES, instance=instance)
        else:
            form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Successfully save your profile')
            return redirect('ownerprofile')
    else:
        form = UserProfileForm(instance=instance)
    context = {'form': form}
    return render(request, 'registrations/UserProfile.html', context)


def ownerProfile(request):
    user = request.user
    return render(request, 'registrations/userProfileView.html', {'user': user})


def updateprofile(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None
    username = request.user.username
    userp = User.objects.get(username=username)
    if request.method == 'POST':
        if instance:
            p_form = UserProfileForm(
                request.POST, request.FILES, instance=instance)
        else:
            p_form = UserProfileForm(request.POST, request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            profile_obj = p_form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            email = u_form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists() and userp.email != email:
                messages.warning(
                    request, 'Your Provided email is already in Use in another profile.')
                return redirect('ownerprofile')
            elif userp.email == email:
                u_form.save()
            else:
                user = u_form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('registrations/accounts.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email1 = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email1.send()
                messages.warning(
                    request, ' Email Changed. Temporarily Your accound has been deactivated.')
                messages.info(
                    request, 'Activate your account From your email address and only then you can login.')
                logout(request)
                return redirect('home')
            messages.success(request, 'Successfully updated.')
            return redirect('ownerprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=instance)
    userp = UserProfile.objects.filter(user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': request.user,
        'userp': userp
    }
    # redirect to a new URL:
    return render(request, 'registrations/updateprofile.html', context)


class Teacher_list(ListView):
    model = UserProfile
    template_name = 'registrations/userlist.html'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['district_area'] = Country.objects.all().order_by('name')
        context['prefer_class'] = Class.objects.all().order_by('name')
        context['user_profile'] = UserProfile.objects.all()
        return context


class MemberShip(LoginRequiredMixin, CreateView):
    model = Membership
    form_class = MemberShipForm
    template_name = 'registrations/membership.html'
    success_url = '/'


def filter(request):
    if request.method == "POST":
        district_area = request.POST['district_area']
        prefer_class = request.POST['prefer_class']
        if district_area or prefer_class:
            queryset = (Q(district_area__icontains=district_area)) | (
                Q(prefer_class__icontains=prefer_class))
            results = UserProfile.objects.filter(queryset).distinct()
        else:
            results = []
    numbers_list = range(1, 100000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'registrations/search.html', {'results': results,'numbers': numbers})
