import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

print_message("arcpy module imported successfully...")

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\ehooten\LPA\Data\Sample.gdb"

fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"C:\Users\ehooten\LPA\Data\ne_10m_admin_0_countries.shp"

numFeats = arcpy.GetCount_management(fc)
arcpy.AddMessage("{0} has {1} feature(s)".format(fc,numFeats))

#arcpy.CreateFileGDB_management(r"C:\Users\ehooten\LPA\Data","Sample")
#arcpy.Select_analysis(fc,"Egypt","NAME = 'Egypt'")                


print_message("Script completed!")
