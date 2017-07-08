
import requests
import googlemaps
import os


try:
    API_KEY = os.environ["APIKEY"]
except KeyError:
    print "You need a Google API Key for the Distance Matrix API"

gmaps_client = googlemaps.Client(key=API_KEY)



def get_resource_addresses(names):
    """Make a call to the Google Places API for each shelter name."""

    info = []
    for name in names:
        try: 
            resp = gmaps_client.places(name)
            if resp['status'] == "OK":
                print "OK"
                info.append((name, resp['results'][0]['formatted_address']))
        except ApiError, e:
            print e
    return info
