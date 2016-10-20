# GoogleTasks2Trello
This script aims transfer your Google Calendar Tasks into Trello.
I spend to much time trying and failing different softs that I decided to write this simple script (please be kind, as this is one of my first script in Python.)

Here is how to install and use it:

* Install Python: https://www.python.org/downloads  (tested with python_3_5_2)
* Install the following python libs:
	* pip install --upgrade google-api-python-client
	* pip install httplib2
	* pip install trolly  (tested with trello-0.9.1)

* To access your Google Task with python: 
	** create a new project in https://console.developers.google.com
	** search "Tasks API"and activate it
	** create an OAuth 2.0 ID
	** Modify client_secret.json with the correct Client ID and client secret

* To access your Trello  with python:
	** create a list ("List IMPORT" for ex.) in the desired board
	** Got to https://trello.com/app-key and generate a trello API KEY and change it below (TRELLO_API_KEY)
	** On the same page, generate a token and change it below (TRELLO_TOKEN)

* Execute the following script multiple times and follow instructions

Enjoy!

Notes:
* If your already run this script on a google account and you want to re-run it with a different account, you need to delete the file tasks.dat and re-run
* If you use chrome with profiles that doesn't match the one you want, use the following option: 
	** googletasks2trello.py --noauth_local_webserver