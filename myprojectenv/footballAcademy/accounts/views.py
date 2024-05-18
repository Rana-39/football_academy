# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, UpdateBioForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        academy_code = form.cleaned_data['academy_code']
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
    players = CustomUser.objects.filter(role='player')
    coaches = CustomUser.objects.filter(role='coach')
    context = {'players': players, 'coaches': coaches}
    return render(request, 'accounts/listOfPlayers.html', context)

@login_required
def update_bio(request):
    if request.method == 'POST':
        form = UpdateBioForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Adjust the redirect to the appropriate profile view
    else:
        form = UpdateBioForm(instance=request.user)
    return render(request, 'accounts/update_bio.html', {'form': form})