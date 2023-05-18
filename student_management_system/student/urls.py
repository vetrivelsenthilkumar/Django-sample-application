from .views import StudentView
from .import views
from django.urls import path

urlpatterns = [
    path('student/', StudentView.as_view()),
    path('student/<int:id>/', StudentView.as_view()),
    path('student/<int:pk>/', views.GetStudentById, name='GetStudentById')
]