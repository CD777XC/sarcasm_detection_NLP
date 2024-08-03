##### DOCKER CONTAINER #####

# Defining python version
FROM python:3.11.2-buster

# Defining working dir
WORKDIR /app

# Copying app into container
COPY . .

# Upgrading pip and intalling requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Running command
CMD ["uvicorn", "app.api:sarcasm_detection", "--host", "0.0.0.0", "--port", "8080"]