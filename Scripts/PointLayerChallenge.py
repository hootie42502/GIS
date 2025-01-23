import arcpy


aprx = arcpy.mp.ArcGISProject(r"C:\Users\ehooten\LPA\Projects\SymbologyProject\SymbologyProject.aprx")

mapx = aprx.listMaps()[0]

point = mapx.listLayers("Countries")[0]

print(point.symbology)

sym = point.symbology

sym.updateRenderer("UniqueValueRenderer")

sym.renderer.fields = ["CONTINENT"]

point.symbology = sym

print(point.symbology)

aprx.save()

del aprx
