# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /backend

# Install dependencies
RUN pip install --upgrade pip
RUN pip install django
RUN pip install mysqlclient
RUN pip install django-autoreload
RUN pip install python-dotenv
RUN pip install django-cors-headers

# Copy the backend code into the container at /backend
COPY /django_backend/ /backend

# Expose port 7012 to allow external access
EXPOSE 7012

# Run the Django application with auto-reload
CMD ["python", "manage.py", "runserver", "0.0.0.0:7012"]