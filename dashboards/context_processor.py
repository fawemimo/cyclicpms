import socket
import json
import urllib.request
import ipinfo
import pycountry
import requests
from urllib.request import urlopen
import re as r
import geocoder
from countryinfo import CountryInfo
import holidays
from datetime import date


def user_country_context(request):
#     endpoint = f'https://ipinfo.io/{ip}/json'
#     response = requests.get(endpoint, verify = True)

#     if response.status_code != 200:
#         return 'Status:', response.status_code, 'Problem with the request. Exiting.'
#         exit()

#     data = response.json()
 # get IP ADDRESS of the location
    ip = geocoder.ip("me")

    # get the country name of the IP location
    country_name = ip.country
    # get the currencies of the country
    currencies = CountryInfo(country_name).currencies()
    # save the name of the country as a variable
    my_country = country_name

    # pass the country name into pycountry for the details of the country
    user_country_details = pycountry.countries.get(alpha_2=my_country)
   

    context = {
        'user_country_details':user_country_details

    }
    return context