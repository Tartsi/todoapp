from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required

User = get_user_model()


def login(request):
    """Return the index-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'index.html' template
    """

    if 'next' in request.GET:
        return render(request, 'index.html', {'login_first': True})

    return render(request, 'index.html')


def register_view(request):
    """Returns the registration-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'register.html' template
    """

    return render(request, 'register.html')


def login_view(request):
    """Logins a registered user to the application.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Returns login-page with error messages if
        login unsuccessful, else returns todo-page of the user
    """

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('listings_view')

            # Show appropriate error messages if login unsuccessful
            messages.error(request, "Invalid username or password")
            return render(request, 'index.html', {'form': form})

        # Show appropriate error messages if login unsuccessful
        for field in form.errors:
            for error in form.errors[field]:
                messages.error(request, error)

        return render(request, 'index.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url='login')
def listings_view(request):
    """Renders the listings page with all the tasks of the logged-in user.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'listings.html' template
        with the tasks of the logged-in user
    """

    # Retrieve all tasks of the logged-in user
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'listings.html', {'tasks': tasks})


def add_user(request):
    """Adds a user to the database.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the appropriate
        page regarding the outcome of the registration process
    """

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            try:

                form.save()
                return render(request, 'index.html', {'created': True})

            except Exception as error:

                messages.error(request, str(error))
                print('Error creating account', str(error))
                return render(request, 'register.html', {'form': form})
        else:

            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, error)

            return render(request, 'register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
