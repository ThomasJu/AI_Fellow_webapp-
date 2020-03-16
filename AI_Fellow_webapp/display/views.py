from django.shortcuts import render

# Create your views here.
def display(request):
    
    # images = request.GET.get('images')
    text_input = request.GET.get('text_input')
    
    # print(images)
    print(text_input)
    
    context = {'foo': 'bar'}
    return render(request, 'display.html', context)