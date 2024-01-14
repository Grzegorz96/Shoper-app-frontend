![shoperlogo](https://github.com/Grzegorz96/Shopper-app-frontend/assets/129303867/df33c699-7ad4-473d-8a52-f9a6c3a97225)
# SHOPER.app

The SHOPER.app is an original project that allows users to sell their products and services. Registered users can create announcements and communicate with other users via the application. The user can also upload and download graphic files from the server. The search engine algorithm will allow the user to find exactly what he need. The implemented like system will improve the display of announements that the user is interested in. The application has many useful functions and solutions. It also has its own server application and database. The client application was written for the Windows operating system.


## Description of the modules

The program consists of 6 modules, each of which plays a unique role in the functioning of the application. Below is a brief description of each module:

Classes.py:
- The Classes.py module contains object classes that are needed to create objects using retrieved JSON data. Objects make it much easier to later operate on data in other modules. The logged-in user class also has its setters for modifying the object's value. 

Config_data.py:
- The Config_data.py module contains the necessary global variables that must be available for each module in the application. Data stored in variables is used throughout the entire duration of the program. 

Backend_requests.py:
- The Backend_requests.py module is used from the Functions.py module to directly make requests to the server. Using this module, all data is sent to and received from the server, invoking requests is additionally wrapped in a try, except block, so when an operation fails on the frontend side, the error will be handled appropriately.

Functions.py:
- The Functions.py module contains all the functions that the GUI.py module needs to work properly. Validates all data entered by the user, determines whether the request should proceed, and determines what to do with the received response object. This module creates user, announcements, user announcements, favorite announcements, messages and conversations objects. Features such as converting image files from binary to object and all photo modification features. The function module is a decision-making module and it mainly determines what the user can and cannot do and what to do with the received data. 

GUI.py:
- The GUI.py module is responsible for the graphical initialization of the application. Application windows and panels are created at its level. Data that was previously downloaded from the server is displayed from this module. This script contains functions for page pagination, also photoButton objects are created here, which are later used to identify changes made to photos while adding and editing announcement.

Main.py:
- The Main.py module is a file that is executed when the program is started, it is used to initialize the application window, static photos, top panel and the first page of the application.


## Features

- User registration.
- user login.
- User logout.
- login verification.
- password verification.
- Destroying all created windows when logging in and out.
- Modification of user data.
- Displaying and pagination user's announcements separately for active ones and separately for completed ones.
- Editing user announcements.
- Editing announcements photos (deleting, adding, modifying the main photo).
- Moving a user's announcements to completed.
- Restoring a user's announcements to active.
- Moving user's announcements to deleted.
- Automatic refresh of pages after performing a modifying operation.
- Adding announcements (optionally with photos).
- Displaying and pagination user's downloaded conversations separately as a seller and separately as a customer.
- Viewing messages.
- Sending messages.
- Displaying and pagination user's downloaded favorite announcements separately for active ones and separately for completed ones.
- Adding announcements to favorites.
- Deleting announcements from favorites.
- Announcements search engine that accepts optional phrase, location and category parameters. You can specify the parameters you need.
- Displaying and pagination downloaded announcements from the search engine or the Shoper button.
- Displaying the announcement page.
- Announcement photo gallery
- Validation of all data entered on the frontend.
- Password hiding function from the user page.
- Displaying messages to the user on failures or successes.
- Compressing the image file before sending to backend.


## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, Pillow, requests, urllib3

**Server:** 
- Languages: Python, SQL
- Third Party Libraries: Flask, mysql-connector-python, python-dotenv, werkzeug
- Hosting for API: www.pythonanywhere.com
- Hosting for MySQL database: www.pythonanywhere.com

## Installation

### To quickly launch the application on Windows:
- Download Shoper-app-frondend repository:
```bash
 git clone https://github.com/Grzegorz96/Shoper-app-frondend.git
```
- Enter the directory Shoper-app-frondend/Shoper_app_exe.
- If you want to move the Shoper_app.exe file, do it together with the Photos folder. You can also create a copy of the .exe file on your desktop.
- Run Shoper_app.exe.


### For manually launching the application on the IDE:
#### Requirements:
##### Programs and libraries:
- Python 3.11.1
- IDE, for example Pycharm
- Pillow 10.0.0
- requests 2.31.0
- urllib3 2.0.4
#### Instruction:
- Download Shoper-app-frondend repository:
```bash
 git clone https://github.com/Grzegorz96/Shoper-app-frondend.git
```
- Go to the Shoper-app-frondend directory.
- Open the Shoper-app-frondend on your IDE.
- Create virtual enviroment for the project (Windows):
```bash
 py -m venv venv
```
- Activate virtual enviroment (Windows):
```bash
 venv/Scripts/activate.bat
```
- Install required packages on your virtual enviroment:
```bash
 pip install -r requirements.txt
```
- or
```bash
 pip install Pillow==10.0.0
 pip install requests==2.31.0
 pip install urllib3==2.0.4
```
- Run Main.py on Windows:
```bash
 py .\Main.py
```
Program SHOPER.PL connects to the enpoints on the cloud server, you don't need to create a local backend server.


## Lessons Learned

It took me almost 2 months to work on this program and its backend and database. During this time, I had to solve a lot of problems related to these programs. The first version of the program did not include a backend and the connection to the database was made directly from the frontend. I had to rewrite the entire project and add an API to it and then combine it into a logical whole. I learned how to work with multimedia files on the server and I was trained in working with the http protocol. I had to come up with a messaging system so that everything worked correctly, without errors, and that users always received their messages. I have completed most of the functions I set for myself. A big challenge for me was creating a photo editing function - the user can change photos in various ways and each of these cases had to be handled correctly. Creating the necessary tables into the database and creating appropriate relationships between them was also a good test and learning experience. All information displayed to the user is downloaded directly from the server, so there is no fear that something is out of date. I have created a pagination system for displayed announcements and conversations, thanks to which users can create and download as many announcements and conversations as they want, there is no limit. I had a problem with file compression, i created a program to compress files on the backend but it was not a good idea because Flask on the server does not work asynchronously and with each delay, the next query has to wait. I solved this problem by creating compressions on the frontend just before sending the file. Making this project entirely by myself showed me how much work is needed to create a working application.


## Features to be implemented
- Email verification function.
- Password recovery and change function via a code sent to email.
- Delete account function.
- Filtering and sorting announcements function.
- Function of displaying another user's account.
- Function covering password characters (during registration and login).
- Changing the download of graphic files to a package of files. Currently the files are downloaded separately. To perform 16 queries when downloading photos to the home page, after compression files it takes about 6 seconds.

 
## Authors

[@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/Shopper-app-frontend/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the home page
![main_shoper](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/42f0e0c4-6b05-4bcf-b9d5-e05af3068f1c)
##### Screenshot of the user page
![user_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/4296e23a-340c-4da4-85f8-b0602402740f)
##### Screenshot of the favorite page
![fav_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/2e9e0caa-308d-472c-9438-91251cd881d1)
##### Screenshot of the login/register window
![login_window](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/9ddfd480-832a-424e-bef2-eaa72a1d3163)
##### Screenshot of adding the announcement
![add_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/ad27a4e7-fb1a-449d-b8d8-e9370b193a51)
##### Screenshot of the window for selecting an image file
![add_ann_window](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/96b88d22-91aa-4180-a0ec-f3b02a2b367a)
##### Screenshot of editing the announcement
![edit_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/eed330e2-99c0-4a2e-88dd-18957d72eceb)
##### Screenshot of selecting category in home page
![main_category](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/79d1cd3f-2751-4e6a-ba88-b715e9273416)
##### Screenshot of the message page
![conversations](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/9f912607-7582-45b7-8138-193cf3845198)
##### Screenshot of the announcement page
![ann_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/cd3dc7c2-44ab-4476-94a4-20fa04511deb)
##### Screenshot of the announcements page with message
![ann_with_mess](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/6a020872-de6e-4283-aa18-16bb2d8b0caf)
##### Screenshot of the home page with message
![main_with_mess](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/27cc32bb-92a2-43cd-94af-aceb77ba4a25)
##### Screenshot of successfully restoring the announcement
![restored](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/67b63f2d-fc9b-4eb5-80d1-876f78b77242)
##### Screenshot of successfully completing the announcement
![completed](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/dc5b24c1-2593-4419-a828-ab429d62cccd)
##### Screenshot of successfully adding the announcement
![add_ann_success](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/e5f2e618-2016-4f00-97f6-a193e2ec1656)
##### Screenshot of successfully editing the announcement
![edit_ann_success](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/7fe590d6-5f4e-44bf-b4d6-457e0184044a)
