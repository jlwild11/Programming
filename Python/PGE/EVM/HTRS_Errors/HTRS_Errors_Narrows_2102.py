# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# HTRS_Errors_Narrows_2102.py
#
#   (generated by ArcGIS/ModelBuilder)
#   Edited by Jameson Wilder
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from datetime import datetime

# Edit these variables
Folder_Location = r"S:\ArcGIS\Projects\EVM\Narrows_2102\HTRS_Errors"
Circuit = str("Narrows_2102")
Expression_2_Date = str('2019-09-30 23:52:29')

## Edit these variables. Comment out the Veg Points you are not using. Or add a veg point location not listed

Vegetation_Point_Selected = "NARROWS_2102_V7_EVM_Veg_092019\\Vegetation Point"
#Vegetation_Point_Selected = "BANGOR_1101_V7_EVM_Veg_092019\\Vegetation Point"




# Local variables:
Vegetation_Point = Vegetation_Point_Selected

Expression = "(((\"STATUS\" = 'Work Identified' ) OR ( \"STATUS\" = 'In-Progress' ) OR ( \"STATUS\" = 'Quarantine' )) AND ((\"Tree_Matrix_Score\" = NULL) OR (\"Tree_Matrix_Score\" = '') OR ( \"Impact_Matrix_Score\" = NULL ) OR ( \"Impact_Matrix_Score\" = '' )))"

Expression_2 = "\"INS_DATE\" > date" + "'%s'" %Expression_2_Date


datestring = str(datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S'))
CircuitFileName = str("HTRS_Errors_" + Circuit + "_")
ExcelFileName = str(CircuitFileName + datestring + ".xls")
HTRS_Errors_xls = Folder_Location + "\\" + ExcelFileName


# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(Vegetation_Point, "NEW_SELECTION", Expression)

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(Vegetation_Point, "SUBSET_SELECTION", Expression_2)

# Process: Table To Excel
arcpy.TableToExcel_conversion(Vegetation_Point, HTRS_Errors_xls, "ALIAS", "CODE")

