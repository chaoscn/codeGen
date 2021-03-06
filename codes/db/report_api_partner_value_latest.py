tableReportAPIPartnerValueLatest={
    "tableName": "report_api_partner_value_latest",
    "columns": (
        ("bi_sequence_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_report_id", "int", "not null"),
        ("i_server_id", "int", "not null"),
        ("i_partner_id", "int", "not null"),
        ("ti_current_hour", "tinyint", "not null"),
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
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "report_id_server_id_partner_id", "unique": True, "columns": ("i_report_id", "i_server_id", "i_partner_id", ) },
        ),
    }
tables.append(tableReportAPIPartnerValueLatest)

tableReportAPIPartnerValueLatest["dataObjectExtra"]="""
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
tableReportAPIPartnerValueLatest["sps"]=(
    {
        "spName": "GetReportAPIPartnerValueLatestsByReportID",
        "description": "Get report API partner value latests by report ID",
        "inputParameters": """@i_report_id           int""",
        "sqlQuery":
"""SELECT
        bi_sequence_id            AS 'sequenceID',
        i_report_id               AS 'reportID',
        i_server_id               AS 'serverID',
        i_partner_id              AS 'partnerID',
        ti_current_hour           AS 'currentHour',
        f_report_value_0          AS 'reportValue0',
        f_report_value_1          AS 'reportValue1',
        f_report_value_2          AS 'reportValue2',
        f_report_value_3          AS 'reportValue3',
        f_report_value_4          AS 'reportValue4',
        f_report_value_5          AS 'reportValue5',
        f_report_value_6          AS 'reportValue6',
        f_report_value_7          AS 'reportValue7',
        f_report_value_8          AS 'reportValue8',
        f_report_value_9          AS 'reportValue9',
        f_report_value_10         AS 'reportValue10',
        f_report_value_11         AS 'reportValue11',
        f_report_value_12         AS 'reportValue12',
        f_report_value_13         AS 'reportValue13',
        f_report_value_14         AS 'reportValue14',
        f_report_value_15         AS 'reportValue15',
        f_report_value_16         AS 'reportValue16',
        f_report_value_17         AS 'reportValue17',
        f_report_value_18         AS 'reportValue18',
        f_report_value_19         AS 'reportValue19',
        f_report_value_20         AS 'reportValue20',
        f_report_value_21         AS 'reportValue21',
        f_report_value_22         AS 'reportValue22',
        f_report_value_23         AS 'reportValue23',
        b_failed_0                AS 'failed0',
        b_failed_1                AS 'failed1',
        b_failed_2                AS 'failed2',
        b_failed_3                AS 'failed3',
        b_failed_4                AS 'failed4',
        b_failed_5                AS 'failed5',
        b_failed_6                AS 'failed6',
        b_failed_7                AS 'failed7',
        b_failed_8                AS 'failed8',
        b_failed_9                AS 'failed9',
        b_failed_10               AS 'failed10',
        b_failed_11               AS 'failed11',
        b_failed_12               AS 'failed12',
        b_failed_13               AS 'failed13',
        b_failed_14               AS 'failed14',
        b_failed_15               AS 'failed15',
        b_failed_16               AS 'failed16',
        b_failed_17               AS 'failed17',
        b_failed_18               AS 'failed18',
        b_failed_19               AS 'failed19',
        b_failed_20               AS 'failed20',
        b_failed_21               AS 'failed21',
        b_failed_22               AS 'failed22',
        b_failed_23               AS 'failed23',
        dt_inserted_datetime      AS 'insertedDateTime',
        dt_updated_datetime       AS 'updatedDateTime'
    FROM report_api_partner_value_latest WITH (FORCESEEK)
    WHERE i_report_id             = @i_report_id
    
    CHKERR({ERROR_GET_REPORT_API_PARTNER_VALUE_LATESTS_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "GetReportAPIPartnerValueLatestsByReportIDAndServerIDs",
        "description": "Get report API partner value latests by report ID and server IDs",
        "inputParameters":
"""@i_report_id           int,
    @vc_server_ids         varchar(8000)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_ids)
    SET @vc_server_ids = dbo.fnm_GetFilteredString{}VERSION_SUFFIX (@vc_server_ids)

    DECLARE @nvc_sql_query       nvarchar(max)

    SET @nvc_sql_query = '
        SELECT
            bi_sequence_id             AS ''sequenceID'',
            i_report_id                AS ''reportID'',
            i_server_id                AS ''serverID'',
            i_partner_id               AS ''partnerID'',
            ti_current_hour            AS ''currentHour'',
            f_report_value_0           AS ''reportValue0'',
            f_report_value_1           AS ''reportValue1'',
            f_report_value_2           AS ''reportValue2'',
            f_report_value_3           AS ''reportValue3'',
            f_report_value_4           AS ''reportValue4'',
            f_report_value_5           AS ''reportValue5'',
            f_report_value_6           AS ''reportValue6'',
            f_report_value_7           AS ''reportValue7'',
            f_report_value_8           AS ''reportValue8'',
            f_report_value_9           AS ''reportValue9'',
            f_report_value_10          AS ''reportValue10'',
            f_report_value_11          AS ''reportValue11'',
            f_report_value_12          AS ''reportValue12'',
            f_report_value_13          AS ''reportValue13'',
            f_report_value_14          AS ''reportValue14'',
            f_report_value_15          AS ''reportValue15'',
            f_report_value_16          AS ''reportValue16'',
            f_report_value_17          AS ''reportValue17'',
            f_report_value_18          AS ''reportValue18'',
            f_report_value_19          AS ''reportValue19'',
            f_report_value_20          AS ''reportValue20'',
            f_report_value_21          AS ''reportValue21'',
            f_report_value_22          AS ''reportValue22'',
            f_report_value_23          AS ''reportValue23'',
            b_failed_0                 AS ''failed0'',
            b_failed_1                 AS ''failed1'',
            b_failed_2                 AS ''failed2'',
            b_failed_3                 AS ''failed3'',
            b_failed_4                 AS ''failed4'',
            b_failed_5                 AS ''failed5'',
            b_failed_6                 AS ''failed6'',
            b_failed_7                 AS ''failed7'',
            b_failed_8                 AS ''failed8'',
            b_failed_9                 AS ''failed9'',
            b_failed_10                AS ''failed10'',
            b_failed_11                AS ''failed11'',
            b_failed_12                AS ''failed12'',
            b_failed_13                AS ''failed13'',
            b_failed_14                AS ''failed14'',
            b_failed_15                AS ''failed15'',
            b_failed_16                AS ''failed16'',
            b_failed_17                AS ''failed17'',
            b_failed_18                AS ''failed18'',
            b_failed_19                AS ''failed19'',
            b_failed_20                AS ''failed20'',
            b_failed_21                AS ''failed21'',
            b_failed_22                AS ''failed22'',
            b_failed_23                AS ''failed23'',
            dt_inserted_datetime       AS ''insertedDateTime'',
            dt_updated_datetime        AS ''updatedDateTime''
        FROM report_api_partner_value_latest WITH (FORCESEEK)
        WHERE i_report_id = @i_report_id
          AND i_server_id IN (' + @vc_server_ids + ')'
    EXEC sp_executesql @nvc_sql_query,
        N'@i_report_id int',
        @i_report_id = @i_report_id

    CHKERR({ERROR_GET_report_api_partner_value_latestS_BY_REPORT_ID_AND_SERVER_IDS})
    RETURN 0""",
    },
    {
        "spName": "DeleteReportAPIPartnerValueLatestsByReportID",
        "description": "Delete report API partner value latests by report ID",
        "inputParameters": """@i_report_id           int""",
        "sqlQuery":
"""TRANINIT

    DELETE FROM report_api_partner_value_latest
    WHERE i_report_id = @i_report_id
    
    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({ERROR_DELETE_REPORT_API_PARTNER_VALUE_LATESTS_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportAPIPartnerValueLatestsByServerID",
        "description": "Delete report API partner value latests by server ID",
        "inputParameters": """@i_server_id           int""",
        "sqlQuery":
"""TRANINIT

    DELETE FROM report_api_partner_value_latest
    WHERE i_server_id = @i_server_id
    
    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({ERROR_DELETE_REPORT_API_PARTNER_VALUE_LATESTS_BY_SERVER_ID})
    TRANRETURN""",
    },
    {
        "spName": "InsertOrUpdateReportAPIPartnerValueLatest",
        "description": "Insert or update report API partner value latest",
        "inputParameters":
"""@i_report_id                 int,
    @i_server_id                 int,
    @i_partner_id                int,
    @ti_current_hour             tinyint,
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
    @dt_updated_datetime         datetime""",
        "sqlQuery":
"""DECLARE @bi_sequence_id int
    SET @bi_sequence_id = 0

    TRANINIT
    
    SELECT @bi_sequence_id = bi_sequence_id
    FROM report_api_partner_value_latest WITH (FORCESEEK)
    WHERE i_report_id                 = @i_report_id
      AND i_server_id                 = @i_server_id
      AND i_partner_id                = @i_partner_id

    IF (@bi_sequence_id = 0)
    BEGIN
        INSERT INTO report_api_partner_value_latest
        (
            i_report_id,
            i_server_id,
            i_partner_id,
            ti_current_hour,
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
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @i_report_id,
            @i_server_id,
            @i_partner_id,
            @ti_current_hour,
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
            @dt_updated_datetime,
            @dt_updated_datetime
        )
        SELECT @@IDENTITY AS 'identity'
    END
    ELSE
    BEGIN
        UPDATE report_api_partner_value_latest
        SET
            ti_current_hour     = @ti_current_hour,
            f_report_value_0    = @f_report_value_0,
            f_report_value_1    = @f_report_value_1,
            f_report_value_2    = @f_report_value_2,
            f_report_value_3    = @f_report_value_3,
            f_report_value_4    = @f_report_value_4,
            f_report_value_5    = @f_report_value_5,
            f_report_value_6    = @f_report_value_6,
            f_report_value_7    = @f_report_value_7,
            f_report_value_8    = @f_report_value_8,
            f_report_value_9    = @f_report_value_9,
            f_report_value_10   = @f_report_value_10,
            f_report_value_11   = @f_report_value_11,
            f_report_value_12   = @f_report_value_12,
            f_report_value_13   = @f_report_value_13,
            f_report_value_14   = @f_report_value_14,
            f_report_value_15   = @f_report_value_15,
            f_report_value_16   = @f_report_value_16,
            f_report_value_17   = @f_report_value_17,
            f_report_value_18   = @f_report_value_18,
            f_report_value_19   = @f_report_value_19,
            f_report_value_20   = @f_report_value_20,
            f_report_value_21   = @f_report_value_21,
            f_report_value_22   = @f_report_value_22,
            f_report_value_23   = @f_report_value_23,
            b_failed_0          = @b_failed_0,
            b_failed_1          = @b_failed_1,
            b_failed_2          = @b_failed_2,
            b_failed_3          = @b_failed_3,
            b_failed_4          = @b_failed_4,
            b_failed_5          = @b_failed_5,
            b_failed_6          = @b_failed_6,
            b_failed_7          = @b_failed_7,
            b_failed_8          = @b_failed_8,
            b_failed_9          = @b_failed_9,
            b_failed_10         = @b_failed_10,
            b_failed_11         = @b_failed_11,
            b_failed_12         = @b_failed_12,
            b_failed_13         = @b_failed_13,
            b_failed_14         = @b_failed_14,
            b_failed_15         = @b_failed_15,
            b_failed_16         = @b_failed_16,
            b_failed_17         = @b_failed_17,
            b_failed_18         = @b_failed_18,
            b_failed_19         = @b_failed_19,
            b_failed_20         = @b_failed_20,
            b_failed_21         = @b_failed_21,
            b_failed_22         = @b_failed_22,
            b_failed_23         = @b_failed_23,
            dt_updated_datetime = @dt_updated_datetime
        WHERE bi_sequence_id = @bi_sequence_id
        SELECT @bi_sequence_id AS 'identity'
    END

    TRANCHKERR({ERROR_INSERT_OR_UPDATE_REPORT_API_PARTNER_VALUE_LATEST})
    TRANRETURN""",
    },
    )