from django.urls import path
from . import views
urlpatterns=[
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("",views.home, name="home"),
    path("<str:product_label>", views.product, name="product_label")
       
]