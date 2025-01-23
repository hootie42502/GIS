import arcpy,pprint

def print_source(layerName):
    lyrToPrint = mapx.listLayers(layerName)[0]
    print("Layer: {0} \n    Data Source: {1}".format(lyrToPrint.name,lyrToPrint.dataSource))

def print_dict(dict2Print):
    pprint.pprint(dict2Print)
    

aprx = arcpy.mp.ArcGISProject(r"C:\Users\ehooten\LPA\Projects\DataSourceProject\DataSourceProject.aprx")
mapx = aprx.listMaps()[0]
print_source("Countries")

lyr = mapx.listLayers("Countries")[0]
defaultGDB = r"C:\Users\ehooten\LPA\Projects\DataSourceProject\DataSourceProject.gdb"
origConnPropDict = lyr.connectionProperties
print_dict(origConnPropDict)


newConnPropDict = {'connection_info': {'database': defaultGDB},
 'dataset': 'Countries_African',
 'workspace_factory': 'File Geodatabase'}
lyr.updateConnectionProperties(origConnPropDict,newConnPropDict)

print_dict(newConnPropDict)
print_source("Countries")


del aprx
    
