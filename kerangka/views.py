from turtle import title
from django.shortcuts import render,HttpResponse,redirect
from django.http import FileResponse
#from kerangka.models import EmpInsert
from django.contrib import messages
from .models import EmpInsert
from django.core.paginator import Paginator
from django.db import connection

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
        context['current_user'] = current_user  # Add current_user to the context dictionary
        
        try:
            user = EmpInsert.objects.get(username=current_user)
            context['email'] = user.email
        except EmpInsert.DoesNotExist:
            # Handle the case where the user does not exist in the database
            context['email'] = None
        
        return render(request, 'home.html', context)
    else:
        return redirect('login')
    
    return render(request,'login.html', context)
   
    #return render(request,'home.html', context)

def Produk(request):
    context ={
        'title':title
    }
   
    return render(request,'produk.html', context)

def Scheduler(request):
    context ={
        'title':title
    }
    if 'user' in request.session:
        current_user = request.session['user']
        context['current_user'] = current_user  # Add current_user to the context dictionary
        try:
            user = EmpInsert.objects.get(username=current_user)
            context['email'] = user.email
        except EmpInsert.DoesNotExist:
            # Handle the case where the user does not exist in the database
            context['email'] = None
        with connection.cursor() as cursor:
            cursor.execute("select * from ms_projek_python")
            columns = [col[0] for col in cursor.description]
            listjob = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        records_per_page = 3
        paginator = Paginator(listjob, records_per_page)
        page_number = request.GET.get('page')
        listjob = paginator.get_page(page_number)
        
        max_page_count = 3
        num_pages = paginator.num_pages
        current_page = listjob.number
         
        if num_pages <= max_page_count:
            page_range = range(1, num_pages + 1)
        else:
            half_max = max_page_count // 2
            if current_page <= half_max:
                page_range = range(1, max_page_count + 1)
            elif current_page >= num_pages - half_max:
                page_range = range(num_pages - max_page_count + 1, num_pages + 1)
            else:
                page_range = range(current_page - half_max, current_page + half_max + 1)
                
        context['listjob'] = listjob
        context['page_range'] = page_range 

        
        return render(request, 'jobscheduler.html', context)
    else:
        return redirect('login')

def Listjobrunning(request):
    context ={
        'title':title
    } 
    if 'user' in request.session:
        current_user = request.session['user']
        context['current_user'] = current_user  # Add current_user to the context dictionary
        try:
            user = EmpInsert.objects.get(username=current_user)
            context['email'] = user.email
        except EmpInsert.DoesNotExist:
            # Handle the case where the user does not exist in the database
            context['email'] = None
        with connection.cursor() as cursor:
            cursor.execute("select * from ms_log_python_rekon")
            columns = [col[0] for col in cursor.description]
            listjob = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        records_per_page = 8
        paginator = Paginator(listjob, records_per_page)
        page_number = request.GET.get('page')
        listjob = paginator.get_page(page_number)
        
        max_page_count = 3
        num_pages = paginator.num_pages
        current_page = listjob.number
         
        if num_pages <= max_page_count:
            page_range = range(1, num_pages + 1)
        else:
            half_max = max_page_count // 2
            if current_page <= half_max:
                page_range = range(1, max_page_count + 1)
            elif current_page >= num_pages - half_max:
                page_range = range(num_pages - max_page_count + 1, num_pages + 1)
            else:
                page_range = range(current_page - half_max, current_page + half_max + 1)
                
        context['listjob'] = listjob
        context['page_range'] = page_range 
        return render(request, 'listjobrunning.html', context)
    else:
        return redirect('login')
    


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
        try:
            user = EmpInsert.objects.get(username=uname, password=pwd)
        except EmpInsert.DoesNotExist:
            user = None

        if user:
            # If the user exists, store the username and email in the session
            request.session['user'] = user.username
            request.session['email'] = user.email
            print("berhasil")
            return redirect('home')
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

