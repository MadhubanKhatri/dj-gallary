from django.urls import path
from . import views



urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('upload/', views.UploadView.as_view(), name='upload'),
	path('delete/<int:id>/', views.DeleteView.as_view(), name='delete_img')
]