#!/usr/bin/python3
# iss_report.py
# Author: Denem Orhun
# email:  denemorhun@gmail.com

'''
# API (http://api.open-notify.org/) provides information on the International Space Station.

ISS Python script accepts the following command line argument to print the expected results

# loc
    - print the current location of the ISS
    Example: “The ISS current location at {time} is {LAT, LONG}”

# nextpass:
print the passing details of the ISS for a given location
Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

# people
for each craft print the details of those people that are currently in space
Example: “There are {number} people aboard the {craft}. They are {name[0]}…{name[n]}”

'''

import requests, pytz, argparse
from datetime import datetime

def get_next_pass(lat, long):
    iss_url = 'http://api.open-notify.org/iss-pass.json'
    location = {'lat': lat, 'longitude': long}
    response = requests.get(iss_url, params=location).json()

    if 'response' in response:
        next_pass = response['response'][0]['risetime']
        next_pass_datetime = datetime.fromtimestamp(next_pass, tz=pytz.utc)
        print(f'Next pass for {lat}, {long} is: {next_pass_datetime}')
             
        print( next_pass_datetime)
    else:
        print(f'No ISS flyby can be determined for {lat}, {long}')

def get_people():
    peoples_url = 'http://api.open-notify.org/astros.json'
    response = requests.get(peoples_url).json()
 
    number = int(response['number'])
    craft = response["people"][0]['craft']

    # for k, v in response.items():
    #     print(f'keys {k} : values {v}')
   
    print("craft: ", response["people"][0]['craft'])

    print(f'There are {number} people aboard the {craft}')

    i = 0
    while i < number:
        person = response['people'][i]['name']
        print(f'Astronaut in space: {person}')
        i += 1

def get_position():
    pos_url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(pos_url).json()
    print("The current position of the ISS is at longitude: ", 
            response['iss_position']['longitude'], " latitude: ", response['iss_position']['latitude'])

def cli_args():

 # create a parser
    parser = argparse.ArgumentParser(description='Return info about the ISS.')

    #next pass taking exactly two parameters for latitude and longitude
    parser.add_argument('-n','--nextpass', required=False, metavar='l', type=float, nargs=2,
                        help='Position of the ISS, input lat, long')

    parser.add_argument('-p','--people', required=False, action='store_true',
                        help='display the people on board the craft')

    parser.add_argument('-l', '--location', action='store_true', required=False, help='display the current ISS location')

    args = parser.parse_args()

    if args.location == True:
        get_position()

    if args.people == True:
        get_people()

    if args.nextpass != None:
        get_next_pass( args.nextpass[0], args.nextpass[1] )


def main():
    # define a variable to hold the source URL
    # get_next_pass(37.7833, -122.4167)

    cli_args()

if __name__ == "__main__": main()