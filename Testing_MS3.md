## Testing

### Functionality



#### Home Page

###### 1 Test Description 

Ensure homepage loads correctly.

###### Test

Add new companies via the Add Company form and refresh home page to view result.

#### Expected Outcome 

3 most recent companies added to the website are visible.

###### Pass/Fail

*Pass*



#### Company List Page

###### 2 Test Description 

Ensure company list page loads as expected.

###### Test

Add new companies via the Add Company form and refresh Company List page to view result. 

Select pagination numbers and check correct companies are visible, per page. 

###### Expected Outcome 

All companies added to the website/database are visible.  

Pagination is visible and works as expected (6 entries per page).

###### Pass/Fail

*Pass*



###### 3 Test Description 

Ensure Edit button operates as expected.

###### Test

Edit a company, save and view the results and flash message.

###### Expected Outcome 

Edit form appears and pulls through relevant information for the company that is to be edited. 

Each field can be updated. 

Once submit button is selected, the updated information is saved. 

Company successfully updated flash message appears.

###### Pass/Fail

*Pass*



###### 4 Test Description 

Ensure Delete button operates as expected.

###### Test

Attempt to delete a company, select no and confirm company is still visible.

Delete a company, select yes. 

View the results to ensure deletion and view flash message.

###### Expected Outcome 

Once delete button is selected, a confirmation message appears to check that the user is sure they want to delete the company. 

User selects 'no' and company remains.

User selects 'yes' and the company is deleted. 

Company deleted flash message appears.

###### Pass/Fail

*Pass*



#### Search Form

###### 5 Test Description 

Ensure search form allows for companies to be searched using text and radio buttons.

###### Test

Perform the below test combinations within the search form.

###### Expected Outcome 

The following searches should be possible and correct results provided:

- Text only search

- Remote radiobutton only search

- Roles radiobutton only search

- Text & Remote radiobutton search

- Text & Roles radiobutton only search

###### Pass/Fail

*All Pass*



###### 6 Test Description 

Clear button functionality works as expected.

###### Test

Input a field on the form and select the clear button.

###### Expected Outcome 

When selected, any fields which have been filled will be cleared

###### Pass/Fail

*Pass*



#### Add Company Form 

###### 7 Test Description 

Add Company form works as expected.

###### Test

Input a company, press submit and view result on Company List page.

Attempt to add in a company with incorrect validation as per the above list and press submit.

###### Expected Outcome 

Each field should be completed

- Company type - a drop down option of Sole business or agency. 

- Company name - text field.

- Sector - text field.

- Description - text field with max length of 45 characters.
- Website - url validation.

- Remote working - dropdown options of 'Yes', 'No' and 'Sometimes'
- Level of Roles - dropdown options of 'Junior', 'Mid', 'Senior' and 'Various'

When submit button is selected, company is added to the website/database

If the wrong validation rules are entered, the form should warn the user and block the company from being submitted.

Company successfully added flash message appears.

###### Pass/Fail

*Pass*



#### Registration

###### 8 Test Description 

Registration functionality works as expected.

###### Test

Create a username and password and register.

Check entry in MongoDB.

###### Expected Outcome 

Once Password and Username fields are completed, user is registered.

Flash message appears to confirm this. 

Password is 'hashed' and not in a conceivable format within MongoDB.

###### Pass/Fail

*Pass*



#### Log In

###### 9 Test Description 

Log In functionality works as expected.

###### Test

Login in to the website and check access to add, edit and delete entries.  

When not logged in, a user does not have access to add, edit and delete entries.  

###### Expected Outcome 

When the correct username and password is entered, flash message appears to confirm. User has access to add, edit and delete company entries on the website.

When an incorrect username and password is entered, a flash message appears to notify. User does not have access to add, edit and delete company entries on the website.

###### Pass/Fail

*Pass*



#### Log In

###### 10 Test Description 

Log Out functionality works as expected.

###### Test

Logout of the website and check access to add, edit and delete entries. 

###### Expected Outcome 

When a 'logged in' user selects Log Out on the nav bar, a flash message appears to confirm this. The user does not have access to add, edit and delete company entries on the website.

###### Pass/Fail

*Pass*



### Browser compatibility

Ensure that the site loads correctly on each of the following web browsers

- Chrome - Passed

- Edge - Passed

- Firefox - Passed

- Safari - Passed



#### Code Validation/Beautifier

The code has been passed through the following validation tools:

[W3C Markup Validation](https://validator.w3.org/) 

[W3C CSS validation](https://jigsaw.w3.org/css-validator/) 

[Pep8]http://pep8online.com/


#### Responsiveness

Ensure that the site is responsive and loads correctly on each screen size using the chrome developer tools:

- Small devices - Passed

- Medium devices - Passed
- Large devices - Passed

- x-Large devices - Passed



#### Further testing

Chrome developer tools and Python debugger were used throughout the entirety of the project.

Family and friends have also tested the game for user experience and to aid mobile responsiveness testing.

