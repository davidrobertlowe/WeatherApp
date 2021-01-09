import json
import api_req

# for reference of what input data would be like
# x = '{"coord":{"lon":-123.1193,"lat":49.2497},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":277.91,"feels_like":273.32,"temp_min":277.04,"temp_max":278.71,"pressure":1026,"humidity":81},"visibility":10000,"wind":{"speed":4.12,"deg":90},"clouds":{"all":75},"dt":1610225338,"sys":{"type":1,"id":954,"country":"CA","sunrise":1610208322,"sunset":1610238825},"timezone":-28800,"id":6173331,"name":"Vancouver","cod":200}'

#y = json.loads(x)

#print(y["weather"][0])

data = api_req.req()

def weatherMain(jsonOb):
    "takes a jsonObject and returns the main weather as a string"
    
    return (jsonOb["weather"][0]["main"])

def weatherDescription(jsonOb):
    "takes a jsonObject and returns the weather description as a string"
    
    return (jsonOb["weather"][0]["description"])

def weatherIconId(jsonOb):
    "takes a jsonObject and returns the weather icon id"
    
    return (jsonOb["weather"][0]["icon"])

def temperature(jsonOb):
    "takes a jsonObject and returns the temeprature"
    
    return (jsonOb["main"]["temp"])

def wind(jsonOb):
    "Takes a jsonObject and returns the wind speed and degree"

    return ('Wind speed of ' + str(jsonOb["wind"]["speed"])
            + " at an angle of " + str(jsonOb["wind"]["deg"]) + " degrees.")







    
