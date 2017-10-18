tableConfigReportPartitions={
    "tableName": "config_report_partitions",
    "columns": (
        ("i_sequence_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_partition_id", "int", "NOT NULL"),
        ("i_partition_type", "tinyint", "NOT NULL"),
        ("i_report_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "partition_id_partition_type", "unique": True, "columns": ("i_partition_id", "i_partition_type", ) },
        { "indexName": "partition_type_report_count", "unique": False, "columns": ("i_partition_type", "i_report_count", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, 2, ),
    "initialData": [],
    }
tables.append(tableConfigReportPartitions)

for i in range(0, tableReportValueHourly["tablePartitionCount"]):
    tableConfigReportPartitions["initialData"].append(
        { "dataLine": ("%s" % i, "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") })
for i in range(0, tableReportValueDaily["tablePartitionCount"]):
    tableConfigReportPartitions["initialData"].append(
        { "dataLine": ("%s" % i, "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") })

tableConfigReportPartitions["sps"]=(
    {
        "spName": "GetReportPartitionCountByPartitionType",
        "description": "Get report partition count by partition type",
        "inputParameters": """@i_partition_type           int""",
        "sqlQuery":
"""SELECT
        COUNT(1) AS 'rowcount'
    FROM config_report_partitions WITH (FORCESEEK)
    WHERE i_partition_type      = @i_partition_type
    
    CHKERR({ERROR_GET_REPORT_PARTITION_COUNT_BY_PARTITION_TYPE})
    RETURN 0""",
    },
    {
        "spName": "GetReportCountByPartitionIDAndPartitionType",
        "description": "Get report count by partition ID and partition type",
        "inputParameters": 
"""@i_partition_id             int,
    @i_partition_type           int""",
        "sqlQuery":
"""SELECT
        i_report_count AS 'rowcount'
    FROM config_report_partitions WITH (FORCESEEK)
    WHERE i_partition_id        = @i_partition_id
      AND i_partition_type      = @i_partition_type
    
    CHKERR({ERROR_GET_REPORT_COUNT_BY_PARTITION_ID_AND_PARTITION_TYPE})
    RETURN 0""",
    },
    {
        "spName": "GetTotalReportCountByPartitionType",
        "description": "Get total report count by partition type",
        "inputParameters": """@i_partition_type           int""",
        "sqlQuery":
"""SELECT
        SUM(i_report_count) AS 'rowcount'
    FROM config_report_partitions WITH (FORCESEEK)
    WHERE i_partition_type      = @i_partition_type
    
    CHKERR({ERROR_GET_TOTAL_REPORT_COUNT_BY_PARTITION_TYPE})
    RETURN 0""",
    },
    )

tableConfigReportPartitions["fns"]=(
    {
        "fnName": "GetFileGroupCount",
        "fnType": "ScalarFunction",
        "inputParameters": """""",
        "returnType": "int",
        "sqlQuery": """RETURN %d""" % partitionCount,
    },
    {
        "fnName": "GetFileGroupName",
        "fnType": "ScalarFunction",
        "inputParameters": """@i_id int""",
        "returnType": "varchar(200)",
        "sqlQuery": """RETURN 'MonitoringPartition' + CAST((@i_id %% %d) AS varchar)""" % partitionCount,
    },
    )
