# Planet Vegan 

## UX

### Wireframes

### Project Goals 

* To create a functional vegan recipe site.
* Where vegans of all levels can either find recipes or add recipes.
* They would be able to find different categories of vegan meals.
* They can add recipes to the collection.

This project is for people who are trying to go vegan or who are already. Allowing them to find a variety
of recipes of their picking. The website layout will be simple, clean, consistent and easy to use.

### User stories 

* As a vegan I would like to find a variety different vegan recipes, that help broaden my vegan pallet.
* As a meat-eater, I would like to substitute some of my meals with vegan meals.
* As a long time vegan, I would like to share some of the recipes I've created throughout my journey.
* As vegan student I would like to find simple vegan recipes on a budget. 
* As a vegan, I would add some vegan meals on the website that are affordable and easy to make. 

### How this project will help them

* Help the discover new vegan recipes
* You can search the desired recipes in our search.
* You can create an account on the website and add your recipes.
* every recipe shows you the time it takes to cook and prepare.
* There's an image of each recipe and you can also add your own.

## Features

###  Existing Features
1. Home Page - includes a header image and 4 images for each category, and a URL link to take you to the category pages.
   The home page also includes a search bar to search recipes of your choice.
2. Recipe Dropdown -website includes a dropdown list for categories Breakfast, Lunch, Dinner and Desserts,
   can access the drop-down on any page.
3. Navigation Bar - before you make an account, the navigation bar includes Recipe dropdown, Home, Login and Signup link. 
   When you log in you see, the navigation removes login and, profile, add your recipes and logout are added to the navbar.
4. Login Page - Login page includes a login form, where you enter your username and password to sign in if you have an account.
5. Sign Up Page - sign up page includes a form where you create a username and password to sign in. There are certain requirements
   need to be met to be able to sign up such a minimum of 5 and maximum 15 characters for both username and password to be able to create one. 
6. Profile Page - profile page, when you login, stores all the recipes you've created so you that you can manage them.
7. Edit and Delete button - on the profile page where all your created recipes are stored. Your created recipes include a delete and edit button. You can Delete the recipe or edit it to add more stuff or remove them. 
8. Add Your Recipes Page - page includes a form to create to add new recipes to the website collection, where others can view them.
9. Categories- website included four categories, Breakfast, Lunch, Dinner and Desserts, it takes you to their page where you can view the recipes in said categories. 
10. Recipe layout - You're shown a snippet of the recipe and you click on the open button to show you the full recipe.
11. logout -  logs you out and takes you back the homepage.

### Features Left to Implement

1. I would like to introduce a comment section. Where underneath every recipes, people are able to comment
   on the recipes and over suggestions. People Should also be able to reply to the comments and havea conversation.
2. I would like to introduce more cateogries to the website and allow for a wider range of recipes.
3. Allow people the option to upload videos with their recipes if they want to give people a tutorial that people can follow.

## Design

### Font 
I kept the font styling simple using two fonts. I Used Google Font Awesome to select my chosen font and apply them to my website.
I used Roboto font style for any message such recipes method, recipe title and welcome message because it's a simple and easy
read. I used Petit Formal Script' for the title such navbar and categories title, to make the website more visually appealing.

### Colours
I used a maximumof three colours for my website, which where green, dark grey and white. I only used three colours to give my 
website a cleaner look and make it flow well. I used green for the navbar and footer. i choose green because my website is 
vegan site and that's mostly a plant based diet. I used white for my navbar titles, and i used dark grey for the rest of the
fonts.Also made my catgory dropdow gree to keep with theme. The colours on my website were consistent and minimal.

### Navbar 
The navbar consists of a Recipes dropdown list showing all the recipe categories, Home, Login and Sign Up. When you 
login, the Login is removed, and Logout, Add Your Recipes and Profile can be viewed.
The side nav on the mobile device appears on the right.


### Home Page 
The home page consists of a picture of a vegan dish with a welcome message, welcoming everyone to the page. They're also a
search bar for searching recipes of your choice. Above the search, there's a message encouraging you to sign up. 
Underneath are four meal categories along with a picture of a meal from said category. If you click a category name,
it should take you the recipes from that category.

### Login and Sign Up Page 
Both pages are identical and only differ in the instructions given to tell you to either login or sign up when entering your 
details on the form. The login page has a link the redirects you to the sign-up page if you're not a member and the Sign-Up 
page vice versa. If you log in with incorrect details, a message will flash telling you. When you're signing up if the username
you've typed is already taken a message will flash informing you.

### Profile Page 
When you log in, you're taken to your profile page and the profile stores any recipes that you've already created. However 
if you do not have any recipes, the profile page is empty and only show Username's Profile Title at the top.

### Add Your Recipes Page
This page allows you to upload your recipes on the site. There's a form to fill,  with text areas such as recipe name, description,
method etc. When you've finished, you can upload the recipe. The recipe saved in your profile page

### Edit and Delete Button 
The website allows you to delete and edit your the existing recipes you've created. When you go to your profile page or,
Search your recipe there will be an edit and delete button on your recipe.

### Categories Page
Dropdown takes you to the different category pages, where you can find meals to make a form that category.
The categories are Breakfast, Lunch, Dinner and Dessert.

### Recipe Page 
when you shown a recipe , you're only shown a preview showing the name. Then you you click the card the icon on 
the side it reveals a little more information about the recipe such as how time to make, prep time and serves.
it aslo provides you with a open button. This will  take you the recipe page where you can view the ingredients,
method of making the recipe.

## Testing 

### General Testing 
I used chrome Dev tools to preview my code. When writing my code, especially, HTML and CSS, I would preview it in chrome Dev
tools to checking if it's working. If there was an issue, I would check the element section in dev tools and try to find the issue.
I'd also try firstly type my CSS on the Dev tools to see how it looked before typing it on my CSS page to see if I was happy with the outcome then commit.
Also used Dev tool to make my website responsive only every device, adding media queries for devices I saw my website wasn't responsive on. I created a 
login on my website to check it's the functionality of the website for all pages and how every page operated.I also used CCS and HTML Validator to check
my CSS and HTML code most of the errors I got was due to the system not recognising my jinja template. I used Unicorn revealer when I had an issue with my 
layout when my images were overflowing that helped me find the issues.

### Testing Python
I used the Flask app debugger to test the functionality of my website every time I created my @app route and functions to see if I was working. 
When creating my methods of  POST and GET to retrieve someone's login details from mongodb. I would check my terminal where my python app.py was running to 
see it was getting and posting as required, also checking to see what the HTTP response code was. This was very useful when checking when 
creating my python functions to look for error when something was working because sometimes I may have forgotten to add the method on my from
and that would be causing the issue.
I also used Python tester html to validate my my app.py code.

### Issues and Resolutions 

* When creating my dropdown list for my category on my navbar using materialise. The jquery would only activate the dropdown on the desktop 
  and not the mobile side nav. This was resolved, by creating a separate and dropdown list for the desktop and mobile device and targeting 
  the dropdown separately in jquery. 

* This issues was about my schema data on MongoDB, I had created and stored all my recipes on MongoDB by hand and used a struggling value 
to story my category. This was an issue because I had created four HTML pages for each recipe category. I could not retrieve the recipe
categories by iterating through them due to an error in the categories collection. This was resolved by removing all recipes for my 
categories collection, and changing the value for category_name  field on collection to objectId so that each recipe had a unique id that
could not be changed. I created a category id function that allowed to find the categories and their objectId.This allowed me to iterate
through the categories to retrieve them all so they could appear on my dropdown list. This meant I could delete all  the HTML pages I 
made for the recipe  categories and just have one HTML page for all categories and iterate through them using template jinja and also
delete my python functions for them, which meant less code and better functionality.

* When creating my the card panel to store my recipes they were some minor issues with responsiveness. The recipes on the tablet
devices where not in rows of two and would overlap each other. This was easily solved by changing font sizes of the recipes
names on the tablet devices using media queries.

* My dropdown list for my recipes categories would not appear on my mobile side nav. Whilst it was appearing on my desktop view,
the issue is Flask only allows for loop to used once. I was using it twice as the loop on my desktop and my mobile device, 
regardless of which device I was using. To resolve this issue, I assigned categories to two different
variables so they could be used in different loops, one to be used to call the desktop dropdown list and the other the mobile dropdown.


* I had an issue with my search engine to retrieving the items searches and just redirecting me back to my search page.
I found that did not add the method to the form and that was the issue with my search
and changing  my query to from request.arg to request.form as it was looking for an argument and I had set none and that was
also causing an issue.

*  I had a lot issue with my recipes overflowing and making my website unresponsive and this was because of the of jinja template
for loop and if statement and where I had placed them. To resolve these issue I just had to change their placements.

* My Recipe form  to edit recipes did not have a text area for recipe description so each time, you'd try to get the recipe you'd have to re-enter
you're description because it was not being retrieved in MongoDB. Quickly resolved by adding a recipes description text area
so when trying to edit your recipe.

* I was having trouble insert text in my form using, a mobile device. I would have to click multiple times in order to be
in order to be able to start typing. This was due to not changing the for inside the label, after this was done, there
was no issue. 
## Technologies Used

1. HTML & CSS Progamming languages 
2. [MongoDB](https://account.mongodb.com/): to create my database schema.
3. [Materialize](https://materializecss.com/): to make a responsive frontend framwork, get designs
4. [GitHub](https://github.com/):  Repository host for project and previe live website.
5. [GIT](https://git-scm.com/): Used for version control 
6. [Font Awesome](https://fontawesome.com/): Used for Social media icons e.g. facebook, twitter and instagram.
7. [Google Fonts](https://fonts.google.com/): Tanagerine, Roboto and Lato  
8. Google Chrome developer was the main tool used to check that my website was responsive on all screen sizes.
9. [W3C Markup Validation](https://validator.w3.org/)  HTML validation.
10. [W3C CSS validation](https://jigsaw.w3.org/css-validator/) CSS validation.
11. [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) rectify overflow issues.
12. [Python Tester](https://extendsclass.com/python-tester.html) validate my app.py.
13. [Heroku](https://www.heroku.com/)built my app on.

## Deploying 

1. Set up a Heroku account and create and application.

2. Go to settings and set the VARS for IP and PORT.

3. Go back to gitppod terminal and type - “Heroku login” this will take you to a webpage to login to your Heroku account

5. Use “git init “to initialise and new repository

6. type the command “pip3 freeze > requirements.txt” this will add a new2 file with all the packages to run your python app

7. create a profile “echo web: python run.py > Procfile” if your python file is called run.py

8. run the command “git remote add” and the app URL which can be found on the Heroku dashboard

9. do a “git add.”

10. commit your code ‘git commit -m” your message here”’

11. then run “git push Heroku master”

12. This will then deploy your app

## Credits

### content

* README, website code examples and deploying instruction taken from https://github.com/ajgoward/daddies_recipes_MS3 and https://github.com/ceciliabinck/cook-with-me
 and Code on Institute Mini-Task Manager Project.

### Acknowledgement

I would like to thank :
The tutors at code institute for their help
My mentor Antonio Rodriguez










 








 

