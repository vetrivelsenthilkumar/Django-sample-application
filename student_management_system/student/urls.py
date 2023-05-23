from .views import StudentView
from .import views
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('student/', StudentView.as_view()),
    path('student/update/<int:id>/', StudentView.as_view()),
    path('student/<int:pk>/', views.GetStudentById, name='GetStudentById'),
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view())
]