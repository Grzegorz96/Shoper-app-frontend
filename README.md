![shoperlogo](https://github.com/Grzegorz96/Shopper-app-frontend/assets/129303867/df33c699-7ad4-473d-8a52-f9a6c3a97225)
# SHOPER.app

The SHOPER.app is an original project that allows users to sell their products and services. Registered users can create announcements and communicate with other users via the application. The user can also upload and download graphic files from the server. The search engine algorithm will allow the user to find exactly what he need. The implemented like system will improve the display of announements that the user is interested in. The application has many useful functions and solutions. It also has its own server application and database. The client application was written for the Windows operating system.


## Table of Contents

- [Description of folders and modules](#Description-of-folders-and-modules)
- [Features](#Features)
- [Technology used](#Technology-used)
- [Installation](#Installation)
- [Lessons learned](#Lessons-learned)
- [Authors](#Authors)
- [Contact](#Contact)
- [License](#License)
- [Screnshoots](#Screnshoots)


## Description of folders and modules

### Core:
/main.py:
- The main.py module is the main entry point for the SHOPER application, responsible for initializing key components and starting the main application loop.

### Layout:
/layout/main_window.py:
- The main_window.py module contains the code responsible for configuring the main window of the SHOPER application. This is a key element that ensures the proper appearance and functionality of the main user interface.

/layout/top_panel.py:
- The top_panel.py module defines the init_top_panel() function, which initializes the top panel of the SHOPER application. It is a key element of the user interface that allows the user to navigate and interact with the application

### Pages:
/pages:
- The pages folder contains modules that are responsible for creating views for the user. Each of these modules plays a key role in the functioning of the SHOPER application, providing users with access to various functions, such as managing announcements, viewing messages or editing the user profile. Thanks to these modules, the application can effectively handle user interactions and provide full functionality of the advertising website.

### Logic:
/logic:
- The logic folder in the SHOPER application plays a key role as a central point for managing the logic and functionality of the system. It is divided into four main subfolders: announcements, media, messages and users, each of which is responsible for a specific area of ​​operation in the application.
**The announcements** subfolder contains the functions and logic needed to manage announcements, such as adding, editing, deleting announcements, and displaying them.
##### The media subfolder deals with the manipulation of media files used on the system, such as images and other graphical resources. It includes the integration and management of these resources in the context of announcements.
##### The messages subfolder contains the logic for handling messages between application users. It is responsible for the functions of sending, receiving and managing messages, ensuring communication between users.
##### The users subfolder contains functions related to application user management. Includes registration, login and user account management processes.

### Models:
/models:
- The models folder in SHOPER contains classes that represent key objects and data structures used in the system. The files in this folder define the following classes: Announcement, Message, Conversation, LoggedUser, UserFavoriteAnnouncement, PhotoButton. These classes are central to the data structure and logic of the application, enabling the management of announcements, messages, users, and multimedia operations. Thanks to properly defined classes, the application can effectively handle all aspects of the operation of the advertising website, providing users with a convenient and comprehensive experience of using the application.

### Services:
/services:
- The services folder contains the API subfolder, which contains modules responsible for communicating with the backend via API. Each of these modules (announcements, messages, users, media) contains functions that query the backend to retrieve, send, update or delete data related to announcements, messages, users and multimedia.

### Windows:
/windows/login_register_window.py:
- the login_register_window module initializes a new window containing a login and registration form.

/windows/message_window.py
- the message_window module initializes a new message window.

### Utils:
/utils/config_data.py:
- Stores global data for the entire application, such as configuration settings.

/utils/constants.py:
- Contains constants used in the application, such as lists, tuples, constant configuration parameters.

/utils/formating.py:
- It is used to perform functions related to various formatting of files.

/utils/helpers.py:
- It contains various helper functions used in different parts of the application.

### Assets:
/assets/images:
- Contains static files used in the application.


## Features

- User registration.
- User login.
- User logout.
- Login verification.
- Password verification.
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
- Password hiding functions.
- Displaying messages to the user on failures or successes.
- Deleting account.
- Main photos of announcements received with announcements in base 64 format.
- Image compression and zip packing before sending to the backend for better performance.
- Receiving a package of images in zip form.


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
- Enter the directory Shoper-app-frondend/shoper_app_exe.
- If you want to move the Shoper_app.exe file, do it together with the assets folder. You can also create a copy of the .exe file on your desktop.
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
- Install required packages on your activated virtual enviroment:
```bash
 pip install -r requirements.txt
```
- or
```bash
 pip install Pillow==10.0.0
 pip install requests==2.31.0
 pip install urllib3==2.0.4
```
- Run main.py on Windows:
```bash
 py .\main.py
```
Program SHOPER.PL connects to the enpoints on the cloud server, you don't need to create a local backend server.


## Lessons learned

It took me almost 3 months to work on this program and its backend and database. During this time, I had to solve a lot of problems related to these programs. The first version of the program did not include a backend and the connection to the database was made directly from the frontend. I had to rewrite the entire project and add an API to it and then combine it into a logical whole. I learned how to work with multimedia files on the server and I was trained in working with the http protocol. I had to come up with a messaging system so that everything worked correctly, without errors, and that users always received their messages. I have completed most of the functions I set for myself. A big challenge for me was creating a photo editing function - the user can change photos in various ways and each of these cases had to be handled correctly. Creating the necessary tables into the database and creating appropriate relationships between them was also a good test and learning experience. All information displayed to the user is downloaded directly from the server, so there is no fear that something is out of date. I have created a pagination system for displayed announcements and conversations, thanks to which users can create and download as many announcements and conversations as they want, there is no limit. I had a problem with file compression, i created a program to compress files on the backend but it was not a good idea because Flask on the server does not work asynchronously and with each delay, the next query has to wait. I solved this problem by creating compressions on the frontend just before sending the file. I had to improve the image file management logic on my platform. I improved the way these files were transferred from the server and optimized performance by reducing the number of queries. The main photos needed to display announcements are now downloaded together with the announcements themselves in Base64 format. However, photo lists are now downloaded and sent in ZIP format, allowing multiple files to be grouped into one archive. Making this project entirely by myself showed me how much work is needed to create a working application.


## Features to be implemented
- Email verification function.
- Password recovery and change function via a code sent to email.
- Filtering and sorting announcements function.
- Function of displaying another user's account.

 
## Authors

[@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License
[AGPL-3.0 license](https://github.com/Grzegorz96/Shoper-app-frontend/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the home page
![home_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/db29257a-2049-4388-b312-7b75cea5e590)
##### Screenshot of the user page
![user_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/55295703-b1e4-41d1-929d-4d147c4e8cf2)
##### Screenshot of the favorites page
![favorites_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/1d221d7d-3bb8-41de-8b00-0d5c32475f9e)
##### Screenshot of the login/register window
![login_register_window](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/06db2c30-d5a7-4b05-8022-9b4ae2655adb)
##### Screenshot of the add announcement page
![add_announcement_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/f6d4cad5-3c22-47e5-9440-fed7d2e8629d)
##### Screenshot of the window for selecting an image file
![add_announcement_window](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/5e9c5ea3-0b26-4f6e-ac1b-979b2c085090)
##### Screenshot of the edit announcement page
![edit_announcement_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/330a17a1-39ef-49a0-854b-36dde728f004)
##### Screenshot of selecting category in home page
![home_category](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/5525fb23-5eb0-44ab-9337-1914984c14fb)
##### Screenshot of the messages page
![messages_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/9f62db15-4e5f-4eb0-991b-d3c5b2dc2782)
##### Screenshot of the announcement page
![announcement_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/287bce5a-06bd-46a0-8ee1-77a51a6f3f7b)
##### Screenshot of the announcements page with messages
![announcement_with_messages](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/abdb7419-9da1-4d59-8916-b7f1ad9df8d8)
##### Screenshot of the home page with messages
![home_with_messages](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/df455371-8e5a-4d32-aba1-2eac72ef9600)
##### Screenshot of successfully restoring the announcement
![restored](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/ac4c3f76-712c-46e7-8e59-3cf7525f4ffd)
##### Screenshot of successfully completing the announcement
![completed](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/e5a53558-3ad7-45b6-8e94-e64ea2ff8626)
##### Screenshot of successfully adding the announcement
![add_announcement_success](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/d7743711-6aa6-4480-8a36-5c4f15107cd7)
##### Screenshot of successfully editing the announcement
![edit_announcement_success](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/69b82b02-9c2b-42c3-ba8f-c1683100c90b)
