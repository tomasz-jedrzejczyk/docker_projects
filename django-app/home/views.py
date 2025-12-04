# Add this to your main app (e.g. main/views.py). If you already have views.py,
# merge the custom_404 function into it.
import logging
from django.shortcuts import render
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def custom_404(request, exception):
    """
    Custom 404 handler:
    - Returns JSON when the client requests JSON (API usage).
    - Returns an HTML page for browsers.
    - Logs minimal info for debugging (path, remote addr, user-agent, optional request id).
    """
    # Minimal logging (avoid storing sensitive data)
    request_id = request.headers.get('X-Request-ID') or request.META.get('HTTP_X_REQUEST_ID')
    logger.info(
        "404 Not Found: path=%s remote_addr=%s user_agent=%s request_id=%s",
        request.path,
        request.META.get('REMOTE_ADDR'),
        request.META.get('HTTP_USER_AGENT'),
        request_id,
    )

    # If client prefers JSON, return JSON error payload
    accept = request.headers.get('Accept', '')
    if 'application/json' in accept:
        payload = {
            "code": "not_found",
            "status": 404,
            "message": "Resource not found",
            "path": request.path,
        }
        if request_id:
            payload["request_id"] = request_id
        return JsonResponse(payload, status=404)

    # Otherwise render the 404 HTML template
    return render(request, "404.html", {"request_path": request.path, "request_id": request_id}, status=404)
