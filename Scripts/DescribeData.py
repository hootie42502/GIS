import arcpy

dataElement = r"C:\Users\ehooten\LPA\Data\Sample.gdb\NaturalEarth\railroads"
desc = arcpy.Describe(dataElement)

print("Describing {0}...".format(dataElement))
print("Name:            " + desc.name)
print("DataType:        " + desc.dataType)
print("CatalogPath:     " + desc.catalogPath)
print("Children:")
for child in desc.children:
    print("    {0} is a {1}".format(child.name, child.dataType))

print("\n Script Completed!")
