# Todo-List Web Application

### Description:

- This project is a Todo-list web application designed to help users manage their daily tasks.
- Created using Python with Django for backend and JS, HTML and CSS for a simple, minimalistic frontend.
- The project has a base setup for MySQL database that is commented out. Default database is SQLite3 provided by Django.

### Intented Features:

- User registration
- Task management; Creation, Viewing, Editing and Deleting of tasks
- Basic UI, with simple CSS
- Persistent data storage; Either Django's base SQLite3 or MySQL that has a base for it setup in settings.py (commented out)
- ~~Testing; Unittests; using Django's built-in 'TestCase' class - possibly intergration tests~~ No tests in this project

### Setup:

Clone the project "git clone https://github.com/Tartsi/todoapp"

Install Poetry dependencies

```bash
poetry install
```

Enter poetry shell

```bash
poetry shell
```

### Usage

- Create a user on the registration page that meets the necessary requirements
- Login with the created user
- Now you can add, edit, delete or clear tasks as you wish!
- Logout when done