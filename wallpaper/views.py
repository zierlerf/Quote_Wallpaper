from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Font
from main import ImageCreator
from os import path
from django.conf import settings
# Create your views here.
def index(request):
    width = 750
    height = 1334
    font = Font.objects.get(id=1)
    text = 'Hello'
    if request.method == 'POST':
        if request.POST.get('width') != "":
            width = int(request.POST.get('width'))
        if request.POST.get('height') != "":
            height = int(request.POST.get('height'))
        font = Font.objects.get(name=request.POST.get('font'))
        text = request.POST.get('text')
    ic = ImageCreator(width,height,text,font.path)
    ic.createImage()
    font_list = Font.objects.all()
    template = loader.get_template('wallpaper/index.html')
    context = RequestContext(request,{
        'font_list': font_list,
        'img_path': 'pictures/pic.png',
    })
    return HttpResponse(template.render(context))