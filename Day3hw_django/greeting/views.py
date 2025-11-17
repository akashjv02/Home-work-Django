from django.shortcuts import render

def greeting(request):
    myobjct = [
        {'name' : 'John', 'grade' : 'A', 'status' : 'Passed'},
        {'name' : 'Akash', 'grade' : 'A', 'status' : 'Passed'},
        {'name' : 'Rony', 'grade' : 'B', 'status' : 'Failed'},
        {'name' : 'Raju', 'grade' : 'C', 'status' : 'Failed'}
    ]
    context = {'myobjct' : myobjct}
    return render(request, 'index.html', context)

def empty_list(request):
    myobjct = []   # Empty list
    return render(request, 'index.html', {'myobjct': myobjct})