# Tom Holohan Audio

For the portfolio project I have created a site for clients to book appointment times with a music producer to discuss their project. 

## Contents

1. [Strategy](#strategy)
   1. [Project Goals](#project-goals)
   2. [User Goals](#user-goals)
2. [Flowchart](#flowchart)
3. [User Stories](#user-stories)
   1. [Player User Stories](#player-user-stories)
4. [Technology Design](#technology-design)
   1. [User Interface](#user-interface)
5. [Technologies Used](#technologies-used)
   1. [Languages](#languages)
   2. [Applications](#applications)
   3. [Packages](#packages)
6. [Validation](#validation)
7. [Testing](#testing)
8. [Deployment](#deployment)
   1. [Forking the Github Repository](#forking-the-github-repository)
   2. [Making a Local Clone](#making-a-local-clone)
   3. [Heroku](#heroku)

## Strategy

### Project Goals

As a music producer full time, I was getting sick of losing track of my clients and relying on writing down dates and times for meetings. With this site, clients will able to book in with me themselves in a time that suits them and I will be able to see it all clearly on the admin page. 


### User Goals

User's are coming to this site to learn about the producer, hear some of their work, see some client testimonials and ultimately book a call if they desire. 



## Flowchart

![](Flowchart)


## User Stories
   1. As a {USER}, I want {TO BOOK A CALL}, so that {I CAN ORGANIZE A MEETING WITH THE PRODUCER}.
   2. As a {USER}, I want {TO BE ABLE TO BE ABLE TO CANCEL OR RESCHEDULE MY MEETING}, so that {IF SOMETHING COMES UP I CAN ORGANIZE IT AROUND MY SCHEDULE}.
   3. As a {admin}, I want {to be able to view/manage booked appointments}, so that {I can keep control over them}.
   4. As a {user and admin}, I want {to receive an email confirming my appointment}, so that {I can be informed when it goes through}.
   5. As a {user}, I want {to only be able to book a free slot}, so that {I can speed up the booking process}.
   6. As a {user}, I want {a page I can go to with all the info about my appointment}, so that {I can cancel, reschedule or remind myself about my appointment info}.

## Technology Design

### User interface


## Technologies Used

### Languages
   1. HTML
   2. CSS
   3. Javascript
   4. Python

### Frameworks
   1. [Django](https://www.djangoproject.com/) - The main framework used to create this project.
   2. [Materialize CSS](https://materializecss.com/) - Used for responsive and easy css. 

### Applications
   1. TinyPNG - Used to compress images
   2. Gitpod - Cloud based IDE used for development
   3. Heroku - Cloud platform used to host app
   4. [Pexels](https://www.pexels.com/) - Stock image site used to source images
   5. [Gradient Animator](https://www.gradient-animator.com/) - Used for creation of background gradients


### Packages


## Validation 


## Testing

Full information on the testing of this application can be found in [TESTING.md](TESTING.md)

## Deployment

### Forking the GitHub Repository

1. Go to the page of the relevant Github repository
2. Click 'Fork' on the top right.
3. This will have cloned the repository to your Github account.

### Making a Local Clone

1. Go to the page of the relevant Github repository
2. Click on the 'Code' button.
3. Clone the repository using HTTPS by copying the link.
4. Open Git Bash.
5. Navigate to the directory where your clone will go.
6. Type ```git clone {your clone url}```
7. Press Enter.
8. Your local clone will be in the specified directory.

### Heroku

These are the steps used to deploy this application to Heroku:

- Create an account at [heroku.com](https://.heroku.com/)
- Create a new app with your app name and region.
- Click on create app.
- Go to Resources and search for/add Heroku Postgres.
- Navigate to the "Settings" tab on your app dashboard.
- Under Config Vars, add any sensitive data (creds.json for example)
- In the deploy tab, click 'Connect to Github'.
- Search for your repository and click connect.
- Choose the correct branch for your application
- If desired, click on "Enable Automatic Deploys", which updates the deployed version with the latest commit you have pushed to Github. 

## Credits

### Coding tips and tricks

1. [u/Lushac on Reddit](https://www.reddit.com/r/WebdevTutorials/comments/q8k8mu/image_inside_text_using_html_and_css/) - Background clip css trick on text

### Acknowledgments

Thank you to the Code Institute Slack Community for the help with small problems. Thanks to Midoca, Below Human and Megan Nolan for giving their reviews for the website. 