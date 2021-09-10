# https://www.youtube.com/watch?v=HChq5_7yTGk
import googlemaps
# import pandas as pd
import time
gmaps = googlemaps.Client(key='AIzaSyDGZ5-H3el0Qomiwr0NYWkuXSA_del2koQ')
geocode_result = gmaps.geocode("臺北市")
print('geocode_result')

