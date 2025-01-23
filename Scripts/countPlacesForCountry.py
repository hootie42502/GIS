import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\ehooten\LPA\Projects\FrameworkProject\FrameworkProject.gdb"
countryName= arcpy.GetParameterAsText(0)


def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)

arcpy.analysis.Select(
    in_features=r"C:\Users\ehooten\LPA\Data\ne_10m_admin_0_countries.shp",
    out_feature_class="SelCountry",
    where_clause="NAME = '{0}'".format(countryName)
)
arcpy.analysis.Buffer(
    in_features="SelCountry",
    out_feature_class="SelCountry_Buffer",
    buffer_distance_or_field="200 Kilometers",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)
arcpy.analysis.Clip(
    in_features=r"C:\Users\ehooten\LPA\Data\ne_10m_populated_places.shp",
    clip_features="SelCountry_Buffer",
    out_feature_class="popPlaces_Clip",
    cluster_tolerance=None
)
print_message("There are " + str(arcpy.management.GetCount(
    in_rows="popPlaces_Clip")) + " places in or within 200 KM of {0}".format(countryName))
