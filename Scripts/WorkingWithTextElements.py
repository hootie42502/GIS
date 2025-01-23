import arcpy,os

countryName = "Belgium"

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

#zoom to country in question
countriesLayer.definitionQuery = "NAME = '{0}'".format(countryName)
selCountryExtent = mapFrame.getLayerExtent(countriesLayer)
mapFrame.camera.setExtent(selCountryExtent)
mapFrame.camera.scale = mapFrame.camera.scale * 1.05

#text objects
titleText = lyt.listElements("TEXT_ELEMENT","title_text")[0]
titleText.textSize = 20
titleText.elementPositionX = lyt.pageWidth / 2
titleText.elementPositionY = lyt.pageHeight - 10
titleText.text = "<BOL>{0}</BOL>".format(countryName)

subtitleText = titleText.clone()
subtitleText.textSize = 14
subtitleText.text = "Map of {0} with Topographic Background".format(countryName)
subtitleText.elementPositionY = titleText.elementPositionY - 10

datePathText = titleText.clone()
datePathText.text = 'PDF created <dyn type="date" format="long"/> from <dyn type="project" property="path"/>'
datePathText.textSize = 7
datePathText.elementPositionY = 5

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"C:\Users\ehooten\LPA\PDFs\test.pdf")
os.startfile(r"C:\Users\ehooten\LPA\PDFs\test.pdf")

# Delete project object
del aprx
