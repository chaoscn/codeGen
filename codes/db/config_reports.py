tableConfigReports={
    "tableName": "config_reports",
    "columns": (
        ("i_report_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_report_hash_value", "varchar(128)", "NOT NULL"),
        ("i_hourly_partition_id", "int", "NOT NULL", "DEFAULT ((0))"),
        ("i_daily_partition_id", "int", "NOT NULL", "DEFAULT ((0))"),
        ("vc_report_name", "varchar(200)", "NOT NULL"),
        ("vc_report_short_name", "varchar(30)", "NOT NULL"),
        ("vc_report_description", "varchar(600)", "NULL"),
        ("i_report_type", "int", "NOT NULL"),
        ("x_report_data_source_xml", "xml", "NOT NULL"),
        ("x_report_setting_xml", "xml", "NOT NULL"),
        ("x_report_alert_xml", "xml", "NOT NULL"),
        ("dt_hourly_aggregated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_daily_aggregated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("i_user_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("b_report_public", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("b_report_ready", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "full_text_report_name", "fullText": True, "columns": ("vc_report_name", ) },
        { "indexName": "report_hash_value", "unique": True, "columns": ("vc_report_hash_value", ) },
        { "indexName": "report_type", "unique": False, "columns": ("i_report_type", ) },
        { "indexName": "report_ready", "unique": False, "columns": ("b_report_ready", ) },
        { "indexName": "report_id_hourly_partition_id", "unique": True, "columns": ("i_report_id", "i_hourly_partition_id", ) },
        { "indexName": "report_id_daily_partition_id", "unique": True, "columns": ("i_report_id", "i_daily_partition_id", ) },
        { "indexName": "hourly_aggregated_datetime", "unique": False, "columns": ("dt_hourly_aggregated_datetime", ) },
        { "indexName": "daily_aggregated_datetime", "unique": False, "columns": ("dt_daily_aggregated_datetime", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "xmlIgnores": (
        "x_report_data_source_xml",
        "x_report_setting_xml",
        "x_report_alert_xml",
        ),
    }
tables.append(tableConfigReports)

tableConfigReports["sps"]=(
    {
        "spName": "GetReportByReportID",
        "description": "Get report by report ID",
        "inputParameters": 
"""@i_user_id             int,
    @i_report_id           int""",
        "sqlQuery":
"""SELECT
        i_report_id                   AS 'reportID',
        vc_report_hash_value          AS 'reportHashValue',
        i_hourly_partition_id         AS 'hourlyPartitionID',
        i_daily_partition_id          AS 'dailyPartitionID',
        vc_report_name                AS 'reportName',
        vc_report_short_name          AS 'reportShortName',
        vc_report_description         AS 'reportDescription',
        i_report_type                 AS 'reportType',
        x_report_data_source_xml      AS 'reportDataSourceXml',
        x_report_setting_xml          AS 'reportSettingXml',
        x_report_alert_xml            AS 'reportAlertXml',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
        i_user_count                  AS 'userCount',
        b_report_public               AS 'reportPublic',
        b_report_ready                AS 'reportReady',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime',
        CASE
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WITH (FORCESEEK) WHERE i_report_id = @i_report_id AND i_user_id = @i_user_id AND b_report_owner = 0) THEN 1
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WITH (FORCESEEK) WHERE i_report_id = @i_report_id AND i_user_id = @i_user_id AND b_report_owner = 1) THEN 2
            ELSE 0
        END AS 'userOwnership'
    FROM config_reports
    WHERE i_report_id                 = @i_report_id
    
    CHKERR({ERROR_GET_REPORT_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAllNotReadyReports",
        "description": "Get all not ready reports",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_report_id                   AS 'reportID',
        vc_report_hash_value          AS 'reportHashValue',
        i_hourly_partition_id         AS 'hourlyPartitionID',
        i_daily_partition_id          AS 'dailyPartitionID',
        vc_report_name                AS 'reportName',
        vc_report_short_name          AS 'reportShortName',
        vc_report_description         AS 'reportDescription',
        i_report_type                 AS 'reportType',
        x_report_data_source_xml      AS 'reportDataSourceXml',
        x_report_setting_xml          AS 'reportSettingXml',
        x_report_alert_xml            AS 'reportAlertXml',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
        i_user_count                  AS 'userCount',
        b_report_public               AS 'reportPublic',
        b_report_ready                AS 'reportReady',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_reports WITH (FORCESEEK)
    WHERE b_report_ready              = 0
    
    CHKERR({ERROR_GET_ALL_NOT_READY_REPORTS})
    RETURN 0""",
    },
    {
        "spName": "CountReportsByUserID",
        "description": "Count reports by user ID",
        "inputParameters":
"""@i_user_id           int""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount' FROM user_report_settings WHERE i_user_id = @i_user_id

    CHKERR({ERROR_COUNT_REPORTS_BY_USER_ID})
    RETURN 0""",
    },
    {
        "spName": "CountReportsByHashValue",
        "description": "Count reports by hash value",
        "inputParameters":
"""@vc_report_hash_value           varchar(128)""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount' FROM config_reports WITH (FORCESEEK) WHERE vc_report_hash_value = @vc_report_hash_value

    CHKERR({ERROR_COUNT_REPORTS_BY_HASH_VALUE})
    RETURN 0""",
    },
    {
        "spName": "GetPagedReportsByUserIDOrderByDateTimeDesc",
        "description": "Get paged reports by user ID order by datetime desc",
        "inputParameters": 
"""@i_user_id           int,
    @i_page_number         int,
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
            A.i_report_id                   AS 'reportID',
            A.vc_report_hash_value          AS 'reportHashValue',
            A.i_hourly_partition_id         AS 'hourlyPartitionID',
            A.i_daily_partition_id          AS 'dailyPartitionID',
            A.vc_report_name                AS 'reportName',
            A.vc_report_short_name          AS 'reportShortName',
            A.vc_report_description         AS 'reportDescription',
            A.i_report_type                 AS 'reportType',
            A.x_report_data_source_xml      AS 'reportDataSourceXml',
            A.x_report_setting_xml          AS 'reportSettingXml',
            A.x_report_alert_xml            AS 'reportAlertXml',
            A.dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
            A.dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
            A.i_user_count                  AS 'userCount',
            A.b_report_public               AS 'reportPublic',
            A.b_report_ready                AS 'reportReady',
            A.vc_updated_by                 AS 'updatedBy',
            A.dt_inserted_datetime          AS 'insertedDateTime',
            A.dt_updated_datetime           AS 'updatedDateTime',
            CASE
                WHEN B.b_report_owner = 0 THEN 1
                WHEN B.b_report_owner = 1 THEN 2
                ELSE 0
            END AS 'userOwnership',
            ROW_NUMBER() OVER (ORDER BY A.dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_reports A WITH (FORCESEEK), user_report_settings B WITH (FORCESEEK)
        WHERE A.i_report_id = B.i_report_id
          AND B.i_user_id   = @i_user_id
        ORDER BY A.dt_inserted_datetime DESC
    ) C
    WHERE C.rowNumber > @i_max_rowcount - @i_page_size AND C.rowNumber <= @i_max_rowcount
    ORDER BY C.rowNumber

    CHKERR({ERROR_GET_PAGED_REPORTS_BY_USER_ID_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "GetPagedReportsByReportIDOrderByReportID",
        "description": "Get paged reports by report ID order by report ID",
        "inputParameters": 
"""@i_report_id           int,
    @i_page_size           int""",
        "sqlQuery":
"""IF (@i_page_size<0 OR @i_page_size>5000)
        RAISERROR('Page size is invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    SELECT TOP (@i_page_size)
        i_report_id                   AS 'reportID',
        vc_report_hash_value          AS 'reportHashValue',
        i_hourly_partition_id         AS 'hourlyPartitionID',
        i_daily_partition_id          AS 'dailyPartitionID',
        vc_report_name                AS 'reportName',
        vc_report_short_name          AS 'reportShortName',
        vc_report_description         AS 'reportDescription',
        i_report_type                 AS 'reportType',
        x_report_data_source_xml      AS 'reportDataSourceXml',
        x_report_setting_xml          AS 'reportSettingXml',
        x_report_alert_xml            AS 'reportAlertXml',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
        i_user_count                  AS 'userCount',
        b_report_public               AS 'reportPublic',
        b_report_ready                AS 'reportReady',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_reports
    WHERE i_report_id                 > @i_report_id
    ORDER BY i_report_id ASC
    
    CHKERR({ERROR_GET_PAGED_REPORTS_BY_REPORT_ID_ORDER_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPagedReportsOrderByDateTimeDesc",
        "description": "Get paged reports order by datetime desc",
        "inputParameters": 
"""@i_user_id                   int,
    @i_page_number               int,
    @i_page_size                 int""",
        "sqlQuery":
"""IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT
        *,
        CASE
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WHERE i_report_id = reportID AND i_user_id = @i_user_id AND b_report_owner = 0) THEN 1
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WHERE i_report_id = reportID AND i_user_id = @i_user_id AND b_report_owner = 1) THEN 2
            ELSE 0
        END AS 'userOwnership'
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_report_id                   AS 'reportID',
            vc_report_hash_value          AS 'reportHashValue',
            i_hourly_partition_id         AS 'hourlyPartitionID',
            i_daily_partition_id          AS 'dailyPartitionID',
            vc_report_name                AS 'reportName',
            vc_report_short_name          AS 'reportShortName',
            vc_report_description         AS 'reportDescription',
            i_report_type                 AS 'reportType',
            x_report_data_source_xml      AS 'reportDataSourceXml',
            x_report_setting_xml          AS 'reportSettingXml',
            x_report_alert_xml            AS 'reportAlertXml',
            dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
            dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
            i_user_count                  AS 'userCount',
            b_report_public               AS 'reportPublic',
            b_report_ready                AS 'reportReady',
            vc_updated_by                 AS 'updatedBy',
            dt_inserted_datetime          AS 'insertedDateTime',
            dt_updated_datetime           AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_reports
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_GET_PAGED_REPORTS_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "CountReports",
        "description": "Count reports",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount'
    FROM config_reports

    CHKERR({ERROR_COUNT_REPORTS})
    RETURN 0""",
    },
    {
        "spName": "CountReportsBySearchCriteria",
        "description": "Count reports by search criteria",
        "inputParameters":
"""@vc_search_criteria           varchar(400)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    SELECT COUNT(1) AS 'rowcount'
    FROM config_reports
    WHERE CONTAINS(vc_report_name, @vc_search_criteria)

    CHKERR({ERROR_COUNT_REPORTS_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "SearchReportsBySearchCriteria",
        "description": "Search reports by search criteria",
        "inputParameters":
"""@i_user_id                int,
    @vc_search_criteria       varchar(400),
    @i_page_number            int,
    @i_page_size              int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT
        *,
        CASE
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WHERE i_report_id = reportID AND i_user_id = @i_user_id AND b_report_owner = 0) THEN 1
            WHEN EXISTS (SELECT 'X' FROM user_report_settings WHERE i_report_id = reportID AND i_user_id = @i_user_id AND b_report_owner = 1) THEN 2
            ELSE 0
        END AS 'userOwnership'
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_report_id                   AS 'reportID',
            vc_report_hash_value          AS 'reportHashValue',
            i_hourly_partition_id         AS 'hourlyPartitionID',
            i_daily_partition_id          AS 'dailyPartitionID',
            vc_report_name                AS 'reportName',
            vc_report_short_name          AS 'reportShortName',
            vc_report_description         AS 'reportDescription',
            i_report_type                 AS 'reportType',
            x_report_data_source_xml      AS 'reportDataSourceXml',
            x_report_setting_xml          AS 'reportSettingXml',
            x_report_alert_xml            AS 'reportAlertXml',
            dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
            dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
            i_user_count                  AS 'userCount',
            b_report_public               AS 'reportPublic',
            b_report_ready                AS 'reportReady',
            vc_updated_by                 AS 'updatedBy',
            dt_inserted_datetime          AS 'insertedDateTime',
            dt_updated_datetime           AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_reports
        WHERE CONTAINS(vc_report_name, @vc_search_criteria)
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_SEARCH_REPORTS_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "CountReportsByUserIDAndSearchCriteria",
        "description": "Count reports by user ID and search criteria",
        "inputParameters":
"""@i_user_id                int,
    @vc_search_criteria       varchar(400)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    SELECT COUNT(A.i_report_id) AS 'rowcount'
    FROM config_reports A, user_report_settings B
    WHERE CONTAINS(A.vc_report_name, @vc_search_criteria)
      AND A.i_report_id = B.i_report_id
      AND B.i_user_id   = @i_user_id

    CHKERR({ERROR_COUNT_REPORTS_BY_USER_ID_AND_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "SearchReportsByUserIDAndSearchCriteria",
        "description": "Search reports by user ID and search criteria",
        "inputParameters":
"""@i_user_id                int,
    @vc_search_criteria       varchar(400),
    @i_page_number            int,
    @i_page_size              int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            A.i_report_id                   AS 'reportID',
            A.vc_report_hash_value          AS 'reportHashValue',
            A.i_hourly_partition_id         AS 'hourlyPartitionID',
            A.i_daily_partition_id          AS 'dailyPartitionID',
            A.vc_report_name                AS 'reportName',
            A.vc_report_short_name          AS 'reportShortName',
            A.vc_report_description         AS 'reportDescription',
            A.i_report_type                 AS 'reportType',
            A.x_report_data_source_xml      AS 'reportDataSourceXml',
            A.x_report_setting_xml          AS 'reportSettingXml',
            A.x_report_alert_xml            AS 'reportAlertXml',
            A.dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
            A.dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
            A.i_user_count                  AS 'userCount',
            A.b_report_public               AS 'reportPublic',
            A.b_report_ready                AS 'reportReady',
            A.vc_updated_by                 AS 'updatedBy',
            A.dt_inserted_datetime          AS 'insertedDateTime',
            A.dt_updated_datetime           AS 'updatedDateTime',
            CASE
                WHEN B.b_report_owner = 0 THEN 1
                WHEN B.b_report_owner = 1 THEN 2
                ELSE 0
            END AS 'userOwnership',
            ROW_NUMBER() OVER (ORDER BY A.dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_reports A, user_report_settings B
        WHERE CONTAINS(A.vc_report_name, @vc_search_criteria)
          AND A.i_report_id = B.i_report_id
          AND B.i_user_id   = @i_user_id
        ORDER BY A.dt_inserted_datetime DESC
    ) C
    WHERE C.rowNumber > @i_max_rowcount - @i_page_size AND C.rowNumber <= @i_max_rowcount
    ORDER BY C.rowNumber

    CHKERR({ERROR_SEARCH_REPORTS_BY_USER_ID_AND_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "GetAllRecommendedReports",
        "description": "Get all recommended reports",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        A.i_report_id                   AS 'reportID',
        A.vc_report_hash_value          AS 'reportHashValue',
        A.i_hourly_partition_id         AS 'hourlyPartitionID',
        A.i_daily_partition_id          AS 'dailyPartitionID',
        A.vc_report_name                AS 'reportName',
        A.vc_report_short_name          AS 'reportShortName',
        A.vc_report_description         AS 'reportDescription',
        A.i_report_type                 AS 'reportType',
        A.x_report_data_source_xml      AS 'reportDataSourceXml',
        A.x_report_setting_xml          AS 'reportSettingXml',
        A.x_report_alert_xml            AS 'reportAlertXml',
        A.dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
        A.dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
        A.i_user_count                  AS 'userCount',
        A.b_report_public               AS 'reportPublic',
        A.b_report_ready                AS 'reportReady',
        A.vc_updated_by                 AS 'updatedBy',
        A.dt_inserted_datetime          AS 'insertedDateTime',
        A.dt_updated_datetime           AS 'updatedDateTime'
    FROM config_reports A, config_recommended_reports B WITH (FORCESEEK)
    WHERE A.i_report_id = B.i_report_id
    ORDER BY B.i_recommended_report_id

    CHKERR({ERROR_GET_ALL_RECOMMENDED_REPORTS})
    RETURN 0""",
    },
    {
        "spName": "CountRecommendedReports",
        "description": "Count recommended reports",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount' FROM config_recommended_reports

    CHKERR({ERROR_COUNT_RECOMMENDED_REPORTS})
    RETURN 0""",
    },
    {
        "spName": "GetPagedRecommendedReports",
        "description": "Get paged recommended reports",
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
            A.i_report_id                   AS 'reportID',
            A.vc_report_hash_value          AS 'reportHashValue',
            A.i_hourly_partition_id         AS 'hourlyPartitionID',
            A.i_daily_partition_id          AS 'dailyPartitionID',
            A.vc_report_name                AS 'reportName',
            A.vc_report_short_name          AS 'reportShortName',
            A.vc_report_description         AS 'reportDescription',
            A.i_report_type                 AS 'reportType',
            A.x_report_data_source_xml      AS 'reportDataSourceXml',
            A.x_report_setting_xml          AS 'reportSettingXml',
            A.x_report_alert_xml            AS 'reportAlertXml',
            A.dt_hourly_aggregated_datetime AS 'hourlyAggregatedDateTime',
            A.dt_daily_aggregated_datetime  AS 'dailyAggregatedDateTime',
            A.i_user_count                  AS 'userCount',
            A.b_report_public               AS 'reportPublic',
            A.b_report_ready                AS 'reportReady',
            A.vc_updated_by                 AS 'updatedBy',
            A.dt_inserted_datetime          AS 'insertedDateTime',
            A.dt_updated_datetime           AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY B.i_recommended_report_id DESC) AS 'rowNumber'
        FROM config_reports A, config_recommended_reports B WITH (FORCESEEK)
        WHERE A.i_report_id = B.i_report_id
        ORDER BY B.i_recommended_report_id
    ) C
    WHERE C.rowNumber > @i_max_rowcount - @i_page_size AND C.rowNumber <= @i_max_rowcount
    ORDER BY C.rowNumber

    CHKERR({ERROR_GET_PAGED_RECOMMENDED_REPORTS})
    RETURN 0""",
    },
    {
        "spName": "InsertReport",
        "description": "Insert report",
        "inputParameters":
"""@vc_report_hash_value           varchar(128),
    @vc_report_name                 varchar(200),
    @vc_report_short_name           varchar(30),
    @vc_report_description          varchar(600),
    @i_report_type                  int,
    @x_report_data_source_xml       xml,
    @x_report_setting_xml           xml,
    @x_report_alert_xml             xml,
    @dt_hourly_aggregated_datetime  datetime,
    @dt_daily_aggregated_datetime   datetime,
    @b_report_public                bit,
    @b_report_ready                 bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_report_hash_value)
    CHECK_NOTNULL(@vc_report_name)
    CHECK_NOTNULL(@vc_report_short_name)
    CHECK_NOTNULL(@x_report_data_source_xml)
    CHECK_NOTNULL(@x_report_setting_xml)
    CHECK_NOTNULL(@x_report_alert_xml)
    CHECK_NOTNULL(@dt_hourly_aggregated_datetime)
    CHECK_NOTNULL(@dt_daily_aggregated_datetime)

    TRANINIT
    
    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_reports
        WHERE vc_report_hash_value = @vc_report_hash_value
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        DECLARE @i_hourly_partition_id      int
        DECLARE @i_daily_partition_id       int

        SELECT TOP 1 @i_hourly_partition_id = i_partition_id
        FROM config_report_partitions WITH (UPDLOCK)
        WHERE i_partition_type = 0
        ORDER BY i_report_count ASC, i_partition_id ASC

        SELECT TOP 1 @i_daily_partition_id = i_partition_id
        FROM config_report_partitions WITH (UPDLOCK)
        WHERE i_partition_type = 1
        ORDER BY i_report_count ASC, i_partition_id ASC

        UPDATE config_report_partitions
        SET i_report_count = i_report_count + 1
        WHERE (i_partition_type = 0 AND i_partition_id = @i_hourly_partition_id)
           OR (i_partition_type = 1 AND i_partition_id = @i_daily_partition_id)

        INSERT INTO config_reports
        (
            vc_report_hash_value,
            i_hourly_partition_id,
            i_daily_partition_id,
            vc_report_name,
            vc_report_short_name,
            vc_report_description,
            i_report_type,
            x_report_data_source_xml,
            x_report_setting_xml,
            x_report_alert_xml,
            dt_hourly_aggregated_datetime,
            dt_daily_aggregated_datetime,
            i_user_count,
            b_report_public,
            b_report_ready,
            vc_updated_by,
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @vc_report_hash_value,
            @i_hourly_partition_id,
            @i_daily_partition_id,
            @vc_report_name,
            @vc_report_short_name,
            @vc_report_description,
            @i_report_type,
            @x_report_data_source_xml,
            @x_report_setting_xml,
            @x_report_alert_xml,
            @dt_hourly_aggregated_datetime,
            @dt_daily_aggregated_datetime,
            0,
            @b_report_public,
            @b_report_ready,
            SYSTEM_USER,
            GETUTCDATE(),
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END
    
    TRANCHKERR({ERROR_INSERT_REPORT})
    TRANRETURN""",
    },
    {
        "spName": "UpdateReportByReportID",
        "description": "Update report by report ID",
        "inputParameters": 
"""@i_report_id                      int,
    @vc_report_hash_value             varchar(128),
    @i_hourly_partition_id            int,
    @i_daily_partition_id             int,
    @vc_report_name                   varchar(200),
    @vc_report_short_name             varchar(30),
    @vc_report_description            varchar(600),
    @i_report_type                    int,
    @x_report_data_source_xml         xml,
    @x_report_setting_xml             xml,
    @x_report_alert_xml               xml,
    @dt_hourly_aggregated_datetime    datetime,
    @dt_daily_aggregated_datetime     datetime,
    @b_report_public                  bit,
    @b_report_ready                   bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_report_hash_value)
    CHECK_NOTNULL(@vc_report_name)
    CHECK_NOTNULL(@vc_report_short_name)
    CHECK_NOTNULL(@x_report_data_source_xml)
    CHECK_NOTNULL(@x_report_setting_xml)
    CHECK_NOTNULL(@x_report_alert_xml)
    CHECK_NOTNULL(@dt_hourly_aggregated_datetime)
    CHECK_NOTNULL(@dt_daily_aggregated_datetime)

    TRANINIT

    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_reports (UPDLOCK)
        WHERE i_report_id             = @i_report_id
    )
    BEGIN
        IF EXISTS
        (
            SELECT TOP 1 'x'
            FROM config_reports WITH (FORCESEEK)
            WHERE vc_report_hash_value = @vc_report_hash_value
              AND i_report_id          <> @i_report_id
        )
        BEGIN
            SELECT 0 AS 'rowcount'
        END
        ELSE
        BEGIN
            UPDATE config_reports
            SET
                vc_report_hash_value          = @vc_report_hash_value,
                i_hourly_partition_id         = @i_hourly_partition_id,
                i_daily_partition_id          = @i_daily_partition_id,
                vc_report_name                = @vc_report_name,
                vc_report_short_name          = @vc_report_short_name,
                vc_report_description         = @vc_report_description,
                i_report_type                 = @i_report_type,
                x_report_data_source_xml      = @x_report_data_source_xml,
                x_report_setting_xml          = @x_report_setting_xml,
                x_report_alert_xml            = @x_report_alert_xml,
                dt_hourly_aggregated_datetime = @dt_hourly_aggregated_datetime,
                dt_daily_aggregated_datetime  = @dt_daily_aggregated_datetime,
                b_report_public               = @b_report_public,
                b_report_ready                = @b_report_ready,
                vc_updated_by                 = SYSTEM_USER,
                dt_updated_datetime           = GETUTCDATE()
            WHERE i_report_id                 = @i_report_id

            SELECT @@ROWCOUNT AS 'rowcount'
        END
    END
    ELSE
    BEGIN
        SELECT 0 AS 'rowcount'
    END
    
    TRANCHKERR({ERROR_UPDATE_REPORT_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteReportByReportID",
        "description": "Delete report by report ID",
        "inputParameters": 
"""@i_report_id int""",
        "sqlQuery":
"""TRANINIT

    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_reports (UPDLOCK)
        WHERE i_report_id = @i_report_id
    )
    BEGIN
        IF EXISTS
        (
            SELECT i_user_id
            FROM users (UPDLOCK)
            WHERE i_user_id IN (SELECT i_user_id FROM user_report_settings (UPDLOCK) WHERE i_report_id = @i_report_id)
        )
        BEGIN
            UPDATE users
            SET i_report_count = i_report_count - 1
            WHERE i_user_id IN (SELECT i_user_id FROM user_report_settings (UPDLOCK) WHERE i_report_id = @i_report_id)

            DELETE FROM user_report_settings
            WHERE i_report_id = @i_report_id
        END

        DECLARE @i_hourly_partition_id      int
        DECLARE @i_daily_partition_id       int

        SELECT
            @i_hourly_partition_id = i_hourly_partition_id,
            @i_daily_partition_id  = i_daily_partition_id
        FROM config_reports (UPDLOCK)
        WHERE i_report_id             = @i_report_id

        DELETE FROM config_recommended_reports
        WHERE i_report_id = @i_report_id

        DELETE FROM config_reports
        WHERE i_report_id = @i_report_id

        SELECT @@ROWCOUNT AS 'rowcount'

        UPDATE config_report_partitions
        SET i_report_count = i_report_count - 1
        WHERE (i_partition_type = 0 AND i_partition_id = @i_hourly_partition_id)
           OR (i_partition_type = 1 AND i_partition_id = @i_daily_partition_id)

    END
    ELSE
    BEGIN
        SELECT 0 AS 'rowcount'
    END
    
    TRANCHKERR({ERROR_DELETE_REPORT_BY_REPORT_ID})
    TRANRETURN""",
    },
    )