from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Create your views here.
def display(request):
    
    image_url = request.GET.get('image')
    text_input = request.GET.get('text_input')
    
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), text_input)
    img.save("meme.jpg", "JPEG")

    return render(request, 'display.html')

def download(request):
    print("where ewehr")
    return render(request, 'download.html')