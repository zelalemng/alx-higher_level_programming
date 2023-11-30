#!/bin/bash
# make a message containing you got me!, in the body of the response
curl -sL -X PUT -d user_id=98 -H "You got m!" 35.153.67.210:5000/catch_me
