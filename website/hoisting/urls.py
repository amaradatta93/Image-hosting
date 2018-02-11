from django.conf.urls import url

from . import views

app_name = 'hoisting'

urlpatterns = [
    url(r'^upload/', views.save_image, name='upload'),
    url(r'^get/(?P<id>[0-9]+)/$', views.get_image_by_id, name='image_by_id'),
    url(r'^<int:width>/<int:height>/', views.get_image_by_resolution, name='image_by_resolution')
]
