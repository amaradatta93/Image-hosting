Image Hosting - Web

# Dev Setup
1. Clone the repository
2. Create a virtual environment using: `virtualenv env`
3. Activate virtual env: `source env/bin/activate`
4. Install requirements: `pip install -r requirements.txt`

# Run the project
5. `python manage.py makemigrations --settings=website.config.dev`
6. `python manage.py migrate --settings=website.config.dev`
7. `python manage.py runserver --settings=website.config.dev`
8. Browse to http://localhost:8000/