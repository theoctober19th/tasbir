# Tasbir
Tasbir is an Instagram clone web application written in Python using Django Framework. The technologies used in this project are: 
* Django
* Python
* JavaScript (jQuery)
* HTML
* CSS

### Instructions

1. Create a virtual environment and then activate it.  
    `python -m venv env env && source env/bin/activate`

2. Clone this repo in your machine and change directory to `tasbir`.  
    `git clone https://github.com/theoctober19th/tasbir.git && cd tasbir`

3. Install packages from `requirements.txt`  
    `pip install -r requirements.txt`

4. Make migrations and migrate  
    `python manage.py makemigrations photo_app user_app && python manage.py migrate`

5. Run the server.  
    `python manage.py runserver`


