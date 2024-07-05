## Use the offical python 3.9 image

FROM python:3.9

## set the working directory to /code

WORKDIR /code

## Copy the current directory contents in the contaniner at /code

COPY ./requirements.txt /code/requirements.txt

## intsall the requirements.xtx

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Set up a new user named "user"

RUN useradd user

#switch to the "user" user
USER user

# Set home to the user's home directory 

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH


#set the working directory to the user's home directory 

WORKDIR $HOME/app

# copy the current directory contents into the container at $home/app setting the owner to 

COPY --chown=user . $HOME/app


## start the FASTAPI app on port 7860 

CMD [ "unicorn", "app:app", "--host", "0.0.0.0", "--post", "7860" ]



