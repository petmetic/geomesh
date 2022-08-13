from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/<str:uuid>/', views.report, name='report'),
    path('download/,<str:uuid>/', views.download, name='download'),
]