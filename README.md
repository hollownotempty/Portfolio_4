# Tom Holohan Audio

For the portfolio project I have created a site for clients to send their music a music producer to be mixed and mastered remotely. 

## Contents

1. [Strategy](#strategy)
   1. [Project Goals](#project-goals)
   2. [User Goals](#user-goals)
2. [Structure](#structure)
3. [Flowchart](#flowchart)
4. [User Stories](#user-stories)
   1. [Player User Stories](#player-user-stories)
5. [Technology Design](#technology-design)
   1. [User Interface](#user-interface)
6. [Technologies Used](#technologies-used)
   1. [Languages](#languages)
   2. [Applications](#applications)
   3. [Packages](#packages)
7. [Validation](#validation)
8. [Testing](#testing)
9. [Deployment](#deployment)
   1. [Forking the Github Repository](#forking-the-github-repository)
   2. [Making a Local Clone](#making-a-local-clone)
   3. [Heroku](#heroku)

## Strategy

### Project Goals

As a producer, a site like this makes handling clients easy. With an easy submission form users can submit their [stems](https://www.musicgateway.com/blog/how-to/stems-in-music-production-what-are-they-why-are-they-useful) to be mixed and mastered by a producer. This project originally started out as a system for booking calls, but ultimately the goal from a meeting is to start working on the music, right? After some thought about where the project was going I pivoted to a new system where clients can submit their music directly with notes and info about their project so that I can download the files from the site, get to work and send them back the finished project. 


### User Goals

User's are coming to this site to learn about the producer, hear some of their work, see some client testimonials and ultimately submit music to be mixed and/or mastered if they desire. 

## Structure

All pages on this site contain a nav bar and footer that contain links to the other pages on the site as well as social media links and small about section on the producer.

### Home

The home screen is simple enough. It contains:

   - A hero section with a tagline
   - A button that also leads to the submission page
   - Artist testimonials

### Login/Signup

A simple form system for the purpose of signing in and signing up.

### Submit Page

A page with one form on it that takes the users info along with their stems link. 

### Admin Appointments Page

A page for the admin that displays all the current submissions with the given details by the user.

## Flowchart

![Flowchart](static/images/flowchart/booking_flowchart.pdf)

## Wireframes

The wireframes for this project can be viewed [here](static/images/wireframes)

## User Stories
   1. As a {USER}, I want {TO CONTACT THE PRODUCER}, so that {I CAN GET THEM TO WORK ON MY MUSIC}.
   2. As a {admin}, I want {TO BE ABLE TO VIEW/MANAGE SUBMITTED INFO}, so that {I CAN KEEP CONTROL OVER THEM}.
   3. As a {user and admin}, I want {TO RECEIVE AN EMAIL CONFIRMING MY SUBMISSION}, so that {I CAN BE INFORMED WHEN IT GOES THROUGH}.
   4. As a {USER}, I want {TO UPLOAD A LINK TO MY FILES}, so that {THE ADMIN CAN DOWNLOAD THEM}.
   5. As a {ADMIN}, I want {TO BE ABLE TO SEND THE USERS THEIR FILES}, so that {THEY CAN HAVE THE FINISHED PROJECT}.
   6. As a {ADMIN}, I want {TO BE ABLE TO DOWNLOAD THE USERS STEMS}, so that {I CAN WORK ON THEIR PROJECT}.
   8. As a {user}, I want {a page I can go to with all the info about my appointment}, so that {I can cancel, reschedule or remind myself about my appointment info}.
   9. As a {USER}, I want {TO SEE TESTIMONIALS FROM PAST CLIENTS}, so that {I CAN SEE WHAT PEOPLE ARE SAYING BEFORE I HIRE THE PRODUCER}.
   10. As a {ADMIN}, I want {THE SUBMISSIONS REVIEW PAGE TO BE PRIVATE}, so that {REGULAR USERS CANT SEE/DOWNLOAD OTHERS FILES}.
   11. As a {USER}, I want {SITE MESSAGES UPON SITE ACTIONS}, so that {I CAN GET FEEDBACK IF I HAVE CORRENTLY OR INCORRECTLY USED THE SITE}.
   12. As a {ADMIN}, I want {THE CONFIRMATION EMAIL TO SEND AN INVOICE TO THE CLIENT}, so that {THEY CAN PAY FOR THE SERVICE USING PAYPAL}.

## Technology Design

### Data Models
   This project uses one main data model and that is the Appointment model. This is the model that logs all the info that the user gives in the ModelForm, including first name, last name, email, file link and the date it was booked. 

### User Interface
   The interface for this website did not need to be too complicated, as a simple site like this does not need to reinvent the wheel. Everything was styled using MaterializeCSS to keep a cohesive look. Users are also presented with djangos built in messages upon certain actions (such as loggin in, loggin out, submitting a form etc) to keep them informed on their journey through the site.

## Technologies Used

### Languages
   1. HTML
   2. CSS
   3. Javascript
   4. Python
   5. Django Template Language

### Frameworks
   1. [Django](https://www.djangoproject.com/) - The main framework used to create this project.
   2. [Materialize CSS](https://materializecss.com/) - Used for responsive and easy css. 

### Applications
   1. TinyPNG - Used to compress images
   2. Gitpod - Cloud based IDE used for development
   3. Heroku - Cloud platform used to host app
   4. [Pexels](https://www.pexels.com/) - Stock image site used to source images
   5. [Gradient Animator](https://www.gradient-animator.com/) - Used for creation of background gradients
   6. LucidChart - Used to create the flowchart for this project. 

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