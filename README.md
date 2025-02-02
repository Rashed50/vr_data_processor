This is the VR Sensor data processor project. The project mainly run the MQTT broker in the server and active the port to
 receive/publish message. This is Python Django project. 

 # How to run the project 
 First of all you have to ensure the python and postgresql are installed in your machine. then pull the project from the repository and then 
 open the project in any IDE like visual studio code (vs code). then create a virutal environment using below code 

 ```
    python -m venv env_name
 ```

 Activate the created virtual environment first open command terminal from your computer and goto to the project directory using cd command and then using below command

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


 finally you are ready to run the project. But one think need to keep in mind that mqtt broker will connect with server using SSL certificate so you have to confirm the certificate  location correctly. You have to update that path as per your project location below code inside the mqtt_tls_broker.py file .

 ```
    client.tls_set("E:\\Germany File\\Martin Becker\\projects\\vr_data_processor\\vr_data_processor\\datasource\\certificate\\client_cert.cer" , tls_version=ssl.PROTOCOL_TLSv1_2)
 ```

 Now you can run the project by run this below code in two way eigther specific port or withour mentioning port .
  Here 8081 is port number that this project will run on this port. Don't use any port number that is engased by another application.

 ```
    python manage.py runserver

    or

    python manage.py runserver 8081 

 ```

After successfully run the application . you project will run on a ip address that you will see after run the project . now you can open you browser and the webpage . after open 
web browser MQTT Broker will be ready to receive message. MQTT subscribed topic name is "vrsensors". That means if you publish message in this topic name from any other mqtt broker application my project will recive that published message. The message json format is as like and all these fields are  mentory information  that you have publish and my MQTT broker is ready to that format otherwise will show error when parsing the receiving message.

```
   "msg": "this is testing message from mqttx other application",
   "session_id" : "546464646",
   "frame_number" : 6549671763,
   "timestamp" : 1734351949

```
