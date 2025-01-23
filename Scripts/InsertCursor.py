import arcpy

arcpy.env.overwriteOutput = True

#CREATE A NEW TABLE
fGDB = r"C:\Users\ehooten\LPA\Projects\CursorProject\CursorProject.gdb"
tableName = "testTable"
fgdbTable = r"{0}\{1}".format(fGDB,tableName)
arcpy.management.CreateTable(fGDB, tableName)
arcpy.management.AddField(fgdbTable, "TextField","TEXT",field_length=5)
arcpy.management.AddField(fgdbTable, "IntField","SHORT")
arcpy.management.AddField(fgdbTable, "FloatField","FLOAT")

fieldList = ["TextField", "IntField", "FloatField"]
cursor = arcpy.da.InsertCursor(fgdbTable,fieldList)
cursor.insertRow(["A",1,0.1])
cursor.insertRow(["B",3,0.2])
cursor.insertRow(["C",5,0.3])
del cursor

with arcpy.da.SearchCursor(fgdbTable,fieldList) as cursor:
    for row in cursor:
       print(row)


#CREATE GEOMETRY AND INSERT IT INTO FC
shp = r"C:\Users\ehooten\LPA\Data\ne_10m_admin_0_countries.shp"
fc = r"C:\Users\ehooten\LPA\Projects\CursorProject\CursorProject.gdb\countries"
arcpy.management.CopyFeatures(shp, fc)

cursor = arcpy.da.InsertCursor(fc,["SHAPE@","NAME"])

sr = arcpy.SpatialReference("WGS 1984")
nullIslandPt = arcpy.Point(0,0)
nullIslandGeom = arcpy.PointGeometry(nullIslandPt,sr).buffer(5)
cursor.insertRow([nullIslandGeom,"Null Island"])
del cursor
                  


print("Script Completed!")
