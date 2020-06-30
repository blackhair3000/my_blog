from django.urls import path, re_path
from . import views

app_name = 'editor'

urlpatterns = [
    path('uploadImage/', views.upload_images, name="upload_image"),
    path('create/content/', views.create_content, name="create_content"),
    re_path('content/detail/(?P<src_id>[0-9]*)/$', views.display_content, name="display_content"),
]
