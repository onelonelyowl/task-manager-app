# todos
let users add bio to their page but not required on registration
add phone styling
add pagination to main list page and maybe to comments too
make a requirements txt so people can reproduce the venv
add an account info page - with options to update stuff like username etc
add profile view for public view where you cannot change details etc
***teh two above can be the same, just show an edit button if its ur page
add tests
get a custom font
add an archiving features/complete button, ways to filter by already completed tasks
css/styling/beautify
only let users update their own tasks -- done - needs better error handling clientside
how to make create/update page have real date selection things  ---- done
add user authentication/multiple users, tracks what tasks are created by who -- done
add user registration page -- done
display due date on main page -- done
add comments to each specific task -- done
need to update createview to handle users who arent logged in -- done
add exception handling -- turns out it is just easier to restrict what the user can do




registration page taken from https://learndjango.com/tutorials/django-signup-tutorial

# task-manager-app

To practise what you have learned each day, you could build a task manager application:

    Create a task manager application where users can register, log in, and manage their tasks.
    Implement features such as creating tasks, assigning priorities, setting due dates, and marking tasks as complete.
    Use Django's authentication framework for user registration and login, and leverage Django's models and forms for task management.

Here are some things you could do for each section of the plan to put your learning into practise:
1. Setup and Project Structure

    Set up a new Django project using the django-admin startproject command.
    Create a new Django app within your project using the python manage.py startapp command.
    Define the basic project structure and configure the necessary settings.

2. Models and Databases

    Define a model for tasks in your app's models.py file, including fields like title, description, priority, due date, etc.
    Generate and apply migrations to create the database table for the tasks model.
    Implement basic database operations like creating, retrieving, updating, and deleting tasks using Django's ORM.

3. Views and Templates

    Create a view function to handle displaying a list of tasks.
    Design and implement a template to render the list of tasks using Django's template system.
    Update the view function to pass the list of tasks to the template context and render it.

4. Forms and User Authentication

    Create a form for adding new tasks in your app's forms.py file.
    Implement a view function to handle the form submission and create a new task.
    Implement user authentication using Django's authentication framework for user registration and login.

5. Advanced Functionality and Refinement

    Enhance the task manager with additional features like task editing, marking tasks as complete, and filtering tasks.
    Improve the user experience by adding pagination to the task list view.
    Apply styling and CSS to make the task manager visually appealing.

Remember, this is just one suggestion and you are more than welcome to come up with your own idea for something to build in order to practise what you've learned.
