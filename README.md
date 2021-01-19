# IG App

#### This is an application (akin to instagram) where user can post there pics in their profiles once having signed in, and get to also like other users pictures and connect.

## Project live si
 Visit the live link [here:] (https://b-ig-app.herokuapp.com/accounts/login/?next=/)

## Features
* User can log in to application and view other peoples posts.
* A user can like and comment on a post.
* A user can upload posts and edit their profile.
* Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## Screenshots
1. <image src = 'https://github.com/Barnabas27/IG/blob/master/static/images/page1.png'>

## Behavior Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets redirected to the login page  | User logs in | Directed to the home page where they see posted photos | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Home page loads | Add comment  | Comment posted appears |
|  Homepage loads | Click `profile` | User's profile appears | 
| Homepage loads | Click `upload image` icon | User's redirected to a page where they can upload an image | 
| Homepage loads | Click `settings` icon | A modal appears where one can change their password or logout | 
| Homepage loads | User inputs in the search form and presses enter | Searched results show |
| A list of users displays | Click `follow` button to follow | Reloaded to the homepage

## Setup/Installation requirements
1. Clone or download and unzip the repository from https://github.com/Barnabas27/IG.git

2. Install the virtual environment
  -   `pip install pipenv`
3. Activate the virtual environment
  - `pipenv shell`
4. Install the Pre-requisites by running the command:
  - `pipenv install -r requirements.txt`

## Technologies Used
* PYTHON 3.*
* DJANGO FRAMEWORK
* BOOTSTRAP4
* CSS
* POSTGRESS

## Support and contact details
contact me @ bkamau032@gmail.com

### License
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2019.All rigths reserved