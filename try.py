import json, requests, sys, datetime

cityName = raw_input("Enter city name.\n")

f = open("APIKEY_weather.txt");
api = f.readlines()
api = api[0][:-1]

#Didn't give my API ID for obvious reasons.
link = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s"%(cityName,api)
try:
    data = requests.get(link)

    if(data.status_code != 200):
        print "Error "+str(data.status_code)
        print "Closing program..."
        sys.exit()
    else:
        jsondata = json.loads(data.text)
        print "Weather Forecast \n"
        print "City name - "+jsondata['name']
        print "Last updated at - " + datetime.datetime.fromtimestamp(jsondata['dt']).strftime("%d-%m-%Y, %H:%M:%S")
        print "\nWeather - " + str(jsondata['weather']['main'])
        print "Weather Description - "+jsondata['weather'][0]['description']
        print "\nMin. temperature - " + str(jsondata['main']['temp_min']-273.15) +" Celsius."
        print "Max. temperature - " + str(jsondata['main']['temp_max']-273.15) + " Celsius."
        print "Atmospheric pressure - "+str(jsondata['main']['pressure']) + " hPa"
        print "Humidity - " + str(jsondata['main']['humidity']) + "%\n"
except:
    print "Some error occured. Sorry for that."
