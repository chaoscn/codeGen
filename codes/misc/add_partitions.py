targetSQLFolderPath=os.path.join(targetDBPath, "create")
createDir(targetSQLFolderPath)

parameters={}
sqls=[]
for i in range(0, partitionCount):
    parameters["partitionID"]="%d" % i
    sqls.append(templateCreateAddPartitions.substitute(parameters))
createFile(os.path.join(targetSQLFolderPath, "add_partitions_template.sql"), "".join(sqls))

parameters={}
sqls=[]
parameters["partitionIndexes"]=",".join(map(lambda x: "%d" % x, range(0, partitionCount-1)))
createFile(os.path.join(targetSQLFolderPath, "create_partition_function.sql"), templateCreateCreatePartitionFunction.substitute(parameters))

parameters={}
sqls=[]
parameters["fileGroupNames"]=",".join(map(lambda x: "MonitoringPartition%d" % x, range(0, partitionCount)))
createFile(os.path.join(targetSQLFolderPath, "create_partition_scheme.sql"), templateCreateCreateSchemeFunction.substitute(parameters))