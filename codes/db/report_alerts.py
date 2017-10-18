tableReportAlerts={
    "tableName": "report_alerts",
    "columns": (
        ("bi_report_alert_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "NOT NULL"),
        ("x_report_alert_email_xml", "xml", "NOT NULL"),
        ("b_report_alert_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id_datetime", "unique": False, "columns": ("i_report_id", "dt_inserted_datetime", "dt_updated_datetime", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_report_id", "foreignTableName": "config_reports", "foreignColumnName": "i_report_id", },
        ),
    "xmlIgnores": (
        "x_report_alert_email_xml",
        ),
    }
tables.append(tableReportAlerts)

tableReportAlerts["sps"]=(
    {
        "spName": "CountReportAlertsByReportIDAndDateTime",
        "description": "Count report alerts by report ID and datetime",
        "inputParameters":
"""@i_report_id               int,
    @dt_inserted_datetime_from datetime,
    @dt_inserted_datetime_to   datetime""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount'
    FROM report_alerts WITH (FORCESEEK)
    WHERE i_report_id          = @i_report_id
      AND dt_inserted_datetime >= @dt_inserted_datetime_from
      AND dt_inserted_datetime < @dt_inserted_datetime_to

    CHKERR({ERROR_COUNT_REPORT_ALERTS_BY_REPORT_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetPagedReportAlertsByReportIDAndDateTimeOrderByDateTimeDesc",
        "description": "Get paged report alerts by report ID and datetime order by datetime desc",
        "inputParameters":
"""@i_report_id               int,
    @dt_inserted_datetime_from datetime,
    @dt_inserted_datetime_to   datetime,
    @i_page_number             int,
    @i_page_size               int""",
        "sqlQuery":
"""IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT *
    FROM
    (
        SELECT TOP (@i_page_size)
            bi_report_alert_id          AS 'reportAlertID',
            i_report_id                 AS 'reportID',
            x_report_alert_email_xml    AS 'reportAlertEmailXml',
            b_report_alert_enabled      AS 'reportAlertEnabled',
            dt_inserted_datetime        AS 'insertedDateTime',
            dt_updated_datetime         AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM report_alerts WITH (FORCESEEK)
        WHERE i_report_id               = @i_report_id
          AND dt_inserted_datetime      >= @dt_inserted_datetime_from
          AND dt_inserted_datetime      < @dt_inserted_datetime_to
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber
    
    CHKERR({ERROR_GET_PAGED_REPORT_ALERTS_BY_REPORT_ID_AND_DATETIME_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "CountReportAlertsByDateTime",
        "description": "Count report alerts by datetime",
        "inputParameters":
"""@dt_inserted_datetime_from datetime,
    @dt_inserted_datetime_to   datetime""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount'
    FROM report_alerts
    WHERE dt_inserted_datetime >= @dt_inserted_datetime_from
      AND dt_inserted_datetime < @dt_inserted_datetime_to

    CHKERR({ERROR_COUNT_REPORT_ALERTS_BY_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetPagedReportAlertsByDateTimeOrderByDateTimeDesc",
        "description": "Get paged report alerts by datetime order by datetime desc",
        "inputParameters":
"""@dt_inserted_datetime_from datetime,
    @dt_inserted_datetime_to   datetime,
    @i_page_number             int,
    @i_page_size               int""",
        "sqlQuery":
"""IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT *
    FROM
    (
        SELECT TOP (@i_page_size)
            bi_report_alert_id          AS 'reportAlertID',
            i_report_id                 AS 'reportID',
            x_report_alert_email_xml    AS 'reportAlertEmailXml',
            b_report_alert_enabled      AS 'reportAlertEnabled',
            dt_inserted_datetime        AS 'insertedDateTime',
            dt_updated_datetime         AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM report_alerts WITH (FORCESEEK)
        WHERE dt_inserted_datetime      >= @dt_inserted_datetime_from
          AND dt_inserted_datetime      < @dt_inserted_datetime_to
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber
    
    CHKERR({ERROR_GET_PAGED_REPORT_ALERTS_BY_DATETIME_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "InsertReportAlert",
        "description": "Get insert report alert",
        "inputParameters":
"""@i_report_id                     int,
    @x_report_alert_email_xml        xml,
    @b_report_alert_enabled          bit,
    @dt_inserted_datetime            datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_report_alert_email_xml)

    TRANINIT

    INSERT INTO report_alerts
    (
        i_report_id,
        x_report_alert_email_xml,
        b_report_alert_enabled,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @i_report_id,
        @x_report_alert_email_xml,
        @b_report_alert_enabled,
        @dt_inserted_datetime,
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_GET_INSERT_REPORT_ALERT})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportAlertsByDateTimeAndMaxCount",
        "description": "Delete report alerts by datetime and max count",
        "inputParameters":
"""@dt_inserted_datetime_to datetime,
    @i_max_count             int""",
        "sqlQuery":
"""CHECK_NOTNULL(@dt_inserted_datetime_to)

    TRANINIT

    DELETE TOP (@i_max_count) FROM report_alerts
    WHERE dt_inserted_datetime < @dt_inserted_datetime_to

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_REPORT_ALERTS_BY_DATETIME_AND_MAX_COUNT})
    TRANRETURN""",
    },
    {
        "spName": "EnableReportAlertByID",
        "description": "Enable report alert by ID",
        "inputParameters":
"""@bi_report_alert_id     bigint,
    @b_report_alert_enabled bit""",
        "sqlQuery":
"""TRANINIT

    UPDATE report_alerts
    SET b_report_alert_enabled = @b_report_alert_enabled
    WHERE bi_report_alert_id   = @bi_report_alert_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_ENABLE_REPORT_ALERT_BY_ID})
    TRANRETURN""",
    },
    {
        "spName": "EnableReportAlertsByReportID",
        "description": "Enable report alerts by report ID",
        "inputParameters":
"""@i_report_id            int,
    @b_report_alert_enabled bit""",
        "sqlQuery":
"""TRANINIT

    UPDATE report_alerts
    SET b_report_alert_enabled = @b_report_alert_enabled
    WHERE i_report_id          = @i_report_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_ENABLE_REPORT_ALERTS_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "EnableReportAlertsByReportIDAndDateTime",
        "description": "Enable report alerts by report ID and datetime",
        "inputParameters":
"""@i_report_id               int,
    @dt_inserted_datetime_from datetime,
    @dt_inserted_datetime_to   datetime,
    @b_report_alert_enabled    bit""",
        "sqlQuery":
"""TRANINIT

    UPDATE report_alerts
    SET b_report_alert_enabled = @b_report_alert_enabled
    WHERE i_report_id          = @i_report_id
      AND dt_inserted_datetime >= @dt_inserted_datetime_from
      AND dt_inserted_datetime < @dt_inserted_datetime_to

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_ENABLE_REPORT_ALERTS_BY_REPORT_ID_AND_DATETIME})
    TRANRETURN""",
    },
    )