# 'dataset' holds the input data for this script
import pandas as pd
# pyproj must be installed prior to import, (pip install pyproj)
from pyproj import Proj
df = pd.DataFrame(dataset)

def UTM2Geo(easting, northing, zona):
  UTM= Proj('+proj=utm +zone='+str(zona)+' +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs')
  geo = UTM(easting,northing,inverse=True)
  return geo
# Converting easting and northing UTM zone 50S to Latitude and Longitude
# Change UTM zone respectively
df['Longitude'] = UTM2Geo(df['Easting'].values,df['Northing'].values,50)[0]
df['Latitude'] = UTM2Geo(df['Easting'].values,df['Northing'].values,50)[1]
