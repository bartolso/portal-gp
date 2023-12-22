from django.shortcuts import render

def elections(request):
    return render(request, 'elections/elections.html', {})

def oct29(request):
    return render(request, 'elections/29oct.html', {})