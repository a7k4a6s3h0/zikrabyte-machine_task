from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .validate_userdetails import Validate_data
# Create your views here.

User = get_user_model()

def user_redister(request):

    if request.user.is_authenticated:
        return redirect("sucess")

    if request.method == 'POST':

        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        
        if password_1 == password_2:

            
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            username = first_name + ' ' + last_name

            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists!')

            else:

                output_dict = Validate_data(email=email, password=password_2).validate_all()

                if not output_dict['all_correct']:
                    output_dict.pop('all_correct')
                    return render(request, 'error.html', {'error_message': output_dict})
                    
                User.objects.create_user(username=username, password=password_1, last_name = last_name, first_name = first_name, email = email)
                print('user created')
                messages.success(request, "Sucessfully registered")
                return redirect('login')
            
        messages.error(request, "Both Password Not Matching.....!!!")
        return redirect('register')    

    return render(request, 'index.html')


def sucess_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    return render(request, 'sucess.html', {'user':request.user})



def login_view(request):

    if request.user.is_authenticated:
        return redirect("sucess")
    
    if request.method == 'POST':

        password_1 = request.POST.get('password_1')
        username = request.POST.get('username')

        user = authenticate(request, username=username, password = password_1)

        if user:
            login(request, user)
            messages.success(request,'sucessfully logined')
            return redirect('sucess')
        messages.error(request,"Invalid Crediebtaials....!!!")
        return redirect('login')  
      
    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('login')