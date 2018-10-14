from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm


def SaveProfile(request):
    saved = False

    if request.method == 'POST':
        # get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        # if request.FILES is not added as a parameter, form validation will fail with an 'empty picture' message

        if MyProfileForm.is_valid():
            profile = Profile() # initialize an instance of profile model
            profile.location = MyProfileForm.cleaned_data['location']
            profile.picture = MyProfileForm.cleaned_data['picture']
            profile.save()
            saved = True
        else:
            MyProfileForm = ProfileForm()
        return render(request, 'saved.html', locals())

        

