#date: 2018/12/3

from main import views

urlpatterns = [
    path('login/', views.login),
    path('password/', views.password),


]