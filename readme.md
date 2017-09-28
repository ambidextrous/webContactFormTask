# Web Contact Form

## Accessing form

Once cloned and set up, the form can be reached at `http://127.0.0.1:8000/email/`

## Screenshots

![Screenshot of web contact form](https://github.com/ambidextrous/webContactFormTast/blob/master/contact.png "Web contact form")

Web contact form

![Screenshot of 'Thank you' page](https://github.com/ambidextrous/webContactFormTask/blob/master/thanks.png "Thank you page")

'Thank you' page

## Automatic Email Sending

As set up the form will send confirmation emails to the user and to any administrators listing  in `settings.py`. These messages are sent via a throw-away gmail account. To have the form print emails to the console instead, go to `django_contact_form/setting.py` and uncomment the line:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

A new thread is created to send the emails to speed up the transition to the 'Thank You' page.

## Design choices

1. I decided to use Django's built-in forms instead of coding my own as they're tried and tested, meet all of the given requirments and come with additional security features such as CSRF tokens. 

2. I've tried to keep the everything as simple as possible while still meeting the given requirments and not get carried away with gold-plating things.

3. This is not production quality code. A lot of Django / web development best practice has not been implemented, as it seemed like overkill for a sample form. E.g. an email password has been left in the `settings.py` file, debug mode has been left on and CSS is included directly in the `base.html` template. If working on production code I would take care of such things.

## Testing

This task seemed a bit small for automatic tests, but it has been carefully checked against the given requirements manually.
