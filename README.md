# 3308SP21_021_2
Authors: Jesse, Timothy, Nathan, Jeremy, Eliza, Ben Weriler

include the project description and an overview of the application architecture.

Description:


Architecture:

The donateup website is a flask app deployed on AWS with a postgresql database backend. The website serves through an nginx proxy to the flask app. Nginx as the proxy allowed for ease of implementing an SSL cert for the site.

The website can be used to create donations. [Ben URL detection description]

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

How to install Chrome extension:

How to use website:

Users can sign up for an account with their name, email, and a password. Once they have signed up, they can login into the site to view and update basic profile information. Users need to have an active session in order for their donations to be logged. Future features will allow the user to view their donation history in their profile page.
