import arcpy

arcpy.env.overwriteOutput = True

if not arcpy.Exists(r"C:\Users\ehooten\LPA\Data\test.gdb"):
    arcpy.management.CreateFileGDB(r"C:\Users\ehooten\LPA\Data", "test")


arcpy.env.workspace = r"C:\Users\ehooten\LPA\Data\test.gdb"
arcpy.conversion.FeatureClassToFeatureClass(
    r"C:\Users\ehooten\LPA\Data\ne_10m_admin_0_countries.shp",
    r"C:\Users\ehooten\LPA\Data\test.gdb",
    "Countries")

arcpy.conversion.FeatureClassToFeatureClass(
    r"C:\Users\ehooten\LPA\Data\ne_10m_admin_1_states_provinces.shp",
    r"C:\Users\ehooten\LPA\Data\test.gdb",
    "States")
                                            
print(arcpy.Exists(r"C:\Users\ehooten\LPA\Data\test.gdb\Countries"))

arcpy.analysis.Select("Countries","TrinidadTobago","NAME = 'Trinidad and Tobago'")

arcpy.analysis.Buffer(
    in_features="TrinidadTobago",
    out_feature_class="SelCountry_Buffer",
    buffer_distance_or_field="200 NauticalMiles",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="GEODESIC"
)

arcpy.env.extent = "SelCountry_Buffer"

arcpy.management.CopyFeatures("States","StatesInExtent")

print(arcpy.Exists(r"C:\Users\ehooten\LPA\Data\test.gdb\TrinidadTobago"))

print(arcpy.management.GetCount("StatesInExtent"))
print("\nScript Comnpleted!")
