#Jennifer Goeres
#7-30-2021
#Class Project my API key is: 62eb1965fd2256b5b653d5752466dc4a
#This is the draft. My main focus was to establish a connection to the weather application.
#My goal over the next few weeks is to get it functioning and returning the weather back.

import json, requests


#App id as signed up from openweathermap.org
APPID = '62eb1965fd2256b5b653d5752466dc4a'

#Welcome message when you open the application.
def displayWelcomeMessage():
	print('Thank you for visiting our site for your local weather.')
	print('Please enter your information below.')
	print()

#Return information when given zip code.
def get_url_zipcode(zipcode):
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s' % (zipcode, APPID) 
    return  url


#Return information when given city.
def get_url_city(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (city, APPID)
    return url 


def main():

        #Ask for zip code or city
        user_input = input('Enter zip code or city: ')
        print('Retrieving weather information.')

        #Get correct url based on input
        if user_input.isdecimal():
            url = get_url_zipcode(user_input)
        else :
            url = get_url_city(user_input)
        
        response = requests.get(url)


        #Did the connection work?
        try:
            response.raise_for_status()
            print('Connection is successful')
        except:
            print('Connection was unsuccessful')




displayWelcomeMessage()
main()

