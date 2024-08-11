from django.urls import path
from .views import HomePageView, RegisterView, LoginView

app_name = 'main'

urlpatterns = [
    path('a', HomePageView.as_view(), name="home"),
    path('', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),

]
