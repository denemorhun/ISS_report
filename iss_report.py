#!/usr/bin/python3
# iss_report.py
# Author: Denem Orhun
# email:  denemorhun@gmail.com

'''
# API (http://api.open-notify.org/) provides information on the International Space Station.

ISS Python script accepts the following command line argument to print the expected results

# -l. --location
    - print the current location of the ISS
    Example: “The ISS current location at {time} is {LAT, LONG}”

# -n, --nextpass:
print the passing details of the ISS for a given location
Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

# -p, --people
for each craft print the details of those people that are currently in space
Example: “There are {number} people aboard the {craft}. They are {name[0]}…{name[n]}”

'''

import requests, pytz, argparse
from datetime import datetime

###############################################################################
# Commandline arguments selection menu
###############################################################################
def make_selection():

    # create a parser
    parser = argparse.ArgumentParser(description='Return info about the ISS.')

    #next pass taking exactly two parameters for latitude and longitude
    parser.add_argument('-n','--nextpass', required=False, metavar='l', type=float, nargs=2,
                        help='Next duration of the ISS at <latitude>, <longitude>.')

    parser.add_argument('-p','--people', required=False, action='store_true',
                        help='Display the people aboard the craft.')

    parser.add_argument('-l', '--location', action='store_true', 
                        required=False, help='Display the current ISS location at point in time.')

    # parse the arguments
    args = parser.parse_args()

    if args.location:
        get_location()

    if args.people:
        get_people()

    # <latitude>, <longitude>
    if args.nextpass != None:
        get_next_pass( args.nextpass[0], args.nextpass[1] )

###############################################################################
# Get current location of the ISS at a point in time
###############################################################################
def get_location():

    # Get the request and convert to json object
    pos_url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(pos_url).json()

    # Convert the timestamp from json to UTC format
    time_at_loc = datetime.utcfromtimestamp(response['timestamp']).strftime("%T, %D")
    
    location = {'latitude': response['iss_position']['latitude'], 'longitude': response['iss_position']['longitude']}

    print(f"The ISS at {time_at_loc} UTC is at {location}")

###############################################################################
# Display the duration of the ISS at <latitude><longitude>
###############################################################################
def get_next_pass(latitude, longitude):
    iss_url = 'http://api.open-notify.org/iss-pass.json'
    location = {'latitude': latitude, 'longitude': longitude}
    # response = requests.get(iss_url, params=location).json()

    #print("Response", response)

    for k, v in response.items():
        print(f'keys {k} : values {v}')

    # if 'response' in response:
    #     next_pass = response['response'][0]['risetime']
    #     next_pass_datetime = datetime.fromtimestamp(next_pass, tz=pytz.utc)
    #     print(f'Next pass for {latitude}, {longitude} is: {next_pass_datetime}')
             
    #     print( next_pass_datetime)
    # else:
    #     print(f'No ISS flyby can be determined for {latitude}, {longitude}')

###############################################################################
# Display the people aboard the craft
###############################################################################
def get_people():
    astros_url = 'http://api.open-notify.org/astros.json'
    response = requests.get(astros_url).json()
 
    number = int(response['number'])
    craft = response["people"][0]['craft']

    print(f'There are {number} people aboard the {craft}.')
    print("The astronauts in space:")
    # print the names of the astronauts
    i = 0
    while i < number:
        astronaut = response['people'][i]['name']
        print(astronaut)
        i += 1

###############################################################################
# Driver Code
###############################################################################
def main():

    make_selection()

if __name__ == "__main__": main()