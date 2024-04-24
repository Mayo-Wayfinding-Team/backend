# Django Backend Local Host Setup Guide

## Steps for Running the Backend Locally

1. **Clone the Repository**
   
   ```bash
   git clone <repository_url>
2. Install Django. If you haven't installed Django yet, run:
   ```
   pip install django
   ```
3. Install MySQL Client. If you haven't installed the MySQL client, run:
   ```
   pip install mysqlclient
   ```
4. Configure Database Credentials. In the settings.py file, enter your MySQL username and password:
   ```
   # settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_mysql_username',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
   Replace your_database_name, your_mysql_username, and your_mysql_password with their respective information.
5. Navigate to Django Project Directory
   ```
   cd django_backend
   ```
6. `Optional` Make Migrations. Run the following command to create migrations:
   ```
   python manage.py makemigrations django_backend
   ```
7. `Optional` Apply Migrations. Apply migrations to your database:
   ```
   python manage.py migrate django_backend
   ```

8. Run the Server. Start the Django development server:
   ```
   python manage.py runserver
   ```
   You can specify a custom port by adding it after the command, e.g., python manage.py runserver 8001.

## Steps for Hosting the Database Locally

1. **Connect to MySQL Server**

   Open your terminal and connect to your MySQL server using the following command:

   ```bash
   mysql -u your_username -p -h localhost -P 3306
   ```
   Replace your_username with your MySQL username.
2. Create a New Database (if needed) If you need to create a new database, you can do so using the following command:
   ```
   CREATE DATABASE your_database_name;
   ```
   Replace your_database_name with the desired name for your new database.
3. Select Database. Once connected, select the database you want to use:
   ```
   USE your_database_name;
   ```
   Replace your_database_name with the name of your database.
4. Import Database Schema. Using a sql file for your database schema, you can import it using the following command:
   ```
   SOURCE /path/to/your/database_dump_file.sql;
   ```
   Replace /path/to/your/database_dump_file.sql with the path to your SQL dump file.
5. After importing the database schema, you can verify that the tables and data are correctly imported by querying the database.
   ```
   SHOW TABLES;
   ```
