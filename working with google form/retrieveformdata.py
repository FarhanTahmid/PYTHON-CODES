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
form_id = '1vbjGv4oBNewGMtsQU1WpOXcjwd6ucKyKq5c9ROWW-KE'
response_id='ACYDBNiP_THjAyDLUTPgFucQQ9pfzl_EveQBYc3pqEsragkRPyBcG9QNOMGAg7kPjcctsoE'
result = service.forms().responses().get(formId=form_id,responseId=response_id).execute()

print(result)