from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def post_add(request):
    return render(request, 'content/post-add.html')

def post_edit(request):
    return render(request, 'content/post-edit.html')