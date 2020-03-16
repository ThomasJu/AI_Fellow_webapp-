from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from django.utils.encoding import smart_str

# Display the memes created by users
def display(request):
    
    # fetch the items receive from last webpages
    image_url = request.GET.get('image')
    text_input = request.GET.get('text_input')
    
    # combine the text users created into the photo
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), text_input)
    img.save("meme.jpg", "JPEG")

    return render(request, 'display.html')

# allow users download the meme
def download(request):
    '''
    some code that performs download features
    '''
    return render(request, 'download.html')