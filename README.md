![TechieMeme Logo](/static/images/readme_images/techiememe_logo.png)
![mockup](/static/images/readme_images/mockup_dark.png)

# Introduction

TechieMeme is a website meant to lighten up peoples day who like technology or related things. Like Code, science, maths or hardware as an example. Inspiration for this site came from Code Institute Slack channel **community-tech-humour**, which I really love. On this site the user can view, like and comment on the memes that they like or upload their own memes and edit, delete them if necessary. This website was created as a learning exercise for my [Code Institute](https://codeinstitute.net/ie/) fourth portfolio project. 

The live app can be found [here.](https://techiememe-50a6f4eb45eb.herokuapp.com// "TechieMeme.")

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
7. As a user, I want to be able to easily view my profile.
8. As a user, I want to be able to easily view other users profiles.
9. As a user, I want to be able to easily search for memes.

### Authenticated User Goals
10. As a authenticated user, I want to be able to easily upload my own memes.
11. As a authenticated user, I want to be able to easily edit my own memes.
12. As a authenticated user, I want to be able to easily delete my own memes.
13. As a authenticated user, I want to be able to easily like memes.
14. As a authenticated user, I want to be able to easily comment on memes.
15. As a authenticated user, I want to be able to report memes.
16. As a authenticated user, I want to be able to easily contact the developer.
17. As a authenticated user, I want to be able to easily edit my profile.
18. As a authenticated user, I want to be able to easily delete my profile.
19. As a user, I want to be able to

### Site owner objectives
20. As a site owner, I want to be able to log into the admin panel.
21. As a site owner, I want to be able to easily manage memes incase of inappropriate content.
22. As a site owner, I want to be able to easily manage users incase of inappropriate content.
23. As a site owner, I want to be able to provide fun and easy to use website.



# Design

## Look and feel


## Colour


## Font

## Flowcharts


# Tools and technologies used

## Languages



## Other tools and programs.

- [Lucid](https://lucid.co/) was used when creating flow charts.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the game is deployed using the [Code Institute](https://codeinstitute.net/ie/) Python template.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.


## Existing Features

### Home Page

- 

![Home Page](/assets)  

### Memes Page

- 

![Memes Page](/assets/)  

### Users Page 

- 

![Users Page](/assets) 

### Upload Meme

- 

![Upload Meme](/assets/)


### Features Left to Implement

-  
    

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
- Validating was done by live website on Heroku. Some errors were found but they are all related to Django template's.

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
#### techiememe project app

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


 ## Manual Testing

This app was developed on a Dell desktop running Windows 10.


### User Stories Testing

| Expectation | Solution |
| --- | --- |
|     |     |


### Home Page Testing.
![](/assets/images/welcome_page_small.png)
| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
|     |     |     |     |



## Interesting bug or problems
     

## Unfixed Bugs


## Deployment


### Deploy with Heroku

1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your google sheets credentials. 
    1. Type the name of the credentials (CREDS in my case) file into the "KEY" field.
    2. Open your IDE and find CREDS.json in your project files.
    3. Copy/paste everything in this file to the "VALUE" field and click the "Add" button.
9. Just below in the "Buildpacks" section click on the "Add buildback" button. Buildpacks have to be installed in this order.
    1. Click on the "Python" button to select it and then the "Save changes" button.
    2. Click again on the "Add buildback" button.
    3. Click on the "nodejs" button to select it and then the "Save changes" button.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Enable Automatic Deploys" button to update the deploy also when you push a new commit to GitHub.
    3. At the very bottom of the page click on the "Deploy Branch" button.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.


### Clone project 

- To clone this project.  
    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on "repositories".
    -  Find and click on the "Python-Quiz-Game-PP3" repository.
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
    - Open my [GitHub repository](https://github.com/Inc21/Python-Quiz-Game-PP3).
    - Click on the 'Fork' button on the top right of the screen.
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.

## Content


# Credits

Would like to say thanks to all for the support throughout the project.

- [Real Python](https://realpython.com/) Great site for some extra Python content. A lot of inspiration was taken from there.
- [Code Institute](https://codeinstitute.net/ie/) Love Sandwiches.
- [Slack community](https://slack.com/intl/en-ie/) and my classmates for tips and tricks and entertainment.
- My mentor Dick Vlaanderen who's continuously very supportive of me and very knowledgeable.
