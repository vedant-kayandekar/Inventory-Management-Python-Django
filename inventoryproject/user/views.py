from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm , UserUpdateForm , ProfileUpdateForm
from .models import Profile
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
          form.save()
          user_name = form.cleaned_data.get('username')
          messages.success(request,f'{user_name} account is created ! Login now')
          return redirect('user-login')
    else:
       form = CreateUserForm()
    
  
    context = {
        'form': form,

    }
    return render(request,'user/register.html', context )


def profile(request):
   return render(request, 'user/profile.html')

# def settings(request):
#    user_profile = Profile.objects.get(user=request.staff)

#    if request.method == 'POST':

#       if request.FILES.get('image') == None:
#          image = user_profile.image
#          mobile_number = request.POST['phone']
#          user_address = request.POST['address']

#          user_profile.image = image
#          user_profile.phone = mobile_number
#          user_profile.address = user_address
#          user_profile.save()
#       if request.FILES.get('image') != None:
#          image = request.FILES.get('image')
#          phone = request.POST['phone']
#          address = request.POST['address']

#          user_profile.image = image
#          user_profile.phone = mobile_number
#          user_profile.address = user_address
#          user_profile.save()

#       return redirect('settings')
#    return render(request, 'settings.html',{'user_profile': user_profile})


def profile_update(request):
   if request.method == 'POST':
      user_form = UserUpdateForm(request.POST, instance=request.user)
      profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
      if user_form.is_valid and profile_form.is_valid():
         user_form.save()
         profile_form.save()
         return redirect('user-profile')
   else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = ProfileUpdateForm(instance=request.user.profile)

   context = {
    'user_form' : user_form,
    'profile_form' : profile_form
   }
   return render(request,'user/profile_update.html', context)