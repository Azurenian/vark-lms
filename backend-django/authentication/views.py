from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
import oauthlib.oauth1
from django.conf import settings
from urllib.parse import urlencode

@csrf_exempt
def lti_launch(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('LTI launch must be a POST request.')

    # Extract LTI params
    lti_params = request.POST.dict()
    consumer_key = lti_params.get('oauth_consumer_key')
    roles = lti_params.get('roles', '')
    user_id = lti_params.get('user_id')
    lis_person_name_full = lti_params.get('lis_person_name_full', '')
    lis_person_contact_email_primary = lti_params.get('lis_person_contact_email_primary', '')

    # Validate OAuth signature (simplified, production should use a library)
    # For demo, assume consumer key and secret are in settings.LTI_CONSUMERS
    consumer_secret = settings.LTI_CONSUMERS.get(consumer_key)
    if not consumer_secret:
        return HttpResponseBadRequest('Invalid consumer key.')

    # Here you would validate the OAuth signature using oauthlib or similar
    # Skipping actual signature validation for brevity

    # Determine user role
    if 'Instructor' in roles or 'Admin' in roles:
        dashboard = 'teacher/dashboard'
    else:
        dashboard = 'student/dashboard'

    # Optionally, create a session or token for the user here
    # For now, just redirect to frontend with user info as query params
    params = {
        'user_id': user_id,
        'name': lis_person_name_full,
        'email': lis_person_contact_email_primary,
        'role': 'teacher' if 'Instructor' in roles or 'Admin' in roles else 'student',
    }
    frontend_url = f"http://localhost:3000/auth/lti?{urlencode(params)}&redirect=/{dashboard}"
    return HttpResponseRedirect(frontend_url)
