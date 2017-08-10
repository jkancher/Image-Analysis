# Image-Analysis
Using Dropbox API for image analysis using Watson IBM API Visual Recognition

Objective: Compare 2 images in the dropbox to identify whether the object in the image has been taken by comaring it to another image. 
This program uses Dropbox api/token and Watson IBM api

Steps to get started:

Dropbox setup:
1) Create a dropbox account (www.dropbox.com)
2) Insert all the images you want to compare in your dropbox
    Can be in a folder or on the main dashboard of your dropbox.
3) Create a dropbox app that gives accesss to your entire dropbox or dropbox file with your images.
4) Obtain the app key and secret key on your dropbox app
5) Generate and obtain the generated token from your dropbox app

Watson IBM setup:
1) Go to Watson IBM and create an account (https://www.ibm.com/cloud-computing/bluemix/)
2) Go to IBM Bluemix account page
3) Create a new service
4) The service should be under Watson called Visual Recognition
5) Create the service
6) Obtain the api key for that service once created

Use python to compare the images:
1) Download/copy the file analysis.py
2) In the file replace the api key for the watson IBM with your api key.
3) Run the program and follow the instructions given by the file
DONE
