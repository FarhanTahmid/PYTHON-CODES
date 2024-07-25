from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Prints the responses of your specified form:
form_id = '1luOxW4FGP1574XqKJlduJJlFQN5sIcLIKOujhfL6iUM'
response_id='ACYDBNjFVr379DFr01MOlBfpM7c9UQHvBHbsxPONl6hIFBMyUtthTwXH_gYn2MZhJc5OZfw'
result = service.forms().responses().get(formId=form_id,responseId=response_id).execute()
# result = service.forms().responses().list(formId=form_id).execute()
print(result)