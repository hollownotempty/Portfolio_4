# Testing

## Manual Testing

Testing the app was done manually by creating many users to create dummy data and submissions to make sure the app ran perfectly. This was done by creating profiles using different emails, logging in, making a submission and checking if the confirmation email was received on that account, the submission was visible in the submissions page on the admin account and that the user was able to go to their profile page to view, edit and delete their submission if they required. Here is a list of the tests ran during the development of this project. 

1. Creating new accounts to make sure the signup form worked properly. 
2. Logging in using the correct information to see if logging in worked. 
3. Using incorrect login information to make sure it didn't allow an unregistered user in. 
4. Making submissions under different accounts to make sure the submissions were attributed to their usernames on the backend (this was checked in the django admin panel)
5. Making submissions to see if the email capabilities worked properly and that an automatic email was sent to the user. 
6. Logging in and out to make sure the views worked and that the logged in state was presented differently to the logged out. 
7. Searching the urls to admin-only pages to make sure that if a user who wasn't an admin managed to find those urls that they would not be able to access the page. 
8. Editing submissions repeatedly on a user profile page to make sure that edits took effect and were presented in their new state to the user.
9. Creating and then deleting submissions from the front-end to make sure that they were removed properly from the database. 
10. Javascript carousel was tested on different devices to make sure it could be swiped with a finger or clicked
11. Javascript Sidenav had to be tested on a few different mobile devices to make sure it implemented properly (these included an iphone, samsung galaxy, ipad, ipod touch and ipad mini)

## User Story Testing

1. As a {USER}, I want {TO CONTACT THE PRODUCER}, so that {I CAN GET THEM TO WORK ON MY MUSIC}.
    <br>
    1. User goes to the site 

    2. User creates an account or logs in

    3. User goes to the submit page

    4. User fills out form and hits submit

2. As a {admin}, I want {TO BE ABLE TO VIEW/MANAGE SUBMITTED INFO}, so that {I CAN KEEP CONTROL OVER THEM}.
    <br>
    1. Admin goes to the site

    2. Admin logs into their superuser account

    3. Admin navigates to 'Submissions' page

3. As a {user and admin}, I want {TO RECEIVE AN EMAIL CONFIRMING MY SUBMISSION}, so that {I CAN BE INFORMED WHEN IT GOES THROUGH}.
    <br>
    This is acheived by this view 
    ```
    def submit_page(request):

        if request.method == 'POST':
            form = SubmitForm(request.POST)
            if form.is_valid:
                instance = form.save()
                instance.user = request.user
                instance.save()
                # The following code sends an email upon form completion to the 
                # email corresponding with the currently logged in user.
                email = instance.user.email
                subject, from_email, recipient_list = 'Your Submission', settings.EMAIL_HOST_USER, [email, ]
                text_content = plaintext_message.render()
                html_content = html_message.render()
                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.success(request, 'Contact request submitted successfully.')
                return redirect('submit')

4. As a {USER}, I want {TO UPLOAD A LINK TO MY FILES}, so that {THE ADMIN CAN DOWNLOAD THEM}.
    <br>
    When the user fills out the form it includes a field for the user to add a link, which they can access again at a later date from their profile page. 

5. As a {ADMIN}, I want {TO BE ABLE TO SEND THE USERS THEIR FILES}, so that {THEY CAN HAVE THE FINISHED PROJECT}.
    <br>
    1. Admin goes to submissions page

    2. Admin locates the submission they want to find the user of

    3. Admin reads email on the submission

    4. Admin sends files to that email

6. As a {ADMIN}, I want {TO BE ABLE TO DOWNLOAD THE USERS STEMS}, so that {I CAN WORK ON THEIR PROJECT}.
    <br>
    1. Admin goes to submissions page

    2. Admin locates the necessary submission

    3. Admin clicks the file link

    4. Admin downloads files from the given link

8. As a {user}, I want {a page I can go to with all the info about my submission}, so that {I can cancel, reschedule or remind myself about my submission info}.
    <br>
    1. Users navigate to their profile page

    2. Under submission history they can find all their submissions

    3. Here they can change their submission or delete it. 

9. As a {USER}, I want {TO SEE TESTIMONIALS FROM PAST CLIENTS}, so that {I CAN SEE WHAT PEOPLE ARE SAYING BEFORE I HIRE THE PRODUCER}.
    <br>
    1. User navigates to home page
    2. User scrolls down and sees testimonials at the bottom

10. As a {ADMIN}, I want {THE SUBMISSIONS REVIEW PAGE TO BE PRIVATE}, so that {REGULAR USERS CANT SEE/DOWNLOAD OTHERS FILES}.
    <br>
    This is achieved with the Django template language to only display the info to a super user
    ```
        {% if user.is_superuser %}
            <div class="container">
                <h3>
                    Submissions
                </h3>
                <div class="row">
                    <!-- Renders all appointment objects in individual divs -->
                    {% for a in appointments %}
                    <div class="appointment-display col s12 ultralightblue-palette-color">
                            <p>Username: {{ a.user }}</p>
                            <p>Email: {{ a.user.email }}</p>
                            <a href="{{ a.file_link }}" class="links" target="_blank">Stems/Stereo File</a>
                            <p>Message: {{ a.message }}</p>
                            <a href="{% url 'delete_submission' a.id %}" class="btn delete-submission-btn">Delete Submission</a>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% else %}
                <div class="container">
                    <h1>
                        You are not an admin!
                    </h1>
                    <p>
                        You have insufficient privileges to access this page. 
                    </p>
                    <br>
                    <p><a href="{% url 'home' %}">Return Home</a></p>
                </div>
            {% endif %}

11. As a {USER}, I want {SITE MESSAGES UPON SITE ACTIONS}, so that {I CAN GET FEEDBACK IF I HAVE CORRENTLY OR INCORRECTLY USED THE SITE}.
    <br>

    This is done using Djangos built in messages. 
    ```
    {% if messages %}
        {% for message in messages %}
            <div id="messages">
                <div class="container">
                    {{ message }}
                </div>
            </div>
        {% endfor %}
    {% endif %}



## Bugs

- Upon deployment to heroku and opening the app, the user would be presented with an application error.

    <details>
    <summary>Solution</summary>
    <br>
    The config var containing the Cloudinary link still contained "CLOUDINARY_URL=" in the value. Once this was removed the application booted properly.
    </details>

- When trying to set up the ```send_mail()``` I was receiving an SMTPAuthenticationError (see screenshot).

    ![email_send_bug](screenshots/testing/email_send_bug.png)

    <details>
    <summary>Solution</summary>
    <br>
    This was solved firstly by going to my google account and turning on the setting `Allow Less Secure Apps'. I then had to go [here](https://g.co/allowaccess) to unblock the app and allow it to log. 
    </details>

- When creating the login and signup templates, they would render without the custom CSS with the following terminal error 
```Refused to apply style from <URL> because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled angular```
    <details>
    <summary>Solution</summary>
    <br>
    Providing ```{% load static %}``` at the beginning of base.html using template tags instead of manually writing the css path caused the css to render. This required me to go through 
    all of the existing media and switch it to a static link as well. 
    </details>

- Messages are meant to be displayed upon login or a failed login attempt. Login was successful as proven by the admin page opening up on the logged in profile, but the messages for failed login would not display on the login page 
    <details>
    <summary>Solution</summary>
    </details>

- This isn't necessarily a bug but due to Django's default User model using the username field to identify a user and the email field not being unique, multiple users are able to signup using the same email. Ideally both the username and the email would be unique.
    <details>
    <summary>Solution</summary>
    </details>