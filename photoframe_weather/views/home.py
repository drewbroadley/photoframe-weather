from django.template.response import TemplateResponse

def home(request):
    home = TemplateResponse(request, 'home.html', {})
    return home
