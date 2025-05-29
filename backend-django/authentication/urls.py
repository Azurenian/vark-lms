from django.urls import path
from .views import lti_launch

urlpatterns = [
    path('lti/launch/', lti_launch, name='lti_launch'),
]
