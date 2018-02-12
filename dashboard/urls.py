from django.conf.urls import url
from django.views.generic import TemplateView

import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/', TemplateView.as_view(template_name='add_image.html'), name='add_image'),
]
