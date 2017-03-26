import json, requests, sys, datetime
import Tkinter

f = open("APIKEY_weather.txt");
api = f.readlines()
api = api[0][:-1]
def get_weather(cityName):
    link = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s"%(cityName,api)
    try:
        data = requests.get(link)

        if(data.status_code != 200):
            print "Error "+str(data.status_code)
            print "Closing program..."
            sys.exit()
        else:
            weather={}
            jsondata = json.loads(data.text)
            weather['location']=jsondata["coord"]
            weather['temperature']=jsondata["main"]["temp"]
            weather['pressure']=jsondata["main"]["pressure"]
            weather['humidity']=jsondata["main"]["humidity"]
            #weather['sunrise']=jsondata["sys"]["sunrise"]
            #weather['sunset']=jsondata["sys"]["sunset"]
            weather['description']=jsondata["weather"][0]["description"]
            weather['name']=jsondata["name"]
            print weather
            #gui initiated here
            frame1=Tkinter.Toplevel(height=400,width=300)
            Tkinter.Label(frame1,text="Place",font="Arial 12 bold").grid(row=0,column=0)
            Tkinter.Label(frame1,text=weather['name'],font="Arial 12").grid(row=0,column=1)
            Tkinter.Label(frame1,text="Location",font="Arial 12 bold").grid(row=1,column=0)
            Tkinter.Label(frame1,text=weather['location'],font="Arial 12").grid(row=1,column=1)
            Tkinter.Label(frame1,text="Temperature",font="Arial 12 bold").grid(row=2,column=0)
            Tkinter.Label(frame1,text=weather['temperature'],font="Arial 12").grid(row=2,column=1)
            Tkinter.Label(frame1,text="Pressure",font="Arial 12 bold").grid(row=3,column=0)
            Tkinter.Label(frame1,text=weather['pressure'],font="Arial 12").grid(row=3,column=1)
            Tkinter.Label(frame1,text="Humidity",font="Arial 12 bold").grid(row=4,column=0)
            Tkinter.Label(frame1,text=weather['humidity'],font="Arial 12").grid(row=4,column=1)
            Tkinter.Label(frame1,text="Description",font="Arial 12 bold").grid(row=5,column=0)
            Tkinter.Label(frame1,text=weather['description'],font="Arial 12").grid(row=5,column=1)
            frame1.grid()
            frame1.mainloop()

            return True

            #return weather
            # print "Weather Forecast \n"
            # print "City name - "+jsondata['name']
            # print "Last updated at - " + datetime.datetime.fromtimestamp(jsondata['dt']).strftime("%d-%m-%Y, %H:%M:%S")
            # print "\nWeather - " + str(jsondata['weather']['main'])
            # print "Weather Description - "+jsondata['weather'][0]['description']
            # print "\nMin. temperature - " + str(jsondata['main']['temp_min']-273.15) +" Celsius."
            # print "Max. temperature - " + str(jsondata['main']['temp_max']-273.15) + " Celsius."
            # print "Atmospheric pressure - "+str(jsondata['main']['pressure']) + " hPa"
            # print "Humidity - " + str(jsondata['main']['humidity']) + "%\n"
    except:
        print "Some error occured. Sorry for that."

