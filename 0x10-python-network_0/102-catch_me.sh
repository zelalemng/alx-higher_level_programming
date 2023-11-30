#!/bin/bash
# make a message containing you got me!, in the body of the response
curl -sL -X PUT -d user_id=98 -H "You got m!" 0.0.0.0:5000/catch_me
