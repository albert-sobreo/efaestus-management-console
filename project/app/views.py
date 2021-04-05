from django import views
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from .serializers import *

# Create your APIs here.

class UserAPI(viewsets.ModelViewSet):
    serializer_class = UserSZ
    queryset = User.objects.all()

class WorkAPI(viewsets.ModelViewSet):
    serializer_class = WorkSZ
    queryset = Work.objects.all()

class WorkNestedAPI(viewsets.ModelViewSet):
    serializer_class = WorkNestedSZ
    queryset = Work.objects.all()

class UnfinishedWorkAPI(viewsets.ModelViewSet):
    serializer_class = WorkSZ
    queryset = Work.objects.filter(status__in=['Pending', 'In Progress'])

class BugNestedAPI(viewsets.ModelViewSet):
    serializer_class = BugNestedSZ
    queryset = Bug.objects.all()

class BugAPI(viewsets.ModelViewSet):
    serializer_class = BugSZ
    queryset = Bug.objects.all()

class UnresolvedBugAPI(viewsets.ModelViewSet):
    serializer_class = BugSZ
    queryset = Bug.objects.filter(status='Unresolved')


# Create your views here.

def test(request):
    return render(request, 'template.html')

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('/login/')
        else:
            return render(request, 'register.html', {"form": form})

@login_required
def homeView(request):
    return render(request, "home.html")

def logoutView(request):
    logout(request)
    return redirect('/')