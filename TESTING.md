# Testing

## User Story Testing



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