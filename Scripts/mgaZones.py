import arcpy,os

arcpy.env.overwriteOutput = True

#project object
aprx = arcpy.mp.ArcGISProject(
    r"C:\Users\ehooten\LPA\Projects\MGAZonesProject\MGAZonesProject.aprx")

#map objects
map54 = aprx.listMaps("Map 54")[0]
map55 = aprx.listMaps("Map 55")[0]
map56 = aprx.listMaps("Map 56")[0]

# layer object
placesLayer = map54.listLayers("Queensland Places")[0]

# layout object
lyt = aprx.listLayouts()[0]

#map frame objects
mapFrame54 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 54")[0]
mapFrame55 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 55")[0]
mapFrame56 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 56")[0]

#spatialRefTextObj
srText54 = lyt.listElements(
    "TEXT_ELEMENT",
    "Spatial Reference Text 54")[0]

srText55 = lyt.listElements(
    "TEXT_ELEMENT",
    "Spatial Reference Text 55")[0]

srText56 = lyt.listElements(
    "TEXT_ELEMENT",
    "Spatial Reference Text 55")[0]

finalPDF = r"C:\Users\ehooten\LPA\PDFs\MGAZones.pdf"
if(arcpy.Exists(finalPDF)):
   arcpy.management.Delete(finalPDF)
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

placesSorted = sorted(
    [row[0] for row in arcpy.da.SearchCursor(placesLayer,"NAME")])

placesCoordsDict = {row[0]:row[1] for row in arcpy.da.SearchCursor(
    placesLayer,["NAME","SHAPE@XY"])}

srPlacesLayer = arcpy.Describe(placesLayer).spatialReference

for pageCount,placeName in enumerate(placesSorted[:10]):
    xCoord,yCoord = placesCoordsDict[placeName]
    mgaZone = 1 + int((xCoord + 180) /6)
    print("{0} is in zone {1}".format(placeName,mgaZone))
    srMGA = arcpy.SpatialReference("GDA2020 MGA Zone {0}".format(mgaZone))

    geogFC = r"{0}\geogFC".format(aprx.defaultGeodatabase)
    projFC = r"{0}\projFC".format(aprx.defaultGeodatabase)

    arcpy.management.CreateFishnet(geogFC,
                                   "{0} {1}".format(xCoord - 0.25, yCoord - 0.25),
                                   "{0} {1}".format(xCoord - 0.25, yCoord + 0.25),
                                   0.5, 0.5, 1, 1,
                                   geometry_type="POLYGON",
                                   labels="NO_LABELS")

    arcpy.DefineProjection_management(geogFC,srPlacesLayer)
    arcpy.management.Project(geogFC,projFC,srMGA)
    projFCExtent = arcpy.Describe(projFC).extent

    if mgaZone == 54:
       mapFrame54.visible = True
       mapFrame54.camera.setExtent(projFCExtent)
       mapFrame54.camera.scale *= 1.05
       mapFrame55.visible = False
       mapFrame56.visible = False
       srText54.visible = True
       srText55.visible = False
       srText56.visible = False
    elif mgaZone == 55:
       mapFrame55.visible = True
       mapFrame55.camera.setExtent(projFCExtent)
       mapFrame55.camera.scale *= 1.05
       mapFrame54.visible = False
       mapFrame56.visible = False
       srText54.visible = False
       srText55.visible = True
       srText56.visible = False
    elif mgaZone == 56:
       mapFrame56.visible = True
       mapFrame56.camera.setExtent(projFCExtent)
       mapFrame56.camera.scale *= 1.05
       mapFrame55.visible = False
       mapFrame54.visible = False
       srText54.visible = False
       srText55.visible = False
       srText56.visible = True
    else:
       print("unexpected azone number")

    titleText = lyt.listElements("TEXT_ELEMENT","Title")[0]
    titleText.text = placeName

    lyt.exportToPDF(r"C:\Users\ehooten\LPA\PDFs\test{0}.pdf".format(pageCount))
    pdfDoc.appendPages(r"C:\Users\ehooten\LPA\PDFs\test{0}.pdf".format(pageCount))

pdfDoc.saveAndClose()
del pdfDoc
os.startfile(finalPDF)
del aprx
    
