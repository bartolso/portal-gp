from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión.")
            
            return redirect('home')
        else:
            messages.error(request, "Ha habido un problema. Comprueba los datos.")
            return redirect('login')
    
    else:
        return(render(request, 'users/login.html', {}))
    
def logout_user(request):
    logout(request)
    messages.info(request, "Has cerrado la sesión.")
    return redirect('home')

def user(request):
    user = request.user
    return render(request, 'users/user.html', {'user': user})