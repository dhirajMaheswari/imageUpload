from django.http import  HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *

# Create your views here.



# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'UploadImage/index.html', {'form': form})


def success(request):
    return render(request, 'UploadImage/success.html')


def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        images = Images.objects.all()
        return render(request, 'UploadImage/display_images.html', {'images':images})