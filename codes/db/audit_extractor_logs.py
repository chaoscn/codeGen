tableAuditExtractorLogs={
    "tableName": "audit_extractor_logs",
    "columns": (
        ("bi_extractor_log_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_server_id", "int", "NOT NULL"),
        ("i_extractor_type_id", "int", "NOT NULL"),
        ("i_extractor_action_id", "int", "NOT NULL"),
        ("t_extractor_message", "text"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "server_id_extractor_type_id_inserted_datetime", "unique": False, "columns": ("i_server_id", "i_extractor_type_id", "dt_inserted_datetime", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    }
tables.append(tableAuditExtractorLogs)

tableAuditExtractorLogs["sps"]=(
    {
        "spName": "GetExtractorLogsByInsertedDateTime",
        "description": "Get extractor logs by inserted datetime",
        "inputParameters":
"""@dt_inserted_datetime_from  datetime,
    @dt_inserted_datetime_to    datetime""",
        "sqlQuery":
"""SELECT
        bi_extractor_log_id     AS 'extractorLogID',
        i_server_id             AS 'serverID',
        i_extractor_type_id     AS 'extractorTypeID',
        i_extractor_action_id   AS 'extractorActionID',
        t_extractor_message     AS 'extractorMessage',
        dt_inserted_datetime    AS 'insertedDatetime'
    FROM audit_extractor_logs WITH (FORCESEEK)
    WHERE dt_inserted_datetime  >= @dt_inserted_datetime_from
      AND dt_inserted_datetime  < @dt_inserted_datetime_to
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_EXTRACTOR_LOGS_BY_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetExtractorLogsByServerIDAndInsertedDateTime",
        "description": "Get extractor logs by server ID and inserted datetime",
        "inputParameters":
"""@i_server_id                int,
    @dt_inserted_datetime_from  datetime,
    @dt_inserted_datetime_to    datetime""",
        "sqlQuery":
"""SELECT
        bi_extractor_log_id     AS 'extractorLogID',
        i_server_id             AS 'serverID',
        i_extractor_type_id     AS 'extractorTypeID',
        i_extractor_action_id   AS 'extractorActionID',
        t_extractor_message     AS 'extractorMessage',
        dt_inserted_datetime    AS 'insertedDatetime'
    FROM audit_extractor_logs WITH (FORCESEEK)
    WHERE i_server_id           = @i_server_id
      AND dt_inserted_datetime  >= @dt_inserted_datetime_from
      AND dt_inserted_datetime  < @dt_inserted_datetime_to
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_EXTRACTOR_LOGS_BY_SERVER_ID_AND_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetExtractorLogsByServerIDAndTypeIDAndInsertedDateTime",
        "description": "Get extractor logs by server ID and type ID and inserted datetime",
        "inputParameters":
"""@i_server_id                int,
    @i_extractor_type_id        int,
    @dt_inserted_datetime_from  datetime,
    @dt_inserted_datetime_to    datetime""",
        "sqlQuery":
"""SELECT
        bi_extractor_log_id     AS 'extractorLogID',
        i_server_id             AS 'serverID',
        i_extractor_type_id     AS 'extractorTypeID',
        i_extractor_action_id   AS 'extractorActionID',
        t_extractor_message     AS 'extractorMessage',
        dt_inserted_datetime    AS 'insertedDatetime'
    FROM audit_extractor_logs WITH (FORCESEEK)
    WHERE i_server_id           = @i_server_id
      AND i_extractor_type_id   = @i_extractor_type_id
      AND dt_inserted_datetime  >= @dt_inserted_datetime_from
      AND dt_inserted_datetime  < @dt_inserted_datetime_to
    ORDER BY dt_inserted_datetime DESC
    
    CHKERR({ERROR_GET_EXTRACTOR_LOGS_BY_SERVER_ID_AND_TYPE_ID_AND_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetPagedExtractorLogsOrderByInsertedDateTimeDesc",
        "description": "Get paged extractor logs order by inserted datetime desc",
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
            A.bi_extractor_log_id     AS 'extractorLogID',
            A.i_server_id             AS 'serverID',
            A.i_extractor_type_id     AS 'extractorTypeID',
            A.i_extractor_action_id   AS 'extractorActionID',
            A.t_extractor_message     AS 'extractorMessage',
            A.dt_inserted_datetime    AS 'insertedDatetime',
            ROW_NUMBER() OVER (ORDER BY A.dt_inserted_datetime DESC) AS 'rowNumber'
        FROM audit_extractor_logs A
        ORDER BY A.dt_inserted_datetime DESC
    ) C
    WHERE C.rowNumber > @i_max_rowcount - @i_page_size AND C.rowNumber <= @i_max_rowcount
    ORDER BY C.rowNumber

    CHKERR({ERROR_GET_PAGED_EXTRACTOR_LOGS_ORDER_BY_INSERTED_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "InsertExtractorLog",
        "description": "Insert extractor log",
        "inputParameters":
"""@i_server_id               int,
    @i_extractor_type_id       int,
    @i_extractor_action_id     int,
    @t_extractor_message       text,
    @dt_inserted_datetime      datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@t_extractor_message)

    TRANINIT
    
    IF (@dt_inserted_datetime IS NULL)
        SET @dt_inserted_datetime = GETUTCDATE()

    INSERT INTO audit_extractor_logs
    (
        i_server_id,
        i_extractor_type_id,
        i_extractor_action_id,
        t_extractor_message,
        dt_inserted_datetime
    )
    VALUES
    (
        @i_server_id,
        @i_extractor_type_id,
        @i_extractor_action_id,
        @t_extractor_message,
        @dt_inserted_datetime
    )
    
    SELECT @@IDENTITY AS 'identity'

    TRANCHKERR({ERROR_INSERT_EXTRACTOR_LOG})
    TRANRETURN""",
    },
    {
        "spName": "DeleteExtractorLogsByDateTimeAndMaxCount",
        "description": "Delete extractor logs by datetime and max count",
        "inputParameters":
"""@dt_inserted_datetime_to      datetime,
    @i_max_count               int""",
        "sqlQuery":
"""CHECK_NOTNULL(@dt_inserted_datetime_to)

    TRANINIT

    DELETE TOP (@i_max_count) FROM audit_extractor_logs
    WHERE dt_inserted_datetime < @dt_inserted_datetime_to

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_EXTRACTOR_LOGS_BY_DATETIME_AND_MAX_COUNT})
    TRANRETURN""",
    },
    )