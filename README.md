# step_in_python
my way to python
# quickstart.py:
Using the google calender API to fetch 10 recent event from your Google Account .
Step 1 :
Turn on the Google Calendar API. use the link : https://console.developers.google.com/start/api?id=calendar
On the Add credentials to your project page, click the Cancel button.
In the OAuth consent screen tab, select an Email address, enter a Product name if not already set, and click the Save button.
Select the Credentials tab, click the Create credentials button and select OAuth client ID.
Select the application type Other, enter the name "Google Calendar API Quickstart"
Click the file_download (Download JSON) button to the right of the client ID.
Move this file to your working directory and rename it client_secret.json.
Step 2 :
Install the Google Client Library. 
CL syntax : pip install --upgrade google-api-python-client
Step 3:
create the quickstart.py file
Done !! run it to find a new tab opening in your default browser ... may need you to sign in .. get 10 upcoming events 


