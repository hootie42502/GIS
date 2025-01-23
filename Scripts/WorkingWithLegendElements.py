import arcpy,os

# Enable overwriting of outputs
arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"C:\Users\ehooten\LPA\Projects\LayoutProject\LayoutProject.aprx")

# Map object
mapx = aprx.listMaps("Map")[0]

# Layer object
countriesLayer = mapx.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame object
mapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
mapFrame.elementWidth = lyt.pageWidth - 20
mapFrame.elementHeight = mapFrame.elementWidth
mapFrame.elementPositionX = 10
mapFrame.elementPositionY = lyt.pageHeight / 4

# legend object
legend = lyt.listElements("LEGEND_ELEMENT", "Legend")[0]
legend.title = "Contents"
legend.showTitle = True

placesLayer = mapx.addDataFromPath(r"C:\Users\ehooten\LPA\Data\ne_10m_populated_places.shp")

legend.syncNewLayer = False

railraodsLayer = mapx.addDataFromPath(r"C:\Users\ehooten\LPA\Data\ne_10m_railroads.shp")

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"C:\Users\ehooten\LPA\PDFs\test.pdf")
os.startfile(r"C:\Users\ehooten\LPA\PDFs\test.pdf")

# Delete project object
del aprx
