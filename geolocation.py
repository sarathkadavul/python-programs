#uses google maps api
#pip install googlemaps for installing googlemaps api module
import googlemaps

#gets the address
location = raw_input("Enter the address")

#you can generate your own key from developer.google.com
gmkey = googlemaps.Client(key="AIzaSyAxa5bAMnE913kjuPSFz2xDxTvo_4X6OKc")

#requests for geocode function with location as parameter
geoloc = gmkey.geocode(location)

filter1 = geoloc[0]

filter2 =  filter1['geometry']

filter3 = filter2['location']

lat = filter3['lat']
lng = filter3['lng']
print 'latitude = ',lat
print 'longitude = ',lng
