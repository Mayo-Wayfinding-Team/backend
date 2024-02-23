# Django Backend
## steps for running the backend
- Clone the directory
- if you havent installed django run: 
  ```
  pip install django
  ```
- if you havent installed mysqlclient run:
  ```
  pip install mysqlclient
  ```
- in the settings.py file enter your mySQL username and password
- Cd into django project
  ```
  cd django_backend
  ```
- (optional) make migrations
  ```
  python manage.py migrate django_backend
  ```
- run the server you can change the port by adding port number after this such as 8001
  ```
  python manage.py runserver
  ```
