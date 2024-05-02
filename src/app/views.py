from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

User = get_user_model()


def index(request):
    """Return the index-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'index.html' template
    """

    return render(request, 'index.html')


def register(request):
    """Returns the registration-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'register.html' template
    """

    return render(request, 'register.html')


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


def login_user(request):
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
                login(request, user)
                return render(request, 'listings.html')

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
