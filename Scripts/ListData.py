import arcpy
print("Script Starting...")

arcpy.env.workspace = r"C:\Users\ehooten\LPA"

wsList = arcpy.ListWorkspaces()

for ws in wsList:
    arcpy.env.workspace = ws
    gdbList = arcpy.ListWorkspaces("","FileGDB")
    print("\nWorkspace:" + ws)

    
    for gdb in gdbList:
        arcpy.env.workspace = gdb
        fcList = arcpy.ListFeatureClasses()
        print("    |\n    \__GDB: " + gdb)

        for fc in fcList:
            print("    :    \__FeatClass: " + fc)

        fdsList = arcpy.ListDatasets("","Feature")
        for fds in fdsList:
            print("    :    \__FeatDataset: " + fds)
            arcpy.env.workspace = fds
            fdsfcList = arcpy.ListFeatureClasses()
            
            for fdsfc in fdsfcList:
                print("    :        \__FeatClass: " + fc)
            
    
        arcpy.env.workspace = gdb
        tablesList = arcpy.ListTables()
        for table in tablesList:
            print("    :    \__Table: " + table)

            flds = [x.name for x in arcpy.ListFields(table)]
            fldsType = [x.type for x in arcpy.ListFields(table)]
            for index,field in enumerate(flds):
                print("    :        \__Field: " + str(field) + " || TYPE : " + str(fldsType[index]))
            
            
        

print("\nScript Completed!")
