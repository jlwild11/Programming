# Import system modules
import arcpy
import re
# Set environment settings
arcpy.env.workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\PythonTesting\PythonTesting.gdb"

# Set local variables
inTable = "TM_Marking_Master_05"
field = "COMMENTS"
expression = "add_period(!COMMENTS!)"
expression_type = "PYTHON3"


codeblock = """
def add_period(text):
    period = '.'
    sentences = text + period
    return sentences"""


# Execute CalculateField
arcpy.CalculateField_management(inTable, field, expression, expression_type, codeblock)
