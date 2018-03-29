### Condenast
This application consists of APIs for listing nearby place list, details of each place and contributor details. Also, to add, update and delete data from database when there is any change in contentful

### Prerequisities 
* Python 2.7 
* MongoDB
* Contentful Service

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Steps to setup the configuration and start the application with ubuntu os.
  1. Install pip 
        - sudo apt-get install python-pip python-dev build-essential
  2. Install virtualenv and virtualenvwrapper
        - sudo pip install virtualenv virtualenvwrapper
        - sudo pip install --upgrade pip
  3. Create a backup of the .bashrc file
        - cp ~/.bashrc ~/.bashrc-org
  4. Create a directory to store all the virtual environments and set WORKON_HOME     to virtual environments directory
        - mkdir ~/.virtualenvs
        - export WORKON_HOME=~/.virtualenvs
  5. Open bashrc file and add the following line at the end of bashrc file
        - sudo nano ~/.bashrc 
        - . /usr/local/bin/virtualenvwrapper.sh

  6. Re-source terminal using the following command
        - source ~/.bashrc
  7. Create new virtual environment
        - mkvirtualenv VIRTUALENV_NAME

  8. Activate the virtualenv
        - workon VIRTUALENV_NAME
  9. Create a folder and go inside the folder and clone the project
        - mkdir foldername && cd foldername
        - clone the project.
  10. Deactivate the virtualenv and open the postactivate file from bin folder
        - deactivate
       - sudo nano ~/.virtualenvs/VITRUALENV_NAME/bin/postactivate
  11.  Add the following line in postactivate to load the settings on        virtual environment activation
        - export DJANGO_SETTINGS_MODULE=project_name.settings.local
  12. To remove the settings once the virtual environment is deactivated open       postdeactivate file
        - sudo nano ~/.virtualenvs/VITRUALENV_NAME/bin/postdeactivate
   and add 
        - unset DJANGO_SETTINGS_MODULE	
  13. Activate virtual env and install all requirements
        - workon VIRTUALENV_NAME
        - pip install -r requirements.txt
  
### Run server and test if project set up is successful
python manage.py runserver

### Databases used
MongoDB

### Database and contentful configuration.
For every environment there is a sesparate database and contentful space.
Add the configuration in the respective environment file and load it accordingly in postactivate file.

