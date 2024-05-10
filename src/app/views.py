from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task

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
    tasks = Task.objects.filter(user=request.user, completed=False)
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'listings.html', {'tasks': tasks, 'completed_tasks': completed_tasks})


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


def add_task(request):
    """Adds a task to the database.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirects to the listings-page after adding the task
    """

    if request.method == 'POST':

        task_description = request.POST.get('description')
        task = Task(user=request.user, task=task_description)

        try:
            task.save()
            print('Task added to the database successfully')
            return redirect('listings_view')

        except Exception as error:
            messages.error(request, str(error))
            print('Error creating task:', str(error))
            return redirect('listings_view')

    return redirect('listings_view')


def edit_task(request):
    """Edits a task in the database.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirects to the listings-page after editing the task
    """

    if request.method == 'POST':

        task_id = request.POST.get('task_id')
        new_task_description = request.POST.get('new_task_description')
        task = Task.objects.get(id=task_id)
        task.task = new_task_description

        try:
            task.save()
            print('Task edited successfully')
            return redirect('listings_view')

        except Exception as error:
            messages.error(request, str(error))
            print('Error editing task:', str(error))
            return redirect('listings_view')

    return redirect('listings_view')


def add_task_to_complete(request):
    """Adds a task to the completed tasks of the logged-in user.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirect to the listings-page after adding the task
        to the completed tasks
    """

    if request.method == 'POST':

        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = True

        try:
            task.save()
            print('Task added to completed tasks successfully')
            return redirect('listings_view')

        except Exception as error:
            messages.error(request, str(error))
            print('Error completing task:', str(error))
            return redirect('listings_view')

    return redirect('listings_view')


def delete_task(request):
    """Deletes a task from the database.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirects to the listings page
        after deleting the task
    """

    if request.method == 'POST':

        task_id = request.POST.get('task_id')
        Task.objects.filter(id=task_id).delete()
        return redirect('listings_view')

    return redirect('listings_view')


def clear_listed_task(request):
    """Clears all the listed tasks of the logged-in user.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirects to the listings page
        after clearing all tasks
    """

    if request.method == 'POST':
        Task.objects.filter(user=request.user, completed=False).delete()
        return redirect('listings_view')

    return redirect('listings_view')


def clear_completed_task(request):
    """Clears all completed tasks of the logged-in user.

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Redirects to the listings page after clearing
        all completed tasks
    """

    if request.method == 'POST':
        Task.objects.filter(user=request.user, completed=True).delete()
        return redirect('listings_view')

    return redirect('listings_view')
