from django.shortcuts import render
from .form import LoginForm

def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'thankyou.html',{
                'name' : form['fullname'].value
                
            })
    return render(request,'index.html')