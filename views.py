from django.shortcuts import render

def base(request):
    return render(request, 'base/base.html')

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'about/about.html')

def cart(request):
    return render(request, 'cart/cart.html')

def profile(request):
    return render(request, 'profile/profile.html')

def contact(request):
    return render(request, 'contact/contact.html')

def products(request):
    return render(request, 'Products/products.html')

def charcoal(request):
    return render(request, 'Products/charcoal.html')

def oil(request):
    return render(request, 'Products/oil.html')

def food(request):
    return render(request, 'Products/food.html')

def kitchen(request):
    return render(request, 'Products/kitchen.html')

def submit(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the form data here (e.g., send an email)

        # Redirect to a thank you page
        return render(request, 'thankyou/thankyou.html')

def thank_you(request):
    return render(request, 'thankyou/thankyou.html')

def error(request, exception):
    return render(request, '404error/404error.html',  {'exception': exception})