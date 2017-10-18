tableReportValueDaily={
    "tableName": "report_value_daily",
    "tablePartitionCount": 256,
    "columns": (
        ("bi_sequence_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "not null"),
        ("i_server_id", "int", "not null"),
        ("f_report_value", "float", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id_server_id_inserted_datetime", "unique": True, "columns": ("i_report_id", "i_server_id", "dt_inserted_datetime", ) },
        ),
    }
tables.append(tableReportValueDaily)

tableReportValueDaily["views"]=[]
for i in range(0, int(math.ceil(1.0*tableReportValueDaily["tablePartitionCount"]/maxTableCountInView))):
    startIndex, endIndex=i*maxTableCountInView, min(tableReportValueDaily["tablePartitionCount"], (i+1)*maxTableCountInView)
    tableReportValueDaily["views"].append(
        {
            "viewName": "%s_%d_%d" % (tableReportValueDaily["tableName"], startIndex, endIndex-1),
            "sqlQuery": "\n    UNION ALL\n    ".join(map(lambda x: "SELECT * FROM %s_%d" % (tableReportValueDaily["tableName"], x), range(startIndex, endIndex)))
        },
        )

tableReportValueDaily["sps"]=(
    {
        "spName": "GetReportValueDailiesByReportIDAndDateTime",
        "description": "Get report value dailies by report ID and datetime",
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
            f_report_value            AS ''reportValue'',
            b_failed                  AS ''failed'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id = @i_report_id
          AND dt_inserted_datetime >= @dt_inserted_datetime_from
          AND dt_inserted_datetime < @dt_inserted_datetime_to'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILIES_BY_REPORT_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueDailiesByReportIDAndServerIDsAndDateTime",
        "description": "Get report value dailies by report ID and server IDs and datetime",
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
            f_report_value            AS ''reportValue'',
            b_failed                  AS ''failed'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id = @i_report_id
          AND i_server_id IN (' + @vc_server_ids + ')
          AND dt_inserted_datetime >= @dt_inserted_datetime_from
          AND dt_inserted_datetime < @dt_inserted_datetime_to'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILIES_BY_REPORT_ID_AND_SERVER_IDS_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueDailySumsByReportIDAndDateTimeGroupByDataCenterID",
        "description": "Get report value daily sums by report ID and datetime group by data center ID",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        SELECT
            B.i_data_center_id              AS ''id'',
            SUM(A.f_report_value)           AS ''value''
        FROM 
            (
                SELECT
                    i_server_id             AS ''i_server_id'',
                    SUM(f_report_value)     AS ''f_report_value''
                FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
                WHERE i_report_id          = @i_report_id
                  AND b_failed             = 0
                  AND dt_inserted_datetime >= @dt_inserted_datetime_from
                  AND dt_inserted_datetime < @dt_inserted_datetime_to
                GROUP BY i_server_id
            ) A, 
            config_servers B
        WHERE A.i_server_id = B.i_server_id
        GROUP BY B.i_data_center_id'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILY_SUMS_BY_REPORT_ID_AND_DATETIME_GROUP_BY_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueDailyAvgsByReportIDAndDateTimeGroupByDataCenterID",
        "description": "Get report value daily avgs by report ID and datetime group by data center ID",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        SELECT
            B.i_data_center_id              AS ''id'',
            AVG(A.f_report_value)           AS ''value''
        FROM 
            (
                SELECT
                    i_server_id             AS ''i_server_id'',
                    AVG(f_report_value)     AS ''f_report_value''
                FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
                WHERE i_report_id          = @i_report_id
                  AND b_failed             = 0
                  AND dt_inserted_datetime >= @dt_inserted_datetime_from
                  AND dt_inserted_datetime < @dt_inserted_datetime_to
                GROUP BY i_server_id
            ) A, 
            config_servers B
        WHERE A.i_server_id = B.i_server_id
        GROUP BY B.i_data_center_id'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILY_AVGS_BY_REPORT_ID_AND_DATETIM_GROUP_BY_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueDailySumsByReportIDAndDateTimeGroupByDataCenterIDAndDateTime",
        "description": "Get report value daily sums by report ID and datetime group by data center ID and datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        SELECT
            B.i_data_center_id          AS ''dataCenterID'', 
            A.dt_inserted_datetime      AS ''insertedDateTime'',
            AVG(A.f_report_value)       AS ''reportValue''
        FROM
            report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' A WITH (FORCESEEK),
            config_servers B
        WHERE A.i_report_id          = @i_report_id
          AND A.b_failed             = 0
          AND A.dt_inserted_datetime >= @dt_inserted_datetime_from
          AND A.dt_inserted_datetime < @dt_inserted_datetime_to
          AND A.i_server_id = B.i_server_id
        GROUP BY B.i_data_center_id, A.dt_inserted_datetime'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILY_SUMS_BY_REPORT_ID_AND_DATETIME_GROUP_BY_DATA_CENTER_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueDailyAvgsByReportIDAndDateTimeGroupByDataCenterIDAndDateTime",
        "description": "Get report value daily avgs by report ID and datetime group by data center ID and datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        SELECT
            B.i_data_center_id          AS ''dataCenterID'', 
            A.dt_inserted_datetime      AS ''insertedDateTime'',
            AVG(A.f_report_value)       AS ''reportValue''
        FROM
            report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' A WITH (FORCESEEK),
            config_servers B
        WHERE A.i_report_id          = @i_report_id
          AND A.b_failed             = 0
          AND A.dt_inserted_datetime >= @dt_inserted_datetime_from
          AND A.dt_inserted_datetime < @dt_inserted_datetime_to
          AND A.i_server_id = B.i_server_id
        GROUP BY B.i_data_center_id, A.dt_inserted_datetime'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @dt_inserted_datetime_from   datetime,
            @dt_inserted_datetime_to     datetime',
        @i_report_id               = @i_report_id,
        @dt_inserted_datetime_from = @dt_inserted_datetime_from,
        @dt_inserted_datetime_to   = @dt_inserted_datetime_to

    CHKERR({ERROR_GET_REPORT_VALUE_DAILY_AVGS_BY_REPORT_ID_AND_DATETIME_GROUP_BY_DATA_CENTER_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "DeleteReportValueDailiesByReportID",
        "description": "Delete report value dailies by report ID",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        DELETE FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
        WHERE i_report_id = @i_report_id
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@i_report_id int',
        @i_report_id = @i_report_id

    TRANCHKERR({ERROR_DELETE_REPORT_VALUE_DAILIES_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportValueDailiesByDateTime",
        "description": "Delete report value dailies by datetime",
        "inputParameters":
"""@i_daily_partition_id        int,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        DELETE FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
        WHERE dt_inserted_datetime < @dt_inserted_datetime_to
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@dt_inserted_datetime_to datetime',
        @dt_inserted_datetime_to = @dt_inserted_datetime_to

    TRANCHKERR({ERROR_DELETE_REPORT_VALUE_DAILIES_BY_DATETIME})
    TRANRETURN""",
    },
    {
        "spName": "InsertOrUpdateReportValueDaily",
        "description": "Insert or update report value daily",
        "inputParameters":
"""@i_daily_partition_id        int,
    @i_report_id                 int,
    @i_server_id                 int,
    @f_report_value              float,
    @b_failed                    bit,
    @dt_inserted_datetime        datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)

    SET @nvc_sql_query = '
        DECLARE @bi_sequence_id int
        SET @bi_sequence_id = 0
        SELECT @bi_sequence_id = bi_sequence_id
        FROM report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id = @i_report_id
          AND i_server_id = @i_server_id
          AND dt_inserted_datetime = @dt_inserted_datetime
        IF (@bi_sequence_id = 0)
        BEGIN
            INSERT INTO report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + ' (
                i_report_id,
                i_server_id,
                f_report_value,
                b_failed,
                dt_inserted_datetime
                ) VALUES (
                @i_report_id,
                @i_server_id,
                @f_report_value,
                @b_failed,
                @dt_inserted_datetime
                )
            SELECT @@IDENTITY AS ''identity''
        END
        ELSE
        BEGIN
            UPDATE report_value_daily_' + CAST(@i_daily_partition_id AS varchar) + '
            SET
                f_report_value       = @f_report_value,
                b_failed             = @b_failed,
                dt_inserted_datetime = @dt_inserted_datetime
            WHERE bi_sequence_id = @bi_sequence_id
            SELECT @bi_sequence_id AS ''identity''
        END'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @i_server_id                 int,
            @f_report_value              float,
            @b_failed                    bit,
            @dt_inserted_datetime        datetime',
        @i_report_id          = @i_report_id,
        @i_server_id          = @i_server_id,
        @f_report_value       = @f_report_value,
        @b_failed             = @b_failed,
        @dt_inserted_datetime = @dt_inserted_datetime

    TRANCHKERR({ERROR_INSERT_OR_UPDATE_REPORT_VALUE_DAILY})
    TRANRETURN""",
    },
    )