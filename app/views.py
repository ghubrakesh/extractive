from django.shortcuts import render, redirect, HttpResponse
from .forms import ExtractedTextForm
from .notebook import image_to_text

def home(request):
    return HttpResponse("hello There")

def upload_image(request):
    if request.method == 'POST':
        form = ExtractedTextForm(request.POST, request.FILES)
        if form.is_valid():
            extracted_text = image_to_text(request.FILES['image'])
            form.instance.text = extracted_text
            form.save()
            return render(request, 'display.html', extracted_text)
    else:
        form = ExtractedTextForm()
    return render(request, 'upload.html', {'form': form})