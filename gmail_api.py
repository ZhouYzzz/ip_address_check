
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from apiclient import errors

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = os.path.join(os.path.dirname(__file__), 'client_secret.json')
APPLICATION_NAME = 'IP Address Check'
CREDENTIAL_NAME = 'ip-address-check_credential.json'

try:
  import argparse
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
  flags = None


def get_credentials():
  """Gets valid user credentials from storage.

  If nothing has been stored, or if the stored credentials are invalid,
  the OAuth2 flow is completed to obtain the new credentials.

  Returns:
      Credentials, the obtained credential.
  """
  home_dir = os.path.expanduser('~')
  credential_dir = os.path.join(home_dir, '.credentials')
  if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
  credential_path = os.path.join(credential_dir, CREDENTIAL_NAME)

  store = Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
      credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
      credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
  return credentials


def get_service():
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)
  return service


def send_message(service, user_id, message_raw):
  try:
    message = (service.users().messages().send(userId=user_id, body={'raw': message_raw})
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)


def get_personal_email_address(service):
  try:
    results = service.users().getProfile(userId='me').execute()
    return results['emailAddress']
  except errors.HttpError as error:
    print('An error occurred: %s' % error)


def main():
  """Shows basic usage of the Gmail API.

  Creates a Gmail API service object and outputs a list of label names
  of the user's Gmail account.
  """
  service = get_service()

  results = service.users().getProfile(userId='me').execute()
  print(results['emailAddress'])

  # results = service.users().labels().list(userId='me').execute()
  # labels = results.get('labels', [])
  #
  # if not labels:
  #   print('No labels found.')
  # else:
  #   print('Labels:')
  #   for label in labels:
  #     print(label['name'])


if __name__ == '__main__':
  main()
