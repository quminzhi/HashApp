from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import App
from .tools.rexchecker import ReXChecker
from .tools.login import greet
from random import randrange
from .forms import ArtForm
import requests

def homeView(request):
    apps_two = App.objects.filter(page_no='two')
    apps_three = App.objects.filter(page_no='three')

    context = {
        'apps_two': apps_two,
        'apps_three': apps_three,
    }

    return render(request, 'app/home.html', context)

#  TODO: ReXChecker

def rexcheckerView(request):

    context = {
    }

    if (request.method == 'POST'):
        regex = request.POST['regex']
        samples = request.POST['samples']

        if (regex is None) or (samples is None):
            return HttpResponse("ValueError: fail to receive data")

        # begin to check
        pattern = regex
        test_samples = samples.splitlines()

        results = ReXChecker(pattern, test_samples)

        context = {
            'pattern': pattern,
            'results': results,
            'regex': regex,
            'samples': samples,
        }

    return render(request, 'app/rexchecker.html', context)

#  TODO: Login Demo

def loginView(request):
    page = 'Login'
    info = greet()

    context = {
        'page': page,
        'wallpaper_num': info['wallpaper_num'],
        'greet': info['greet'],
        'date': info['date'],
        'color_mode': info['color_mode'],
    }

    return render(request, 'app/login-register.html', context)

def registerView(request):
    page = 'Register'

    context = {
        'page': page,
    }

    return render(request, 'app/login-register.html', context)

def byteArtView(request):
    background_no = randrange(9)
    background_url = '../../static/app/images/byte-art/background/bg-' + str(background_no) + '.jpg'
    
    if (request.method == 'POST'):
        form = ArtForm(request.POST, request.FILES)    
        if (form.is_valid()):
            art = form.save(commit=False)
            art.origin_image = request.FILES['origin_image']
            art.style_image = request.FILES['style_image']
            art.save()
            
            # TODO: send request to API
            HOST = '18.118.24.63'
            PORT = '8000'
            data = {
                'uid': str(art.id),
                'origin': art.originImageURL,
                'style': art.styleImageURL
            }
            
            response = requests.post('http://' + HOST + ':' + PORT + '/api/stylizer/upload/', data)
            json = response.json()
            
            # TODO: render html
            origin_url = art.originImageURL
            style_url = art.styleImageURL
            stylized_url = 'http://' + HOST + ':' + PORT + json['stylized']
            
            allowDownload = True
            
            context = {
                'nickname': art.nickname,
                'email': art.email,
                'background_url': background_url,
                'origin_url': origin_url,
                'style_url': style_url,
                'stylized_url': stylized_url,
                'allow_download': allowDownload,
            }
            
            return render(request, 'app/byte-art.html', context)
    
    # local image, referred by static
    default_origin_url = '/static/app/images/byte-art/default-origin-1.jpg'
    default_style_url = '/static/app/images/byte-art/default-style-1.jpg'
    default_stylized_url = '/static/app/images/byte-art/stylized-1.jpg'
    allowDownload = False
    
    context = {
        'background_url': background_url,
        'origin_url': default_origin_url,
        'style_url': default_style_url,
        'stylized_url': default_stylized_url,
        'allow_download': allowDownload,
    }
        
    return render(request, 'app/byte-art.html', context)
