tableReportAPIPartnerValueDaily={
    "tableName": "report_api_partner_value_daily",
    "tablePartitionCount": 256,
    "columns": (
        ("bi_sequence_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "not null"),
        ("i_server_id", "int", "not null"),
        ("i_partner_id", "int", "not null"),
        ("f_report_value", "float", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id_server_id_partner_id_inserted_datetime", "unique": True, "columns": ("i_report_id", "i_server_id", "i_partner_id", "dt_inserted_datetime", ) },
        ),
    }
tables.append(tableReportAPIPartnerValueDaily)

tableReportAPIPartnerValueDaily["views"]=[]
for i in range(0, int(math.ceil(1.0*tableReportAPIPartnerValueDaily["tablePartitionCount"]/maxTableCountInView))):
    startIndex, endIndex=i*maxTableCountInView, min(tableReportAPIPartnerValueDaily["tablePartitionCount"], (i+1)*maxTableCountInView)
    tableReportAPIPartnerValueDaily["views"].append(
        {
            "viewName": "%s_%d_%d" % (tableReportAPIPartnerValueDaily["tableName"], startIndex, endIndex-1),
            "sqlQuery": "\n    UNION ALL\n    ".join(map(lambda x: "SELECT * FROM %s_%d" % (tableReportAPIPartnerValueDaily["tableName"], x), range(startIndex, endIndex)))
        },
        )

tableReportAPIPartnerValueDaily["sps"]=(
    {
        "spName": "GetReportAPIPartnerValueDailiesByReportIDAndDateTime",
        "description": "Get report API partner value dailies by report ID and datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        SELECT
            bi_sequence_id            AS ''sequenceID'',
            i_report_id               AS ''reportID'',
            i_server_id               AS ''serverID'',
            i_partner_id              AS ''partnerID'',
            f_report_value            AS ''reportValue'',
            b_failed                  AS ''failed'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id          = @i_report_id
          AND dt_inserted_datetime >= @dt_inserted_datetime_from
          AND dt_inserted_datetime < @dt_inserted_datetime_to'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id                = @i_report_id,
        @dt_inserted_datetime_from  = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to    = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_API_PARTNER_VALUE_DAILIES_BY_REPORT_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportAPIPartnerValueDailiesByReportIDAndServerIDsAndDateTime",
        "description": "Get report API partner value dailies by report ID and server IDs and datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @vc_server_ids               varchar(8000),
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_ids)
    SET @vc_server_ids = dbo.fnm_GetFilteredString{}VERSION_SUFFIX (@vc_server_ids)

    DECLARE @nvc_sql_query       nvarchar(max)

    SET @nvc_sql_query = '
        SELECT
            bi_sequence_id            AS ''sequenceID'',
            i_report_id               AS ''reportID'',
            i_server_id               AS ''serverID'',
            i_partner_id              AS ''partnerID'',
            f_report_value            AS ''reportValue'',
            b_failed                  AS ''failed'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id          = @i_report_id
          AND i_server_id IN (' + @vc_server_ids + ')
          AND dt_inserted_datetime >= @dt_inserted_datetime_from
          AND dt_inserted_datetime < @dt_inserted_datetime_to'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id                = @i_report_id,
        @dt_inserted_datetime_from  = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to    = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_API_PARTNER_VALUE_DAILIES_BY_REPORT_ID_AND_SERVER_IDS_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "DeleteReportAPIPartnerValueDailiesByReportID",
        "description": "Delete report API partner value dailies by report ID",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)
    
    SET @nvc_sql_query = '
        DELETE FROM report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
        WHERE i_report_id = @i_report_id
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@i_report_id int',
        @i_report_id = @i_report_id

    TRANCHKERR({ERROR_DELETE_REPORT_API_PARTNER_VALUE_DAILIES_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportAPIPartnerValueDailiesByDateTime",
        "description": "Delete report API partner value dailies by datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)
    
    SET @nvc_sql_query = '
        DELETE FROM report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
        WHERE dt_inserted_datetime < @dt_inserted_datetime_to
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@dt_inserted_datetime_to datetime',
        @dt_inserted_datetime_to = @dt_inserted_datetime_to

    TRANCHKERR({ERROR_DELETE_REPORT_API_PARTNER_VALUE_DAILIES_BY_DATETIME})
    TRANRETURN""",
    },
    {
        "spName": "InsertOrUpdateReportAPIPartnerValueDaily",
        "description": "Insert or update report API partner value daily",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @i_server_id                 int,
    @i_partner_id                int,
    @f_report_value              float,
    @b_failed                    bit,
    @dt_inserted_datetime        datetime""",
        "sqlQuery":
"""TRANINIT
    
    DECLARE @nvc_sql_query       nvarchar(max)
    
    SET @nvc_sql_query = '
        DECLARE @bi_sequence_id int
        SET @bi_sequence_id = 0
        SELECT @bi_sequence_id = bi_sequence_id
        FROM report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id           = @i_report_id
          AND i_server_id           = @i_server_id
          AND i_partner_id          = @i_partner_id
          AND dt_inserted_datetime  = @dt_inserted_datetime
        IF (@bi_sequence_id = 0)
        BEGIN
            INSERT INTO report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
            (
                i_report_id,
                i_server_id,
                i_partner_id,
                f_report_value,
                b_failed,
                dt_inserted_datetime
            )
            VALUES
            (
                @i_report_id,
                @i_server_id,
                @i_partner_id,
                @f_report_value,
                @b_failed,
                @dt_inserted_datetime
            )
            SELECT @@IDENTITY AS ''identity''
        END
        ELSE
        BEGIN
            UPDATE report_api_partner_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
            SET
                f_report_value          = @f_report_value,
                b_failed                = @b_failed,
                dt_inserted_datetime    = @dt_inserted_datetime
            WHERE bi_sequence_id = @bi_sequence_id
            SELECT @bi_sequence_id AS ''identity''
        END'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @i_server_id                 int,
            @i_partner_id                int,
            @f_report_value              float,
            @b_failed                    bit,
            @dt_inserted_datetime        datetime',
        @i_report_id            = @i_report_id,
        @i_server_id            = @i_server_id,
        @i_partner_id           = @i_partner_id,
        @f_report_value         = @f_report_value,
        @b_failed               = @b_failed,
        @dt_inserted_datetime   = @dt_inserted_datetime

    TRANCHKERR({ERROR_INSERT_OR_UPDATE_REPORT_API_PARTNER_VALUE_DAILY})
    TRANRETURN""",
    },
    )