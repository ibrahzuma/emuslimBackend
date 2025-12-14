from django.http import JsonResponse
from django.conf import settings

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check API routes, exclude admin/dashboard
        if request.path.startswith('/api/'):
            api_key = request.headers.get('X-Api-Key')
            if api_key != settings.API_KEY_SECRET:
                return JsonResponse({'error': 'Unauthorized: Invalid API Key'}, status=401)

        return self.get_response(request)
