from arcgis import GIS
import keyring
#Login to AGOL
system = "AGOL"
username = "mge_gis"
#password = ""
###store password with:
#keyring.set_password(system, username, password)
password = keyring.get_password(system, username)
gis = GIS("https://arcgis.com", username, password)