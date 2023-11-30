#!/bin/bash
# make a message containing you got me!, in the body of the response
curl -o /dev/null -sw "You got m!" 0.0.0.0:5000/catch_me
