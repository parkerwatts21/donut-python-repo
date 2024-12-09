# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /donut-python-repo

# Copy the requirements file into the container
COPY requirements.txt /donut-python-repo/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /donut-python-repo/

# Collect static files into the STATIC_ROOT directory
RUN python3 manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the Django application
CMD ["gunicorn", "missingpersons.wsgi:application", "--bind", "0.0.0.0:8000"]