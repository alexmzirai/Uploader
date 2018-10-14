from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^profile/', TemplateView.as_view(template_name='profile.html')), # interesting :)
    url(r'^saved/', views.SaveProfile, name='saved'),

]
