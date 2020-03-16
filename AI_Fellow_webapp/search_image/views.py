from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import image_input
from flickrapi import FlickrAPI

FLICKR_PUBLIC = ""# FLICKER_PUBLIC_KEY
FLICKR_SECRET = ""# FLICKER_SECRET_KEY

# Index page with a search bar for user to search for images
def index(request):
    context = {'foo': 'bar'}
    return render(request, 'index.html', context)


# Using FlickrAPI to search image and let user enter the message wanted to be shown on the meme
def search_image(request):
    image_input = request.GET.get('image_input')

    # use FLICKRAPI to serach photos
    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
    images = flickr.photos.search(text=image_input, per_page=5, extras=extras)
    photos = images['photos']
    photo_url = []
    
    # create dictionary sended into webpage
    for picture in photos['photo']:
        photo_url.append([picture['url_m'], picture['title']])
        
    return render(request, 'image_input.html', context={'photo_url':photo_url})
