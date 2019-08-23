#!/usr/bin/python

import arcpy
import os

# Set local variables
workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\EVM\Sierra\El_Dorado\El_Dorado_2101\Tiger_Lily_2\TigerLily_2.gdb\Veg_Points_Work"

#Set spatial join variables
in_layer_or_view = os.path.join(workspace, "Veg_Points_2_Projects_Join")
selection_type = "NEW_SELECTION"
Project_Order_Number = 6
Project_Order_Number = str(Project_Order_Number)
where_clause = '"Proj_Order" = '+ Project_Order_Number

arcpy.SelectLayerByAttribute_management(in_layer_or_view, selection_type, where_clause)
