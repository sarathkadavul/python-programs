import googlemaps

location = raw_input("Enter the address")

gmkey = googlemaps.Client(key="AIzaSyAxa5bAMnE913kjuPSFz2xDxTvo_4X6OKc")

geoloc = gmkey.geocode(location)

filter1 = geoloc[0]

filter2 =  filter1['geometry']

filter3 = filter2['location']

lat = filter3['lat']
lng = filter3['lng']
print 'latitude = ',lat
print 'longitude = ',lng
