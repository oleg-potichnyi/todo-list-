# To-do list Project

This project was created for to-do list management

## Installation

Python3 must be already installed

```shell
# Clone the repository:
git clone https://github.com/oleg-potichnyi/todo-list-
# Change directory to the project folder:
cd todolist
# Set up a virtual environment:
python3 -m venv venv
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
# Install dependencies:
pip install -r requirements.txt
# Environment variables:
## To use the .env and .env.sample files, simply duplicate the .env.sample file and rename it as .env.
## Fill in the variables in the .env file with your actual configuration values, 
## keeping sensitive information private, while the .env.sample file acts as a reference
## for other developers to understand the required environment variables.
# Run this command to apply migrations and update the database schema:
python manage.py migrate
# Start the development server:
python manage.py runserver
```

## Feature

* Management of tasks and their names directly from the site interface
