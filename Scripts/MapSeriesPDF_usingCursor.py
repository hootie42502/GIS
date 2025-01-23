import arcpy,os

# Enable overwriting of outputs
arcpy.env.overwriteOutput = True
country = "Cambodia"

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"C:\Users\ehooten\LPA\Projects\MapSeriesProject\MapSeriesProject.aprx")

# Map objects
mainMap = aprx.listMaps("Main Map")[0]
overviewMap = aprx.listMaps("Overview Map")[0]

# Layer object
countriesLayer = mainMap.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame objects
mainMapFrame = lyt.listElements(
    'MAPFRAME_ELEMENT',"Main Map Frame")[0]

overviewMapFrame = lyt.listElements(
    'MAPFRAME_ELEMENT',"Overview Map Frame")[0]

#title object
titleText = lyt.listElements('TEXT_ELEMENT',"Text")[0]

finalPDF = r"C:\Users\ehooten\LPA\PDFs\test.pdf"
if arcpy.Exists(finalPDF):
    arcpy.management.Delete(finalPDF)
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

countriesSorted = sorted([row[0] for row in arcpy.da.SearchCursor(
    countriesLayer,
    "NAME")])

for pageCount,countryName in enumerate(countriesSorted[:10]):

    country = countryName
    titleText.text = country

    #Set zoom
    countriesLayer.definitionQuery = "NAME = '{0}'".format(country)
    selCountryExtent = mainMapFrame.getLayerExtent(countriesLayer)
    mainMapFrame.camera.setExtent(selCountryExtent)
    mainMapFrame.camera.scale *= 1.05

    # Export to PDF and open in Adobe Acrobat Reader
    lyt.exportToPDF(r"C:\Users\ehooten\LPA\PDFs\{0}.pdf".format(country))
    pdfDoc.appendPages(r"C:\Users\ehooten\LPA\PDFs\{0}.pdf".format(country))
#save pdf
pdfDoc.saveAndClose()
os.startfile(finalPDF)
del pdfDoc
# Delete project object
del aprx
