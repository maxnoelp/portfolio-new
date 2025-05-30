from django.urls import path

from portfolio.landingpage.views import contact_view
from portfolio.landingpage.views import landing_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("kontakt/", contact_view, name="contact"),
]
