from django.urls import path

from . import views

urlpatterns = [
    path('webhook', views.webhook, name='webhook'),
    # path('/check',views.check_for_msg)
]