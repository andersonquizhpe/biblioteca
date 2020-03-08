from django.shortcuts import render, render_to_response
#path('', include('apps.home.urls'), name='home_page'),
# Create your views here.
def homePage(request):
    return render_to_response ('user/login.html')