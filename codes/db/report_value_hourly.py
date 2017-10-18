tableReportValueHourly={
    "tableName": "report_value_hourly",
    "tablePartitionCount": 256,
    "columns": (
        ("bi_sequence_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "not null"),
        ("i_server_id", "int", "not null"),
        ("f_report_value_0", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_1", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_2", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_3", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_4", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_5", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_6", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_7", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_8", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_9", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_10", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_11", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_12", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_13", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_14", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_15", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_16", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_17", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_18", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_19", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_20", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_21", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_22", "float", "NOT NULL", "DEFAULT ((0))"),
        ("f_report_value_23", "float", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_0", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_1", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_2", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_3", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_4", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_5", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_6", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_7", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_8", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_9", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_10", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_11", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_12", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_13", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_14", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_15", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_16", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_17", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_18", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_19", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_20", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_21", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_22", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_failed_23", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id_server_id_inserted_datetime", "unique": True, "columns": ("i_report_id", "i_server_id", "dt_inserted_datetime", ) },
        ),
    }
tables.append(tableReportValueHourly)

tableReportValueHourly["views"]=[]
for i in range(0, int(math.ceil(1.0*tableReportValueHourly["tablePartitionCount"]/maxTableCountInView))):
    startIndex, endIndex=i*maxTableCountInView, min(tableReportValueHourly["tablePartitionCount"], (i+1)*maxTableCountInView)
    tableReportValueHourly["views"].append(
        {
            "viewName": "%s_%d_%d" % (tableReportValueHourly["tableName"], startIndex, endIndex-1),
            "sqlQuery": "\n    UNION ALL\n    ".join(map(lambda x: "SELECT * FROM %s_%d" % (tableReportValueHourly["tableName"], x), range(startIndex, endIndex)))
        },
        )

tableReportValueHourly["dataObjectExtra"]="""
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Security", "CA2104:DoNotDeclareReadOnlyMutableReferenceTypes")]
        public static readonly int HOURS_COUNT = 24;

        public virtual bool IsFailed(int index)
        {
            CheckIndex(index);
            switch (index)
            {
                case 0: return Failed0;
                case 1: return Failed1;
                case 2: return Failed2;
                case 3: return Failed3;
                case 4: return Failed4;
                case 5: return Failed5;
                case 6: return Failed6;
                case 7: return Failed7;
                case 8: return Failed8;
                case 9: return Failed9;
                case 10: return Failed10;
                case 11: return Failed11;
                case 12: return Failed12;
                case 13: return Failed13;
                case 14: return Failed14;
                case 15: return Failed15;
                case 16: return Failed16;
                case 17: return Failed17;
                case 18: return Failed18;
                case 19: return Failed19;
                case 20: return Failed20;
                case 21: return Failed21;
                case 22: return Failed22;
                case 23: return Failed23;
                default:
                    throw new IndexOutOfRangeException();
            }
        }

        public virtual void SetFailed(int index, bool value)
        {
            CheckIndex(index);
            switch (index)
            {
                case 0: Failed0 = value; break;
                case 1: Failed1 = value; break;
                case 2: Failed2 = value; break;
                case 3: Failed3 = value; break;
                case 4: Failed4 = value; break;
                case 5: Failed5 = value; break;
                case 6: Failed6 = value; break;
                case 7: Failed7 = value; break;
                case 8: Failed8 = value; break;
                case 9: Failed9 = value; break;
                case 10: Failed10 = value; break;
                case 11: Failed11 = value; break;
                case 12: Failed12 = value; break;
                case 13: Failed13 = value; break;
                case 14: Failed14 = value; break;
                case 15: Failed15 = value; break;
                case 16: Failed16 = value; break;
                case 17: Failed17 = value; break;
                case 18: Failed18 = value; break;
                case 19: Failed19 = value; break;
                case 20: Failed20 = value; break;
                case 21: Failed21 = value; break;
                case 22: Failed22 = value; break;
                case 23: Failed23 = value; break;
                default:
                    throw new IndexOutOfRangeException();
            }
        }

        public virtual void SetAllFailed(bool value)
        {
            for (int i = 0; i < HOURS_COUNT; ++i)
                SetFailed(i, value);
        }
        
        public virtual double GetReportValue(int index)
        {
            CheckIndex(index);
            switch (index)
            {
                case 0: return ReportValue0;
                case 1: return ReportValue1;
                case 2: return ReportValue2;
                case 3: return ReportValue3;
                case 4: return ReportValue4;
                case 5: return ReportValue5;
                case 6: return ReportValue6;
                case 7: return ReportValue7;
                case 8: return ReportValue8;
                case 9: return ReportValue9;
                case 10: return ReportValue10;
                case 11: return ReportValue11;
                case 12: return ReportValue12;
                case 13: return ReportValue13;
                case 14: return ReportValue14;
                case 15: return ReportValue15;
                case 16: return ReportValue16;
                case 17: return ReportValue17;
                case 18: return ReportValue18;
                case 19: return ReportValue19;
                case 20: return ReportValue20;
                case 21: return ReportValue21;
                case 22: return ReportValue22;
                case 23: return ReportValue23;
                default:
                    throw new IndexOutOfRangeException();
            }
        }

        public virtual void SetReportValue(int index, double value)
        {
            CheckIndex(index);
            switch (index)
            {
                case 0: ReportValue0 = value; break;
                case 1: ReportValue1 = value; break;
                case 2: ReportValue2 = value; break;
                case 3: ReportValue3 = value; break;
                case 4: ReportValue4 = value; break;
                case 5: ReportValue5 = value; break;
                case 6: ReportValue6 = value; break;
                case 7: ReportValue7 = value; break;
                case 8: ReportValue8 = value; break;
                case 9: ReportValue9 = value; break;
                case 10: ReportValue10 = value; break;
                case 11: ReportValue11 = value; break;
                case 12: ReportValue12 = value; break;
                case 13: ReportValue13 = value; break;
                case 14: ReportValue14 = value; break;
                case 15: ReportValue15 = value; break;
                case 16: ReportValue16 = value; break;
                case 17: ReportValue17 = value; break;
                case 18: ReportValue18 = value; break;
                case 19: ReportValue19 = value; break;
                case 20: ReportValue20 = value; break;
                case 21: ReportValue21 = value; break;
                case 22: ReportValue22 = value; break;
                case 23: ReportValue23 = value; break;
                default:
                    throw new IndexOutOfRangeException();
            }
        }

        protected virtual void CheckIndex(int index)
        {
            if (index < 0 || index > 23)
                throw new IndexOutOfRangeException();
        }
"""
tableReportValueHourly["sps"]=(
    {
        "spName": "GetReportValueHourliesByReportIDAndDateTime",
        "description": "Get report value hourlies by report ID and datetime",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(max)

    SET @nvc_sql_query = '
        SELECT
            bi_sequence_id            AS ''sequenceID'',
            i_report_id               AS ''reportID'',
            i_server_id               AS ''serverID'',
            f_report_value_0          AS ''reportValue0'',
            f_report_value_1          AS ''reportValue1'',
            f_report_value_2          AS ''reportValue2'',
            f_report_value_3          AS ''reportValue3'',
            f_report_value_4          AS ''reportValue4'',
            f_report_value_5          AS ''reportValue5'',
            f_report_value_6          AS ''reportValue6'',
            f_report_value_7          AS ''reportValue7'',
            f_report_value_8          AS ''reportValue8'',
            f_report_value_9          AS ''reportValue9'',
            f_report_value_10         AS ''reportValue10'',
            f_report_value_11         AS ''reportValue11'',
            f_report_value_12         AS ''reportValue12'',
            f_report_value_13         AS ''reportValue13'',
            f_report_value_14         AS ''reportValue14'',
            f_report_value_15         AS ''reportValue15'',
            f_report_value_16         AS ''reportValue16'',
            f_report_value_17         AS ''reportValue17'',
            f_report_value_18         AS ''reportValue18'',
            f_report_value_19         AS ''reportValue19'',
            f_report_value_20         AS ''reportValue20'',
            f_report_value_21         AS ''reportValue21'',
            f_report_value_22         AS ''reportValue22'',
            f_report_value_23         AS ''reportValue23'',
            b_failed_0                AS ''failed0'',
            b_failed_1                AS ''failed1'',
            b_failed_2                AS ''failed2'',
            b_failed_3                AS ''failed3'',
            b_failed_4                AS ''failed4'',
            b_failed_5                AS ''failed5'',
            b_failed_6                AS ''failed6'',
            b_failed_7                AS ''failed7'',
            b_failed_8                AS ''failed8'',
            b_failed_9                AS ''failed9'',
            b_failed_10               AS ''failed10'',
            b_failed_11               AS ''failed11'',
            b_failed_12               AS ''failed12'',
            b_failed_13               AS ''failed13'',
            b_failed_14               AS ''failed14'',
            b_failed_15               AS ''failed15'',
            b_failed_16               AS ''failed16'',
            b_failed_17               AS ''failed17'',
            b_failed_18               AS ''failed18'',
            b_failed_19               AS ''failed19'',
            b_failed_20               AS ''failed20'',
            b_failed_21               AS ''failed21'',
            b_failed_22               AS ''failed22'',
            b_failed_23               AS ''failed23'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' WITH (FORCESEEK)
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

    CHKERR({ERROR_GET_REPORT_VALUE_HOURLIES_BY_REPORT_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueHourliesByReportIDAndServerIDsAndDateTime",
        "description": "Get report value hourlies by report ID and server IDs and datetime",
        "inputParameters":
"""@i_hourly_partition_id       int,
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
            f_report_value_0          AS ''reportValue0'',
            f_report_value_1          AS ''reportValue1'',
            f_report_value_2          AS ''reportValue2'',
            f_report_value_3          AS ''reportValue3'',
            f_report_value_4          AS ''reportValue4'',
            f_report_value_5          AS ''reportValue5'',
            f_report_value_6          AS ''reportValue6'',
            f_report_value_7          AS ''reportValue7'',
            f_report_value_8          AS ''reportValue8'',
            f_report_value_9          AS ''reportValue9'',
            f_report_value_10         AS ''reportValue10'',
            f_report_value_11         AS ''reportValue11'',
            f_report_value_12         AS ''reportValue12'',
            f_report_value_13         AS ''reportValue13'',
            f_report_value_14         AS ''reportValue14'',
            f_report_value_15         AS ''reportValue15'',
            f_report_value_16         AS ''reportValue16'',
            f_report_value_17         AS ''reportValue17'',
            f_report_value_18         AS ''reportValue18'',
            f_report_value_19         AS ''reportValue19'',
            f_report_value_20         AS ''reportValue20'',
            f_report_value_21         AS ''reportValue21'',
            f_report_value_22         AS ''reportValue22'',
            f_report_value_23         AS ''reportValue23'',
            b_failed_0                AS ''failed0'',
            b_failed_1                AS ''failed1'',
            b_failed_2                AS ''failed2'',
            b_failed_3                AS ''failed3'',
            b_failed_4                AS ''failed4'',
            b_failed_5                AS ''failed5'',
            b_failed_6                AS ''failed6'',
            b_failed_7                AS ''failed7'',
            b_failed_8                AS ''failed8'',
            b_failed_9                AS ''failed9'',
            b_failed_10               AS ''failed10'',
            b_failed_11               AS ''failed11'',
            b_failed_12               AS ''failed12'',
            b_failed_13               AS ''failed13'',
            b_failed_14               AS ''failed14'',
            b_failed_15               AS ''failed15'',
            b_failed_16               AS ''failed16'',
            b_failed_17               AS ''failed17'',
            b_failed_18               AS ''failed18'',
            b_failed_19               AS ''failed19'',
            b_failed_20               AS ''failed20'',
            b_failed_21               AS ''failed21'',
            b_failed_22               AS ''failed22'',
            b_failed_23               AS ''failed23'',
            dt_inserted_datetime      AS ''insertedDateTime''
        FROM report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' WITH (FORCESEEK)
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

    CHKERR({ERROR_GET_REPORT_VALUE_HOURLIES_BY_REPORT_ID_AND_SERVER_IDS_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueHourlySumsByReportIDAndDateTimeGroupByDataCenterIDAndDateTime",
        "description": "Get report value hourly sums by report ID and datetime group by data center ID and datetime",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(max)
    
    SET @nvc_sql_query = '
        DECLARE @b_true              bit
        DECLARE @b_false             bit
        SET     @b_true              = 1
        SET     @b_false             = 0
    
        SELECT
            B.i_data_center_id                                                          AS ''dataCenterID'',
            SUM(CASE A.b_failed_0   WHEN 0 THEN A.f_report_value_0  ELSE NULL END)      AS ''reportValue0'',
            SUM(CASE A.b_failed_1   WHEN 0 THEN A.f_report_value_1  ELSE NULL END)      AS ''reportValue1'',
            SUM(CASE A.b_failed_2   WHEN 0 THEN A.f_report_value_2  ELSE NULL END)      AS ''reportValue2'',
            SUM(CASE A.b_failed_3   WHEN 0 THEN A.f_report_value_3  ELSE NULL END)      AS ''reportValue3'',
            SUM(CASE A.b_failed_4   WHEN 0 THEN A.f_report_value_4  ELSE NULL END)      AS ''reportValue4'',
            SUM(CASE A.b_failed_5   WHEN 0 THEN A.f_report_value_5  ELSE NULL END)      AS ''reportValue5'',
            SUM(CASE A.b_failed_6   WHEN 0 THEN A.f_report_value_6  ELSE NULL END)      AS ''reportValue6'',
            SUM(CASE A.b_failed_7   WHEN 0 THEN A.f_report_value_7  ELSE NULL END)      AS ''reportValue7'',
            SUM(CASE A.b_failed_8   WHEN 0 THEN A.f_report_value_8  ELSE NULL END)      AS ''reportValue8'',
            SUM(CASE A.b_failed_9   WHEN 0 THEN A.f_report_value_9  ELSE NULL END)      AS ''reportValue9'',
            SUM(CASE A.b_failed_10  WHEN 0 THEN A.f_report_value_10 ELSE NULL END)      AS ''reportValue10'',
            SUM(CASE A.b_failed_11  WHEN 0 THEN A.f_report_value_11 ELSE NULL END)      AS ''reportValue11'',
            SUM(CASE A.b_failed_12  WHEN 0 THEN A.f_report_value_12 ELSE NULL END)      AS ''reportValue12'',
            SUM(CASE A.b_failed_13  WHEN 0 THEN A.f_report_value_13 ELSE NULL END)      AS ''reportValue13'',
            SUM(CASE A.b_failed_14  WHEN 0 THEN A.f_report_value_14 ELSE NULL END)      AS ''reportValue14'',
            SUM(CASE A.b_failed_15  WHEN 0 THEN A.f_report_value_15 ELSE NULL END)      AS ''reportValue15'',
            SUM(CASE A.b_failed_16  WHEN 0 THEN A.f_report_value_16 ELSE NULL END)      AS ''reportValue16'',
            SUM(CASE A.b_failed_17  WHEN 0 THEN A.f_report_value_17 ELSE NULL END)      AS ''reportValue17'',
            SUM(CASE A.b_failed_18  WHEN 0 THEN A.f_report_value_18 ELSE NULL END)      AS ''reportValue18'',
            SUM(CASE A.b_failed_19  WHEN 0 THEN A.f_report_value_19 ELSE NULL END)      AS ''reportValue19'',
            SUM(CASE A.b_failed_20  WHEN 0 THEN A.f_report_value_20 ELSE NULL END)      AS ''reportValue20'',
            SUM(CASE A.b_failed_21  WHEN 0 THEN A.f_report_value_21 ELSE NULL END)      AS ''reportValue21'',
            SUM(CASE A.b_failed_22  WHEN 0 THEN A.f_report_value_22 ELSE NULL END)      AS ''reportValue22'',
            SUM(CASE A.b_failed_23  WHEN 0 THEN A.f_report_value_23 ELSE NULL END)      AS ''reportValue23'',
            CASE    WHEN SUM(1 - b_failed_0) = 0    THEN @b_true     ELSE @b_false END  AS ''failed0'',
            CASE    WHEN SUM(1 - b_failed_1) = 0    THEN @b_true     ELSE @b_false END  AS ''failed1'',
            CASE    WHEN SUM(1 - b_failed_2) = 0    THEN @b_true     ELSE @b_false END  AS ''failed2'',
            CASE    WHEN SUM(1 - b_failed_3) = 0    THEN @b_true     ELSE @b_false END  AS ''failed3'',
            CASE    WHEN SUM(1 - b_failed_4) = 0    THEN @b_true     ELSE @b_false END  AS ''failed4'',
            CASE    WHEN SUM(1 - b_failed_5) = 0    THEN @b_true     ELSE @b_false END  AS ''failed5'',
            CASE    WHEN SUM(1 - b_failed_6) = 0    THEN @b_true     ELSE @b_false END  AS ''failed6'',
            CASE    WHEN SUM(1 - b_failed_7) = 0    THEN @b_true     ELSE @b_false END  AS ''failed7'',
            CASE    WHEN SUM(1 - b_failed_8) = 0    THEN @b_true     ELSE @b_false END  AS ''failed8'',
            CASE    WHEN SUM(1 - b_failed_9) = 0    THEN @b_true     ELSE @b_false END  AS ''failed9'',
            CASE    WHEN SUM(1 - b_failed_10) = 0   THEN @b_true     ELSE @b_false END  AS ''failed10'',
            CASE    WHEN SUM(1 - b_failed_11) = 0   THEN @b_true     ELSE @b_false END  AS ''failed11'',
            CASE    WHEN SUM(1 - b_failed_12) = 0   THEN @b_true     ELSE @b_false END  AS ''failed12'',
            CASE    WHEN SUM(1 - b_failed_13) = 0   THEN @b_true     ELSE @b_false END  AS ''failed13'',
            CASE    WHEN SUM(1 - b_failed_14) = 0   THEN @b_true     ELSE @b_false END  AS ''failed14'',
            CASE    WHEN SUM(1 - b_failed_15) = 0   THEN @b_true     ELSE @b_false END  AS ''failed15'',
            CASE    WHEN SUM(1 - b_failed_16) = 0   THEN @b_true     ELSE @b_false END  AS ''failed16'',
            CASE    WHEN SUM(1 - b_failed_17) = 0   THEN @b_true     ELSE @b_false END  AS ''failed17'',
            CASE    WHEN SUM(1 - b_failed_18) = 0   THEN @b_true     ELSE @b_false END  AS ''failed18'',
            CASE    WHEN SUM(1 - b_failed_19) = 0   THEN @b_true     ELSE @b_false END  AS ''failed19'',
            CASE    WHEN SUM(1 - b_failed_20) = 0   THEN @b_true     ELSE @b_false END  AS ''failed20'',
            CASE    WHEN SUM(1 - b_failed_21) = 0   THEN @b_true     ELSE @b_false END  AS ''failed21'',
            CASE    WHEN SUM(1 - b_failed_22) = 0   THEN @b_true     ELSE @b_false END  AS ''failed22'',
            CASE    WHEN SUM(1 - b_failed_23) = 0   THEN @b_true     ELSE @b_false END  AS ''failed23'',
            A.dt_inserted_datetime                                                      AS ''insertedDateTime''
        FROM 
            report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' A WITH (FORCESEEK),
            config_servers B
        WHERE A.i_report_id = @i_report_id
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

    CHKERR({ERROR_GET_REPORT_VALUE_HOURLY_SUMS_BY_REPORT_ID_AND_DATETIME_GROUP_BY_DATA_CENTER_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "GetReportValueHourlyAvgsByReportIDAndDateTimeGroupByDataCenterIDAndDateTime",
        "description": "Get report value hourly avgs by report ID and datetime group by data center ID and datetime",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @i_report_id                 int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""DECLARE @nvc_sql_query       nvarchar(max)
    
    SET @nvc_sql_query = '
        DECLARE @b_true              bit
        DECLARE @b_false             bit
        SET     @b_true              = 1
        SET     @b_false             = 0
        
        SELECT
            B.i_data_center_id                                                          AS ''dataCenterID'',
            AVG(CASE A.b_failed_0   WHEN 0 THEN A.f_report_value_0  ELSE NULL END)      AS ''reportValue0'',
            AVG(CASE A.b_failed_1   WHEN 0 THEN A.f_report_value_1  ELSE NULL END)      AS ''reportValue1'',
            AVG(CASE A.b_failed_2   WHEN 0 THEN A.f_report_value_2  ELSE NULL END)      AS ''reportValue2'',
            AVG(CASE A.b_failed_3   WHEN 0 THEN A.f_report_value_3  ELSE NULL END)      AS ''reportValue3'',
            AVG(CASE A.b_failed_4   WHEN 0 THEN A.f_report_value_4  ELSE NULL END)      AS ''reportValue4'',
            AVG(CASE A.b_failed_5   WHEN 0 THEN A.f_report_value_5  ELSE NULL END)      AS ''reportValue5'',
            AVG(CASE A.b_failed_6   WHEN 0 THEN A.f_report_value_6  ELSE NULL END)      AS ''reportValue6'',
            AVG(CASE A.b_failed_7   WHEN 0 THEN A.f_report_value_7  ELSE NULL END)      AS ''reportValue7'',
            AVG(CASE A.b_failed_8   WHEN 0 THEN A.f_report_value_8  ELSE NULL END)      AS ''reportValue8'',
            AVG(CASE A.b_failed_9   WHEN 0 THEN A.f_report_value_9  ELSE NULL END)      AS ''reportValue9'',
            AVG(CASE A.b_failed_10  WHEN 0 THEN A.f_report_value_10 ELSE NULL END)      AS ''reportValue10'',
            AVG(CASE A.b_failed_11  WHEN 0 THEN A.f_report_value_11 ELSE NULL END)      AS ''reportValue11'',
            AVG(CASE A.b_failed_12  WHEN 0 THEN A.f_report_value_12 ELSE NULL END)      AS ''reportValue12'',
            AVG(CASE A.b_failed_13  WHEN 0 THEN A.f_report_value_13 ELSE NULL END)      AS ''reportValue13'',
            AVG(CASE A.b_failed_14  WHEN 0 THEN A.f_report_value_14 ELSE NULL END)      AS ''reportValue14'',
            AVG(CASE A.b_failed_15  WHEN 0 THEN A.f_report_value_15 ELSE NULL END)      AS ''reportValue15'',
            AVG(CASE A.b_failed_16  WHEN 0 THEN A.f_report_value_16 ELSE NULL END)      AS ''reportValue16'',
            AVG(CASE A.b_failed_17  WHEN 0 THEN A.f_report_value_17 ELSE NULL END)      AS ''reportValue17'',
            AVG(CASE A.b_failed_18  WHEN 0 THEN A.f_report_value_18 ELSE NULL END)      AS ''reportValue18'',
            AVG(CASE A.b_failed_19  WHEN 0 THEN A.f_report_value_19 ELSE NULL END)      AS ''reportValue19'',
            AVG(CASE A.b_failed_20  WHEN 0 THEN A.f_report_value_20 ELSE NULL END)      AS ''reportValue20'',
            AVG(CASE A.b_failed_21  WHEN 0 THEN A.f_report_value_21 ELSE NULL END)      AS ''reportValue21'',
            AVG(CASE A.b_failed_22  WHEN 0 THEN A.f_report_value_22 ELSE NULL END)      AS ''reportValue22'',
            AVG(CASE A.b_failed_23  WHEN 0 THEN A.f_report_value_23 ELSE NULL END)      AS ''reportValue23'',
            CASE    WHEN SUM(1 - b_failed_0) = 0    THEN @b_true     ELSE @b_false END  AS ''failed0'',
            CASE    WHEN SUM(1 - b_failed_1) = 0    THEN @b_true     ELSE @b_false END  AS ''failed1'',
            CASE    WHEN SUM(1 - b_failed_2) = 0    THEN @b_true     ELSE @b_false END  AS ''failed2'',
            CASE    WHEN SUM(1 - b_failed_3) = 0    THEN @b_true     ELSE @b_false END  AS ''failed3'',
            CASE    WHEN SUM(1 - b_failed_4) = 0    THEN @b_true     ELSE @b_false END  AS ''failed4'',
            CASE    WHEN SUM(1 - b_failed_5) = 0    THEN @b_true     ELSE @b_false END  AS ''failed5'',
            CASE    WHEN SUM(1 - b_failed_6) = 0    THEN @b_true     ELSE @b_false END  AS ''failed6'',
            CASE    WHEN SUM(1 - b_failed_7) = 0    THEN @b_true     ELSE @b_false END  AS ''failed7'',
            CASE    WHEN SUM(1 - b_failed_8) = 0    THEN @b_true     ELSE @b_false END  AS ''failed8'',
            CASE    WHEN SUM(1 - b_failed_9) = 0    THEN @b_true     ELSE @b_false END  AS ''failed9'',
            CASE    WHEN SUM(1 - b_failed_10) = 0   THEN @b_true     ELSE @b_false END  AS ''failed10'',
            CASE    WHEN SUM(1 - b_failed_11) = 0   THEN @b_true     ELSE @b_false END  AS ''failed11'',
            CASE    WHEN SUM(1 - b_failed_12) = 0   THEN @b_true     ELSE @b_false END  AS ''failed12'',
            CASE    WHEN SUM(1 - b_failed_13) = 0   THEN @b_true     ELSE @b_false END  AS ''failed13'',
            CASE    WHEN SUM(1 - b_failed_14) = 0   THEN @b_true     ELSE @b_false END  AS ''failed14'',
            CASE    WHEN SUM(1 - b_failed_15) = 0   THEN @b_true     ELSE @b_false END  AS ''failed15'',
            CASE    WHEN SUM(1 - b_failed_16) = 0   THEN @b_true     ELSE @b_false END  AS ''failed16'',
            CASE    WHEN SUM(1 - b_failed_17) = 0   THEN @b_true     ELSE @b_false END  AS ''failed17'',
            CASE    WHEN SUM(1 - b_failed_18) = 0   THEN @b_true     ELSE @b_false END  AS ''failed18'',
            CASE    WHEN SUM(1 - b_failed_19) = 0   THEN @b_true     ELSE @b_false END  AS ''failed19'',
            CASE    WHEN SUM(1 - b_failed_20) = 0   THEN @b_true     ELSE @b_false END  AS ''failed20'',
            CASE    WHEN SUM(1 - b_failed_21) = 0   THEN @b_true     ELSE @b_false END  AS ''failed21'',
            CASE    WHEN SUM(1 - b_failed_22) = 0   THEN @b_true     ELSE @b_false END  AS ''failed22'',
            CASE    WHEN SUM(1 - b_failed_23) = 0   THEN @b_true     ELSE @b_false END  AS ''failed23'',
            A.dt_inserted_datetime                                                      AS ''insertedDateTime''
        FROM 
            report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' A WITH (FORCESEEK),
            config_servers B
        WHERE A.i_report_id = @i_report_id
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

    CHKERR({ERROR_GET_REPORT_VALUE_HOURLY_AVGS_BY_REPORT_ID_AND_DATETIME_GROUP_BY_DATA_CENTER_ID_AND_DATETIME})
    RETURN 0""",
    },
    {
        "spName": "DeleteReportValueHourliesByReportID",
        "description": "Delete report value hourlies by report ID",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @i_report_id                 int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)
    
    SET @nvc_sql_query = 'DELETE FROM report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + '
        WHERE i_report_id = @i_report_id
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@i_report_id int',
        @i_report_id = @i_report_id
    
    TRANCHKERR({ERROR_DELETE_REPORT_VALUE_HOURLIES_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportValueHourliesByDateTime",
        "description": "Delete report value hourlies by datetime",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query       nvarchar(4000)
    
    SET @nvc_sql_query = 'DELETE FROM report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + '
        WHERE dt_inserted_datetime < @dt_inserted_datetime_to
        SELECT @@ROWCOUNT AS ''rowcount'''
    EXEC sp_executesql @nvc_sql_query,
        N'@dt_inserted_datetime_to datetime',
        @dt_inserted_datetime_to = @dt_inserted_datetime_to
    
    TRANCHKERR({ERROR_DELETE_REPORT_VALUE_HOURLIES_BY_DATETIME})
    TRANRETURN""",
    },
    {
        "spName": "InsertOrUpdateReportValueHourly",
        "description": "Insert or update report value hourly",
        "inputParameters":
"""@i_hourly_partition_id       int,
    @i_report_id                 int,
    @i_server_id                 int,
    @f_report_value_0            float,
    @f_report_value_1            float,
    @f_report_value_2            float,
    @f_report_value_3            float,
    @f_report_value_4            float,
    @f_report_value_5            float,
    @f_report_value_6            float,
    @f_report_value_7            float,
    @f_report_value_8            float,
    @f_report_value_9            float,
    @f_report_value_10           float,
    @f_report_value_11           float,
    @f_report_value_12           float,
    @f_report_value_13           float,
    @f_report_value_14           float,
    @f_report_value_15           float,
    @f_report_value_16           float,
    @f_report_value_17           float,
    @f_report_value_18           float,
    @f_report_value_19           float,
    @f_report_value_20           float,
    @f_report_value_21           float,
    @f_report_value_22           float,
    @f_report_value_23           float,
    @b_failed_0                  bit,
    @b_failed_1                  bit,
    @b_failed_2                  bit,
    @b_failed_3                  bit,
    @b_failed_4                  bit,
    @b_failed_5                  bit,
    @b_failed_6                  bit,
    @b_failed_7                  bit,
    @b_failed_8                  bit,
    @b_failed_9                  bit,
    @b_failed_10                 bit,
    @b_failed_11                 bit,
    @b_failed_12                 bit,
    @b_failed_13                 bit,
    @b_failed_14                 bit,
    @b_failed_15                 bit,
    @b_failed_16                 bit,
    @b_failed_17                 bit,
    @b_failed_18                 bit,
    @b_failed_19                 bit,
    @b_failed_20                 bit,
    @b_failed_21                 bit,
    @b_failed_22                 bit,
    @b_failed_23                 bit,
    @dt_inserted_datetime        datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @nvc_sql_query  nvarchar(max)

    SET @nvc_sql_query = '
        DECLARE @bi_sequence_id int
        SET @bi_sequence_id = 0
        SELECT @bi_sequence_id = bi_sequence_id 
        FROM report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' WITH (FORCESEEK)
        WHERE i_report_id = @i_report_id
          AND i_server_id = @i_server_id
          AND dt_inserted_datetime = @dt_inserted_datetime
        IF (@bi_sequence_id = 0)
        BEGIN
            INSERT INTO report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + ' (
                i_report_id,
                i_server_id,
                f_report_value_0,
                f_report_value_1,
                f_report_value_2,
                f_report_value_3,
                f_report_value_4,
                f_report_value_5,
                f_report_value_6,
                f_report_value_7,
                f_report_value_8,
                f_report_value_9,
                f_report_value_10,
                f_report_value_11,
                f_report_value_12,
                f_report_value_13,
                f_report_value_14,
                f_report_value_15,
                f_report_value_16,
                f_report_value_17,
                f_report_value_18,
                f_report_value_19,
                f_report_value_20,
                f_report_value_21,
                f_report_value_22,
                f_report_value_23,
                b_failed_0,
                b_failed_1,
                b_failed_2,
                b_failed_3,
                b_failed_4,
                b_failed_5,
                b_failed_6,
                b_failed_7,
                b_failed_8,
                b_failed_9,
                b_failed_10,
                b_failed_11,
                b_failed_12,
                b_failed_13,
                b_failed_14,
                b_failed_15,
                b_failed_16,
                b_failed_17,
                b_failed_18,
                b_failed_19,
                b_failed_20,
                b_failed_21,
                b_failed_22,
                b_failed_23,
                dt_inserted_datetime
                ) VALUES (
                @i_report_id,
                @i_server_id,
                @f_report_value_0,
                @f_report_value_1,
                @f_report_value_2,
                @f_report_value_3,
                @f_report_value_4,
                @f_report_value_5,
                @f_report_value_6,
                @f_report_value_7,
                @f_report_value_8,
                @f_report_value_9,
                @f_report_value_10,
                @f_report_value_11,
                @f_report_value_12,
                @f_report_value_13,
                @f_report_value_14,
                @f_report_value_15,
                @f_report_value_16,
                @f_report_value_17,
                @f_report_value_18,
                @f_report_value_19,
                @f_report_value_20,
                @f_report_value_21,
                @f_report_value_22,
                @f_report_value_23,
                @b_failed_0,
                @b_failed_1,
                @b_failed_2,
                @b_failed_3,
                @b_failed_4,
                @b_failed_5,
                @b_failed_6,
                @b_failed_7,
                @b_failed_8,
                @b_failed_9,
                @b_failed_10,
                @b_failed_11,
                @b_failed_12,
                @b_failed_13,
                @b_failed_14,
                @b_failed_15,
                @b_failed_16,
                @b_failed_17,
                @b_failed_18,
                @b_failed_19,
                @b_failed_20,
                @b_failed_21,
                @b_failed_22,
                @b_failed_23,
                @dt_inserted_datetime
                )
            SELECT @@IDENTITY AS ''identity''
        END
        ELSE
        BEGIN
            UPDATE report_value_hourly_' + CAST(@i_hourly_partition_id AS varchar) + '
            SET
                f_report_value_0 = @f_report_value_0,
                f_report_value_1 = @f_report_value_1,
                f_report_value_2 = @f_report_value_2,
                f_report_value_3 = @f_report_value_3,
                f_report_value_4 = @f_report_value_4,
                f_report_value_5 = @f_report_value_5,
                f_report_value_6 = @f_report_value_6,
                f_report_value_7 = @f_report_value_7,
                f_report_value_8 = @f_report_value_8,
                f_report_value_9 = @f_report_value_9,
                f_report_value_10 = @f_report_value_10,
                f_report_value_11 = @f_report_value_11,
                f_report_value_12 = @f_report_value_12,
                f_report_value_13 = @f_report_value_13,
                f_report_value_14 = @f_report_value_14,
                f_report_value_15 = @f_report_value_15,
                f_report_value_16 = @f_report_value_16,
                f_report_value_17 = @f_report_value_17,
                f_report_value_18 = @f_report_value_18,
                f_report_value_19 = @f_report_value_19,
                f_report_value_20 = @f_report_value_20,
                f_report_value_21 = @f_report_value_21,
                f_report_value_22 = @f_report_value_22,
                f_report_value_23 = @f_report_value_23,
                b_failed_0 = @b_failed_0,
                b_failed_1 = @b_failed_1,
                b_failed_2 = @b_failed_2,
                b_failed_3 = @b_failed_3,
                b_failed_4 = @b_failed_4,
                b_failed_5 = @b_failed_5,
                b_failed_6 = @b_failed_6,
                b_failed_7 = @b_failed_7,
                b_failed_8 = @b_failed_8,
                b_failed_9 = @b_failed_9,
                b_failed_10 = @b_failed_10,
                b_failed_11 = @b_failed_11,
                b_failed_12 = @b_failed_12,
                b_failed_13 = @b_failed_13,
                b_failed_14 = @b_failed_14,
                b_failed_15 = @b_failed_15,
                b_failed_16 = @b_failed_16,
                b_failed_17 = @b_failed_17,
                b_failed_18 = @b_failed_18,
                b_failed_19 = @b_failed_19,
                b_failed_20 = @b_failed_20,
                b_failed_21 = @b_failed_21,
                b_failed_22 = @b_failed_22,
                b_failed_23 = @b_failed_23,
                dt_inserted_datetime = @dt_inserted_datetime
            WHERE bi_sequence_id = @bi_sequence_id
            SELECT @bi_sequence_id AS ''identity''
        END'

    EXEC sp_executesql @nvc_sql_query,
        N'  @i_report_id                 int,
            @i_server_id                 int,
            @f_report_value_0            float,
            @f_report_value_1            float,
            @f_report_value_2            float,
            @f_report_value_3            float,
            @f_report_value_4            float,
            @f_report_value_5            float,
            @f_report_value_6            float,
            @f_report_value_7            float,
            @f_report_value_8            float,
            @f_report_value_9            float,
            @f_report_value_10           float,
            @f_report_value_11           float,
            @f_report_value_12           float,
            @f_report_value_13           float,
            @f_report_value_14           float,
            @f_report_value_15           float,
            @f_report_value_16           float,
            @f_report_value_17           float,
            @f_report_value_18           float,
            @f_report_value_19           float,
            @f_report_value_20           float,
            @f_report_value_21           float,
            @f_report_value_22           float,
            @f_report_value_23           float,
            @b_failed_0                  bit,
            @b_failed_1                  bit,
            @b_failed_2                  bit,
            @b_failed_3                  bit,
            @b_failed_4                  bit,
            @b_failed_5                  bit,
            @b_failed_6                  bit,
            @b_failed_7                  bit,
            @b_failed_8                  bit,
            @b_failed_9                  bit,
            @b_failed_10                 bit,
            @b_failed_11                 bit,
            @b_failed_12                 bit,
            @b_failed_13                 bit,
            @b_failed_14                 bit,
            @b_failed_15                 bit,
            @b_failed_16                 bit,
            @b_failed_17                 bit,
            @b_failed_18                 bit,
            @b_failed_19                 bit,
            @b_failed_20                 bit,
            @b_failed_21                 bit,
            @b_failed_22                 bit,
            @b_failed_23                 bit,
            @dt_inserted_datetime        datetime',
        @i_report_id = @i_report_id,
        @i_server_id = @i_server_id,
        @f_report_value_0 = @f_report_value_0,
        @f_report_value_1 = @f_report_value_1,
        @f_report_value_2 = @f_report_value_2,
        @f_report_value_3 = @f_report_value_3,
        @f_report_value_4 = @f_report_value_4,
        @f_report_value_5 = @f_report_value_5,
        @f_report_value_6 = @f_report_value_6,
        @f_report_value_7 = @f_report_value_7,
        @f_report_value_8 = @f_report_value_8,
        @f_report_value_9 = @f_report_value_9,
        @f_report_value_10 = @f_report_value_10,
        @f_report_value_11 = @f_report_value_11,
        @f_report_value_12 = @f_report_value_12,
        @f_report_value_13 = @f_report_value_13,
        @f_report_value_14 = @f_report_value_14,
        @f_report_value_15 = @f_report_value_15,
        @f_report_value_16 = @f_report_value_16,
        @f_report_value_17 = @f_report_value_17,
        @f_report_value_18 = @f_report_value_18,
        @f_report_value_19 = @f_report_value_19,
        @f_report_value_20 = @f_report_value_20,
        @f_report_value_21 = @f_report_value_21,
        @f_report_value_22 = @f_report_value_22,
        @f_report_value_23 = @f_report_value_23,
        @b_failed_0 = @b_failed_0,
        @b_failed_1 = @b_failed_1,
        @b_failed_2 = @b_failed_2,
        @b_failed_3 = @b_failed_3,
        @b_failed_4 = @b_failed_4,
        @b_failed_5 = @b_failed_5,
        @b_failed_6 = @b_failed_6,
        @b_failed_7 = @b_failed_7,
        @b_failed_8 = @b_failed_8,
        @b_failed_9 = @b_failed_9,
        @b_failed_10 = @b_failed_10,
        @b_failed_11 = @b_failed_11,
        @b_failed_12 = @b_failed_12,
        @b_failed_13 = @b_failed_13,
        @b_failed_14 = @b_failed_14,
        @b_failed_15 = @b_failed_15,
        @b_failed_16 = @b_failed_16,
        @b_failed_17 = @b_failed_17,
        @b_failed_18 = @b_failed_18,
        @b_failed_19 = @b_failed_19,
        @b_failed_20 = @b_failed_20,
        @b_failed_21 = @b_failed_21,
        @b_failed_22 = @b_failed_22,
        @b_failed_23 = @b_failed_23,
        @dt_inserted_datetime = @dt_inserted_datetime

    TRANCHKERR({ERROR_INSERT_OR_UPDATE_REPORT_VALUE_HOURLY})
    TRANRETURN""",
    },
    )