from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('update/<str:pk>/', views.update, name="update"),
    path('disupdate/<str:pk>/', views.disupdate, name="disupdate"),
    path('create/', views.create, name="create"),
    path('sec/', views.sec, name="sec"),
    path('area/<str:pk>/', views.area, name="area"),
    path('startsec/<str:pk>/', views.startsec, name="startsec"),
    path('about/<str:pk>/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('started/', views.started, name="started"),
	path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)