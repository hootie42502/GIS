import arcpy

arcpy.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\ehooten\LPA\Projects\GeomProject\GeomProject.gdb"

#MEASURE AREA OF FISHNET AND GET SPATIAL REFERENCE
geomList = arcpy.management.CopyFeatures("FishnetPolys", arcpy.Geometry())
area = 0.0
for geom in geomList:
    if area == 0.0:
        sr = geom.spatialReference
    
    area += geom.area

print("Total area: {0}".format(area))
print("Spatial Reference: {0}".format(sr.name))

#ADD POINTS
point = arcpy.Point(2.5, 1.75)
pointGeom = arcpy.PointGeometry(point,sr)
point2 = arcpy.Point(3, 3)
pointGeom2 = arcpy.PointGeometry(point2,sr)
point3 = arcpy.Point(5, 1.75)
pointGeom3 = arcpy.PointGeometry(point3,sr)
arcpy.management.CopyFeatures([pointGeom,pointGeom2,pointGeom3],"PtGeom")

#ADD MULTIPLE POINTS
coordLists = [[(1.1,2.4),(4.9,2.6),(3.2,7.3)],
              [(6.1,8.8),(5.2,7.6),(7.1,2.3),(9.1,5.3)]]
multiPtGeom = []
for coordList in coordLists:
    multiPtGeom.append(
        arcpy.Multipoint(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),sr))
arcpy.management.CopyFeatures(multiPtGeom,"MultiPtGeom")

#ADD POLYLINES
polyLineGeom = []
for coordList in coordLists:
    polyLineGeom.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),sr))
arcpy.management.CopyFeatures(polyLineGeom,"PolyLineGeom")

#ADD POLYGONS
polygonGeom = []
for coordList in coordLists:
    polygonGeom.append(
        arcpy.Polygon(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),sr))
arcpy.management.CopyFeatures(polygonGeom,"PolygonGeom")

#ADD MULTIPART POLYGON
arrayList = []
for coordList in coordLists:
    arrayList.append(
        arcpy.Array([arcpy.Point(*coords) for coords in coordList]))

multiPartPolyGeom = arcpy.Polygon(arcpy.Array(arrayList),sr)
arcpy.management.CopyFeatures(multiPartPolyGeom,"MultiPartPolyGeom")

#ADD MULTIPART POLYLINE
arrayList = []
for coordList in coordLists:
    arrayList.append(
        arcpy.Array([arcpy.Point(*coords) for coords in coordList]))

multiPartLineGeom = arcpy.Polyline(arcpy.Array(arrayList),sr)
arcpy.management.CopyFeatures(multiPartLineGeom,"MultiPartLineGeom")

#ADD BUFFER TO multiPartLineGeom
bufferGeom = multiPartLineGeom.buffer(0.5)
arcpy.management.CopyFeatures(bufferGeom, "BufferGeom")

#ADD CONVEX HULL GEOMETRY
convexHullGeom = multiPartLineGeom.convexHull()
arcpy.management.CopyFeatures(convexHullGeom, "ConvexHullGeom")

#ADD CIRCLE GEOMETRY
circleCenter = arcpy.Point(5,3)
circleCenterGeom = arcpy.PointGeometry(circleCenter,sr)

circleGeom = circleCenterGeom.buffer(3)
arcpy.management.CopyFeatures(circleGeom, "CircleGeom")

#ADD INTERSECT GEOMETRY
intersectGeom = circleGeom.intersect(multiPartPolyGeom,4)
arcpy.management.CopyFeatures(intersectGeom, "IntersectGeom")

#SEPERATE MULTIPART GEOM INTO NEW GEOMS
intersectGeomList = []
for i in range(0,intersectGeom.partCount):
    intersectGeomList.append(
        arcpy.Polygon(
            arcpy.Array(intersectGeom.getPart(i)),sr))
arcpy.management.CopyFeatures(intersectGeomList, "IntersectSinglePartGeom")



#END OF SCRIPT
print("Script Completed")
