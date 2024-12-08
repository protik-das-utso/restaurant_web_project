from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'index.html')
def BookTableView(request):
    return render(request, 'book.html')
def MenuView(request):
    return render(request, 'menu.html')
def AboutView(request):
    return render(request, 'about.html')