from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.shortcuts import redirect


# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html')

@login_required
def update_profile(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile/update_profile.html', {'form': form})