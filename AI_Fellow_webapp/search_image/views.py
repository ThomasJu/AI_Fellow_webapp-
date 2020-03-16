from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import image_input

import pprint
from flickrapi import FlickrAPI
FLICKR_PUBLIC = '79fab41e5645d0b653338dba0b2430a0'
FLICKR_SECRET = 'f8cae0b2d1bae413'


def index(request):
    context = {'foo': 'bar'}
    return render(request, 'index.html', context)

def search_image(request):
    image_input = request.GET.get('image_input')

    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
    images = flickr.photos.search(text=image_input, per_page=5, extras=extras)
    photos = images['photos']
    photo_url = []
    
    pp = pprint.PrettyPrinter(indent=4)
    
    for picture in photos['photo']:
        photo_url.append([picture['url_m'], picture['title']])
    pp.pprint(photo_url)
    return render(request, 'image_input.html', context={'photo_url':photo_url})
