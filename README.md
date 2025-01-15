This is the VR Sensor data processor project. The project mainly run the MQTT broker in the server and active the port to
 receive/publish message. This is Python Django project. 

 # How to run the project 
 First of all you have to ensure the python and postgresql are installed in your machine. then pull the project from the repository and then 
 open the project in any IDE like visual studio code (vs code). then create a virutal environment using below code 

 ```
    python -m venv env_name
 ```

 ## Activate the created virtual environment first open command terminal from your computer and goto to the project directory using cd command and then using below command

 ```
    env_name\Scripts\activate
 ```

 If every ok then you virtual environment will be activate and at the biginning of your teminal last lien you will see the env_name.
 now you have to install required library that are need to successfully run this project. All the required library are mentioned in the required.txt file. You can install from the txt file using below command

 ```
    pip install -r required.txt
 ```

 after successfully install all required package now you need to open postgresql and create database "vrsensors_db". you can use any other name but if you create database in different name. please use that name in DATABASES section in the setting.py file. now  you can create migrate file using below command

 ```
python manage.py makemigrations
 ```

 After successfully do all these steps now you can run migrations file using below command 

 ```
    python manage.py migrate
 ```


 finally you are ready to run the project

 ```
    python manage.py runserver
 ```