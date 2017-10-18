tableConfigReportSources={
    "tableName": "config_report_sources",
    "columns": (
        ("i_report_source_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "NOT NULL"),
        ("i_property_id", "int", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id", "unique": False, "columns": ("i_report_id", ) },
        { "indexName": "report_id_property_id", "unique": True, "columns": ("i_report_id", "i_property_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_report_id", "foreignTableName": "config_reports", "foreignColumnName": "i_report_id", },
        { "columnName": "i_property_id", "foreignTableName": "config_properties", "foreignColumnName": "i_property_id", },
        ),
    }
tables.append(tableConfigReportSources)

tableConfigReportSources["sps"]=(
    {
        "spName": "GetReportSourcesByReportID",
        "description": "Get report sources by report ID",
        "inputParameters": """@i_report_id          int""",
        "sqlQuery":
"""SELECT
        i_report_source_id     AS 'reportSourceID',
        i_report_id            AS 'reportID',
        i_property_id          AS 'propertyID',
        dt_inserted_datetime   AS 'insertedDateTime'
    FROM config_report_sources WITH (FORCESEEK)
    WHERE i_report_id = @i_report_id
    
    CHKERR({ERROR_GET_REPORT_SOURCES_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "CountReportSourcesByReportID",
        "description": "Count report sources by report ID",
        "inputParameters": """@i_report_id          int""",
        "sqlQuery":
"""SELECT
        count(1)               AS 'rowcount'
    FROM config_report_sources WITH (FORCESEEK)
    WHERE i_report_id = @i_report_id
    
    CHKERR({ERROR_COUNT_REPORT_SOURCES_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertReportSource",
        "description": "Insert report source",
        "inputParameters":
"""@i_report_id          int,
    @i_property_id        int""",
        "sqlQuery":
"""TRANINIT

    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_report_sources WITH (FORCESEEK)
        WHERE i_report_id   = @i_report_id
          AND i_property_id = @i_property_id
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        INSERT INTO config_report_sources
        (
            i_report_id,
            i_property_id,
            dt_inserted_datetime
        )
        VALUES
        (
            @i_report_id,
            @i_property_id,
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END
    
    TRANCHKERR({ERROR_INSERT_REPORT_SOURCE})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportSourceByReportSourceID",
        "description": "Delete report source by report sourceID",
        "inputParameters": """@i_report_source_id          int""",
        "sqlQuery":
"""TRANINIT

    DELETE FROM config_report_sources
    WHERE i_report_source_id = @i_report_source_id

    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({DELETE_REPORT_SOURCE_BY_REPORT_SOURCEID})
    TRANRETURN""",
    },
    )