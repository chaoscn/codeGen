tableConfigRecommendedReports={
    "tableName": "config_recommended_reports",
    "columns": (
        ("i_recommended_report_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id", "unique": False, "columns": ("i_report_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_report_id", "foreignTableName": "config_reports", "foreignColumnName": "i_report_id", },
        ),
    }
tables.append(tableConfigRecommendedReports)

tableConfigRecommendedReports["sps"]=(
    {
        "spName": "InsertRecommendedReport",
        "description": "Insert recommended report",
        "inputParameters":
"""@i_report_id int""",
        "sqlQuery":
"""TRANINIT
    
    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_recommended_reports
        WHERE i_report_id = @i_report_id
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        INSERT INTO config_recommended_reports
        (
            i_report_id,
            vc_updated_by,
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @i_report_id,
            SYSTEM_USER,
            GETUTCDATE(),
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END
    
    TRANCHKERR({ERROR_INSERT_RECOMMENDED_REPORT})
    TRANRETURN""",
    },
    {
        "spName": "UpdateRecommendedReportByRecommendedReportID",
        "description": "Update recommended report by recommended report ID",
        "inputParameters": 
"""@i_recommended_report_id            int,
    @i_report_id                      int""",
        "sqlQuery":
"""TRANINIT

    UPDATE config_recommended_reports
    SET
        i_report_id               = @i_report_id,
        vc_updated_by             = SYSTEM_USER,
        dt_updated_datetime       = GETUTCDATE()
    WHERE i_recommended_report_id = @i_recommended_report_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_RECOMMENDED_REPORT_BY_RECOMMENDED_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteRecommendedReportByReportID",
        "description": "Delete recommended report by report ID",
        "inputParameters": 
"""@i_report_id int""",
        "sqlQuery":
"""TRANINIT

    DELETE FROM config_recommended_reports
    WHERE i_report_id = @i_report_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_RECOMMENDED_REPORT_BY_REPORT_ID})
    TRANRETURN""",
    },
    )