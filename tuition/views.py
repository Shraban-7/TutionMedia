from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from tuition.forms import TuitionPostForm
from tuition.models import TuitionPost, Country, Subject, Class, Medium, City, Feedback
from django.db.models import Q, query


class TuitionPostCreateView(CreateView):
    model = TuitionPost
    form_class = TuitionPostForm
    # fields = ''
    template_name = 'tuition/TuitionPostCreate.html'
    success_url = '/'


class TuitionListView(ListView):
    model = TuitionPost
    template_name = 'tuition/TuitionPostList.html'
    ordering = ['-created_at']
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['countrys'] = Country.objects.all().order_by('name')
        context['classes'] = Class.objects.all().order_by('name')
        return context


class TuitionDetailView(LoginRequiredMixin, DetailView):
    model = TuitionPost
    template_name = 'tuition/TuitionPostDetail.html'


class Home(TemplateView):
    template_name = 'base.html'


def search(request):
    if request.method == "POST":
        district = request.POST['country_i']
        classes = request.POST['class_i']
        if district or classes:
            queryset = (Q(country__name__icontains=district)) | (
                Q(class_other__icontains=classes))
            results = TuitionPost.objects.filter(queryset).distinct()
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
    return render(request, 'tuition/filter.html', {'results': results, 'numbers': numbers})


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'tuition/city_dropdown_list_options.html', {'cities': cities})


class Feedback_view(CreateView):
    model = Feedback
    fields = ['author_email', 'feed_details']
    template_name = 'tuition/Contact.html'
    success_url = '/Contact'
