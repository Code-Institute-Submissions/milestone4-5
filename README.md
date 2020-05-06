

# CycleOlogy - Milestone Project 4
***

## Table of Contents

 * List item
 *	Fuctionality of the Project
 *	User Experience 
	 *	User Stories
	 *	Design 
	 *	Wireframes
*	Technology Used 
*	Database
*	Features 
*	Testing 
*	Deployment 
*	Credits 

***
## Welcome to CycleOlogy 

![enter image description here](https://cycleology.s3-eu-west-1.amazonaws.com/media/images/LOGO-SMALL.jpg)

***
## User Experience

### User Stories

#### Public User
-	As a public user, I want to be able to view all products on any device (mobile / tablet / desktop)
-	As a public user, I want to be able to pick a product category
-	As a public user, I want to be able to pick a product from a subcategory
-	As a public user, I want to be able to search for a product
-	As a public user, I want to be able to get more information on a product
-	As a public user, I want to be able to add a product to my shopping cart
-	As a public user, I want to be able to add a quantity of the same item
-	As a public user, I want to be able view my shopping cart
-	As a public user, I want to be able to adjust the quantity in my shopping cart for a specific product
-	As a public user, I want to be able to delete an item in my shopping cart.
-	As a public user I want the able to purchase the items in my shopping cart
-	As a public user I want to be able to register as a user
-	As a public user, I want to be able to change my password
-	As a public user, I want to be able to send the company a message

#### Administer User

 - As a Administer User, I want to be able to add products
 - As a Administer User, I want to be able to delete products
 - As a Administer User, I want to be able to modify products
 - As a Administer User, I want to be able to view orders
 - As a Administer User, I want public to register

#### Developer User

 - As a Developer User, I want site to be secure
 - As a Developer User, I want site to be responsive
 - As a Developer User, I want to be error free
 - As a Developer User, I want to build a website that is scalable and that can be enhanced with further development

### Strategy

### Scope

The scope of the site was to provide a ecommerce website for a new up and coming cycle shop, and to demonstrate the skills that I learnt on the Coding Institute Full Stack Developers course, HTML, CSS, JQuery, Python, Django python,

### Structure

The Navigation bar is fixed to the top of the screen so that it’s available at all times.

The shopping cart is always visible and accessible for the user, so there is a different CSS for mobile views so that it doesn’t collapse into the mobile nav icon.

The user can select all products, or refine their query using the categories or subcategories

The search functionally allows a user to search within the name and display all products that match.

The page restricts the amount of products to 6 and there is pagination functionality to allow the user to scan through the products on other pages.

The product details page allows to user to view more information on the product

The shopping cart page allows the user to adjust / delete items and also proceed to checkout. To enhance user experience I have removed the table slider on mobile views, instead I have modified the form so that its only contains the necessary information

The checkout page allows the user to enter in their name and address for delivery, and also make a credit card payment.

The contact page allows the user to enter a message for the administrator of the website

The footer contains links to all social media

## Technology Used
###	Languages, Frameworks, Editors, Version Control

 - HTML, CSS, JS and Python 
 - Django 
 - Bootstrap Framework
 - GitHub Used to store the repository, keep version control, and push link to Heroko 
 - Heroku 

### Tools Used
- Balsamiq Used to create wireframes
- W3C HTML Validator used to check HTML code
- W3C CSS Validator used to check CSS code
- htmlformatter.com used to beautify the HTML code
- Font Awesome Icons
- Favicon Generator
- Google Chrome DevTools
- AWS Amazon
- Stripe

## Database

#### Product Details 

|Name                | Format     | 
| ------------------ | --------------- | 
|catagory | models.CharField(max_length=254, choices=PRODUCT_CATAGORY) |
|subcatagory | models.CharField(max_length=254, choices=PRODUCT_SUBCATAGORY) |
|name | models.CharField(max_length=254, default='') |
|product_summary | models.TextField(default='') |
|product_description|models.TextField(null = True, blank=True)|
|product_features|models.TextField(null = True, blank=True)|
|price|models.DecimalField(max_digits=6, decimal_places=2)|
|image1|models.ImageField(upload_to='images',null = True, blank=True)|
|image2|models.ImageField(upload_to='images',null = True, blank=True)|
|image3|models.ImageField(upload_to='images',null = True, blank=True)|


#### Checkout Order

|Name                | Format     | 
| ------------------ | --------------- | 
|full_name  |models.CharField(max_length=50, blank=False)|
|phone_number  |models.CharField(max_length=20, blank=False)|
|country |models.CharField(max_length=40, blank=False)|
|postcode |models.CharField(max_length=20, blank=True)|
|town_or_city |models.CharField(max_length=40, blank=False)|
|street_address1 |models.CharField(max_length=40, blank=False)|
|street_address2 |models.CharField(max_length=40, blank=False)|
|county|models.CharField(max_length=40, blank=False)|
|date|models.DateField()|


#### Order item
|Name                | Format     | 
| ------------------ | --------------- | 
|order   |models.ForeignKey(Order, null=False)|
|product   |models.ForeignKey(Product, null=False)|
|quantity |models.IntegerField(blank=False)|


## Testing

|Fuctionality               | Page    | User Type | Browser | Initial test Pass / Fail  |Final test Pass / Fail |Comments |
| ----| ---- | ---- |  ---- | ---- | ---- | ---- |
|	Image Carousel is it display correctly	|	 Home Page 	|	Registered User	|	Chrome	|	Pass	|		|		|
|	Image Carousel is it display correctly	|	 Home Page 	|	Public User	|	Chrome	|	Pass	|		|		|
|	Image Carousel is it display correctly and responsive 	|	 Home Page 	|	Registered User	|	Mobile	|	Pass	|		|		|
|	Image Carousel is it display correctly and responsive 	|	 Home Page 	|	Public User	|	Mobile	|	Pass	|	
|	Text on about page is it displaying correctly 	|	About Page	|	Registered User	|	Chrome	|	Pass	|		|		|
|	Text on about page is it displaying correctly 	|	About Page	|	Public User	|	Chrome	|	Pass	|		|		|
|	Text on about page is it displaying correctly 	|	About Page	|	Registered User	|	Mobile	|	Pass	|		|		|
|	Text on about page is it displaying correctly 	|	About Page	|	Public User	|	Mobile	|	Pass	|		|		|
|	Text on about page are there any spelling mistakes	|	About Page	|		|		|	Fail 	|	Pass	|	Spelling errors fixed 	|
|	Form is displaying correctly 	|	Contact Page	|	Registered User	|	Chrome	|	Pass	|		|		|
|	Form is displaying correctly 	|	Contact Page	|	Public User	|	Chrome	|	Pass	|		|		|
|	Form is displaying correctly and responsive	|	Contact Page	|	Registered User	|	Mobile	|	Pass	|		|		|
|	Form is displaying correctly and responsive	|	Contact Page	|	Public User	|	Mobile	|	Pass	|		|		|
|	Form checks that  fields are filled in before sending 	|	Contact Page	|		|		|	Pass	|		|		|
|	Text on about page are there any spelling mistakes	|	Contact Page	|		|		|	Pass	|		|		|
|	link to email opens default email application 	|	Contact Page	|		|	Chrome	|	Fail	|	Pass	|	Link missing 	|
|	link to email opens default email application 	|	Contact Page	|		|	Mobile	|	Fail	|	Pass 	|	Link missing 	|
|	link to phone  opens default phone application 	|	Contact Page	|		|	Chrome	|	Fail	|	Pass	|	Link missing 	|
|	link to phone opens default phone application 	|	Contact Page	|		|	Mobile	|	Fail	|	Pass 	|	Link missing 	|
|	link to google maps l opens default google maps in new tab	|	Contact Page	|		|	Chrome	|	Fail	|	Pass	|	Link missing 	|
|	link to google maps opens default google maps in new tab	|	Contact Page	|		|	Mobile	|	Fail	|	Pass 	|	Link missing 	|
|	Product card displays correctly 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Images are all uniform across all cards 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Names are all uniform across all cards 	|	Products	|		|	Chrome	|	Fail	|		|	Issues with length 	|
|	Price are all uniform across all cards 	|	Products	|		|	Chrome	|	Fail	|		|	Issues with length 	|
|	Names are all uniform across all cards 	|	Products	|		|	Chrome	|	Fail	|		|	Issues with length 	|
|	Order buttons are all uniform across all cards 	|	Products	|		|	Chrome	|	Fail	|		|	Issues with length 	|
|	Names are all uniform across all cards 	|	Products	|		|	Mobile	|	N/A	|		|	as cards are shown vertically issue with name length  is not visible 	|
|	Price are all uniform across all cards 	|	Products	|		|	Mobile	|	N/A	|		|	as cards are shown vertically issue with name length  is not visible 	|
|	Names are all uniform across all cards 	|	Products	|		|	Mobile	|	N/A	|		|	as cards are shown vertically issue with name length  is not visible 	|
|	Order buttons are all uniform across all cards 	|	Products	|		|	Mobile	|	N/A	|		|	as cards are shown vertically issue with name length  is not visible 	|
|	Product card displays correctly 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Six product cards is the maximum shown on 1 page 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	pagination allows the customer to move forward and back to view more products 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	pagination allows the customer to move forward and back to view more products 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Clicking on the Buy button adds product to cart 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Users can adjust quantity of product 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Value of zero is not allowed 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Clicking on the product card brings the user to a detail product page 	|	Products	|		|	Chrome	|	Pass	|		|		|
|	Six product cards is the maximum shown on 1 page 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	pagination allows the customer to move forward and back to view more products 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	pagination allows the customer to move forward and back to view more products 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Clicking on the Buy button adds product to cart 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Users can adjust quantity of product 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Value of zero is not allowed 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Clicking on the product card brings the user to a detail product page 	|	Products	|		|	Mobile	|	Pass	|		|		|
|	Product details displays correctly 	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	Product details displays correctly 	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	Image Carousel is it display correctly	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	Image Carousel is it display correctly	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	User can add itdem to cart	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	User can add itdem to cart	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	User can adjust quantity	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	User can adjust quantity	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	User can see text on product discription tab	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	User can see text on product discription tab	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	User can see text on Product Into tab	|	Product details 	|		|	Chrome	|	Pass	|		|		|
|	User can see text on Product Into tab	|	Product details 	|		|	Mobile	|	Pass	|		|		|
|	Shoping cart is displayed correctly 	|	Shopping cart	|		|	Chrome	|	Pass	|		|		|
|	Shoping cart is displayed correctly 	|	Shopping cart	|		|	Mobile	|	Pass	|		|		|
|	User can adjust quantity 	|	Shopping cart	|		|	Chrome	|	Pass	|		|		|
|	User can adjust quantity 	|	Shopping cart	|		|	Mobile	|	Pass	|		|		|
|	Users can delete items 	|	Shopping cart	|		|	Chrome	|	Pass	|		|		|
|	Users can delete items 	|	Shopping cart	|		|	Mobile	|	Pass	|		|		|
|	Users can preceed to Checkout 	|	Shopping cart	|		|	Chrome	|	Pass	|		|		|
|	Users can preceed to Checkout 	|	Shopping cart	|		|	Mobile	|	Pass	|		|		|
|	Users can continue shopping 	|	Shopping cart	|		|	Chrome	|	Pass	|		|		|
|	Users can continue shopping 	|	Shopping cart	|		|	Mobile	|	Pass	|		|		|
|	Checkout displays all products correctly 	|	Checkout	|		|	Chrome	|	Pass	|		|		|
|	Checkout displays all products correctly 	|	Checkout	|		|	Mobile	|	Pass	|		|		|
|	User can add in details into order form 	|	Checkout	|		|	Chrome	|	Pass	|		|		|
|	User can add in details into order form 	|	Checkout	|		|	Mobile	|	Pass	|		|		|
|	User can make payment with valid credit card 	|	Checkout	|		|	Chrome	|	Pass	|		|		|
|	User can make payment with valid credit card 	|	Checkout	|		|	Mobile	|	Pass	|		|		|
|	Paymnet is rejected if credit card is invalid 	|	Checkout	|		|	Chrome	|	Pass	|		|		|
|	Paymnet is rejected if credit card is invalid 	|	Checkout	|		|	Mobile	|	Pass	|		|		|
|	Navbar is dispayed correctly and fixed to the top 	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Navbar is dispayed correctly and fixed to the top 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Shoping cart gets updated when products added 	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Shoping cart gets updated when products added 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	All links work correctly  	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	All links work correctly  	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Search fuctionality works correctly 	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Search fuctionality works correctly 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Shopping cart is visable in Nav bar when collapsed for pc	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Shopping cart is visable in Nav bar when collapsed for mobile 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Register and login are visable when user not logged in 	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Register and login are visable when user not logged in 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Profile and Log out  is displayed when user loged in 	|	n/a	|		|	Chrome	|	Pass	|		|		|
|	Profile and Log out  is displayed when user loged in 	|	n/a	|		|	Mobile	|	Pass	|		|		|
|	Footer is displayed correctly on all pages 	|	 n/a	|		|	Chrome	|	fail	|		|	Footer is getting pulled up the page leaving a gap at bottom 	|
|	Footer is displayed correctly on all pages 	|	 n/a	|		|	Mobile	|	fail	|		|	Footer is getting pulled up the page leaving a gap at bottom 	|
|	Social Media links in footer all work 	|	 n/a	|		|	Chrome	|		|		|		|
|	Social Media links in footer all work 	|	 n/a	|		|	Mobile	|		|		|		|




Need to add in html testing css testing and python 


## Deployment 
AWS setup 
1.	Create an account on https://aws.amazon.com and log into account 
2.	Connect to S3 and create a new bucket , give it a name and untick all the public blocks 
3.	Go into your new bucket and select properties and then STATIC WEBSITE HOSTING
4.	Now go into permissions and select CORS configuration and add the following
```
<CORSConfiguration>
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
5.	Now go into permissions and select Bucket Policy and add the following 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::cycleology/*"
        }
    ]
}

```
6.	Connect to IAM and create a group 
7.	Now create a policy using AmazonS3FullAccess and add the following 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3::: cycleology ",
                "arn:aws:s3::: cycleology /*"
            ]
        }
    ]
}
```
8.	Assign the policy to the group 
9.	Now add a user and down load the csv file and keep it safe you will use this later.
10.	Test the bucket by uploading a test image file to it 

Strip account 
1.	Setup a Stipe account 
2.	Log into the dashboard and copy API keys 

GitHub and GITPOD
1.	Save a copy of the githup repository https://github.com/pauldardis/milestone4 by clicking on the "download zip" button and extract the file file to your chosen folder.
2.  go to https://github.com/Code-Institute-Org/gitpod-full-template and select "Use this template" and give the Repository a name.
3.  Open the repository using gitpod
4.  Copy the files in step 1 into Gitpod.
5.  Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```
6.  create a env.py file and add the following 
   ```
   import os

os.environ.setdefault("STRIPE_PUBLISHABLE","<enter key here>")
os.environ.setdefault("STRIPE_SECRET","<enter key here>")
os.environ.setdefault("DATABASE_URL","<enter key here>")
os.environ.setdefault("SECRET_KEY", "<enter key here>")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "<enter key here>")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<enter key here>")
os.environ.setdefault("EMAIL", "<email address>")
os.environ.setdefault("EMAIL_PW'", "<enter key here>")
   ```

7.  Create a .gitignore file and add the env.py file name. 
8.  Edit the settings.py file and change so that if has the name of your AWS bucket
   ```
   AWS_STORAGE_BUCKET_NAME = 'cycleology'
      ```
9. open a terminal in Gitpod and type the following 
 ```
    python manage.py makemigration
    python manage.py migrate
    ```
10. Create a superuser with the following command 
    ```
    python manage.py createsuperuser
    ```
11. Commit everything to github
12. Log into Heroku and setup your settings using the data in step 6 
13. Link your Heroku application to the new repository 
14. click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".
15. Test the deployed application. 

