from django.urls import path
from hello_app.views import HelloWorldView, HelloView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='home'),
    path('hello/<name>', HelloView.as_view(), name='personalized hello')
]
