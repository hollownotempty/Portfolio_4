# Testing

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