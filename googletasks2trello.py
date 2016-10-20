import sys

from oauth2client import client
from googleapiclient import sample_tools
import trolly   
import pdb; 


##### PLEASE READ THE README.md

''' References: 
https://github.com/google/google-api-python-client/tree/master/samples/calendar_api
https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/tasks_v1.tasks.html#list

https://github.com/plish/Trolly/blob/master/trolly/list.py
https://developers.trello.com/advanced-reference/list#post-1-lists-idlist-cards
'''


# KEYS/ID SECTION
TRELLO_API_KEY = ''
TRELLO_TOKEN = ''

GOOGLE_CALENDAR_TASK_LIST_ID = ''
TRELLO_BOARD_ID = ''
TRELLO_LIST_ID =''

#
def main(argv):
	# Authenticate and construct service.
	service, flags = sample_tools.init(
		argv, 'tasks', 'v1', __doc__, __file__,
		scope='https://www.googleapis.com/auth/tasks.readonly')

	try:
		current_page_token = None;

		print('\nGOOGLE TASKLISTS:')
		while True:
			tasks_list = service.tasklists().list(pageToken=current_page_token).execute()
			for tasks_list_entry in tasks_list['items']:
				print(' - '+ tasks_list_entry['title'] + ': ' +tasks_list_entry['id'])
			
			current_page_token = tasks_list.get('nextPageToken')
			if not current_page_token:
				break;

	except client.AccessTokenRefreshError:
		print(	'Please verify that the client_secrets.json is correctly setup\n'
				'Original error: The credentials have been revoked or expired, please re-run'
			  	'the application to re-authorize.')


	if (TRELLO_API_KEY == '' or TRELLO_TOKEN == '' ):
		print ( '\n\nTRELLO_API_KEY or TRELLO_TOKEN are missing, Please add them in the KEYS/ID SECTION')
		sys.exit()

	client = trolly.client.Client( TRELLO_API_KEY, TRELLO_TOKEN)
	print('\nTRELLO Boards:')
	for board in client.get_boards():
		print(' - %s' % board)


	if (TRELLO_BOARD_ID == ''):
		print ( '\n\nTRELLO_BOARD_ID missing. Please choose one above and add it in the KEYS/ID SECTION')
		sys.exit()

	trello_board = trolly.board.Board(client, TRELLO_BOARD_ID)
	print ('\nLists in Board ID:' + trello_board.id)
	for rb_list in trello_board.get_lists():
		print(' - %s' % rb_list)
	
	
	if (TRELLO_LIST_ID == ''):
		print ( '\n\nTRELLO_LIST_ID missing. Please choose one above and add it in the KEYS/ID SECTION')
		sys.exit()

	trello_list_to_update = trolly.list.List(client, TRELLO_LIST_ID)

	print('\n')
	tasklist_to_import = service.tasks().list(tasklist=GOOGLE_CALENDAR_TASK_LIST_ID, showCompleted=False).execute()
	for task in tasklist_to_import['items']:
		test_query_params = {}
		if task.get('title',''):
			print('Importing: ' + task.get('title','') + '\n\t notes: ' + task.get('notes','') + '\n\t due: ' + task.get('due',''))
		
			test_query_params['name'] = task.get('title','')
			if task.get('due',''):
				test_query_params['due'] = task.get('due','')
			
			if task.get('notes',''):
				test_query_params['desc'] = task.get('notes','')

			trello_added_card = trello_list_to_update.add_card(query_params=test_query_params)

			'''trello_added_card.add_comments( task.get('notes','') )'''


	print ( '\n\nImport SUCCEEDED')

if __name__ == '__main__':
	main(sys.argv)