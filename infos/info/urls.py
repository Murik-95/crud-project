from django.urls import path
from . import views
from .api_views import PersonListAPIView, PersonDetailAPIView


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),

    # API
    path('api/people/', PersonListAPIView.as_view()),
    path('api/people/<int:pk>/', PersonDetailAPIView.as_view()),
]
