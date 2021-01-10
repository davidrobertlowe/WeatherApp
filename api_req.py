# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json 

city_name = ""
complete_url = ""

# Enter your API key here 
api_key = "24aa68308c034c5d485bda6b7ea92ad7"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
def city(req_city):
    
  global city_name
  city_name = req_city
  
  global complete_url
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
# complete_url variable to store 
# complete url address 


def req():
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
      
    # json method of response object  
    # convert json format data into 
    # python format data 
    return response.json() 

"""
x = requests.get(complete_url).json()
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"]        
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
    weather = z[0]["main"]
    # print following values 
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +                 
          "\n weather = " + 
                    str(weather) +         
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ")  
"""
