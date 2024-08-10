from django.shortcuts import render, redirect
from .models import User
from django.http import JsonResponse

# Create your views here.
def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        User.objects.create(name=name, username=username, email=email)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect('dashboard')
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('dashboard')