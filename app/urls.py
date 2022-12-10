from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

from app import views
from app.views import SignUpView

urlpatterns = [
    path('', views.qr, name="qr"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('profile/', views.profile, name="profile"),
]
