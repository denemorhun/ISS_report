# ISS_report
ISS data feed

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

Example output:
/iss_report.py -n -33.2296 175.9892 -l -p
The ISS at 19:07:11, 12/07/20 UTC is at {'latitude': '-15.5319', 'longitude': '-167.0732'}
There are 7 people aboard the ISS.
The astronauts in space:
Sergey Ryzhikov
Kate Rubins
Sergey Kud-Sverchkov
Mike Hopkins
Victor Glover
Shannon Walker
Soichi Noguchi
Date for next ISS pass for -33.2296, 175.9892 is: 2020-12-08 12:59:14 for 611 seconds.
