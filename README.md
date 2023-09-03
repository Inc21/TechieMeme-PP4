![TechieMeme Logo](/static/images/readme_images/techiememe_logo.png)
![mockup](/static/images/readme_images/mockup_dark.png)


# Introduction

TechieMeme is a website meant to lighten up people's day who like technology or related things. Like Code, science, maths or hardware as an example. Inspiration for this site came from the Code Institute Slack channel **community-tech-humour**, which I really love. On this site, the user can view, like and comment on the memes that they like or upload their own memes and edit, or delete them if necessary. This website was created as a learning exercise for my [Code Institute](https://codeinstitute.net/ie/) fourth portfolio project. 


The live app can be found [here.](https://techiememe-50a6f4eb45eb.herokuapp.com/ "TechieMeme.")

Admin panel can be found [here.](https://techiememe-50a6f4eb45eb.herokuapp.com/admin/login/?next=/admin/ "TechieMeme Admin Panel.")


### Project Goals
- To create a website that is easy to navigate and use.
- To create a website that is visually appealing.
- To create a website that is responsive on all devices.
- To create a website that is interactive.
- To create a website that is fun to use.
- To create a website that is easy to use.


# User Stories

### First Time Visitor Goals
1. As a user, I want to be able to view the site on any device I choose.
2. As a user, I want to be able to easily navigate the site.
3. As a user, I want to be able to easily find the content I am looking for.
4. As a user, I want to be able to easily register for an account.
5. As a user, I want to be able to easily log in and out of my account.
6. As a user, I want to be able to easily recover my password if I forget it.
7. As a user, I want to be able to easily view other user's profiles.
8. As a user, I want to be able to easily search for memes.


### Authenticated User Goals
9. As an authenticated user, I want to be able to easily upload my own memes.
10. As an authenticated user, I want to be able to easily edit my own memes.
11. As an authenticated user, I want to be able to easily delete my own memes.
12. As an authenticated user, I want to be able to easily like memes.
13. As an authenticated user, I want to be able to easily comment on memes.
14. As an authenticated user, I want to be able to report memes.
15. As an authenticated user, I want to be able to easily contact the developer.
16. As a user, I want to be able to easily view my profile.
17. As an authenticated user, I want to be able to easily edit my profile.
18. As an authenticated user, I want to be able to easily delete my profile.


### Site owner objectives
19. As a site owner, I want to be able to log into the admin panel.
20. As a site owner, I want to be able to easily manage memes in case of inappropriate content.
21. As a site owner, I want to be able to easily manage users in case of inappropriate content.
22. As a site owner, I want to be able to provide a fun and easy-to-use website.


# Design

### Look and feel

With the design for this website, the aim was to create a fun and easy-to-use website. The main colours were chosen from black to emoji icon yellow. Had to add some CSS text-shadow trickery to improve the contrast on the light background. Also to improve accessibility for people with visual impairments some of the meme text was changed to darker yellow. 


### Colour

The colour palette was chosen and made on [Coolors](https://coolors.co/).

![Color Palette](/static/images/readme_images/palette.png)


### Typography

- [Google Fonts](https://fonts.google.com/) was used for the font.

Font Lexend was chosen for the site. This font was chosen because it is easy to read and looks good on all devices. By using this font the site is more accessible for people with visual impairments whilst. Two font weights are used, 400 and 700. 400 is used for the main text and 700 is used for the logo and some headings where **bold** text is required. Fall back font is Sans-serif.

| Font Weight 400 | Font Weight 700 |
| --- | --- |
| ![Lexend 400](/static/images/readme_images/lexend_400.png) | ![Lexend 700](/static/images/readme_images/lexend_700.png) |


### Wireframes

#### Desktop Wireframe

Didn't stray too far from the original wireframe. Only a few small things. Text on the footer, and banner and added carousel to the main page instead of pagination as it is on all the other pages.

![Desktop wireframe](/static/images/readme_images/desktop_wireframe.png)


#### Mobile Wireframe

![Mobile wireframe](/static/images/readme_images/mobile_wirframe.png)


# Database Schemas

![Database Schema](/static/images/readme_images/database_schema.png)


### User model

- The user model is the default Django user model.

| key | Field Type | Validation |
| --- | --- | --- |
| id | IntegerField | |
| password | CharField |  |
| last_login | DateTimeField |  |
| is_superuser | BooleanField |  |
| username | CharField | max_length=150, unique=True |
| first_name | CharField | max_length=150, blank=True |
| last_name | CharField | max_length=150, blank=True |
| email | EmailField | max_length=254, unique=True |
| is_staff | BooleanField |  |
| is_active | BooleanField |  |
| date_joined | DateTimeField |  |


### UserProfile model - users app

- UserProfile model is connected to the User model with OneToOneField. This model is used to store extra user information.

| key | Field Type | Validation |
| --- | --- | --- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| username | CharField | max_length=50, null=True, blank=True |
| first_name | CharField | max_length=50, null=True, blank=True |
| last_name | CharField | max_length=50, null=True, blank=True |
| location | CharField | max_length=100, null=True, blank=True |
| email | EmailField | max_length=100, null=True, blank=True |
| bio | TextField | max_length=500, null=True, blank=True |
| user_image | ResizedImageField | upload_to='users/', null=True, force_format='WEBP', quality=85, blank=True, default='users/default_user.webp' |
| social_github | URLField | max_length=200, null=True, blank=True |
| social_linkedin | URLField | max_length=200, null=True, blank=True |
| social_facebook | URLField | max_length=200, null=True, blank=True |
| social_youtube | URLField | max_length=200, null=True, blank=True |
| social_website | URLField | max_length=200, null=True, blank=True |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |


### Meme model - memes app

- The meme model is used to store all the memes uploaded by users.

| key | Field Type | Validation |
| --- | --- | --- |
| uploader | ForeignKey | UserProfile, on_delete=models.CASCADE |
| title | CharField | max_length=100, null=True |
| meme_img | ResizedImageField | upload_to='memes/', null=True, force_format='WEBP', quality=85, blank=True, default='memes/default.webp |
| tags | ManyToManyField | Tag, blank=True |
| smiley_face | ManyToManyField |  UserProfile, related_name='smiley_face' |
| sad_face | ManyToManyField |  UserProfile, related_name='sad_face', blank=True |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |


### Comment model - memes app

- The Comment model is used to store all the comments on the memes.

| key | Field Type | Validation |
| --- | --- | --- |
| meme | ForeignKey | Meme, on_delete=models.CASCADE, related_name='comment' |
| user | ForeignKey | UserProfile, on_delete=models.CASCADE, null=True, blank=True |
| comment | TextField | max_length=500 |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |


### Tag model - memes app

- Tag model is used to store all the tags for the memes.

| key | Field Type | Validation |
| --- | --- | --- |
| name | CharField | max_length=20, null=True, blank=True |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |


### ContactForm model - memes app

- The contactForm model is used to store all the contact forms sent to developers by users.

| key | Field Type | Validation |
| --- | --- | --- |
| name | CharField | max_length=100, null=True |
| email | EmailField | max_length=250, null=True |
| subject | CharField | max_length=150, null=True |
| message | TextField | max_length=500, null=True |
| created | DateTimeField | auto_now_add=True |
| id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False |


# Agile Development

Link to my [GitHub Agile Project](https://github.com/users/Inc21/projects/6)

As it is my first time using Agile Development, I decided to use the [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) and [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) prioritization method. I used [GitHub Projects](https://github.com/users/Inc21/projects/6) to create the board. 

Did find it a bit difficult to use at first but after a while, I got the hang of it. As a solo developer who is time-constrained, I found it a bit time-consuming to create all the Epics and User stories. However, I can see the benefits of using this method in a team environment. As of now, I will continue to use this method for my future projects and I hope to learn more about it. My first-ever hackathon is coming soon where I will be working in a team and I will be surely using the Agile method.

I created 4 columns, Epics, To-Do, In Progress and Done. I also created 9 labels:

- For MoSCoW prioritization: Must Have, Should Have, Could Have, Won't Have.

![Must Have](/static/images/readme_images/labels/must-have.png) ![Should Have](/static/images/readme_images/labels/should-have.png) ![Could Have](/static/images/readme_images/labels/could-have.png) ![Won't Have](/static/images/readme_images/labels/wont-have.png)

- And 5 helper labels: Dev-task, Epic, User-story, In-progress, Done.

![Dev-task](/static/images/readme_images/labels/dev-task.png) ![Epic](/static/images/readme_images/labels/epic.png) ![User-story](/static/images/readme_images/labels/user-story.png) ![In-progress](/static/images/readme_images/labels/in-progress.png) ![Done](/static/images/readme_images/labels/done.png)

- Created 9 Epics divided into 24 User stories. Epics and user stories are connected with the # link on the title and in the description.

| Example | Image |
| --- | --- |
| Epic | ![Epic](/static/images/readme_images/epic_example.png) |
| User story | ![User story](/static/images/readme_images/user_story_example.png) |

- My Kanban board:

| then | now |
| --- | --- |
| ![Kanban board](/static/images/readme_images/agile_kanban_board.png) | ![Kanban board](/static/images/readme_images/kanban.png) |


# Tools and technologies used

### Languages and Frameworks

This project was created using the following languages and frameworks:

- [Django](https://www.djangoproject.com/) as the Python web framework.
    - [Python](https://www.python.org/) as the backend programming language.
- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
    - [Bootstrap 5](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.
    - [jQuery](https://jquery.com/) to simplify DOM manipulation.
    

### Django Packages

Django installs a few packages by default and some packages get installed with other packages. Will list out the ones that I installed.

| Packages | Description (copied from the web) |
| :--- | --- |
| [boto3](https://pypi.org/project/boto3/) | Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. You can find the latest, most up-to-date, documentation at our doc site, including a list of services that are supported. |
| [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) | django-crispy-bootstrap5 provides you with a crispy-forms template pack to use with django-crispy-forms in your Django projects. |
| [Django](https://pypi.org/project/Django/) | Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. |
| [django-allauth](https://pypi.org/project/django-allauth/) | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. |
| [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) | django-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behaviour of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application. |
| [django-resized](https://pypi.org/project/django-resized/) | Django-resized is the best approach to resize and convert images. It is a Django app that allows easy image resizing using the easy-thumbnails app as a backend. |
| [django-storages](https://pypi.org/project/django-storages/) | Django Storages is a collection of custom storage backends for Django. |
| [Pillow](https://pypi.org/project/Pillow/) | PIL is the Python Imaging Library. |
| [psycopg2](https://pypi.org/project/psycopg2/) | Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s. |
| [waitress](https://pypi.org/project/waitress/) | Waitress is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library. It runs on CPython on Unix and Windows under Python 2.7+ and Python 3.5+. It is also known to run on PyPy 1.6.0 on UNIX. It supports HTTP/1.0 and HTTP/1.1. |
| [whitenoise](https://pypi.org/project/whitenoise/) | With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (It can still optionally do all that if you want, though.) |


### Other tools and programs.

- [Amazon AWS S3](https://aws.amazon.com/) was used to store static and media files.
- [Amazon AWS IAM](https://aws.amazon.com/iam/) was used to create a user for the project.
- [Amazon RDS](https://aws.amazon.com/rds/) was used to create a PostgreSQL database.
- [Font Awesome](https://fontawesome.com/) was used for all icons.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Coolors](https://coolors.co/) was used to create the colour palette.
- [Favicon.io](https://favicon.io/) was used to create the favicon.
- [Birme](https://www.birme.net) was used to convert static images to .webp format.
- [ami.responsivedesign.is](http://ami.responsivedesign.is/) was used to create the mockup image.
- [Lucid](https://lucid.co/) was used when creating database ERD.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.


# Features

<details>
  <summary>Existing Features</summary>

- All pages are responsive on all devices.
- All pages feature a header with the site logo and a navigation bar with links to other pages, login/sign-up links and a search bar. 
- All pages feature a footer with links to contact the developer (It sends admin an e-mail).
- All user actions are confirmed with Django messages.
- All user-uploaded content will be automatically converted to .webp format to save space and bandwidth using [Django-resized](https://pypi.org/project/django-resized/).  

![Django messages](/static/images/readme_images/existing_features/messages.png)


### Home Page

- The home page is the first page the user sees when they visit the site.
- The Page will have a welcome message and a button to take the user to the upload meme page or sign up if the user is not authenticated.
- The user can see the latest memes uploaded by other users on the Bootstrap carousel. 

![Home Page](/static/images/readme_images/existing_features/home_page.png)  


### Memes Page

- The Meme page is where the user can see all the memes uploaded by other users.
- Page will have 4 meme cards per page and the rest will be paginated.
- The User can click on the meme card to see the single meme page.

![Memes Page](/static/images/readme_images/existing_features/memes_page.png)


### Delete Meme Confirmation Page

- The Delete meme confirmation page is where the user can confirm that they want to delete the meme.

![Delete Meme Confirmation Page](/static/images/readme_images/existing_features/delete_meme_confirmation_page.png)


### Single Meme Page

- The Single meme page is where the user can see the single meme.
- User can see the meme title, meme image, meme description, meme category, meme author, meme date uploaded, meme likes, meme comments.
- If the user is the uploader of the meme they will see the edit and delete buttons.
- Authenticated user can comment on the meme and delete their own comments.

![Single Meme Page](/static/images/readme_images/existing_features/single_meme_page.png)


### Report Meme Page

- Report meme page is where the user can report the meme.
- Page has a form with the title of the meme link clicked on, name of the user, email of the user and the reason for reporting the meme.
- The Page also has a back button to take the user back to the single meme page in case they don't want to report the meme.
- This form will send an email to the admin with the details of the report and more details about the authenticated user in case of a malicious report.

![Report Meme Page](/static/images/readme_images/existing_features/report_meme.png)


### Users Page 

- The Users page is where the user can see all the users.
- Page will have 4 user cards per page and the rest will be paginated.
- The User can click on the user card to see the single-user page.

![Users Page](/static/images/readme_images/existing_features/users_page.png)


### Single User Page

- The Single user page is where the user can see the single user.
- User can see the user username, user profile image, user bio, user date joined, last login, user memes, user email, and user social links if provided.
- If the user is the owner of the profile they will see the edit and delete buttons.

![Single User Page](/static/images/readme_images/existing_features/single_user_page.png)


### Edit Profile Page

NB: The page is zoomed out to show the whole page.

- Edit profile page is where the user can edit their profile.
- Page has a pre-populated form with the profile image, first name, last name, location, user email, user bio and user social links.
- The Page also has a back button to take the user back to the single user page in case they don't want to make any changes.

![Edit Profile Page](/static/images/readme_images/existing_features/update_profile_page.png)


### Delete Profile Confirmation Page

NB: This page is only available to the user who owns the profile.
- Delete profile confirmation page is where the user can confirm that they want to delete their profile.
- The Page has a message to confirm that the user wants to delete their profile.
- The Page also has a back button to take the user back to the single-user page in case they don't want to delete their profile.

![Delete Profile Confirmation Page](/static/images/readme_images/existing_features/delete_confirmation_page.png)


### Upload Meme / Edit Meme Page
NB: The page is zoomed out to show the whole page. This page is the same for both upload and edit memes with the edit meme instance pre-populated with current details.
- The Upload meme page is where the user can upload their own memes.
- Page has a form with the meme image, meme title and meme tags.
- The Page also has a back button to take the user back to the memes page in case they don't want to upload/edit a meme.

![Upload Meme Page](/static/images/readme_images/existing_features/upload_meme_page.png)


### Login Page

- The Login page is where the user can log into their account.
- Page has a form with the username and password fields.
- Page has a link to the sign-up page in case the user doesn't have an account and social sign-up links to Google and GitHub.
- Page has a "Forgot password?" link to take the user to the password reset page in case they can't remember their current password.

![Login Page](/static/images/readme_images/existing_features/login_page.png)


### Password Reset Page

- The Password reset page is where the user can reset their password.
- Page has a form with the email field.
- Password reset only works if the user signed up with a valid email address.

![Password Reset Page](/static/images/readme_images/existing_features/password_reset_page.png)


### Logout Page

- The Logout page is where the user can log out of their account.
- The Page has a message to confirm that the user wants to log out.

![Logout Page](/static/images/readme_images/existing_features/logout_page.png)


### Sign-up Page

- The Sign-up page is where the user can sign up for an account.
- Page has a form with the username, email, password1 and password2 fields.
- The Page has a link to the login page in case the user already has an account.
- When the user registers for an account and uses email, they will receive a welcome email and confirmation email with a link to confirm their email address.
- When the user won't upload a profile image, a default image will be used.

| Sign-up Page | Welcome Email | Confirm Email |
| --- | --- | --- |
| ![Sign-up Page](/static/images/readme_images/existing_features/signup_page.png) | ![Welcome Email](/static/images/readme_images/existing_features/welcome_email.png) | ![Confirmation Email](/static/images/readme_images/existing_features/confirmation_email.png) |

|Redirect to edit profile page | Default profile image |
| --- | --- |
| ![Redirect to edit profile page](/static/images/readme_images/existing_features/after_signup.png) | ![Default profile image](/static/images/readme_images/existing_features/default_user_image.png) |


### Contact Developer Page

- Contact developer (link on the footer) page is where the user can contact the developer.
- Page has a form with the user name, email, subject and message fields.
- This page is only available to authenticated users.
- This form will send an email to the developer with the details of the message and more details about the authenticated user.
- The Page also has a back button to take the user back to the home page in case they don't want to contact the developer.

![Contact Developer Page](/static/images/readme_images/existing_features/contact_developer_page.png)


### Custom Error 404 Page

- The 404 page is where the user will be redirected if they try to access a page that doesn't exist.

![404 Page](/static/images/readme_images/existing_features/custom_404_500_page.png)


### Custom Error 500 Page

- The 500 page is where the user will be redirected if there is an internal server error.

![500 Page](/static/images/readme_images/existing_features/error_500.png)


</details>


## Features Left to Implement

- Give some users admin rights to manage memes and users.
- Add an option for a user to add their own custom tags to the meme.
- Add a private messaging feature between users.
- Improve search functionality (search by user name. Currently you can search only users who have uploaded a meme).
- Improve privacy controls and hide some details from other users. 
    

# Testing

## Code Validation

### Google lighthouse Validation

All pages were tested with [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/). Testing was performed in private browsing mode and on the live website on Heroku.

| Page | Image |
| --- | --- |
| Home Page | ![Google lighthouse](/static/images/readme_images/lighthouse/home_page.png) |
| Memes Page | ![Google lighthouse](/static/images/readme_images/lighthouse/memes.png) |
| Single Meme Page | ![Google lighthouse](/static/images/readme_images/lighthouse/single_meme.png) |
| User Page | ![Google lighthouse](/static/images/readme_images/lighthouse/users.png) |
| Single User Page | ![Google lighthouse](/static/images/readme_images/lighthouse/single_user.png) |
| Upload Meme Page | ![Google lighthouse](/static/images/readme_images/lighthouse/upload_meme.png) |
| Login Page | ![Google lighthouse](/static/images/readme_images/lighthouse/login.png) |
| Logout Page | ![Google lighthouse](/static/images/readme_images/lighthouse/logout.png) |
| Contact Developer Page | ![Google lighthouse](/static/images/readme_images/lighthouse/contact_developer_form.png) |
| Report Meme Page | ![Google lighthouse](/static/images/readme_images/lighthouse/report_meme.png) |


### CSS Validation
- No errors were found when passing through the official [W3C](https://validator.w3.org/) validator.
![CSS Validator](/static/images/readme_images/css_validator.png)


### HTML Validation

- All pages were passed through the official [W3C](https://validator.w3.org/nu/) validator.
- Validating was done by a live website on Heroku. Some errors were found but they are all related to Django templates.

| Page | Image |
| --- | --- |
| Home Page | ![HTML Validator](/static/images/readme_images/html_validator/home.png) |
| Memes Page | ![HTML Validator](/static/images/readme_images/html_validator/memes.png) |
| Single Meme Page  ("info" label because image coming from Amazon S3 bucket service ) | ![HTML Validator](/static/images/readme_images/html_validator/single_meme.png) |
| User Page | ![HTML Validator](/static/images/readme_images/html_validator/users.png) |
| Single User Page.  | ![HTML Validator](/static/images/readme_images/html_validator/single_user.png) |
| Code was checked and then checked again no extra ```</P>``` can't be found where W3C validator is reporting it.   | ![HTML Validator](/static/images/readme_images/html_validator/single_user_error.png) |
| Upload Meme Page  (Django ModelForm creating a trailing slash) | ![HTML Validator](/static/images/readme_images/html_validator/upload_meme.png) |
| Login Page | ![HTML Validator](/static/images/readme_images/html_validator/login.png) |
| Sign-up Page | ![HTML Validator](/static/images/readme_images/html_validator/signup.png) |
| Contact Developer Page   (Django ModelForm creating a trailing slash) | ![HTML Validator](/static/images/readme_images/html_validator/contact_developer.png) |
| Report Meme Page   ("info" label because image coming from Amazon S3 bucket service) | ![HTML Validator](/static/images/readme_images/html_validator/report_meme.png) |


### JavaScript Validation

- All JavaScript files were passed through the official [JSHint](https://jshint.com/) validator.

| File | Image |
| --- | --- |
| script.js (Bootstrap carousel on index.html or "Home" page)| ![JSHint Validator](/static/images/readme_images/jshint.png) |


### PEP8 Code Institute Python Linter Validation

- All Python files were passed through the Code Institute [PEP8](https://pep8ci.herokuapp.com/) validator.


#### Techmeme project app

| File | Result |
| --- | --- |
| settings.py | ![PEP8 Linter](/static/images/readme_images/pep8_clear.png) |
| urls.py | All clear, no errors found |


#### memes app

| File | Result |
| --- | --- |
| admin.py | All clear, no errors found |
| apps.py | All clear, no errors found |
| forms.py | All clear, no errors found |
| models.py | All clear, no errors found |
| urls.py | All clear, no errors found |
| views.py | All clear, no errors found |


#### users app

| File | Result |
| --- | --- |
| admin.py | All clear, no errors found |
| apps.py | All clear, no errors found |
| forms.py | All clear, no errors found |
| models.py | All clear, no errors found |
| urls.py | All clear, no errors found |
| views.py | All clear, no errors found |


 # Manual Testing

 <details>
  <summary>Manual Testing</summary>


### Devices and browsers used for testing

This website was developed on a Dell Windows 10 desktop computer using Visual Studio Code. Testing was done on the following devices and browsers:
| Device | Browser | Result |
| --- | --- | --- |
| Dell Windows 10 desktop computer | Google Chrome | Works as expected |
| Dell Windows 10 desktop computer | Microsoft Edge | Works as expected |
| Dell Windows 10 desktop computer | Mozilla Firefox | Works as expected |
| Dell Windows 10 desktop computer | Opera | Works as expected |
|HP Windows 11 laptop 13" Screen | Google Chrome | Works as expected |
|HP Windows 11 laptop 13" Screen | Microsoft Edge | Works as expected |
|HP Windows 11 laptop 13" Screen | Mozilla Firefox | Works as expected |
| Apple iPhone 12 | Safari | Works as expected |
| Apple iPhone 12 | Google Chrome | Works as expected |
| Apple iPhone 12 | Mozilla Firefox | Works as expected |
| Apple iPhone 13 | Safari | Works as expected |
| Apple iPad 10th generation | Safari | Works as expected |


### User Stories Testing

| Expectation | Solution | Image |
| --- | --- | --- |
| As a user, I want to be able to view the site on any device I choose.| Thorough testing was done on all devices and browsers listed above. | |
| As a user, I want to be able to easily navigate the site. | The navigation bar is fixed to the top of the page and is visible on all pages. | ![Navigation bar](/static/images/readme_images/manual_testing/navigation_bar.png) |
| As a user, I want to be able to easily find the content I am looking for. | All pages have a search bar in the navigation bar. | ![Search bar](/static/images/readme_images/manual_testing/search_bar.png) |
| As a user, I want to be able to easily register for an account. | Sign-up button is in the navigation bar and available on all pages. | ![Sign-up button](/static/images/readme_images/manual_testing/signup_button.png) |
| As a user, I want to be able to easily log in and out of my account. | Login and logout buttons are in the navigation bar and available on all pages. | ![Login button](/static/images/readme_images/manual_testing/login_button.png) ![Logout button](/static/images/readme_images/manual_testing/logout_button.png) |
| As a user, I want to be able to easily recover my password if I forget it. | The Forgot password link is provided on the login page. | ![Forgot Password link](/static/images/readme_images/manual_testing/forgot_password_link.png) |
| As a user, I want to be able to easily view other user's profiles. | Users page is available to all users. | ![Users page](/static/images/readme_images/existing_features/users_page.png) |
| As a user, I want to be able to easily search for memes. | Search bar is available on all pages. The memes page is available for all users | ![Search bar](/static/images/readme_images/manual_testing/search_bar.png) |
| As an authenticated user, I want to be able to easily upload my own memes. | The Upload meme button is available on the navigation bar and on all pages. | ![Upload meme button](/static/images/readme_images/manual_testing/upload_meme_button.png) |
|  As an authenticated user, I want to be able to easily edit my own memes. | The Edit button is available on a single meme page. | ![Edit button](/static/images/readme_images/manual_testing/edit_button.png) |
| As an authenticated user, I want to be able to easily delete my own memes. | Delete button is available on single meme page and on single users page. | ![Delete button](/static/images/readme_images/manual_testing/delete_button.png) |
| As an authenticated user, I want to be able to easily like memes. | Like or smiley face button is available on all meme cards, all memes, single memes, page, home page and single users memes | ![Like button](/static/images/readme_images/manual_testing/like_button.png) |
| As an authenticated user, I want to be able to easily comment on memes. | Comment box is available on a single meme page. | ![Comment button](/static/images/readme_images/manual_testing/comment_button.png) |
As an authenticated user, I want to be able to report memes. | Report button is available on every meme card. | ![Report button](/static/images/readme_images/manual_testing/report_button.png) |
|  As an authenticated user, I want to be able to easily contact the developer. | The Contact Developer link is available on the footer and on all pages. | ![Contact developer link](/static/images/readme_images/manual_testing/contact_developer_link.png) |
| As a user, I want to be able to easily view my profile. | The current user profile button is available on the navigation bar by the login/logout buttons. | ![Profile button](/static/images/readme_images/manual_testing/profile_button.png) |
| As an authenticated user, I want to be able to easily edit my profile. | The Edit profile button is available on the single-user page. | ![Edit Profile button](/static/images/readme_images/manual_testing/edit_profile_button.png) |
| As an authenticated user, I want to be able to easily delete my profile. | The Delete profile button is available on the single-user page. | ![Delete profile button](/static/images/readme_images/manual_testing/edit_profile_button.png) |
| As a site owner, I want to be able to log into the admin panel. | Admin panel is available by entering /admin at the end of the URL. | ![Admin panel](/static/images/readme_images/manual_testing/admin_panel.png) |
| As a site owner, I want to be able to easily manage memes in case of inappropriate content. | Admin panel is available by entering /admin at the end of the URL. From there, the website admin can delete any meme | ![Admin panel](/static/images/readme_images/manual_testing/admin_panel_page.png) |
| As a site owner, I want to be able to easily manage users in case of inappropriate content. | Admin panel is available by entering /admin at the end of the URL. From there, the website admin can delete any user | ![Admin panel](/static/images/readme_images/manual_testing/admin_panel_page.png) |
| As a site owner, I want to be able to provide a fun and easy-to-use website. | All of the above. | ![techiememe](/static/images/readme_images/existing_features/home_page.png) |


### Home Page Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on  the main logo in the navigation bar. | User is taken to the home page. | Working as expected. | ![Home Page](/static/images/readme_images/manual_testing/home_page.png) |
| User clicks on the "Home" link in the navigation bar. | User is taken to the home page. | Working as expected. |  |
| User clicks on the "Memes" link in the navigation bar. | User is taken to the memes page. | Working as expected. | ![Memes Page](/static/images/readme_images/manual_testing/memes_page.png) |
| User clicks on the "Users" link in the navigation bar. | User is taken to the user's page. | Working as expected. | ![Users Page](/static/images/readme_images/existing_features/users_page.png) |
| User clicks on the "Upload Meme" link in the navigation bar. | User is taken to the upload meme page. | Working as expected. | ![Upload Meme Page](/static/images/readme_images/existing_features/upload_meme_page.png) |
| User clicks on the "Login" link in the navigation bar. | User is taken to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |
| User clicks on the "Sign-up" link in the navigation bar. | User is taken to the sign-up page. | Working as expected. | ![Sign-up Page](/static/images/readme_images/existing_features/signup_page.png) |
| Logged in user clicks on the "Logout" link in the navigation bar. | User is taken to the logout page. | Working as expected. | ![Logout Page](/static/images/readme_images/existing_features/logout_page.png) |
| User clicks on the "Contact Developer" link in the footer. | User is taken to the contact developer page. | Working as expected. | ![Contact Developer Page](/static/images/readme_images/existing_features/contact_developer_page.png) |
| User clicks on the "Sign up and join the fun" call to action button. | User is taken to the sign-up page. | Working as expected. | ![Sign-up Page](/static/images/readme_images/existing_features/signup_page.png) |
| Authenticated user clicks on the "Upload Meme" call to action button. | User is taken to the upload meme page. | Working as expected. | ![Upload Meme Page](/static/images/readme_images/existing_features/upload_meme_page.png) |
| User clicks on the "Report" button on the meme card. | User is taken to the report meme page. | Working as expected. | ![Report Meme Page](/static/images/readme_images/existing_features/report_meme.png) |
| If the user is not signed in click on the "Report" button on the meme card. | User is taken to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |
|Authenticated User clicks on the "smiley face" or a "sad face" button on the meme card. | Corresponding emoji count goes up by one. | Working as expected. | ![Like button](/static/images/readme_images/manual_testing/like_button.png) |
| If the user is not signed in click on the "smiley face" or a "sad face" button on the meme card. | Info message is displayed. | Working as expected. | ![Info message](/static/images/readme_images/manual_testing/like_message.png) |
| User clicks anywhere on the meme image or title. | User is taken to the single meme page. | Working as expected. | ![Single Meme Page](/static/images/readme_images/existing_features/single_meme_page.png) |
| User clicks on the "uploader" link on the meme card. | User is taken to the single user page. | Working as expected. | ![Single User Page](/static/images/readme_images/existing_features/single_user_page.png) |
| User clicks on the arrow to the right of the carousel. | Carousel moves to the next meme. | Working as expected. | ![Carousel](/static/images/readme_images/manual_testing/carousel.png) |
| User clicks on the arrow to the left of the carousel. | Carousel moves to the previous meme. | Working as expected. | ![Carousel](/static/images/readme_images/manual_testing/carousel.png) |


### Memes Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks anywhere on the meme image or title. | User is taken to the single meme page. | Working as expected. | ![Single Meme Page](/static/images/readme_images/existing_features/single_meme_page.png) |
| User clicks on the "uploader" link on the meme card. | User is taken to the single user page. | Working as expected. | ![Single User Page](/static/images/readme_images/existing_features/single_user_page.png) |
| User clicks on the pagination links. | User is taken to the next page. | Working as expected. | ![Pagination](/static/images/readme_images/manual_testing/pagination_links.png) |
| Authenticated user clicks on the "smiley face" or a "sad face" button on the meme card. | Corresponding emoji count goes up by one. | Working as expected. | ![Like button](/static/images/readme_images/manual_testing/like_button.png) |
| If the user is not signed and clicks on the "smiley face" or a "sad face" button on the meme card. | Info message is displayed. | Working as expected. | ![Info message](/static/images/readme_images/manual_testing/like_message.png) |
| User clicks on the comment icon on the meme card. | User is taken to the single meme page. | Working as expected. | ![Single Meme Page](/static/images/readme_images/existing_features/single_meme_page.png) |


### Single Meme Page Testing.

- The Navigation bar and footer are the same as on the home page.

##### Authenticated user and owner of the meme.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Edit" button. | User is taken to the edit meme page. | Working as expected. | ![Edit Meme Page](/static/images/readme_images/existing_features/upload_meme_page.png) |
| User clicks on the "Delete" button. | User is taken to the delete meme confirmation page. | Working as expected. | ![Delete Meme Confirmation Page](/static/images/readme_images/existing_features/delete_meme_confirmation_page.png) |

##### Authenticated user and not the owner of the meme.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters comment in the comment box and clicks on the "Comment" button. | Comment is added to the comments section. | Working as expected. | ![Comment button](/static/images/readme_images/manual_testing/comment_button.png) |
| User clicks on the uploader link. | User is taken to the single user page. | Working as expected. | ![Single User Page](/static/images/readme_images/existing_features/single_user_page.png) |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Memes Page](/static/images/readme_images/manual_testing/back_button.png) |
| User clicks on the "Report" button. | User is taken to the report meme page. | Working as expected. | ![Report Meme Page](/static/images/readme_images/existing_features/report_meme.png) |
| User clicks on the "smiley face" or a "sad face" button. | Corresponding emoji count goes up by one. | Working as expected. | ![Like button](/static/images/readme_images/manual_testing/like_button.png) |

##### Not authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Memes Page](/static/images/readme_images/manual_testing/back_button.png) |
| User clicks on the "Report" button. | User is redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |
| User clicks on the "smiley face" or a "sad face" button. | Info message is displayed. | Working as expected. | ![Info message](/static/images/readme_images/manual_testing/like_message.png) |


### Users Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks anywhere on the user image or username. | User is taken to the single user page. | Working as expected. | ![Single User Page](/static/images/readme_images/existing_features/single_user_page.png) |
| User clicks on the pagination links. | User is taken to the next page. | Working as expected. | ![Pagination](/static/images/readme_images/manual_testing/pagination_links.png) |


### Single User Page Testing.

- The Navigation bar and footer are the same as on the home page.

##### Authenticated user and owner of the profile.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Edit" button. | User is taken to the edit profile page. | Working as expected. | ![Edit Profile Page](/static/images/readme_images/existing_features/update_profile_page.png) |
| User clicks on the "Delete" button. | User is taken to the delete profile confirmation page. | Working as expected. | ![Delete Profile Confirmation Page](/static/images/readme_images/existing_features/delete_confirmation_page.png) |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Users Page](/static/images/readme_images/manual_testing/back_button.png) |
| User clicks on the "edit" button on their own meme card. | User is taken to the edit meme page. | Working as expected. | ![Edit Meme Page](/static/images/readme_images/existing_features/update_meme_page.png) |
| User clicks on the "delete" button on their own meme card. | User is taken to the delete meme confirmation page. | Working as expected. | ![Delete Meme Confirmation Page](/static/images/readme_images/existing_features/delete_meme_confirmation_page.png) |

##### Not authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Users Page](/static/images/readme_images/manual_testing/back_button.png) |
| User clicks on the "Report" button. | User is redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |
| User clicks on the "smiley face" or a "sad face" button. | Info message is displayed. | Working as expected. | ![Info message](/static/images/readme_images/manual_testing/like_message.png) |
| User clicks on one of the provided profile social media links. | User is taken to the social media page. The page opens in a new window. | Working as expected. | ![Social Media Page](/static/images/readme_images/manual_testing/social_link.png) |


### Upload Meme Page Testing.

- The Navigation bar and footer are the same as on the home page.

##### Not authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "upload meme" button. | User is redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |

##### Authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Memes Page](/static/images/readme_images/manual_testing/back_button.png) |
| User clicks on the "Upload Meme" button. | User is taken to the upload meme page. | Working as expected. | ![Upload Meme Page](/static/images/readme_images/existing_features/upload_meme_page.png) |


### Contact Developer Form Testing.

- The Navigation bar and footer are the same as on the home page.

##### Not authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Contact Developer" link. | User redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |


##### Authenticated user.
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Contact Developer" link. | User is taken to the Contact Developer page. | Working as expected. | ![Contact Developer Page](/static/images/readme_images/manual_testing/contact_developer_form.png) |
| User fills in the form and clicks on the "Send" button. | User is redirected to the home page and a success message is displayed. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/contact_developer_form_message.png) | 


### Update Meme Form Page Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Single Meme Page](/static/images/readme_images/existing_features/update_meme_page.png) |
| User "edits" any of the fields and clicks on the "Update Meme" button. | The user is redirected to the single meme page and a success message is displayed. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/success_message.png) |


### Delete Confirmation Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "back" button. | User is taken one step back. | Working as expected. | ![Single Meme Page](/static/images/readme_images/existing_features/delete_confirmation_page.png) |
| User clicks on the "CONFIRM" button. | The user is redirected to the home page and a red warning message is displayed to confirm the user's action. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/deleted_warning_message.png) |


### Logout Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Logout" button. | User is redirected to the logout page. | Working as expected. | ![Logout Page](/static/images/readme_images/existing_features/logout_page.png) |
| User clicks on the "log out" button on the logout page. | The user is redirected to the home page and a success message is displayed. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/logout_message.png) |


### Login Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "Login" button. | User is redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |


### Home Page Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the "social sign up" button. | User is redirected to the social sign-up page. | Working as expected. | ![Social Sign Up Page](/static/images/readme_images/manual_testing/social_signin.png) |
| User clicks on the "Sign up" link. | User is redirected to the sign-up page. | Working as expected. | ![Sign Up Page](/static/images/readme_images/existing_features/signup_page.png) |
| User clicks on the "Forgot password?" link. | User is redirected to the password reset page. | Working as expected. | ![Forgot Password Page](/static/images/readme_images/manual_testing/password_reset.png) |
| User enters their username and password and clicks on the "Log in" button. | The user is redirected to the home page and a success message is displayed. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/signin_success.png) |


### Password Reset Page Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters a valid email that was used to sign up and clicks on the "Reset my password" button. | User is redirected to the password reset done page | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/password_reset_confirm.png) |
| User clicks on the link in the email. | User is redirected to the password reset confirm page. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/password_reset_email.png) |
| User enters a new password and clicks on the "Change my password" button. | User is redirected to the password reset complete page. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/change_password.png) |
| | | | ![Password Change](/static/images/readme_images/manual_testing/change_password_success.png) |


### Sign Up Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User enters a valid username, email and password and clicks on the "Sign up" button. | The user is redirected to the update profile page and a success message is displayed. | Working as expected. | ![Success Message](/static/images/readme_images/manual_testing/signup_success.png) |
| User clicks on the "Log in" link. | User is redirected to the login page. | Working as expected. | ![Login Page](/static/images/readme_images/existing_features/login_page.png) |



</details>


## Interesting bugs or problems

As is now common with my Code Institute projects, most of this was one interesting problem to solve.
A few of the more interesting ones are listed below.
- How to convert all images to a more web-friendly format.
    - This was solved by using the [Django-resized](https://pypi.org/project/django-resized/) package. This package will convert all images to .webp format and resize them. This will save space and bandwidth.
- Creating the functionality to comment on the memes took much more time than expected. It actually turned out not to be this difficult but I was overthinking it.
    - This was solved by creating a new model for comments and then creating a form for that model. Then I created a view for the form and added it to the single meme page. 
     

## Unfixed Bugs

- IntegrityError at /accounts/social/signup/ 
```UNIQUE constraint failed: account_emailaddress.email```
    - This error is caused by the user trying to sign up with the same email address that they used to sign up with Google or GitHub.
- Carousel misalignment on mobile devices.
    - This is caused by the carousel needing to move a different amount of pixels on different devices. Will be solved in the future just ran out of time for this iteration.
- Search result pagination.
    - When the user enters a short search term, the pagination will show but as as soon as you turn the page it reloads the memes page. This is caused by the search term being in the title or description of the meme. Will be solved in the future just ran out of time for this iteration.


# Deployment

### Deploy with Heroku

1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your environment variables. Usually stored in the env.py file locally. In my case, I have 10 variables: 
    - SECRET_KEY - Django secret key.
    - AWS_ACCESS_KEY_ID - Amazon AWS access key.
    - AWS_SECRET_ACCESS_KEY - Amazon AWS secret access key.
    - AWS_STORAGE_BUCKET_NAME - Amazon AWS bucket name.
    - DATABASE_USER - Amazon RDS database user.
    - EMAIL_HOST_PASS - Email password.
    - EMAIL_HOST_USER - Email address.
    - DATABASE_HOST - Amazon RDS database host.
    - DATABASE_NAME - Amazon RDS database name.
    - DATABASE_PASS - Amazon RDS database password.
9. Copy and paste these variables into the KEY field and their values into the VALUE field.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Deploy Branch" button to deploy.
    3. You should also see an option to enable automatic deployment. If you enable this, every time you push to GitHub, Heroku will automatically deploy the app.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.

NB: You will need to add your Heroku app link to the ALLOWED_HOSTS in the settings.py file. You also need to make sure that DEBUG is set to False, requirements.txt and Procfile are up to date and pushed to GitHub.


### Clone project 

- To clone this project.  
    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on "repositories".
    -  Find and click on the "TechieMeme-PP4" repository.
    - In the repository page that opens, click on the 'Code' button.
    - Menu that opens make sure you are in the "local" tab, copy the link in "HTTPS".
    - paste that link into the relevant section in your ide to clone the repository.
        - CodeAnywhere. 
        - - Click on the "New Workspace" and paste that link to the "Repository URL" field.
        - vsCode. 
        - - Select "File" and "New Window". In the middle of the page select "Clone Git Repository...", 
        - - Paste that link into the search box at the top of the screen and hit enter.
        - - Select the local destination for repository files.
        

### Fork repository

- To fork this repository.
    - Open my [GitHub repository](https://github.com/Inc21/TechieMeme-PP4).
    - Click on the 'Fork' button on the top right of the screen.
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.


# Content

After reading through numerous articles about copyright laws on memes, the general consensus seems to be that as long as I'm not trying to profit off these memes we should be fine. This website is not for profit and was created for educational purposes only.

Here is one of the first responses from my research: [The National Law Review](https://www.natlawreview.com/article/who-owns-memes)

- The Background image on the home page was taken from [Pixabay](https://pixabay.com/).


# Credits

Would like to say thanks to all for the support throughout the project.

- [Dennis Ivy](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg) He has the best Django tutorials on YouTube and the way he explains everything is very easy to understand. I owe a lot to him.
- [Code Institute](https://codeinstitute.net/ie/) for all the support and knowledge.
- [Slack community](https://slack.com/intl/en-ie/) tech-humour channel where I got the inspiration for this project and some feedback. My cohort channel for all the support and feedback.
- My mentor Dick Vlaanderen who's continuously very supportive of me and very knowledgeable.
- I would also like to thank or say sorry to my family. I'm not too sure they have seen me much these past weeks. According to [Wakatime](https://wakatime.com), I have spent nearly 55 hours behind this computer. That's on top of 40 hour work week. ![Wakatime](/static/images/readme_images/wakatime.png).
