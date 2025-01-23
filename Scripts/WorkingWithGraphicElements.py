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

# Graphic objects
borderLineLeft = lyt.listElements("GRAPHIC_ELEMENT", "border_line")[0]
borderLineLeft.name = "border_line_left"
borderLineLeft.elementWidth = 0 #vertical line
borderLineLeft.elementHeight = lyt.pageHeight
borderLineLeft.elementPositionX = 5
borderLineLeft.elementPositionY = lyt.pageHeight /2

borderLineRight = borderLineLeft.clone()
borderLineRight.name = "border_line_right"
borderLineRight.elementPositionX = lyt.pageWidth - 5

borderLineTop = borderLineLeft.clone()
borderLineTop.name = "border_line_top"
borderLineTop.elementHeight = 0 #horizontal line
borderLineTop.elementWidth = lyt.pageWidth
borderLineTop.elementPositionY = lyt.pageHeight - 5
borderLineTop.elementPositionX = lyt.pageWidth /2

borderLineBottom = borderLineTop.clone()
borderLineBottom.name = "border_line_bottom"
borderLineBottom.elementPositionY = 5

borderPointNW = lyt.listElements("GRAPHIC_ELEMENT", "border_point")[0]
borderPointNW.name = "border_point_nw"
borderPointNW.elementHeight = 5
borderPointNW.elementWidth = 5
borderPointNW.elementPositionY = lyt.pageHeight - 2.5
borderPointNW.elementPositionX = 2.5

borderPointSW = borderPointNW.clone()
borderPointSW.name = "border_point_sw"
borderPointSW.elementPositionY = 2.5

borderPointSE = borderPointSW.clone()
borderPointSE.name = "border_point_se"
borderPointSE.elementPositionX = lyt.pageWidth- 2.5

borderPointNE = borderPointNW.clone()
borderPointNE.name = "border_point_ne"
borderPointNE.elementPositionX = lyt.pageWidth - 2.5



# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"C:\Users\ehooten\LPA\PDFs\test.pdf")
os.startfile(r"C:\Users\ehooten\LPA\PDFs\test.pdf")

# Delete project object
del aprx
