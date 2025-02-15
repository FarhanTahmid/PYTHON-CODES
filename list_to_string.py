import json

BBOX=[[2151, 355], [2255, 355], [2255, 399], [2151, 399]]

json_string = json.dumps(BBOX)

print(f"JSON String: {json_string}. Type: {type(json_string)}")