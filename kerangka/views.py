from turtle import title
from django.shortcuts import render,HttpResponse,redirect
from django.http import FileResponse
#from kerangka.models import EmpInsert
from django.contrib import messages
from .models import EmpInsert

import time
# from .models import MyTable

# Create your views here.
# def awal(request):
#     return HttpResponse('berhasil instal')

def Home(request):
    context ={
        'title':title
    }
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'home.html', param)
    else:
        return redirect('login')
    
    return render(request,'login.html', context)
   
    #return render(request,'home.html', context)

def Produk(request):
    context ={
        'title':title
    }
   
    return render(request,'produk.html', context)



def Registrasi(request):
    context ={
        'title':title
    } 
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        typeuser = request.POST.get('typeuser')
        password = request.POST.get('password')
        
        if username and email and password:
            # Check if the username already exists
            check_user = EmpInsert.objects.filter(username=username).exists()
            if not check_user:
                saverecord = EmpInsert()
                saverecord.username = username
                saverecord.email = email
                saverecord.typeuser = typeuser
                saverecord.password = password
                
                saverecord.save()
                
                messages.success(request, 'User registered successfully.')
                return render(request, 'registrasi.html', context)
            else:
               
                messages.error(request, 'Username already exists.')
                return render(request, 'registrasi.html',context) 
        else:
            messages.error(request, 'Please provide all the required fields.')
            return render(request, 'registrasi.html', context)  # Provide the context
    else:
        print("Request method is not POST.")
        return render(request, 'registrasi.html', context)  # Provide the context

    


            
            


def Login(request):
    context ={
        'title':title
    }
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print(uname)
        check_user = EmpInsert.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            print("berhasil")
            return redirect('home')
            #return render(request,'home.html', context)
            
        else:
            print("gagal")
            messages.error(request, 'Gagal Login')
            
    return render(request,'login.html', context)

def logout(request):
    context ={
        'title':title
    }
    try:
        del request.session['user']
    except:
         return redirect('login')
    return redirect('login')



# Call the function with an argument

