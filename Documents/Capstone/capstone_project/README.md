<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Technical Details</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project is an open source platform designed for the specific purpose of providing users with peer-reviewed and rated academic resources. Each field of study has a discussion section where users may exchange information about the field of study. Users are able to interact and rate each resource and each other's posts.

There are platforms available for discussions like reddit, educational platforms such as edx.org and coursera, and there are also places like youtube, stackoverflow, and quora that post information and help people with their questions. A space where users are able to have these sources, and others such as textbooks, rated based on helpfulness is not present. A most important feature is that ratings are specifically made by students and learners. Having a space for this allows users to save lots of time from navigating websites and potentially being distracted in the process. It cultivates a more productive learning process and fosters a healthy growing society through verified information.

### Built With

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

<!-- GETTING STARTED -->

## Getting Started

Download the main directory and open in your preferred IDE. An example of the how it should look, in this case, in visual studio code would be:

<img src="media/profile_pics/outlook.png" alt="webapp screenshot" width="850" height="500">

To run the main program you will run the following command in your terminal after you navigate to the main folder directory (“capstone_project”): python3 manage.py runserver

<img src="media/profile_pics/run.png" alt="webapp screenshot" width="850" height="500">

This is the result if everything compiles correctly. Then either click the http://127.0.0.1:8000/ or copy and paste it onto your browser.

Now you are ready to navigate the platform. You will be presented with the home page. You can initially click sign up to create a profile and after creating one you can edit your profile through the interface present, change username, reset password through email etc. When done you can navigate back home.

Then proceed to click into the developed path which starts with Computer Science. You can explore, rate, and navigate then go onto one of the main 3 branches. The one developed as a template for this project is Theoretical Computer Science. Here can observe/rate etc, then move onto Algorithms → Graphing Algorithms → What are Graphs? At this final page you are presented with the most detailed view and can look at how resources are split for a specific instance. You can also navigate to the discussion at the bottom of the page, make a post, rate someone's post etc.

### Prerequisites

You will need the following installed prior to running this locally.

MacOS

- Python
  ```sh
  brew install python
  ```
- star_rating
  ```
  pip install django-star-ratings
  ```

### Installation

1. Clone the repo using
   ```sh
   git clone
   ```
2. Change directory into the parent directory owl
   ```sh
   cd capstone_project
   ```
3. Run app
   ```sh
   python3 manage.py runserver
   ```
4. Navigate to http://127.0.0.1:8000/
5. To exit, `CTRL+C` on your keyboard

<!-- USAGE EXAMPLES -->

## Technical Details

### Layout:

1. Academia:
   - Holds main views of home page and following field of study pages
   - Includes of a symbolic link to the Star_ratings directory so they can be included in the html files
   - static/academia: holds the CSS and javascript files
   - templates/academia holds the HTML files for the main pages of the platform
   - admin.py allows to update my created class in python to the databases
   - apps.py holds the name of main created class of the app academia that must be registered in Capstone/settings.py
   - models.py holds the classes I created in python to be transported into databases through sqlite3. After models are created you have to run: python3 manage.py makemigrations → python3 manage.py sqlmigrate academia 0001 (this command shows sql code where 001 is number reference) → python3 manage.py migrate ( used to finalize making changes to database and updates it).
   - urls.py holds the webpaths to go from interface to interface.
   - views.py is where I define the main functions for each web page to be created and input the data that it will interact with. Also included are custom views of how the website should be viewed through python code in form of classes functions etc which are attached as parameters to web page functions.
2. Capstone
   - Is the main directory folder and holds the main settings.py file which allows you to interact with database settings, and other website features you want to tweak with.
   - urls.py here holds navigation between different apps within the same website (discussion forum is different app, functionality, and layout)
3. Media
   - Media/profile_pics stores photos for users profiles. In this directory is also a default image for users not uploading photo
4. Star_ratings
   - Holds similar files to academia directory where HTML templates, CSS, javascript files and python files are held to make the rating system functional in front end and back end as done in academia.
   - forms.py holds specific python code for userinteraces on information filled by them.
   - signals.py holds interactions sent between users and code
5. Users
   - Very similar to star_ratings. Holds HTML, CSS, Javascript files and also the python files to set user restrictions, rights, settings, front ent, and interactions.
6. manage.py → used to run server and other functionalities
7. pythonShell.py → runs python scripts and code to interact with models built and back end. (Used for example to run the resource_scrape.py file that initiates data being loaded into the database).
8. resource_scrape.py → main file to scrape web for different resources and load the resources into their own databases based on models created in models.py files to be called from web pages in views.py
9. ReadMe.md → info document
10. setup.py → The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands that operate on your modules do the right thing.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/ArlindS/capstone_project/futurePlans-issues) for a list of proposed features (and known issues).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/druwadi/owl.svg?style=for-the-badge
[contributors-url]: https://github.com/druwadi/owl/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/druwadi/owl.svg?style=for-the-badge
[forks-url]: https://github.com/druwadi/owl/network/members
[stars-shield]: https://img.shields.io/github/stars/druwadi/owl.svg?style=for-the-badge
[stars-url]: https://github.com/druwadi/owl/stargazers
[issues-shield]: https://img.shields.io/github/issues/druwadi/owl.svg?style=for-the-badge
[issues-url]: https://github.com/druwadi/owl/issues
[license-shield]: https://img.shields.io/github/license/druwadi/owl?style=plastic
[license-url]: https://github.com/druwadi/owl/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/druwadi
