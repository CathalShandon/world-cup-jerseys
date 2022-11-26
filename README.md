# World Cup Jerseys

Straddling counties Cork and Kerry, the Beara peninsula in southwest Ireland is one of Ireland’s most compelling and beautiful locations. The Miskish and the Caha mountains form the rugged spine of the peninsula which pokes into the wild Atlantic ocean ensuring that the coastline is ever-present. 

This maritime influence allows subtropical trees and shrubs to escape domesticity and go native in the endless hedgerows lining the leisurely roads that meander between Beara’s cosy, colourful villages and parishes. The peninsula is densely studded with Bronze Age remains: wedge tombs, stone circles and standing stones. 

The Beara Bridle Way is a  linear route. Riders can start in Clonglaskin west of Castletownbere or in Allihies or Urhan. There is a short loop route in Allihies and plans are in place two extend the trail and make three loops. Parking is available in Clonglaskin, Allihies , by the Urhan  Inn  and Travara beach  .

**View the live site [here](https://beara-bridle-trail.herokuapp.com/)**
![Beara Horse Trail mockup images](static/images/mockup.png)



# Table of Contents <a name="Home"></a>

1. [User Experience (UX)](#ux)<br>
    i.  [Strategy](#strategy)<br>
    ii. [Scope](#scope)<br>
    iii. [Structure](#Structure)<br>
    iv. [Skeleton and technical design](#skeleton)<br>
    v. [Surface](#surface)<br>
      
2. [Features](#features)<br>
    i. [Current Features](#features-existing)<br>
    ii. [Features to implement](#features-toimplement)<br>

3. [Testing](#testing)<br>

    i. [User Stories/feature testing](#user-stories-testing)<br>
    ii.  [Automated testing](#automated-testing)<br>
    iii.  [Known issues during development and testing](#known-issues)<br>
    iv. [Validation testing  ](#validation-testing)<br>
    v. [Javascript testing](#js-testing)<br>
    vi. [Unfixed bugs](#unfixed-bugs)<br>
4. [Deployment](#deployment)<br>
5. [Technologies Used](#technology-used)<br>
6. [Credits](#credits)<br>
7. [Acknowledgements](#acknowledgements)<br>

# 1. User Experience (UX) <a name="ux"></a> 
### **Project goals:**
To create an online blog about the different trails where user can login, view and comment and like the trails.
- To enable users to comment and like/unlike the trails.
- To enable to navigate with ease with through the site.
- To ensure a safe environment in which to interact anonymously with secure account set-up.
- To ensure a responsive site accessible to all, across multiple devices.

### **Site owner goal:**
- To enable users to navigate with ease and read content.
- To have the ability to delete posts and deactivate account users when necessary.
- To enable users to register their own accounts and manage passwords.
- A separate ‘site owner’ login to implement secure administration of the site.
- To ensure the site is fully responsive and accessible site for all users across multiple devices

### **User goals:**
- Users should find the platform intuitive and easy to use.
- To login/logout of the site
- Register for an account
- To post under a chosen ‘username’
- Users should be assured the data they provide whilst registering as an account user is going to be kept secure
- Generic aesthetically pleasing styling and colour palette to suit all users and accessibility 


## i. Strategy <a name="strategy"></a>

## User stories

1. As a **site user** I can **login with my username and password** so that **I can access the sites full functionality**

2. As a **logged-in site user** I can **log out of my account** so that **other users cannot access my account**

3. As a **site user** I can **register** so that **I have a role-based login and functionality of commenting and voting on posts**

4. As a **site user** I can **intuitively navigate the site** so that **the layout of the site is consistent**

5. As a **site user** I can **locate the social media accounts** so that **I can follow their updates**

6. As a **logged-in site user** I can **complete a comment on the trails** so that **other users can heard other peoples opinion**

7. As a **logged-in site user** I can **like and unlike** the **trails**


## Website templates



## iv. Skeleton / Technical design <a name="skeleton"></a> 

I used Balsamiq to create wireframes for my project in order to plan out the layout of the interface, navigation and information design of the site on desktop, tablets and mobile devices.
Page | Desktop Version | Mobile Version
--- | --- | ---
About us| ![Desktop about us in wireframe image](static/images/About_us_desktop.png) | ![Mobile about us page wireframe image](static/images/About_us_mobile.png)
Sign Up | ![Desktop sign up wireframe image](static/images/Signup_desktop.png) | ![Mobile sign up wireframe image](static/images/Signup_mobile.png)
Trail | ![Desktop ask question wireframe image](static/images/trail_desktop.png) | ![Mobile ask question wireframe image](static/images/Trail_mobile.png)
Trail Post | ![Desktop open question wireframe image](static/images/Trail_post_desktop.png) | ![Mobile open question wireframe image](static/images/Trail_post_mobile.png)


# 2. Features <a name="features"></a> 
## Existing features <a name="features-existing"></a>

### **Feature 1 Navigation bar**

Navigation bar is featured on all pages at the top of the screen<br>
This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via 'back button'<br>

The navbar collapses to a hamburger menu once the window width drops below 992px to ensure all information is displayed comfortably to the user.

* Search Bar

    The search bar is located in the middle of the navbar, above the links and can be used to search the site for products.

    The search term entered will be used to search the database for any products with matching information in either the product title, product description or product ingredients.

    On screens with a width below 992px, the search bar is hidden and can be displayed by clicking on the 'Search' button that is present in the navbar.

* Footer

    The top part of the footer is a full width div containing links to the Social Media pages for the business.

    The footer is displayed on all pages other than the main landing page of the website, and sits at the bottom of each page.

    The lower section of the footer is split into three columns with the first having a short About Us synopsis. The title of the column also links to the About Us page, but is not underlined due to the link also being available in the navbar.

    The middle column contains Useful Links which direct to individual pages for the Refunds & Returns Policy, Postage & Packaging Policy and Privacy Policy

* Landing Page

    Followed by the large hero photo of Kane, Ronaldo and Messi and a link to the jerseys for sale

* Product List page

    This page is available to both site visitors without a log-in and registered users who are logged in.
    All the products which are reviewed and approved are listed in this page.
    All the products have buttons to View the post detail page which is only visible for users who are logged in.
    Edit button is also present in the post list if the post was created by the user who is viewing the page.

* Product Detail page

    This page is available to everyone who are visting the site.
    This page consists of a detailed view of the post which includes the content of the post, difficulty level and suitable dog size, in addition to the information displayed in the post list.
    Also available on this page are other users' comments on this post. Only the approved comments are displayed on this page.
    There is another function to allow other users to press the Like button and leave a comment regarding the post. The comment entered here need to be reviewed by the site owner before displayed in this post detail page.

* Create a Post page

    This page can be accessed by registered users who are logged in. Button link is located in the navbar for easy access to this page once logged in.
    There are messages to let users know which fields are required to create a post. Title field has to be a unique one, therefore there is a placeholder in the title field with a message ‘Your unique post title’ to advise you to create a unique title.
    Image upload is available but users can opt not to upload an image if they choose so.
    Once the create button is pressed, users will be directed to the post list page and a message to inform the user about the post is displayed below the navbar.

* Edit post page

    Edit post page is accessed by edit post button which is available in either post list or post detail page for users who are logged in. The button is visible for the user's own post only so that the post can only be edited by its own user or by superuser using the admin page.

    The required fields are identical to create post but all the entries of the post are retrieved so that users can edit only the field they wish to update.

    This page also contains a delete the post link which will display the page to confirm their intention to delete the post.

* Delete Post page

    When the user presses ‘Delete This Post’ link from the edit post page, this Delete Post page displays and asks the user for confirmation to delete the post. Users can either click the Confirm Delete button or cancel and go back to Posts.
    When the Confirm Delete button is pressed, the user will be redirected to the Post List page and 	a message will show below the navbar to inform that the post was deleted.

* Account

    A user icon is located in the top right of the page, allowing the user access to manage their account and personal information.
    Clicking on the icon displays a dropdown menu using Bootstrap's dropdown plugin with a number of options
            -Login & Register are displayed if the user is not logged in.
            -My Profile & Logout are displayed if the user is logged in.
            -Admin Dashboard & Add Product are displayed if the user is a superuser.


* Profile Detail page

    This page can be accessed by the View Profile button in the Members page or Post detail page if the user has their post displayed in the page.
    The page includes the image that the user posted and some brief description about them if they opted to enter any fields.
    Each user’s empty profile is created when they register to the site so every registered user has their own profile, but they can leave all the fields blank if they wish.

* Profile Edit page

    This page is displayed when the user clicks the button with their username which is located in the navigation bar.
    All the fields are optional so they can enter any field they wish to update and leave the rest as blank.
    Once the profile is updated, the user will be directed to the post list page and a message will be displayed to inform the user that their profile is updated.

 * About the Site page

    This page can be accessed from any page within the site from the link in the footer. 
    The page states which pages are accessible for users who are not logged in and what can registered and logged-in users can do on each page

* Register page

    This page can be opened from the register button in the navigation bar.
    New site visitors are simply asked to enter username, password and password confirmation to register for the use of this site. Email field can be left blank as it is optional.
    Once successfully registered, users will be redirected to the index page and have access to all the pages which are open for registered users.

* Login page

    Registered and returning users can use the login button to open the login page and supply their username and password to login.
    On successful login, users will be redirected to the index page with a message to inform them that they logged in successfully and they can choose any options provided in the page.

* Logout page

    Once a user is logged in, the Login button in the navigation bar will be replaced with the Logout button.
    Users can simply click this button to log out and confirm to sign out. This will display the home page with a message to inform that the user has successfully logged out.

* Cart

    A cart icon is also located in the top right corner of the page displaying the value of the current contents of the cart, and the number of items that are present in the cart.

    Clicking the cart icon will take the user to the cart page where they can complete their shopping journey.

# 3. Testing <a name="testing"></a> 

### Responsiveness 

Throughout the site is tested to ensure all pages are displayed appropriately in all screen sizes

## Testing User Stories

### 1. As a Site Admin I can create, read, update and delete trails and comments so that I can manage the site content

* An admin site has been provided so that the Site Admin can manage trails and comments.

* Trails and comments can be created, read, updated and deleted from the site.

* Trails and comments main fields are being displayed for the Site Admin to identify them easily.

* Trails and comments can be filtered and searched to narrow down a specific group.

### 2. As a logged-in site user I can log out of my account so that other users cannot access my account.

* Registered Site Users are give the option of logging out of website.

* Registered Site Users are able to click on logout button which will be show another page.

* Registered Site Users the are given the choice to click if they are sure they want to logout.

* Registered Site Users are not able to gain any access of any other user account.

### 3. As a Site User I can register an account so that I can create trails leave comments and like trails.

* Account registration has been provided for Site User.

* Registered Site Users are given the possibility to submit trails and comments.

* Registered Site Users are able to edit and delete their own trails.

* Registered Site Users are able to like and unlike trails.

### 4.As a site user I can intuitively navigate the site so that the layout of the site is consistent.

* The site is easy to naviagte and easy to use across all devices.

### 5.As a site user I can locate the social media accounts so that I can follow their updates.

* The links facebook, twitter all allow users to click on and follow the creators more on social media

### 6.As a logged-in site user I can complete a comment on the trails so that other users can heard other peoples opinion.

* A Leave comments on trail page has been provided for registered Site Users.

* A comment form is available in the trail post page for the Site Users to be able to comment on the trail posts.

* A leave comment button is displayed to the registered Site Users under the trail content inside the trail page.
 

### 7.As a logged-in site user I can like and unlike the trails.

* Like and unlike buttons are provided for registered Site Users next to each trail.

* Registered Site Users can like or unlike others trails.



## Code Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code of the project in order to ensure there were no syntax errors.

![index.html validation](static/images/html_validation.png)


### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the CSS code of the project in order to ensure there were no syntax errors. 

W3C CSS Validator found no errors or warnings on my CSS.

![CSS validation image](static/images/css_validation.png)

### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

[PEP8 online](http://pep8online.com/) was further used to validate the Python code to validate the Python code for PEP8 requirements. See below the validation results and the reviewed results. 

| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| admin.py | No errors / warnings |![admin.py code reviewed image](static/images/admin.png) |
| forms.py | No errors / warnings| ![forms.py code reviewed image](static/images/form.png) |
| models.py | No errors / warnings | ![models.py code reviewed image](static/images/model.png) |
| urls.py | No errors / warnings| ![urls.py code reviewed image](static/images/url.png) |
| views.py | No errors / warnings| ![views.py code reviewed image](static/images/Views.png) |


## Accessibility


## Manual Testing

## Manual testing on each page.

Along with testing user stories manually, each page has been manually tested to ensure that the links and the contents are properly placed and functioning, and that all data entry is appropriately handled as expected. Page access is also tested for the restricted pages.

Every link within the page has been checked to ensure that it displays the page appropriately.
Visual inspections carried out to ensure that restricted page links or buttons are not visible on the page.

#### Landing page

**Users who have not logged in**  
 They are presented with Login and Register buttons to the right of the navigation bar. Visual inspections are carried out to ensure that the buttons are displaying appropriately to logged in users and users who are not logged in a number of times.

**Registered and logged in users**

 On the opening page, they can click on Login to open the Login page. After successful login, manual testing took place to ensure that the message of successful login is displayed and Register and Login buttons are replaced by three buttons which are, 'Create a Post', 'Username' and 'Logout'. Visual inspection to ensure there is a Members link beside the Forum menu on the left is added to the menu.
 Each button and link is manually tested to ensure it opens the appropriate page 

 #### Post List page

**For site visitor who has not logged in**

Visual inspections are carried out so that no links to the post detail page or edit post are present in each post in the list. 
Ensure that all the posts displayed in the page are approved posts and information displayed is correct as created post

**For registered and logged in users**

Ensure the post list is only displaying approved posts with correct information entered by the user.
A View button is present in each post and links will open the selected post detail page.
For a currently logged in user’s own post, an Edit button is present in the post panel and selecting it will open the ‘Edit’ post page with selected post entry retrieved.

#### Post Detail page

**For a site visitor who has not logged in**

Access is attempted by copying the individual post address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users**

Visually inspected all post entries are correctly retrieved and displayed in the post.
A View Profile button opens the selected users profile page.
Ensure that the clicking like button increments the number only once and selecting it again removes the count by one.
When submitting a comment, the feedback message displays in the comment panel so that the user is notified about the status of their comment.
Once approved by superuser, the number of the comment increments by one and the comment displays in the Comments panel

#### Create a Post page

**For site visitor who has not logged in**

Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users**

Entering an existing title field will return the error message to prompt the user to enter another title.
Attempting to create a post with a blank required field returns an error message.
File upload is successful without any issue.
When ‘Create button’ is pressed and entry is successful, the page will redirect to ‘post list page’ with a message to notify the user about the status of the post

#### Edit post page

**For site visitor who has not logged in**
Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users** 

Displayed edit post page has corresponding selected post entries in each field.
Removing the required fields does not let a user to update the post.
An Error message is used to inform users if a required field is left blank or an attempt to update is not showing at the moment.
Upon successful update,  the page redirects to the post list page with a message to inform the users the update was successful.
Delete this post link opens Delete post page

#### Delete Post page

**For site visitor who has not logged in**

Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in. 

**For registered and logged in users**
Cancel and go back to post link opens the post list.
Pressing Confirm Delete button actually deletes the selected post and associated comments and then returns post list page with message to notify the user the post is deleted

#### Members Page

**For site visitor who has not logged in**

Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users**

Page displays with each member in a panel with their image, name and button to open their individual profile page.
A Button to open individual profile page opens the profile of the selected member.

#### View profile page

**For site visitor who has not logged in**

Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users**

A user’s profile page displays when selected.

A 'Back to profile list' link returns to the Member page

#### Profile Edit page

**For site visitor who has not logged in**

Access is attempted by copying the page address to ensure that the page is not displayed for the site visitors who are not logged in.

**For registered and logged in users**
On pressing their 'username' button in the navigation bar, their own profile page opens for editing.
Upload the image works without any issues.
As all the fields are optional there is no error message present.
Successful update will redirect to 'Post list' page with a notification message 

#### About the Site page

Page displays for any site visitors and information provided is clear

#### Register page

Tested all validation works without any issues.
Ensure that an existing username cannot be registered and returns the error.
Password validations are in place.
Upon successful registration, the user is redirected to landing page with a notification for their login

#### Login page

Various usernames are used for login attempt and to ensure the login process meets the standard.
Upon successful login, the user is redirected to landing page with a notification for their login

#### Logout page
Ensure logout will redirect to the landing page with a notification for their logout and restricted pages cannot be accessed.


# 4. Deployment <a name="deployment"></a> 

### Deployment
Here is the deployment procedure  that I have taken to deploy this project on Heroku

1. In the Heroku dashboard, click new, then enter the app name and specify the region.

2. In the Add-on section in the resources tab, search postgres, then select Heroku Postgres and submit order from button in the popup window.

3. In the setting tab, click on Reveal Config Vars button then copy the value for DATABASE_URL key.

4. Create env.py directly under the repo directory same lavel as manage.py and make sure the file name is included in .gitignore as this is a setting for local development site in Gitpod. 
Heroku Config vars need to be set accordingly including DATABASE_URL and SECRET_KEY

5. In setting.py file include followings:

    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env
    modify SECRET_KEY line to SECRET_KEY = os.
    environ.get('SECRET_KEY')

    Replace DATABASES as
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

6. In the Gitpod terminal, migrate the change by
python3 manage.py migrate. Check the resource tab in heroku and choose 
Heroku Postgres then ensure the changes are reflected in the database

7. Login to Cloudinary and copy the API Environment variable and paste in env.py and also Config Vars in Heroku.

8. DISABLE_COLLECTSTATIC set to 1 in Config Vars in Heroku as the initial deployment does not contain static files yet.

9. In setting.py configure followings:
 
    * Add 'cloudinary_storage', before 'django.contrib.staticfiles', and 'cloudinary' after it.

    * Set STATICFILES_DIRS, STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL and DEFAULT_FILE_STORAGE so that Django can use the directories appropriately.

    * Set TEMPLATES_DIR just below BASE_DIR and insert TEMPLATES_DIR in TEMPLATES array
    'DIRS': []

    * Set ALLOWED_HOSTS array as 'tailsontrails.herokuapp.com', 'localhost'

10. Create Procfile with the contents 

    web: gunicorn tails_on_trails.wsgi

11. In the deployment tab in Heroku page, connect to GitHub and search for the repository then Connect.

    Click on Deploy Branch


# 5. Technologies Used <a name="technology-used"></a>  <a name="Home"></a>
## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.

* [Django Template](https://jinja.palletsprojects.com)  
    * Django Template was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/)  
    * jQuery was used as a JavaScript library to help writing less JavaScript code.  


### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.


### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Tiny PNG](https://tinypng.com)    
    * Tiny PNG was used to reduce the file size of the images.

* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Favicon.cc](https://www.favicon.cc/) 
    * Favicon.cc was used to create the site favicon.


# 6. Credits <a name="credits"></a>
See below list of tutorials and documentation i used throughout this project
- The basic skelton setup for this project was based on  “I think therefore I blog project by the Code Institute 
- I used and adapted code for the navbar , emails and search Boutique Ado project by the Code Institute


# 7. Acknowledgements <a name="acknowledgements"></a>
I would like to thank Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.
I would also like to thank my tutor Marcel for his invaluable support, feedback and guidance through the whole process.