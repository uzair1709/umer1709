import phonenumbers
from phonenumbers import geocoder
import folium

def get_location(phone_number):
    parsed_number=phonenumbers.parse(phone_number)
    location= geocoder.description_for_number(parsed_number,"en")
    my_map= folium.Map(location=[20,0],zoom_start=2)
    folium.Marker([20,0],popup=location).add_to(my_map)
    my_map.save("haya.html")
    return{
        "phone_number": phone_number,
        "location":location

    }
print(get_location("+97433572883"))