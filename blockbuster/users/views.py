from django.shortcuts import redirect, render
from .forms import UserSignupForm

import pdb

# Create your views here.
def signup(request):
    if request.method == 'POST':
        new_user = UserSignupForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('index')
    else:
        form = UserSignupForm()
        context = { "form": form }
        return render(request, 'users/signup.html', context)        