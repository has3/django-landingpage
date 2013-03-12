from django.conf.urls import patterns, include, url
from landingpage.models import LandingPageForm
from django.views.generic.base import TemplateView
from landingpage.views import NewCreateView

urlpatterns = patterns('',
    url(r'^$', NewCreateView.as_view(
        model=LandingPageForm,
        success_url="thankyou")),
    url(r'^thankyou/$', TemplateView.as_view(
        template_name="landingpage/thankyou.html")),
)