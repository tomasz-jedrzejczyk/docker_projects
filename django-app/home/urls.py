from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Serve the app's index page using a simple TemplateView.
    path('', TemplateView.as_view(template_name='home/index.html'), name='home-index'),
]
