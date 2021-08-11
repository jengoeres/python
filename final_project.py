#Jennifer Goeres
#8-14-2021
#Class Project my API key is: 62eb1965fd2256b5b653d5752466dc4a


import json, requests


#App id as signed up from openweathermap.org
APPID = '62eb1965fd2256b5b653d5752466dc4a'

#Welcome message when you open the application.
def displayWelcomeMessage():
	print('\nThank you for using our program to check your local weather.')
	print('\nPlease enter your information below.')

#Return information when given zip code.
def get_url_zipcode(zipcode):
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s&units=imperial' % (zipcode, APPID) 
    return  url

#Return information when given city.
def get_url_city(city):
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=imperial' % (city, APPID)
    return url 

def main():

        #Ask for zip code or city
        user_input = input('\nEnter zip code or city: ')
        print('\nRetrieving weather information.')
        print()

        #Get correct url based on input
        if user_input.isdecimal():
            url = get_url_zipcode(user_input)
        else :
            url = get_url_city(user_input)
        
        response = requests.get(url)

        #Did the connection work?
        try:
            response.raise_for_status()
            print('\nConnection is successful')

            weathers = json.loads(response.text)['list']
         
            #Display the weather to user.
            print('\nTemperature in F degree today is: ' + str(weathers[0]['main'] ['temp']))
            print('\nTemperature tomorrow is: ' + str(weathers[1]['main'] ['temp']))
            print('\nWeather tomorrow is: ' + weathers[1]['weather'][0]['main'])
        except:
            print('\nConnection was unsuccessful')
            main()
        
checkAgain = 'yes'
while checkAgain == 'yes' or checkAgain == 'y':
    displayWelcomeMessage()
    main()
    
    print('\nWould you like to check another location?: ')
    checkAgain = input()
    if checkAgain == "no" or checkAgain == 'n':
        print("\nThank you for visiting our site. We hope you enjoy your day!")



