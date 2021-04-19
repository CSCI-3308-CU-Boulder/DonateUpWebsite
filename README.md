# 3308SP21_021_2
Authors: Jesse, Timothy, Nathan, Jeremy, Eliza, Ben Weriler

Description:
Donate Up is a website and chrome extension with the ability to donate a small amount of change to charity after a purchase. Once the user selects a donation amount they will be prompted to donate via PayPal. The Website was designed to be friendly with a pleasant and eye-catching appearance. The site offers an about-us, login, account, and donation/home page. On the donation page, if the user inserts a URL of an item the website will output a donation price currently set to the full price of the item, this is subject to change. This outputted donation price will also be added to the PayPal button for the user to donate. Users are able to create accounts and login to allow their donations to be tracked. The Chrome extension automatically opens when a user opens a cart page and prompts the user to donate a selected amount of change to a charity of choice from above. This price is then added to the PayPal button with the memo of the selected charity.


Architecture:

The donateup website is a flask app deployed on AWS with a postgresql database backend. The website serves through an nginx proxy to the flask app. Nginx as the proxy allowed for ease of implementing an SSL cert for the site.

The website can be used to create donations using the url form on the home page. This form can detect the cost of purchases for ebay items and allows the user to take a percentage of that donation before hitting "donate."

The Postgresql database is a simple 3 table database for: users, charities, and donation history. SQLalchemy is used to create classes for the DB tables and update/query them.
Authentication and adding users is done through the database. If a user authenticates, the flask session library is used to place a cookie for the session.
If a user has a session cookie with the donateup.life website, their donations either from the main website or from the chrome extension will be logged to the database with that user's information.

Overview of repo:

-Code: this folder contains the code for our project's components.
  -chrome_ext_frame: contains the code and files necessary for the Chrome extension
  -website: contains the code and resources for the flask app website
  -API:
  -psql: contains some infromation on database creation, modification, and access.
-Milestone_Submissions: our teams milestone pdfs as needed
-Resources: some of our research and helpful links
-Team_Meeting_Logs: some of our team meeting logs

The Chrome extension can be installed following the instructions included in the README within that folder.

How to use website:

Users can sign up for an account with their name, email, and a password. Once they have signed up, they can login into the site to view and update basic profile information. Users need to have an active session in order for their donations to be logged.
