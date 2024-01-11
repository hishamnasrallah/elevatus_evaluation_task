
Quickstart
----------

First, clone the project on your local machine: ::

    https://github.com/hishamnasrallah/elevatus_evaluation_task.git

Manual Run
----------

Activate poetry by typing: ::

    poetry shell
If the poetry not installed, install it before implementing the previous command: ::

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    export PATH="$HOME/.poetry/bin:$PATH"
    poetry install
    poetry shell

Then create ``.env`` file and fill it by the following variables ::

    DB_ENGINE=mongodb
    DB_NAME=elevatus
    DB_USERNAME=hisham
    DB_PASSWORD=Amman123
    DB_HOST=localhost
    DB_PORT=27017
    ENVIRONMENT=local

Finally, to run the app:

    uvicorn app.main:app --reload
    or

    uvicorn app.main:app --reload --port {PORT_NUMBER}

now it will be working and running on

    http://127.0.0.1:8000/elevatus/docs#/


Run the app using docker compose
----------
open the terminal and type: ::

    docker-compose up --build -d

if you faced docker issue related to buildkit you can run it using the following command

    DOCKER_BUILDKIT=0 docker-compose up --build -d

now it will be working and running on

    http://127.0.0.1:8000/elevatus/docs#/

**Congratulations the service is working now**

Stop Docker
-----------
type in terminal 

    docker-compose stop

then 
    
    docker-compose rm -f

Very Important Notes
----------

**1- Make sure to create .env file if you won't to use that one in the repo**

**2- 'elevatus' is the prefix for all apis**

**3- main.py inside "app" folder**

**4- I added some extra things to make it more efficient like pagination, peorty instead of requirements.txt, .ignore,
jwt, exceptions, and some other things**

**5- I commented .env from .gitignore to keep a sample of it inside the repo**

**6- change .env values will effect the project every where so no need to make any changes for database anywhere except .env file**


API documentation
----------

All APIs are available on ``{{base_url}}/elevatus/docs``.





