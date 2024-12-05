FROM python:3.8.18

# Set the working directory
WORKDIR /usr/app/

# Copy the current directory contents into the container
COPY . /usr/app/

# Install dependencies
# RUN pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org absl-py==2.1.0 aiohttp==3.10.11 altair==5.4.1 ...

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the application port (if necessary)
EXPOSE 5000

# Set the command to run the app
CMD ["python", "flask_app2.py"]
