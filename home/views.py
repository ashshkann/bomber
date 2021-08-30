from django.shortcuts import render
from .models import header_site, about_site, copy_right
# Create your views here.
def homePage(request):
    data_header = header_site.objects.all()
    data_bodys = about_site.objects.all()
    data_copy_right = copy_right.objects.all()
    context = {
        'data_header': data_header,
        'data_bodys': data_bodys,
        'data_copy_right': data_copy_right,
    }
    return render(request, 'pages/home.html', context)

def done_attack(request):

    context = {

    }
    return render(request, "pages/done_attack.html", context)