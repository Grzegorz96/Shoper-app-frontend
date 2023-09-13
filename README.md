![shoperlogo](https://github.com/Grzegorz96/Shopper-app-frontend/assets/129303867/df33c699-7ad4-473d-8a52-f9a6c3a97225)
# SHOPER.PL

The SHOPER.PL application is an original project that allows users to sell their products and services. Registered users can create announcements and communicate with other users via the application. The user can also upload and download graphic files from the server. The search engine algorithm will allow the user to find exactly what he need. The implemented like system will improve the display of announements that the user is interested in. The application has many useful functions and solutions. It also has its own server application and database. The client application was written for the Windows operating system.

## Description of the modules

The application consists of 6 modules, each module is responsible for a different activity. The Classes.py module contains object classes that are needed to create objects using retrieved JSON data. Objects make it much easier to later operate on data in other modules. The logged-in user class also has its setters for modifying the object's value. The Config_data.py module contains the necessary global variables that must be available for each module in the application. Data stored in variables is used throughout the entire duration of the program. The backend_requests.py module is used from the Functions.py module to directly make requests to the server. Using this module, all data is sent to and received from the server, invoking requests is additionally wrapped in a try, except block, so when an operation fails on the frontend side, the error will be handled appropriately. The Functions.py module contains all the functions that the GUI.py module needs to work properly. Validates all data entered by the user, determines whether the request should proceed, and determines what to do with the received response object. This module creates user, announcements, user announcements, favorite announcements, messages and conversations objects. Features such as converting image files from binary to object and all photo modification features. The function module is a decision-making module and it mainly determines what the user can and cannot do and what to do with the received data. The GUI.py module is responsible for the graphical initialization of the application. Application windows and websites are created at its level. Data that was previously downloaded from the server is displayed from this module. This script contains functions for page pagination and PhotoButton objects are created here, which are later used by the program to identify changes made to multimedia files. The Main.py module is a file that is executed when the program is started, it is used to initialize the application window, static photos, top panel and the first page of the application.

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


## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, Pillow, requests, urllib3

**Server:** 
- Languages: Python, SQL
- Third Party Libraries: Flask, mysql-connector-python, python-dotenv, werkzeug
- Hosting for API: www.pythonanywhere.com
- Hosting for MySQL database: www.pythonanywhere.com

- ## Installation

### To quickly launch the application on Windows:
- Download Shoper-app-frondend repository:
```bash
 git clone https://github.com/Grzegorz96/Shoper-app-frondend.git
```
- Enter the directory Shoper-app-frondend/Shoper_app_exe.
- If you want to move the Shoper_app.exe file, do it together with the photos folder. You can also create a copy of the .exe file on your desktop.
- Run Shoper_app.exe.


### For manually launching the application on the IDE:
#### Requirements:
##### Programs and libraries:
- Python 3.11.1
- Pillow 10.0.0
- requests 2.31.0
- urllib3 2.0.4
#### Instruction:
- Download Shoper-app-frondend repository:
```bash
 git clone https://github.com/Grzegorz96/Shoper-app-frondend.git
```
- Open the Shoper-app-frondend on your IDE.
- Install required packages on your venv:
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
Program SHOPER.PL connects to the enpoints on the cloud server, you don't need to create a local server.


## Lessons Learned

It took me almost 2 months to work on this program and its backend and database. During this time, I had to solve a lot of problems related to these programs. The first version of the program did not include a backend and the connection to the database was made directly from the frontend. I had to rewrite the entire project and add an API to it and then combine it into a logical whole. I learned how to work with multimedia files on the server and I was trained in working with the http protocol. I had to come up with a messaging system so that everything worked correctly, without errors, and that users always received their messages. I have completed most of the functions I set for myself. A big challenge for me was creating a photo editing function - the user can change photos in various ways and each of these cases had to be handled correctly. Creating the necessary tables into the database and creating appropriate relationships between them was also a good test and learning experience. All information displayed to the user is downloaded directly from the server, so there is no fear that something is out of date. I have created a pagination system for displayed announcements and conversations, thanks to which users can create and download as many announcements and conversations as they want, there is no limit. Changes must be made when converting photos from the server from binary and when sending photos to the server. Everything worked fine on the local version of the backend application, but after deploying the application to the server, these activities take too long. Creating this project entirely by myself showed me how much work is needed to create a working application.


## Features to be implemented
- Email verification function.
- Password recovery and change function via a code sent to email.
- Delete account function.
- Filtering and sorting announcements function.
- Function of displaying another user's account.
- hashing of user passwords in the database
- Function covering password characters (during registration and login).
- Improve optimization of reading images on the frontend from the downloaded binary. Currently, the time to convert a photo and assign it to a variable is 0.6-0.7 seconds.
- Improve the optimization of uploading photos to the server, currently it takes 2-3 seconds from execution the request to entering the function on the server, which is definitely too long.


## Authors

- [@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/Shopper-app-frontend/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the home page
![main_shoper](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/353ac4a9-fdb4-4071-bef0-444f1397fed5)
##### Screenshot of the user page
![user_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/880f6a9d-0c3b-4ef3-9ad8-47fbc7da2b38)
##### Screenshot of the favorite page
![fav](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/c3ede5b4-8cad-48e8-b7fd-2447aeca3e5c)
##### Screenshot of adding the announcement
![add_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/8316a6a0-a533-4f63-8281-613d605d030a)
##### Screenshot of editing the announcement
![edit_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/ccafc7fc-dba1-4af8-9b27-f0b1e10a344c)
##### Screenshot of selecting category in home page
![main_category](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/82326049-7939-4530-a5a6-368b1a3565a1)
##### Screenshot of the message page
![mess_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/718525b0-e19c-4930-a7e8-6d60db9f6665)
##### Screenshot of the announcement page
![ann_page](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/6e0e59d1-f114-4047-a9ba-917a6f31151b)
##### Screenshot of the announcements page with message
![ann_with_mess](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/0fd50729-ce44-43e4-9b99-562d17749b7b)
##### Screenshot of the home page with message
![main_with_mess](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/4c69c92c-8c29-4397-921a-dcc188f28133)
##### Screenshot of successfully restoring the announcement
![restore_ann](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/6fd76628-b3b3-4075-8de9-b9c0396826ae)
##### Screenshot of successfully adding the announcement
![success_add](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/585099a8-90c9-4516-87ca-a78dea4ee05d)
##### Screenshot of successfully editing the announcement
![edit_succes](https://github.com/Grzegorz96/Shoper-app-frontend/assets/129303867/8af064c4-7a57-433c-b2be-ba57fdca5c6b)
