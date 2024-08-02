from django.template import loader
from django.http import HttpResponse
from .models import Member
# Create your views here.

def members(request):
    data = Member.objects.all().values()
    template = loader.get_template('index.html')
    content  = {
        'data' : data,
        'var' : "hello",
        'number' : 123,
    }
    return HttpResponse(template.render(content, request)) 