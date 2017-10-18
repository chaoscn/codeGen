tableReportAlertQueue={
    "tableName": "report_alert_tasks",
    "columns": (
        ("bi_report_alert_task_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "NOT NULL"),
        ("x_report_alert_email_xml", "xml", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id", "unique": False, "columns": ("i_report_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_report_id", "foreignTableName": "config_reports", "foreignColumnName": "i_report_id", },
        ),
    "xmlIgnores": (
        "x_report_alert_email_xml",
        ),
    }
tables.append(tableReportAlertQueue)

tableReportAlertQueue["sps"]=(
    {
        "spName": "GetReportAlertTaskByReportAlertTaskID",
        "description": "Get report alert task by report alert task ID",
        "inputParameters":
"""@bi_report_alert_task_id     bigint""",
        "sqlQuery":
"""SELECT TOP 1000
        bi_report_alert_task_id     AS 'reportAlertTaskID',
        i_report_id                 AS 'reportID',
        x_report_alert_email_xml    AS 'reportAlertEmailXml',
        dt_inserted_datetime        AS 'insertedDateTime'
    FROM report_alert_tasks
    WHERE bi_report_alert_task_id   = @bi_report_alert_task_id
    
    CHKERR({ERROR_GET_REPORT_ALERT_TASK_BY_REPORT_ALERT_TASK_ID})
    RETURN 0""",
    },
    {
        "spName": "GetLatestReportAlertTasks",
        "description": "Get latest report alert tasks",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT TOP 1000
        bi_report_alert_task_id     AS 'reportAlertTaskID',
        i_report_id                 AS 'reportID',
        x_report_alert_email_xml    AS 'reportAlertEmailXml',
        dt_inserted_datetime        AS 'insertedDateTime'
    FROM report_alert_tasks
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_LATEST_REPORT_ALERT_TASKS})
    RETURN 0""",
    },
    {
        "spName": "InsertReportAlertTask",
        "description": "Get insert report alert task",
        "inputParameters":
"""@i_report_id                     int,
    @x_report_alert_email_xml        xml,
    @dt_inserted_datetime            datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_report_alert_email_xml)

    TRANINIT

    INSERT INTO report_alert_tasks
    (
        i_report_id,
        x_report_alert_email_xml,
        dt_inserted_datetime
    )
    VALUES
    (
        @i_report_id,
        @x_report_alert_email_xml,
        @dt_inserted_datetime
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_GET_INSERT_REPORT_ALERT_TASK})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportAlertTaskByReportAlertTaskID",
        "description": "Delete report alert task by report alert task ID",
        "inputParameters":
"""@bi_report_alert_task_id      bigint""",
        "sqlQuery":
"""TRANINIT

    DELETE FROM report_alert_tasks
    WHERE bi_report_alert_task_id = @bi_report_alert_task_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_REPORT_ALERT_TASK_BY_REPORT_ALERT_TASK_ID})
    TRANRETURN""",
    },
    )