Image Hosting - Web

# Dev Setup
1. Clone the repository
2. Create a virtual environment using: `virtualenv env`
3. Activate virtual env: `source env/bin/activate`
4. `cd website/`
5. Install requirements: `pip install -r requirements.txt`

# Run the project (from the `Useindio/website` directory)
6. `python manage.py makemigrations`
7. `python manage.py migrate`
8. `python manage.py runserver`
9. Browse to http://localhost:8000/