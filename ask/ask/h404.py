from django.http import Http404

def r404(request, *args, **kwargs):
    raise Http404
