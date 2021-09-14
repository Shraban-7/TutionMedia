$("#id_country").change(function () {
      var url = $("#personForm").attr("data-cities-url");
      var countryId = $(this).val();

      $.ajax({
        url: url,
        data: {
          'country': countryId
        },
        success: function (data) {
          $("#id_city").html(data);
        }
      });

    });