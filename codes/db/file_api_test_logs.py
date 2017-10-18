tableFileAPITestLogs={
    "tableName": "file_api_test_logs",
    "columns": (
        ("i_file_api_test_log_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_api_test_id", "int", "NOT NULL"),
        ("nt_file_content", "ntext", "NOT NULL"),
        ("bi_file_size", "bigint", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "api_test_id_inserted_datetime", "unique": True, "columns": ("i_api_test_id", "dt_inserted_datetime", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_api_test_id", "foreignTableName": "config_api_tests", "foreignColumnName": "i_api_test_id", },
        ),
    }
tables.append(tableFileAPITestLogs)

tableFileAPITestLogs["sps"]=(
    {
        "spName": "GetFileAPITestLogByFileAPITestLogID",
        "description": "Get file API test log by file API test log ID",
        "inputParameters":
"""@i_file_api_test_log_id  int""",
        "sqlQuery":
"""SELECT
        i_file_api_test_log_id      AS 'fileAPITestLogID',
        i_api_test_id               AS 'apiTestID',
        nt_file_content             AS 'fileContent',
        bi_file_size                AS 'fileSize',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM file_api_test_logs
    WHERE i_file_api_test_log_id    = @i_file_api_test_log_id

    CHKERR({ERROR_GET_FILE_API_TEST_LOG_BY_FILE_API_TEST_LOG_ID})
    RETURN 0""",
    },
    {
        "spName": "GetFileAPITestLogByAPITestIDAndInsertedDateTime",
        "description": "Get file API test log by API test ID and inserted datetime",
        "inputParameters":
"""@i_api_test_id              int,
    @dt_inserted_datetime       datetime""",
        "sqlQuery":
"""SELECT
        i_file_api_test_log_id      AS 'fileAPITestLogID',
        i_api_test_id               AS 'apiTestID',
        nt_file_content             AS 'fileContent',
        bi_file_size                AS 'fileSize',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM file_api_test_logs WITH (FORCESEEK)
    WHERE i_api_test_id        = @i_api_test_id
      AND dt_inserted_datetime = @dt_inserted_datetime

    CHKERR({ERROR_GET_FILE_API_TEST_LOG_BY_API_TEST_ID_AND_INSERTED_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetFileAPITestLogsByAPITestID",
        "description": "Get file API test logs by API test ID",
        "inputParameters":
"""@i_api_test_id              int""",
        "sqlQuery":
"""SELECT
        i_file_api_test_log_id      AS 'fileAPITestLogID',
        i_api_test_id               AS 'apiTestID',
        bi_file_size                AS 'fileSize',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM file_api_test_logs WITH (FORCESEEK)
    WHERE i_api_test_id        = @i_api_test_id
    ORDER BY dt_inserted_datetime

    CHKERR({ERROR_GET_FILE_API_TEST_LOGS_BY_API_TEST_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertFileAPITestLog",
        "description": "Insert file API test log",
        "inputParameters":
"""@i_api_test_id          int,
    @nt_file_content        ntext,
    @bi_file_size           bigint,
    @dt_inserted_datetime   datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@nt_file_content)
    CHECK_NOTNULL(@dt_inserted_datetime)

    TRANINIT

    INSERT INTO file_api_test_logs
    (
        i_api_test_id,
        nt_file_content,
        bi_file_size,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @i_api_test_id,
        @nt_file_content,
        @bi_file_size,
        SYSTEM_USER,
        @dt_inserted_datetime,
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_INSERT_FILE_API_TEST_LOG})
    TRANRETURN""",
    },
    {
        "spName": "UpdateFileAPITestLog",
        "description": "Update file API test log",
        "inputParameters":
"""@i_file_api_test_log_id int,
    @nt_file_content        ntext,
    @bi_file_size           bigint""",
        "sqlQuery":
"""CHECK_NOTNULL(@nt_file_content)

    TRANINIT

    UPDATE file_api_test_logs
    SET
        nt_file_content             = @nt_file_content,
        bi_file_size                = @bi_file_size,
        vc_updated_by               = SYSTEM_USER,
        dt_updated_datetime         = GETUTCDATE()
    WHERE i_file_api_test_log_id    = @i_file_api_test_log_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_FILE_API_TEST_LOG})
    TRANRETURN""",
    },
    )