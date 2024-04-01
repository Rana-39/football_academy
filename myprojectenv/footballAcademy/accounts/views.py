from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('profile')  # Redirect to profile page after successful signup
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        academy_code = form.cleaned_data['academy_code']
        # Check if the academy code matches the valid code for the academy
        if academy_code == 'LadersGood':
            return super().form_valid(form)
        else:
            form.add_error('academy_code', 'Invalid academy code. Please contact the academy for the correct code.')
            return self.form_invalid(form)

@login_required
def profile(request):
    user = request.user
    players = CustomUser.objects.exclude(id=user.id).filter(is_staff=False)
    coaches = CustomUser.objects.filter(is_staff=True)
    context = {'user': user, 'players': players, 'coaches': coaches}
    return render(request, 'accounts/profile.html', context)

def listOfPlayers(request):
    players = CustomUser.objects.exclude(is_staff=True)
    coaches = CustomUser.objects.filter(is_staff=True)
    context = {'players': players, 'coaches': coaches}
    return render(request, 'accounts/listOfPlayers.html', context)
