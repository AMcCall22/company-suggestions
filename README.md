# Alison McCallum - Software Engineer Roles



## Milestone 3 Project - Data Centric Development

This website has been designed to provide a repository  to share and view companies that offer web developers/software engineer roles.  This will be a useful, collaborative tool to centrally collate companies that regularly offer opportunities. 

All website visitors will be able to view the list of current companies.

Registered users are currently able to add, delete and edit companies to the website, which allows for a level of 'open management' of the website. This will be reviewed once deployed and admin rights may be introduced at a later stage if deemed necessary.



#### Mock Up images

![](/README_Files/MS3_Mock_Up.png)

#### UX

##### User Stories

As a **junior or established software engineer** searching for a role,  I would like to see the following:

- An intuitive repository which provides a clear list of potential and recommended employees
- A mechanism to add, edit and delete recruiting companies
- A search function which allows me to search by key word, as well as important parameters such as remote working opportunities and level of roles

As a **recruiting company for software engineers**, I would like to see the following: 

- An intuitive repository which provides a clear list of companies
- A mechanism to add, edit and delete my own company 
- A search function which allows me to search for other companies to understand other roles advertised 



##### Wireframes

##### 

Link to [Wireframes](/README_Files/MS3_Wireframes.pdf)

##### 

##### Features

Materialize 1.0.0 was used as the basis of the design to provide a modern and standardised layout throughout the site.

##### Nav-bar

The nav-bar includes the name of the site - CodeScan. This name indicates the site's purpose and if selected, will redirect the user back to homepage from wherever they are in the site.  The nav-bar also includes links to the following sections:

##### Home Page

The home page has a simple design with a tech-related image followed by some text explaining the purpose of the site.  There are also 3 cards which show the 3 most recently added companies to the site. These are refreshed as further companies are added.

##### Company List

The company list page lists, in card format, all of the companies that have been added and are currently held in the MongoDB database.  Registered users are able to edit and delete companies from this page also. 

Pagination has been added, providing a more succinct view of 6 companies per page. 

Edit functionality - This form pulls through all of the field data available for a particular company, and allows each field to be updated and saved. It is very similar to the 'Add Company' form below. 

Delete functionality - This button allows a user to delete a company if deemed appropriate. A flash warning message appears which has to be confirmed before deletion. 

##### Search

This allows users to search companies using a keyword and/or radiobutton search. 

Keyword text search includes words within the name of company or sector, or a descriptive word

Radio buttons were introduced allowing users to search on a combination of the following:

- Text search only
- Remote working option only
- Level of opportunity option only
- Text search and remote working option
- Text search and level of opportunity option

A 'submit button' performs the required search and a 'clear button' resets the search form.

A flash message appears if no results have been found as per the search parameters.



##### Add Company

This form allows users to add new companies to the database. Fields are as follows:

- Company type - a drop down option of Sole business or agency. 

- Company name - text field.

- Sector - text field.

- Description - text field with max length of 45 characters.
- Website - url validation.

- Remote working - dropdown options of 'Yes', 'No' and 'Sometimes'
- Level of Roles - dropdown options of 'Junior', 'Mid', 'Senior' and 'Various'

All fields incorporate the Materialize classes 'data-error "wrong"', 'data-success' "right" and "required" for validation purposes.

##### Login

A simple form for users that are already registered to log in to the site. This will allow them to add, edit and delete company entries. There is a link to a registration form for users that are not currently registered with the site. A flash message appears when a user attempts to open a site page without being logged in, and a message also appears when a user logs in successfully. If a user attempts to log in with an incorrect username or password, a message will appear to warn of this. It will not indicate to the user whether the password or username was incorrect, adding an extra level of security. 

##### Registration

A simple form for users to register with the site. A username (minimum length, 8 char and max length, 20 char) and password (minimum length, 8 char and max length, 15 char) are required to be set up.  Passwords are verified using the password_hash functionality within Flask. 

##### Log Out

A user can easily log out by selecting Logout on the nav bar. This is confirmed by a flash message.  

##### Footer

The footer contains some more detail around the purpose of the website, as well as the social media links of the creator for anyone to contact with site suggestions and feedback. 

#### Technologies Used

- HTML
- CSS
- Javascript
- Materialize
- Flask
- Python
- MongoDB
- Balsamiq
- Github/Gitpod
- Font Awesome
- Google Fonts
- Unicorn Revealer (https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln)



#### Testing

Please find a separate file detailing the testing undertaken here:

[Testing](/Testing_MS3.md)



#### Issues faced and resolved

The search functionality originally used checkboxes but the logic for combining these with a text search proved too complex at this stage. Therefore, radio buttons were introduced in order that  only 1 selection from the remote working dropdown list or 1 selection from the level of opportunities dropdown could be used during a search. These can be used combined with a keyword search.

Pagination within the search function proved too complex so a workaround was introduced. This was necessary because the function calls the all_companies_list.html as a results page, and this html document has pagination embedded within it. Therefore, I increased the limit of the search results per page to 1000, which avoids the need for the function to call the pagination logic (unless the results were > 1000). This will be reviewed in the future.

##### Future Developments

**Registration/Login/Logout**

Further functionality could be added here:

- Registration timeout after certain number of attempts to Login
- Password verification at point of registering
- Logout after certain length of time
- admin user rights if the idea of 'self management' for deleting and editing companies was unsuccessful

**Home Page**

Live updates when new roles are added to websites using a web scrape 

**Search Form**

Pagination logic to be reviewed and added



##### Deployment 

#### Heroku

1. Create the following files, which are  required to be set up to run the Heroku app:

   Requirements.txt details the dependencies required to run the app. Create this file using pip3 freeze --local > requirements.txt

   Procfile signifies to Heroku which files run the app and also how to run the app. Create the file using eco web: python app.py > Procfile

2. Add, commit and push the above files to GitHub. 

3. Create a new app on Heroku by selecting 'New.'  Give a unique name to it and choose Europe as the region.

4. Select Deploy menu and within Deployment method, select GitHub.  Ensure the correct GitHub repository is linked to the app.

5. Within settings, select Reveal Config Vars and set the IP address to 0.0.0.0 and PORT of 5000. Paste the Mongo_URI and Secret Key.

6. Select Deploy menu and Deploy branch button which initiates the building of the required packages. 

7. Once the build is complete, and the app is successfully deployed, select view to view the app.



#### Locally

​	To **clone** this project from GitHub, please follow the steps below:

1. Navigate to the correct repository - [here](https://github.com/AMcCall22/company-suggestions)
2. Click the green button - 'Clone or Download'.
3. Copy the clone URL that appears -https://github.com/AMcCall22/company-suggestions
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type 'git clone' and paste the URL you copied in Step 3.
6. Press Enter to created your local clone.



#### Credits

##### Content

###### **General**

W3 Schools - https://www.w3schools.com/

Traversy Media - https://www.traversymedia.com/

Pretty Printed - https://prettyprinted.com/

###### Pagination

Inspiration taken from Darilli Games - https://github.com/DarilliGames/flaskpaginate/blob/master/app.py

##### Media

Hero image on homepage - https://unsplash.com/photos/Y2m8QfYlpPY - Photo by [AltumCode](https://unsplash.com/@altumcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/programming?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

##### Acknowledgements

Thanks to my mentor, Brian Macharia for his input and direction.

Thanks to student support at Code Institute, with a special mention to Tim Nelson for his guidance. 

Thanks to my peers at Code Institute, of whom I have called on for support during this project.

Thanks also to my husband, Peter McCallum for his support and patience throughout this project.



\------



Disclaimer



This site is currently for educational and practical use 