import pandas as pd
from arcgis import GIS

gis = agol_login_with_keyring.py

item = gis.content.get("f8851052b37f443e975003a994bb247c")
flayer = item.layers[0]
agol_sdf = pd.DataFrame.spatial.from_layer(flayer)
#agol_sdf.head()