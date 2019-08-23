import arcpy
import os


# Set local variables
workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\EVM\Sierra\El_Dorado\El_Dorado_2101\Tiger_Lily_2\TigerLily_2.gdb"
outWorkspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\EVM\Sierra\El_Dorado\El_Dorado_2101\Tiger_Lily_2\TigerLily_2.gdb"


###
####SpatialJoin Projects to Veg_Points to add "Proj_Order" to Veg_Points table
###

#Set spatial join variables
target_features = os.path.join(workspace, "Veg_Points_Work\Veg_Points_1")
join_features = os.path.join(workspace, "Projects")
out_feature_class = os.path.join(outWorkspace, "Veg_Points_Work\Veg_Points_2_Projects_Join")
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = "#"
match_option = "HAVE_THEIR_CENTER_IN"
search_radius = "#"
distance_field_name = "#"

#SpatialJoin Projects to Veg_Points to add "Proj_Order" to Veg_Points table
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, join_operation, join_type, field_mapping, match_option, search_radius, distance_field_name)
