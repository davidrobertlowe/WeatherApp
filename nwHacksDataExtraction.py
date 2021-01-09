import json
import api_req

# for reference of what input data would be like
# x = '{"coord":{"lon":-123.1193,"lat":49.2497},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":277.91,"feels_like":273.32,"temp_min":277.04,"temp_max":278.71,"pressure":1026,"humidity":81},"visibility":10000,"wind":{"speed":4.12,"deg":90},"clouds":{"all":75},"dt":1610225338,"sys":{"type":1,"id":954,"country":"CA","sunrise":1610208322,"sunset":1610238825},"timezone":-28800,"id":6173331,"name":"Vancouver","cod":200}'

#y = json.loads(x)

#print(y["weather"][0])

data = api_req.req()

def weatherMain():
    "takes a jsonObject and returns the main weather as a string"
    
    return (data["weather"][0]["main"])

def weatherDescription():
    "takes a jsonObject and returns the weather description as a string"
    
    return (data["weather"][0]["description"])

def weatherIconId():
    "takes a jsonObject and returns the weather icon id"
    
    return (data["weather"][0]["icon"])

def temperature():
    "takes a jsonObject and returns the temeprature"
    
    return (data["main"]["temp"])

def wind():
    "Takes a jsonObject and returns the wind speed and degree"

    return ('Wind speed of ' + str(data["wind"]["speed"])
            + " at an angle of " + str(data["wind"]["deg"]) + " degrees.")

def checkIfInCA():
    """
    checks if the requested city is in Canada if it is then returns true
    else returns false
    """

    if (data["sys"]["country"] == "CA"):
        return True
    else:
        return False
    
    







    
