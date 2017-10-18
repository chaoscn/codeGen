####################################
#                                  #
#   Compatible with python 2.6.x   #
#   Author: yincao                 #
#                                  #
####################################

import os, sys, re, string, stat, math
import xml.dom.minidom

targetRootPath="C:\codeGen"
sourceRootPath=os.path.join(targetRootPath, "private", "Monitoring", "CodeGen")
sourceTemplatePath=os.path.join(sourceRootPath, "templates")
targetDBPath=os.path.join(targetRootPath, r"private\Monitoring\SQL\MonitoringDB")
targetDOPath=os.path.join(targetRootPath, r"private\Monitoring\MonitoringLib\DO")
targetInterfaceConfigurationsPath=os.path.join(targetRootPath, r"private\Monitoring\MonitoringInterface\Configurations")
targetInterfaceImplementsConfigurationsPath=os.path.join(targetRootPath, r"private\Monitoring\MonitoringLib\Models\InterfaceImplements\Configurations")
targetMonitoringDBWxi=os.path.join(targetRootPath, r"private\Monitoring\Installers\MonitoringDB")
targetMonitoringWebWxi=os.path.join(targetRootPath, r"private\Monitoring\Installers\MonitoringWeb")
targetDAOPath=os.path.join(targetRootPath, r"private\Monitoring\MonitoringLib\DAO")
sourceMonitoringWebCSProjPath=os.path.join(targetRootPath, r"private\Monitoring\MonitoringWeb\MonitoringWeb.csproj")

patternSPInputParameters=re.compile(r"^\s*@([\w_]+)\s+(\w+)", re.I|re.M)

templateCreateAddPartitions=string.Template(open(os.path.join(sourceTemplatePath, "create.add.partitions.sql")).read())
templateCreateCreatePartitionFunction=string.Template(open(os.path.join(sourceTemplatePath, "create.create.partition.function.sql")).read())
templateCreateCreateSchemeFunction=string.Template(open(os.path.join(sourceTemplatePath, "create.create.partition.scheme.sql")).read())
templatePopulateTable=string.Template(open(os.path.join(sourceTemplatePath, "populate.tbl.sql")).read())
templatePopulateIndexNC=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.nc.sql")).read())
templatePopulateIndexNCXML=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.nc.xml.sql")).read())
templatePopulateIndexNCFullText=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.nc.full.text.sql")).read())
templatePopulateIndexNCFullTextForUpgrade=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.nc.full.text.for.upgrade.sql")).read())
templatePopulateIndexFK=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.fk.sql")).read())
templatePopulateIndexSources=string.Template(open(os.path.join(sourceTemplatePath, "populate.index.sources")).read())
templatePopulateView=string.Template(open(os.path.join(sourceTemplatePath, "populate.view.sql")).read())
templatePopulateViewSources=string.Template(open(os.path.join(sourceTemplatePath, "populate.view.sources")).read())
templatePopulateSP=string.Template(open(os.path.join(sourceTemplatePath, "populate.sp.sql")).read())
templatePopulateSPSources=string.Template(open(os.path.join(sourceTemplatePath, "populate.sp.sources")).read())
templatePopulateFN=string.Template(open(os.path.join(sourceTemplatePath, "populate.fn.sql")).read())
templatePopulateFNSources=string.Template(open(os.path.join(sourceTemplatePath, "populate.fn.sources")).read())
templatePopulateTblSources=string.Template(open(os.path.join(sourceTemplatePath, "populate.tbl.sources")).read())
templatePopulateMiscData=string.Template(open(os.path.join(sourceTemplatePath, "populate.misc.data.sql")).read())
templatePopulateMiscUserGrantPerm=string.Template(open(os.path.join(sourceTemplatePath, "populate.misc.user.grantperm.sql")).read())
templateDataObjectWhole=string.Template(open(os.path.join(sourceTemplatePath, "data.object.whole.cs")).read())
templateDataObjectProperty=string.Template(open(os.path.join(sourceTemplatePath, "data.object.property.cs")).read())
templateDataObjectRowToProperty=string.Template(open(os.path.join(sourceTemplatePath, "data.object.row.to.property.cs")).read())
templateDataObjectRowToDataRow=string.Template(open(os.path.join(sourceTemplatePath, "data.object.row.to.data.row.cs")).read())
templateDataObjectToString=string.Template(open(os.path.join(sourceTemplatePath, "data.object.to.string.cs")).read())
templateDataObjectClone=string.Template(open(os.path.join(sourceTemplatePath, "data.object.clone.cs")).read())
templateSpilDataWhole=string.Template(open(os.path.join(sourceTemplatePath, "spil.data.whole.cs")).read())
templateSpilDataPublicMethod=string.Template(open(os.path.join(sourceTemplatePath, "spil.data.public.method.cs")).read())
templateSpilDataBatchAnyWhole=string.Template(open(os.path.join(sourceTemplatePath, "spil.data.batch.any.whole.cs")).read())
templateSpilDataPublicMethodBatchAny=string.Template(open(os.path.join(sourceTemplatePath, "spil.data.public.method.batch.any.cs")).read())
templateInstallerMonitoringDBPartition=string.Template(open(os.path.join(sourceTemplatePath, "installer.monitoringdb.partition.wxi")).read())
templateInstallerMonitoringDBCADuplicateFile=string.Template(open(os.path.join(sourceTemplatePath, "installer.monitoringdb.ca.duplicatefile.wxi")).read())
templateInstallerMonitoringDBImportDataFile=string.Template(open(os.path.join(sourceTemplatePath, "installer.monitoringdb.import.data.file.wxi")).read())
templateInstallerMonitoringDBGeneric=string.Template(open(os.path.join(sourceTemplatePath, "installer.monitoringdb.generic.wxi")).read())
templateInstallerMonitoringDBAttachDBTemplate=string.Template(open(os.path.join(sourceTemplatePath, "installer.monitoringdb.attach.db.template.sql")).read())
templateMonitoringInterfaceConfigurationsIGlobalConfiguration=string.Template(open(os.path.join(sourceTemplatePath, "MonitoringInterface.Configurations.IGlobalConfiguration.cs")).read())
templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfiguration=string.Template(open(os.path.join(sourceTemplatePath, "MonitoringLib.Models.InterfaceImplements.Configurations.GlobalConfiguration.cs")).read())
templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationUpdate=string.Template(open(os.path.join(sourceTemplatePath, "MonitoringLib.Models.InterfaceImplements.Configurations.GlobalConfiguration.update.cs")).read())
templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationPropertyInt=string.Template(open(os.path.join(sourceTemplatePath, "MonitoringLib.Models.InterfaceImplements.Configurations.GlobalConfiguration.property.int.cs")).read())
templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationPropertyString=string.Template(open(os.path.join(sourceTemplatePath, "MonitoringLib.Models.InterfaceImplements.Configurations.GlobalConfiguration.property.string.cs")).read())

maxTableCountInView=256
partitionCount=16

def createDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def createFile(filePath, fileContent):
    if filePath.rfind(".sql")==len(filePath)-4:
        fileContent="""--
-- This file is generated by private\Monitoring\CodeGen\codegen.py
-- Please don't edit this file.
--

""" + fileContent
    isSDAdd=False
    if os.path.isfile(filePath):
        if open(filePath).read()==fileContent:
            print ("Skipped %s" % filePath)
            return
        fileAttributes=os.stat(filePath)[0]
        if not fileAttributes & stat.S_IWRITE:
            command="sd edit %s" % filePath
            print (command)
            process=os.popen(command, "r")
            text=process.read()
            print (text)
            process.close()
    else:
        isSDAdd=True
    fp=open(filePath, "w")
    fp.write(fileContent)
    fp.close()
    print ("Generated %s" % filePath)
    if isSDAdd:
        command="sd add %s" % filePath
        print (command)
        process=os.popen(command, "r")
        text=process.read()
        print (text)
        process.close()

def getSQLCompatibleString(text):
    text=text.replace("'", "''").replace("\r", " ").replace("\n", " ").strip()
    return "'%s'" % text

def getWithoutPlural(text):
    length=len(text)
    if text.rfind("ties")==length-4:
        return "%sy" % text[:length-3]
    if text.rfind("hes")==length-3:
        return text[:length-2]
    if text.rfind("s")==length-1:
        return text[:length-1]
    return text

def getCapitalized(text):
    text=text.lower()
    if text in ("id", "db", "api", "uri"):
        return text.upper()
    if text=="datetime":
        return "DateTime"
    return text.capitalize()

def getAllCapital(text):
    return "".join(map(getCapitalized, text.split("_")))

def getAllCapitalWithoutFirst(text):
    texts=text.split("_")
    return "".join(texts[:1]+map(getCapitalized, texts[1:]))

def getAllCapitalWithSpace(text):
    texts=text.split("_")
    return " ".join(map(getCapitalized, texts))

def getCleanText(text):
    return text.strip("'").replace(".", "").replace(" ", "").replace("_", "").replace("-", "")

def getWithoutFisrt(text):
    return text[text.index("_")+1:]

def getCSTypeFromDBType(dbType):
    dbType=dbType.lower()
    if dbType.find("int")==0:
        return "int"
    if dbType.find("smallint")==0:
        return "int16"
    if dbType.find("tinyint")==0:
        return "byte"
    if dbType.find("bigint")==0:
        return "long"
    if dbType.find("bit")==0:
        return "bool"
    if dbType.find("varchar")==0 or dbType.find("char")==0 or dbType.find("text")==0 or dbType.find("nvarchar")==0 or dbType.find("nchar")==0 or dbType.find("ntext")==0:
        return "string"
    if dbType.find("date")==0:
        return "DateTime"
    if dbType.find("decimal")==0:
        return "decimal"
    if dbType.find("float")==0:
        return "double"
    if dbType.find("xml")==0:
        return "string"
    return "unknow"

def getSQLTypeFromDBType(dbType):
    dbType=dbType.lower()
    if dbType.find("int")==0:
        return "SqlInt32"
    if dbType.find("smallint")==0:
        return "SqlInt16"
    if dbType.find("tinyint")==0:
        return "SqlByte"
    if dbType.find("bigint")==0:
        return "SqlInt64"
    if dbType.find("bit")==0:
        return "SqlBoolean"
    if dbType.find("varchar")==0 or dbType.find("char")==0 or dbType.find("text")==0 or dbType.find("nvarchar")==0 or dbType.find("nchar")==0 or dbType.find("ntext")==0:
        return "string"
    if dbType.find("date")==0:
        return "SqlDateTime"
    if dbType.find("decimal")==0:
        return "SqlDecimal"
    if dbType.find("float")==0:
        return "SqlDouble"
    if dbType.find("xml")==0:
        return "SqlXml"
    return "unknow"

def getCSDefaultValueFromDBType(dbType):
    dbType=dbType.lower()
    if dbType.find("int")==0:
        return "0"
    if dbType.find("smallint")==0:
        return "0"
    if dbType.find("tinyint")==0:
        return "0"
    if dbType.find("bigint")==0:
        return "0"
    if dbType.find("bit")==0:
        return "false"
    if dbType.find("varchar")==0 or dbType.find("char")==0 or dbType.find("text")==0 or dbType.find("nvarchar")==0 or dbType.find("nchar")==0 or dbType.find("ntext")==0:
        return "null"
    if dbType.find("date")==0:
        return "DateTime.MinValue"
    if dbType.find("decimal")==0:
        return "0"
    if dbType.find("float")==0:
        return "0"
    if dbType.find("xml")==0:
        return "null"
    return "unknow"

def getDataObjectProperty(column, xmlIgnore=None):
    parameter={}
    rawColumnName=getWithoutFisrt(column[0])
    parameter["dataObjectPropertyInUpperCase"]=getAllCapital(rawColumnName)
    parameter["dataObjectPropertyInLowerCase"]=getAllCapitalWithoutFirst(rawColumnName)
    parameter["dataObjectDataType"]=getCSTypeFromDBType(column[1])
    if xmlIgnore is not None and column[0] in xmlIgnore:
        parameter["dataObjectXmlSerialize"]="XmlIgnore"
    else:
        parameter["dataObjectXmlSerialize"]="XmlElement"
    return templateDataObjectProperty.substitute(parameter)

def getDataObjectRowToPropertie(column):
    parameter={}
    rawColumnName=getWithoutFisrt(column[0])
    parameter["dataObjectPropertyInUpperCase"]=getAllCapital(rawColumnName)
    parameter["dataObjectPropertyInLowerCase"]=getAllCapitalWithoutFirst(rawColumnName)
    parameter["dataObjectDataType"]=getCSTypeFromDBType(column[1])
    parameter["dataObjectPropertyDefaultValue"]=getCSDefaultValueFromDBType(column[1])
    return templateDataObjectRowToProperty.substitute(parameter)

def getDataObjectRowToDataRow(column):
    parameter={}
    rawColumnName=getWithoutFisrt(column[0])
    parameter["dataObjectPropertyInUpperCaseWithSpace"]=getAllCapitalWithSpace(rawColumnName)
    parameter["dataObjectPropertyInUpperCase"]=getAllCapital(rawColumnName)
    return templateDataObjectRowToDataRow.substitute(parameter)

def getDataObjectToString(column):
    parameter={}
    rawColumnName=getWithoutFisrt(column[0])
    parameter["dataObjectPropertyInUpperCase"]=getAllCapital(rawColumnName)
    return templateDataObjectToString.substitute(parameter)

def getDataObjectClone(column):
    parameter={}
    rawColumnName=getWithoutFisrt(column[0])
    parameter["dataObjectPropertyInUpperCase"]=getAllCapital(rawColumnName)
    return templateDataObjectClone.substitute(parameter)

def getSPDefinations(inputParameters):
    spDefinations=[]
    matchObjects=patternSPInputParameters.findall(inputParameters)
    if matchObjects:
        for matchObject in matchObjects:
            (name, type)=matchObject
            spDefinations.append({ "name": name, "type": type })
    return spDefinations

def getMethodInputs(spDefinations):
    methodInputs=""
    for spDefination in spDefinations:
        methodInputs+=", %s %s" % (getSQLTypeFromDBType(spDefination["type"]), spDefination["name"])
    return methodInputs

def getLogInputs(spDefinations):
    logInputs=""
    for spDefination in spDefinations:
        logInputs+=", \"%s\", %s" % (spDefination["name"], spDefination["name"])
    return logInputs

def getCallInputs(spDefinations):
    callInputs=""
    for spDefination in spDefinations:
        callInputs+=", %s" % spDefination["name"]
    return callInputs

def populateTableDict(table):
    columnDefinations=[]
    for column in table["columns"]:
        columnDefinations.append(" ".join(column))
    table["columnDefinations"]=",\n    ".join(columnDefinations)
    table["pkName"]=getWithoutFisrt(table["columns"][0][0])
    table["pkColumn"]=table["columns"][0][0]
    if "indexs" in table:
        for index in table["indexs"]:
            index["tableName"]=table["tableName"]
            index["indexColumns"]=",\n        ".join(index["columns"])
            if "unique" in index and index["unique"]:
                index["unique"]="UNIQUE"
            else:
                index["unique"]=""
            if "fullText" in index and index["fullText"]:
                index["pkName"]=table["pkName"]
    if "fks" in table:
        for fk in table["fks"]:
            fk["tableName"]=table["tableName"]
            fk["foreignKeyName"]="%s_%s" % (fk["tableName"], fk["foreignTableName"])
    if "sps" in table:
        for sp in table["sps"]:
            spDefinations=getSPDefinations(sp["inputParameters"])
            sp["methodInputs"]=getMethodInputs(spDefinations)
            sp["logIuputs"]=getLogInputs(spDefinations)
            sp["callIuputs"]=getCallInputs(spDefinations)
            sp["methodInputsBatchAny"]=sp["methodInputs"].strip(", ")
            sp["callIuputsBatchAny"]=sp["callIuputs"].strip(", ")
    if "initialData" in table:
        for initialData in table["initialData"]:
            initialData["tableName"]=table["tableName"]
            initialData["columnLine"]=", ".join(map(lambda x: x[0], table["columns"][1:]))
            initialData["where"]=" AND ".join(map(lambda x: "%s = %s" % (table["columns"][x][0], initialData["dataLine"][x-1]), table["initialDataWhereIndex"]))
            initialData["dataLine"]=", ".join(initialData["dataLine"])
    dataObjectProperties=[]
    for column in table["columns"]:
        if "xmlIgnores" in table:
            dataObjectProperties.append(getDataObjectProperty(column, table["xmlIgnores"]))
        else:
            dataObjectProperties.append(getDataObjectProperty(column))
    table["dataObject"]={
            "dataObjectName": "%sDO" % getAllCapital(getWithoutPlural(table["tableName"])),
            "dataObjectProperties": "".join(dataObjectProperties),
            "dataObjectRowToProperties": "".join(map(getDataObjectRowToPropertie, table["columns"])),
            "dataObjectRowToDataRows": "\n".join(map(getDataObjectRowToDataRow, table["columns"])),
            "dataObjectStrings": "\n".join(map(getDataObjectToString, table["columns"])),
            "dataObjectClones": "".join(map(getDataObjectClone, table["columns"])),
        }
    if "dataObjectExtra" in table:
        table["dataObject"]["dataObjectExtra"]=table["dataObjectExtra"]
    else:
        table["dataObject"]["dataObjectExtra"]=""

def getWXIDirFileXML(csProjPath, dirPrefix, guidStore):
    projectFiles=[]
    dom=xml.dom.minidom.parseString(open(csProjPath).read())
    for contentElement in dom.getElementsByTagName("Content"):
        if contentElement.hasAttribute("Include"):
            for copyToOutputDirectoryElement in contentElement.getElementsByTagName("CopyToOutputDirectory"):
                if copyToOutputDirectoryElement.firstChild.nodeValue in ("PreserveNewest", "Always"):
                    projectFiles.append(contentElement.attributes["Include"].value)
    document=xml.dom.minidom.Document()
    wxiDirFileRootElement, featureComponentRefElement=document.createElement("Root"), document.createElement("Root")
    wxiDirFileDictionary={}
    for projectFile in sorted(projectFiles):
        setWXIDirFileDictionary(wxiDirFileDictionary, list(projectFile.split("\\")))
    setWXIDirFileXMLs(document, dirPrefix, wxiDirFileRootElement, featureComponentRefElement, wxiDirFileDictionary, guidStore)
    wxiDirFileXMLs=wxiDirFileRootElement.toprettyxml("  ")
    wxiDirFileXMLs=wxiDirFileXMLs[7:]
    wxiDirFileXMLs=wxiDirFileXMLs[:len(wxiDirFileXMLs)-9]
    featureComponentRefXMLs=featureComponentRefElement.toprettyxml("  ")
    featureComponentRefXMLs=featureComponentRefXMLs[7:]
    featureComponentRefXMLs=featureComponentRefXMLs[:len(featureComponentRefXMLs)-9]
    return wxiDirFileXMLs, featureComponentRefXMLs

def setWXIDirFileXMLs(document, prefix, parentElement, featureComponentRefElement, wxiDirFileDictionary, guidStore):
    if "." in wxiDirFileDictionary:
        componentID="%sComponent" % prefix.replace("\\", "").replace("-", "")
        componentElement=document.createElement("Component")
        componentElement.setAttribute("Guid", guidStore.pop())
        componentElement.setAttribute("Id", componentID)
        parentElement.appendChild(componentElement)
        componentRefElement=document.createElement("ComponentRef")
        componentRefElement.setAttribute("Id", componentID)
        featureComponentRefElement.appendChild(componentRefElement)
        for fileName in wxiDirFileDictionary["."]:
            fileElement=document.createElement("File")
            fileElement.setAttribute("Name", fileName)
            fileElement.setAttribute("Source", "$(var.PROJECTDIR)\\%s\\" % prefix)
            fileElement.setAttribute("Id", "%s%s" % (prefix.replace("\\", "").replace("-", ""), fileName.replace("-", "")))
            componentElement.appendChild(fileElement)
    for dirName in wxiDirFileDictionary:
        if dirName!=".":
            directoryElement=document.createElement("Directory")
            directoryElement.setAttribute("Name", dirName)
            directoryElement.setAttribute("Id", "%s%s" % (prefix.replace("\\", "").replace("-", ""), dirName.replace("\\", "").replace("-", "")))
            parentElement.appendChild(directoryElement)
            setWXIDirFileXMLs(document, "%s\\%s" % (prefix, dirName), directoryElement, featureComponentRefElement, wxiDirFileDictionary[dirName], guidStore)

def setWXIDirFileDictionary(parentDictionary, fileParts):
    if len(fileParts)>1:
        dirName=fileParts.pop(0)
        newParentDictionary={}
        if dirName in parentDictionary:
            newParentDictionary=parentDictionary[dirName]
        else:
            parentDictionary[dirName]=newParentDictionary
        setWXIDirFileDictionary(newParentDictionary, fileParts)
    else:
        fileName=fileParts.pop()
        fileNames=[]
        if "." in parentDictionary:
            fileNames=parentDictionary["."]
        else:
            parentDictionary["."]=fileNames
        fileNames.append(fileName)

tableNames=(
    "user_dashboard_group_settings",
    "config_dashboards",
    "config_dashboard_groups",
    "audit_extractor_logs",
    "audit_service_logs",
    "audit_user_activity_logs",
    "report_alerts",
    "report_alert_tasks",
    "config_common",
    "config_report_sources",
    "config_perf_counters",
    "config_perf_counter_references",
    "config_perf_counter_filters",
    "config_perf_counter_types",
    "config_api_partner_servers",
    "config_properties",
    "config_property_types",
    "config_api_partners",
    "config_partners",
    "config_apis",
    "file_api_test_logs",
    "config_api_tests",
    "report_value_latest",
    "report_value_hourly",
    "report_value_daily",
    "report_api_partner_value_latest",
    "report_api_partner_value_hourly",
    "report_api_partner_value_daily",
    "config_recommended_reports",
    "user_report_settings",
    "users",
    "user_groups",
    "config_reports",
    "config_servers",
    "config_data_centers",
    "config_report_partitions",
    )
tables=[]
for tableName in tableNames:
    execfile(os.path.join(sourceRootPath, r"codes\db\%s.py" % tableName))

execfile(os.path.join(sourceRootPath, r"codes\misc\add_partitions.py"))

for table in tables:
    populateTableDict(table)

# populate\tbl
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "tbl")
createDir(targetSQLFolderPath)
tableSQLFileNameList=[]
for table in tables:
    tableSQLFileName="%s.sql" % table["tableName"]
    if "fileGroupName" not in table:
        table["fileGroupName"]="PRIMARY"
    if "tablePartitionCount" in table:
        originalTableName=table["tableName"]
        sqlStrings=[]
        for i in range(0, table["tablePartitionCount"]):
            table["tableName"]="%s_%d" % (originalTableName, i)
            table["fileGroupName"]="MonitoringPartition%d" % (i%partitionCount)
            sqlStrings.append(templatePopulateTable.substitute(table))
        table["tableName"]=originalTableName
        sqlString="".join(sqlStrings)
    else:
        sqlString=templatePopulateTable.substitute(table)
    createFile(os.path.join(targetSQLFolderPath, tableSQLFileName), sqlString)
    tableSQLFileNameList.append(tableSQLFileName)
parameters={}
parameters["tableSQLFileNameList"]=" \\\n                           ".join(tableSQLFileNameList)
createFile(os.path.join(targetSQLFolderPath, "sources"), templatePopulateTblSources.substitute(parameters))

# populate\index
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "index")
createDir(targetSQLFolderPath)
populateIndexFileNameList=[]
for table in tables:
    if "indexs" in table:
        sqls=[]
        for index in table["indexs"]:
            templatePopulateIndex=templatePopulateIndexNC
            if "xml" in index and index["xml"]:
                templatePopulateIndex=templatePopulateIndexNCXML
            if "fullText" in index and index["fullText"]:
                templatePopulateIndex=templatePopulateIndexNCFullText
            if "tablePartitionCount" in table:
                originalTableName=index["tableName"]
                for i in range(0, table["tablePartitionCount"]):
                    index["tableName"]="%s_%d" % (originalTableName, i)
                    sqls.append(templatePopulateIndex.substitute(index))
                index["tableName"]=originalTableName
            else:
                sqls.append(templatePopulateIndex.substitute(index))
        populateIndexFileName="NC_%s.sql" % table["tableName"]
        populateIndexFileNameList.append(populateIndexFileName)
        createFile(os.path.join(targetSQLFolderPath, populateIndexFileName), "\n\n".join(sqls))
    if "fks" in table:
        sqls=[]
        for fk in table["fks"]:
            if "tablePartitionCount" in table:
                originalTableName=fk["tableName"]
                for i in range(0, table["tablePartitionCount"]):
                    fk["tableName"]="%s_%d" % (originalTableName, i)
                    sqls.append(templatePopulateIndexFK.substitute(fk))
                fk["tableName"]=originalTableName
            else:
                sqls.append(templatePopulateIndexFK.substitute(fk))
        populateIndexFileName="FK_%s.sql" % table["tableName"]
        populateIndexFileNameList.append(populateIndexFileName)
        createFile(os.path.join(targetSQLFolderPath, populateIndexFileName), "\n\n".join(sqls))
populateIndexFileNameList.sort()
# populate\index\sources
parameters={}
parameters["populateIndexFileNameList"]=" \\\n                           ".join(populateIndexFileNameList)
createFile(os.path.join(targetSQLFolderPath, "sources"), templatePopulateIndexSources.substitute(parameters))

# Installers\MonitoringDB\upgrade.fulltext.index.sql
createDir(targetMonitoringDBWxi)
sqls=[]
for table in tables:
    if "indexs" in table:
        for index in table["indexs"]:
            if "fullText" in index and index["fullText"]:
                sqls.append(templatePopulateIndexNCFullTextForUpgrade.substitute(index))
createFile(os.path.join(targetMonitoringDBWxi, "upgrade.fulltext.index.sql"), "\n\n".join(sqls))

# populate\view
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "view")
createDir(targetSQLFolderPath)
populateViewFileNameList=[]
for table in tables:
    if "views" in table:
        populateViewFileName="view_%s.sql" % table["tableName"]
        populateViewFileNameList.append(populateViewFileName)
        sqls=[]
        for view in table["views"]:
            sqls.append(templatePopulateView.substitute(view))
        createFile(os.path.join(targetSQLFolderPath, populateViewFileName), "".join(sqls))
populateViewFileNameList.sort()
# populate\view\sources
parameters={}
parameters["populateViewFileNameList"]=" \\\n                           ".join(populateViewFileNameList)
createFile(os.path.join(targetSQLFolderPath, "sources"), templatePopulateViewSources.substitute(parameters))

# populate\sp
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "sp")
createDir(targetSQLFolderPath)
spNames, spilDataPublicMethods, spilDataPublicMethodsBatchAny=[], [], []
for table in tables:
    if "sps" in table:
        for sp in table["sps"]:
            spNames.append(sp["spName"])
            spilDataPublicMethods.append(templateSpilDataPublicMethod.substitute(sp))
            spilDataPublicMethodsBatchAny.append(templateSpilDataPublicMethodBatchAny.substitute(sp))
            createFile(os.path.join(targetSQLFolderPath, "spm_%s.sql" % sp["spName"]), templatePopulateSP.substitute(sp))
spNames.sort()

# populate\sp\sources
# parameters={}
# parameters["populateSPFileNameList"]=" \\\n                           ".join(populateSPFileNameList)
# createFile(os.path.join(targetSQLFolderPath, "sources"), templatePopulateSPSources.substitute(parameters))

# populate\misc\user\grantperm.sql
parameters={}
parameters["grantPermLines"]="\n".join(map(lambda x: "GRANT EXECUTE ON spm_%s{}VERSION_SUFFIX TO MonitorOperators" % x, spNames))
targetGrantPermFolderPath=os.path.join(targetDBPath, "populate", "misc", "user")
createDir(targetGrantPermFolderPath)
createFile(os.path.join(targetGrantPermFolderPath, "grantperm.sql"), templatePopulateMiscUserGrantPerm.substitute(parameters))

# MonitoringLib\DAO\MonitoringData*.cs
parameters={}
parameters["publicMethods"]="".join(spilDataPublicMethods)
createDir(targetDAOPath)
createFile(os.path.join(targetDAOPath, "MonitoringDataLogging.cs"), templateSpilDataWhole.substitute(parameters))
parameters["publicMethods"]="".join(spilDataPublicMethodsBatchAny)
createFile(os.path.join(targetDAOPath, "MonitoringDataBatchedAnyLogging.cs"), templateSpilDataBatchAnyWhole.substitute(parameters))

# populate\fn
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "fn")
createDir(targetSQLFolderPath)
populateFNFileNameList=[]
for table in tables:
    if "fns" in table:
        for fn in table["fns"]:
            populateFNFileName="fnm_%s.sql" % fn["fnName"]
            populateFNFileNameList.append(populateFNFileName)
            createFile(os.path.join(targetSQLFolderPath, populateFNFileName), templatePopulateFN.substitute(fn))
populateFNFileNameList.sort()
# populate\fn\sources
parameters={}
parameters["populateFNFileNameList"]=" \\\n                           ".join(populateFNFileNameList)
createFile(os.path.join(targetSQLFolderPath, "sources"), templatePopulateFNSources.substitute(parameters))

# populate\misc\data
targetSQLFolderPath=os.path.join(targetDBPath, "populate", "misc", "data")
createDir(targetSQLFolderPath)
populateMiscDataFileNameList, populateMiscDataImportDataCMDLines=[], []
tables.reverse()
for table in tables:
    if "initialData" in table:
        sqls=[]
        for initialData in table["initialData"]:
            sqls.append(templatePopulateMiscData.substitute(initialData))
        populateMiscDataFileName="%s_data.sql" % initialData["tableName"]
        populateMiscDataFileNameList.append(populateMiscDataFileName)
        populateMiscDataImportDataCMDLines.append("cd /d %%1 & sqlcmd -b -E -w 255 -S localhost -d Monitoring -i %s" % populateMiscDataFileName)
        createFile(os.path.join(targetSQLFolderPath, populateMiscDataFileName), "".join(sqls))
tables.reverse()
# populate\misc\data\ImportData.cmd
createFile(os.path.join(targetSQLFolderPath, "ImportData.cmd"), "\n".join(populateMiscDataImportDataCMDLines))

# data object
createDir(targetDOPath)
for table in tables:
    createFile(os.path.join(targetDOPath, "%s.cs" % table["dataObject"]["dataObjectName"]), templateDataObjectWhole.substitute(table["dataObject"]))

# MonitoringDB.wxs
partitionContents, duplicatedFileContents, importDataContents=[], [], []
for i in range(0, partitionCount):
    parameters={}
    parameters["partitionID"]=i
    partitionContents.append(templateInstallerMonitoringDBPartition.substitute(parameters))
    duplicatedFileContents.append(templateInstallerMonitoringDBCADuplicateFile.substitute(parameters))
parameters={}
parameters["contents"]="\n".join(partitionContents)
createFile(os.path.join(targetMonitoringDBWxi, "MonitoringDBPartitions.wxi"), templateInstallerMonitoringDBGeneric.substitute(parameters))
parameters["contents"]="\n".join(duplicatedFileContents)
createFile(os.path.join(targetMonitoringDBWxi, "MonitoringDBCADuplicateFiles.wxi"), templateInstallerMonitoringDBGeneric.substitute(parameters))
for populateMiscDataFileName in populateMiscDataFileNameList:
    parameters={}
    parameters["populateMiscDataFileName"]=populateMiscDataFileName
    importDataContents.append(templateInstallerMonitoringDBImportDataFile.substitute(parameters))
parameters["contents"]="\n".join(importDataContents)
createFile(os.path.join(targetMonitoringDBWxi, "MonitoringDBImportDataFiles.wxi"), templateInstallerMonitoringDBGeneric.substitute(parameters))

# attach.db.template.sql
partitionContents=[]
for i in range(0, partitionCount):
    partitionContents.append("    (FILENAME = N'$ndfPath$$dbFilePrefix$Partition%d.ndf')" % i)
parameters={}
parameters["partitionContents"]=",\n".join(partitionContents)
createFile(os.path.join(targetMonitoringDBWxi, "attach.db.template.sql"), templateInstallerMonitoringDBAttachDBTemplate.substitute(parameters))

# MonitoringWeb.wxs
guidStore=[
    "E36EF155-BE8B-4132-BEEB-3678DFDA4D9D",
    "82282319-C4A1-488e-80EE-7CA11705C74F",
    "6DC099D7-4CA8-461f-81DA-B6D1625BEAA7",
    "CBF4F2C8-88B9-414c-8BCB-FF666E26B82D",
    "315D26C6-BCF3-46f3-8842-0DDE36176F79",
    "3018FA66-4519-4faa-8831-90D1D3074D8C",
    "CF11B4AD-AC62-40b6-A0EB-4AEE725F0827",
    "CAE0822B-7439-42cb-9C25-37C31AB3FCE2",
    "EDE95FE8-F777-4db2-A3B4-5C7BE4886B55",
    "AA823850-ECF8-4939-9051-6827367723F0",
    "8A1C5B2F-317E-4a6f-A52B-38D3C4174111",
    "F71C618B-2EE4-4e41-BE9A-A58B36C11662",
    "4A26F139-727B-4ef0-8787-818C1DC2AC13",
    "DCAB594F-B20C-4d56-A209-47D2565B55C3",
    "54B1DF7C-FF76-4568-84EC-A7CD18411A5C",
    ]
wxiDirFileXML, featureComponentRefXML=getWXIDirFileXML(sourceMonitoringWebCSProjPath, "MonitoringWeb", guidStore)
parameters={}
parameters["contents"]=wxiDirFileXML
createFile(os.path.join(targetMonitoringWebWxi, "MonitoringWebASPNETFiles.wxi"), templateInstallerMonitoringDBGeneric.substitute(parameters))
parameters["contents"]=featureComponentRefXML
createFile(os.path.join(targetMonitoringWebWxi, "MonitoringWebFeatureComponentRefs.wxi"), templateInstallerMonitoringDBGeneric.substitute(parameters))

