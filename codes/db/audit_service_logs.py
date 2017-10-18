tableAuditServiceLogs={
    "tableName": "audit_service_logs",
    "columns": (
        ("bi_service_log_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_service_type_id", "int", "NOT NULL"),
        ("i_service_action_id", "int", "NOT NULL"),
        ("t_service_message", "text"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "service_type_id", "unique": False, "columns": ("i_service_type_id", "dt_inserted_datetime", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    }
tables.append(tableAuditServiceLogs)

tableAuditServiceLogs["sps"]=(
    {
        "spName": "GetServiceLogsByInsertedDateTime",
        "description": "Get service logs by inserted datetime",
        "inputParameters":
"""@dt_inserted_datetime_from  datetime,
    @dt_inserted_datetime_to    datetime""",
        "sqlQuery":
"""SELECT
        bi_service_log_id     AS 'serviceLogID',
        i_service_type_id     AS 'serviceTypeID',
        i_service_action_id   AS 'serviceActionID',
        t_service_message     AS 'serviceMessage',
        dt_inserted_datetime    AS 'insertedDatetime'
    FROM audit_service_logs WITH (FORCESEEK)
    WHERE dt_inserted_datetime  >= @dt_inserted_datetime_from
      AND dt_inserted_datetime  < @dt_inserted_datetime_to
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_SERVICE_LOGS_BY_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetServiceLogsByTypeIDAndInsertedDateTime",
        "description": "Get service logs by type ID and inserted datetime",
        "inputParameters":
"""@i_service_type_id        int,
    @dt_inserted_datetime_from  datetime,
    @dt_inserted_datetime_to    datetime""",
        "sqlQuery":
"""SELECT
        bi_service_log_id     AS 'serviceLogID',
        i_service_type_id     AS 'serviceTypeID',
        i_service_action_id   AS 'serviceActionID',
        t_service_message     AS 'serviceMessage',
        dt_inserted_datetime    AS 'insertedDatetime'
    FROM audit_service_logs WITH (FORCESEEK)
    WHERE i_service_type_id   = @i_service_type_id
      AND dt_inserted_datetime  >= @dt_inserted_datetime_from
      AND dt_inserted_datetime  < @dt_inserted_datetime_to
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_SERVICE_LOGS_BY_TYPE_ID_AND_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetPagedServiceLogsOrderByInsertedDateTimeDesc",
        "description": "Get paged service logs order by inserted datetime desc",
        "inputParameters":
"""@i_page_number         int,
    @i_page_size           int""",
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
        SELECT TOP (@i_max_rowcount)
            A.bi_service_log_id     AS 'serviceLogID',
            A.i_service_type_id     AS 'serviceTypeID',
            A.i_service_action_id   AS 'serviceActionID',
            A.t_service_message     AS 'serviceMessage',
            A.dt_inserted_datetime  AS 'insertedDatetime',
            ROW_NUMBER() OVER (ORDER BY A.dt_inserted_datetime DESC) AS 'rowNumber'
        FROM audit_service_logs A
        ORDER BY A.dt_inserted_datetime DESC
    ) C
    WHERE C.rowNumber > @i_max_rowcount - @i_page_size AND C.rowNumber <= @i_max_rowcount
    ORDER BY C.rowNumber

    CHKERR({ERROR_GET_PAGED_SERVICE_LOGS_ORDER_BY_INSERTED_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "InsertServiceLog",
        "description": "Insert service log",
        "inputParameters":
"""@i_service_type_id       int,
    @i_service_action_id     int,
    @t_service_message       text,
    @dt_inserted_datetime      datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@t_service_message)

    TRANINIT
    
    IF (@dt_inserted_datetime IS NULL)
        SET @dt_inserted_datetime = GETUTCDATE()

    INSERT INTO audit_service_logs
    (
        i_service_type_id,
        i_service_action_id,
        t_service_message,
        dt_inserted_datetime
    )
    VALUES
    (
        @i_service_type_id,
        @i_service_action_id,
        @t_service_message,
        @dt_inserted_datetime
    )
    
    SELECT @@IDENTITY AS 'identity'

    TRANCHKERR({ERROR_INSERT_SERVICE_LOG})
    TRANRETURN""",
    },
    {
        "spName": "DeleteServiceLogsByDateTimeAndMaxCount",
        "description": "Delete service logs by datetime and max count",
        "inputParameters":
"""@dt_inserted_datetime_to      datetime,
    @i_max_count               int""",
        "sqlQuery":
"""CHECK_NOTNULL(@dt_inserted_datetime_to)

    TRANINIT

    DELETE TOP (@i_max_count) FROM audit_service_logs
    WHERE dt_inserted_datetime < @dt_inserted_datetime_to

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_SERVICE_LOGS_BY_DATETIME_AND_MAX_COUNT})
    TRANRETURN""",
    },
    )