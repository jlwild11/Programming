# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# HTRS_Errors_Excel_Export.py
# Created by Model Builder to start from and further edited by Jameson Wilder
# Edited by Jameson Wilder 2019-11-14
# Description: Script created to find Vegetation Points with HTRS errors.
# ---------------------------------------------------------------------------

# Import arcpy module
arcpy.AddMessage("Importing arcpy modules")

import arcpy
from datetime import datetime

# Edit these variables
arcpy.AddMessage("Importing variables")

Vegetation_Point = arcpy.GetParameterAsText(0)
Expression_2_Date = arcpy.GetParameterAsText(1)
RunExcelExport = arcpy.GetParameterAsText(2)


# Local variables:
arcpy.AddMessage("Importing SQL Expression variables")

Expression = "(\"STATUS\" = 'Work Identified' OR \"STATUS\" = 'In-Progress' OR \"STATUS\" = 'Quarantine' ) AND (\"Tree_Matrix_Score\" IS NULL OR \"Tree_Matrix_Score\" = '' OR \"Impact_Matrix_Score\" IS NULL OR \"Impact_Matrix_Score\" = '' )"

Expression_1 = "( \"Tree_Matrix_Score\" IS NULL OR \"Tree_Matrix_Score\" = '' OR  \"Impact_Matrix_Score\" IS NULL  OR  \"Impact_Matrix_Score\" = '' ) AND ( \"STATUS\" = 'Tree Work Complete'  OR  \"STATUS\" = 'Wood Mgmt Complete' ) AND NOT ( \"PRESCRIP\" LIKE 'BC_Br Rmv' OR  \"PRESCRIP\" LIKE 'BCS_Br Rmv+Trt' OR  \"PRESCRIP\" LIKE 'F1A_FP-Rmv1 A' OR  \"PRESCRIP\" LIKE 'F1B_FP-Rmv1 B' OR  \"PRESCRIP\" LIKE 'F1C_FS-R1A+Trt' OR  \"PRESCRIP\" LIKE 'F1D_FS-R1B+Trt' OR  \"PRESCRIP\" LIKE 'F2A_FP-Rmv2 A' OR  \"PRESCRIP\" LIKE 'F2B_FP-Rmv2 B' OR  \"PRESCRIP\" LIKE 'F2C_FS-R2A+Trt' OR  \"PRESCRIP\" LIKE 'F2D_FS-R2B+Trt' OR  \"PRESCRIP\" LIKE 'F3A_FP-Rmv3 A' OR  \"PRESCRIP\" LIKE 'F3B_FP-Rmv3 B' OR  \"PRESCRIP\" LIKE 'F3C_FS-R3A+Trt' OR  \"PRESCRIP\" LIKE 'F3D_FS-R3B+Trt' OR  \"PRESCRIP\" LIKE 'F4A_FP-Rmv4 A' OR  \"PRESCRIP\" LIKE 'F4B_FP-Rmv4 B' OR  \"PRESCRIP\" LIKE 'F4C_FS-R4A+Trt' OR  \"PRESCRIP\" LIKE 'F4D_FS-R4B+Trt' OR  \"PRESCRIP\" LIKE 'R1A_Rmv 1-A' OR  \"PRESCRIP\" LIKE 'R1B_Rmv 1-B' OR  \"PRESCRIP\" LIKE 'R1C_Rmv1-A+Trt' OR  \"PRESCRIP\" LIKE 'R1D_Rmv1-B+Trt' OR  \"PRESCRIP\" LIKE 'R2A_Rmv 2-A' OR  \"PRESCRIP\" LIKE 'R2B_Rmv 2-B' OR  \"PRESCRIP\" LIKE 'R2C_Rmv2-A+Trt' OR  \"PRESCRIP\" LIKE 'R2D_Rmv2-B+Trt' OR  \"PRESCRIP\" LIKE 'R3A_Rmv 3-A' OR  \"PRESCRIP\" LIKE 'R3B_Rmv 3-B' OR  \"PRESCRIP\" LIKE 'R3C_Rmv3-A+Trt' OR  \"PRESCRIP\" LIKE 'R3D_Rmv3-B+Trt' OR  \"PRESCRIP\" LIKE 'R4A_Rmv 4-A' OR  \"PRESCRIP\" LIKE 'R4B_Rmv 4-B' OR  \"PRESCRIP\" LIKE 'R4C_Rmv4-A+Trt' OR  \"PRESCRIP\" LIKE 'R4D_Rmv4-B+Trt' OR  \"PRESCRIP\" LIKE 'RC2_Crane Rmv2' OR  \"PRESCRIP\" LIKE 'RC3_Crane Rmv3' OR  \"PRESCRIP\" LIKE 'RC4_Crane Rmv4' OR  \"PRESCRIP\" LIKE 'Remove' OR  \"PRESCRIP\" LIKE 'Remove + Treat')"

Expression_2 = "\"INS_DATE\" < date" + "'%s'" %Expression_2_Date



# Process: Select Layer By Attribute
arcpy.AddMessage("Running Select Layer By Attribute: HTRS Errors AND have a STATUS of Work Identified or In-Progress or Quarantine")
arcpy.SelectLayerByAttribute_management(Vegetation_Point, "NEW_SELECTION", Expression)


# Process: Select Layer By Attribute (HTRS errors that are STATUS Tree Work Complete or Wood Mgmt Complete AND do not have Prescriptions in Expression_1)
arcpy.AddMessage("Running Select Layer By Attribute: Adding to the previous selection HTRS errors that are STATUS Tree Work Complete or Wood Mgmt Complete AND do not have Prescriptions in Expression_1")
arcpy.SelectLayerByAttribute_management(Vegetation_Point, "ADD_TO_SELECTION", Expression_1)


# Process: Select Layer By Attribute (Date Filter)
arcpy.AddMessage("Running Select Layer By Attribute: Filtering for veg points with Inspection Dates greater than " + Expression_2_Date )
arcpy.SelectLayerByAttribute_management(Vegetation_Point, "REMOVE_FROM_SELECTION", Expression_2)


# Start Process: Table To Excel
ExcelYes = str(RunExcelExport)
arcpy.AddMessage("Create Excel Export Table = "+ ExcelYes)


if ExcelYes == 'true':
  arcpy.AddMessage("Creating Excel Export Table")

  Circuit = arcpy.GetParameterAsText(3)
  Folder_Location = arcpy.GetParameterAsText(4)

  datestring = str(datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S'))
  CircuitFileName = str("HTRS_Errors_" + Circuit + "_")
  ExcelFileName = str(CircuitFileName + datestring + ".xls")
  HTRS_Errors_xls = Folder_Location + "\\" + ExcelFileName

  arcpy.TableToExcel_conversion(Vegetation_Point, HTRS_Errors_xls, "ALIAS", "CODE")
  arcpy.AddMessage("Excel Export Table Created")
else:
  arcpy.AddMessage("Script Finished")
# Finish Process: Table To Excel

arcpy.AddMessage("Script Finished")
