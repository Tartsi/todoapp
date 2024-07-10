# Todo-List Web Application

### Description:

- This project is a Todo-list web application designed to help users manage their daily tasks.
- Created using Python with Django for backend and JS, HTML and CSS for a simple, minimalistic frontend.
- Default database is SQLite3 provided by Django, but the project has a base setup for MySQL database that is commented out. .

### Intented Features:

- User registration
- Task management; Creation, Viewing, Editing and Deleting of tasks
- Basic UI, with simple CSS
- Persistent data storage; Either Django's base SQLite3 or MySQL that has a base for it setup in settings.py (commented out)
- No tests in this project

### Install:

Clone the project "git clone https://github.com/Tartsi/todoapp"

Install Poetry dependencies

```bash
poetry install
```

Enter poetry shell

```bash
poetry shell
```
### Setup:

Create and setup your .env-file where you declare:

- DEBUG = True
- SECRET_KEY = yoursecretkeyhere
- (Optional MySQL database setup files)

Run migrations

```bash
python/python3 manage.py makemigrations
then
python/python3 manage.py migrate
```

Run the server

```bash
python/python3 manage.py runserver
```

Now you can use the application!

### Usage

- Create a user on the registration page that meets the necessary requirements
- Login with the created user
- Now you can add, edit, delete or clear tasks as you wish!
- Logout when done
