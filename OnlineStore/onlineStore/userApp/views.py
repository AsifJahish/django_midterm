from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, BuyerProfileForm, SellerProfileForm
from .models import Buyer, Seller

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'buyer':
                user.is_buyer = True
            elif user_type == 'seller':
                user.is_seller = True
            user.save()
            if user.is_buyer:
                Buyer.objects.create(user=user)
            elif user.is_seller:
                Seller.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    # Determine the user type and instantiate the appropriate profile form
    if request.user.is_buyer:
        profile_form = BuyerProfileForm(instance=request.user.buyer)
    elif request.user.is_seller:
        profile_form = SellerProfileForm(instance=request.user.seller)
    else:
        return redirect('profile')  # Redirect if user type is not identified

    if request.method == 'POST':
        # Re-instantiate the profile form with POST data
        if request.user.is_buyer:
            profile_form = BuyerProfileForm(request.POST, instance=request.user.buyer)
        else:
            profile_form = SellerProfileForm(request.POST, instance=request.user.seller)

        if profile_form.is_valid():
            profile_form.save()  # Save the updated profile
            return redirect('profile')  # Redirect to profile after update

    context = {
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def dashboard(request):
    if request.user.is_buyer:
        return render(request, 'users/buyer_dashboard.html')
    elif request.user.is_seller:
        return render(request, 'users/seller_dashboard.html')
    else:
        return redirect('profile')




def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        # Log in the user
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the profile or another page
    return render(request, 'users/login.html', {'form': form})
