# Games Blog API

**Advanced Front-End Portfolio Project(PP5) - Code Institute**

The *GamesBlog-backend* is the backend for the GamesBlog application, built using Django Rest Framework. It has been designed for a social gaming network ([GamesBlog](https://gamesblog-front-34620d1947f3.herokuapp.com/)) focused on publishing and participating in  posts with friends.<br>

*GamesBlog* is designed for users who want to create posts from their favourite games or everything related to video games.Each post is also open for like,follow and unfollow users allowing them to stay updated and comments.<br>

The API is organized into several key apps:<br>

_profiles_: Handles user profiles and related information.<br>
_comments_: Enables users to comment on Friendventures.<br>
_followers_: Facilitates the following and tracking of other users' activities.<br>
_like_: Option to manage the general interest of the users for a specific post.
<br>
The deployed API can be found here: [Gamesblog-backend](https://gamesblog-f53e2013614c.herokuapp.com/)<br>
The deployed React project can be found [here](https://gamesblog-front-34620d1947f3.herokuapp.com/)<br>
The link for the GitHub repository to the associated front end can be found [here](https://github.com/t0tacci0/gamesblog-frontend)

## Table of Contents

- [User Experience](#user-experience)
- [Structure](#structure)
- [Database](#database)
  - [Models](#models)
- [API Endpoints](#api-endpoints)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools](#tools)
  - [Frameworks](#frameworks)
  - [Libraries and modules](#libraries-and-modules)
- [Testing](#testing)
  - [Python Validator Testing](#python-validator-testing)
  - [Manual testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Browser Compatibility](#browser-compatibility)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Local deployment](#local-deployment)
  - [Forking this GitHub repository](#forking-this-github-repository)
  - [Clone this repository](#clone-this-repository)
  - [Cloudinary](#cloudinary)
  - [Create PostgreSQL using Code Institute Database Maker](#create-postgresql-using-code-institute-database-maker)
- [Credits](#credits)
  - [Code](#code)
  - [ReadMe](#readme)
  - [Acknowledgments](#acknowledgments)


## Credits

### Code

- The initial setup and overall architecture of this project were guided by the Code Institute's Django Rest Framework walkthrough project. The core elements of the Profile, Follower, Like, Comment, along with their respective serializers, filtering capabilities, and tests, were derived from the walkthrough project and subsequently tailored to meet the unique requirements of this project.

- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Stack Overflow](https://stackoverflow.com/)
  - [reddit](https://www.reddit.com/)
  - [forum djangoproject](https://forum.djangoproject.com/)
  - [Django](https://www.djangoproject.com/), [Django Rest Framework]((https://www.django-rest-framework.org/)), [Cloudinary](https://cloudinary.com/documentation)
  - Slack Community

### Acknowledgements

- I would like to thank my mentor Mo Shami for his tips and assistance for the creation of this project.  
- Furthermore, I would like to give a shoutout to the wonderful tutor team who helped me numerous times when I was stuck and struggling to achieve the results I was aiming for. Your support and guidance have been amazing. Thank you!