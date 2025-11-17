from django.shortcuts import render

def greeting(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        favcolor = request.POST.get('favcolor')
        
        return render(request, 'result.html', {
            'form_data': request.POST,
            'name': name,
            'favcolor': favcolor
        })
     
    return render(request, 'index.html')
