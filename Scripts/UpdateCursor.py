import arcpy

shp = r"C:\Users\ehooten\LPA\Data\ne_10m_admin_0_countries.shp"

fc = r"C:\Users\ehooten\LPA\Projects\CursorProject\CursorProject.gdb\countries"

arcpy.env.overwriteOutput = True
arcpy.management.CopyFeatures(
    in_features=shp,
    out_feature_class=fc,
    config_keyword="",
    spatial_grid_1=None,
    spatial_grid_2=None,
    spatial_grid_3=None
)

arcpy.management.AddField(fc,"GDPperPerson","FLOAT")

with arcpy.da.UpdateCursor(fc,['NAME',"GDPperPerson"],"FID < 10") as cursor:
    for row in cursor:
        row[0] = row[0].upper()
        cursor.updateRow(row)
        print(row)



print("\nScript completed")
