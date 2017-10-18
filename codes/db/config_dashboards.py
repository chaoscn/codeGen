tableConfigDashboards={
    "tableName": "config_dashboards",
    "columns": (
        ("i_dashboard_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_user_id", "int", "NOT NULL"),
        ("vc_dashboard_hash_value", "varchar(128)", "NOT NULL"),
        ("vc_dashboard_name", "varchar(200)", "NOT NULL"),
        ("vc_dashboard_short_name", "varchar(30)", "NOT NULL"),
        ("vc_dashboard_description", "varchar(600)", "NULL"),
        ("i_dashboard_type", "int", "NOT NULL"),
        ("x_dashboard_setting_xml", "xml", "NOT NULL"),
        ("i_report_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("b_dashboard_public", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_id", "unique": False, "columns": ("i_user_id", ) },
        { "indexName": "dashboard_hash_value", "unique": True, "columns": ("vc_dashboard_hash_value", ) },
        { "indexName": "full_text_dashboard_name", "fullText": True, "columns": ("vc_dashboard_name", ) },
        { "indexName": "dashboard_type", "unique": False, "columns": ("i_dashboard_type", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_user_id", "foreignTableName": "users", "foreignColumnName": "i_user_id", },
        ),
    "xmlIgnores": (
        "x_dashboard_setting_xml",
        ),
    }
    
tables.append(tableConfigDashboards)

tableConfigDashboards["sps"]=(
    {
        "spName": "GetDashboardByDashboardID",
        "description": "Get dashboard by dashboard ID",
        "inputParameters":
"""@i_dashboard_id          int""",
        "sqlQuery":
"""SELECT
        i_dashboard_id             AS 'dashboardID',
        i_user_id                  AS 'userID',
        vc_dashboard_hash_value    AS 'dashboardHashValue',
        vc_dashboard_name          AS 'dashboardName',
        vc_dashboard_short_name    AS 'dashboardShortName',
        vc_dashboard_description   AS 'dashboardDescription',
        i_dashboard_type           AS 'dashboardType',
        x_dashboard_setting_xml    AS 'dashboardSettingXml',
        i_report_count             AS 'reportCount',
        b_dashboard_public         AS 'dashboardPublic',
        vc_updated_by              AS 'updatedBy',
        dt_inserted_datetime       AS 'insertedDateTime',
        dt_updated_datetime        AS 'updatedDateTime'
    FROM config_dashboards
    WHERE i_dashboard_id       = @i_dashboard_id
    
    CHKERR({ERROR_GET_DASHBOARD_BY_DASHBOARD_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPagedDashboardsOrderByDateTimeDesc",
        "description": "Get paged dashboards order by datetime desc",
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
        *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_dashboard_id             AS 'dashboardID',
            i_user_id                  AS 'userID',
            vc_dashboard_hash_value    AS 'dashboardHashValue',
            vc_dashboard_name          AS 'dashboardName',
            vc_dashboard_short_name    AS 'dashboardShortName',
            vc_dashboard_description   AS 'dashboardDescription',
            i_dashboard_type           AS 'dashboardType',
            x_dashboard_setting_xml    AS 'dashboardSettingXml',
            i_report_count             AS 'reportCount',
            b_dashboard_public         AS 'dashboardPublic',
            vc_updated_by              AS 'updatedBy',
            dt_inserted_datetime       AS 'insertedDateTime',
            dt_updated_datetime        AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_dashboards
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_GET_PAGED_DASHBOARDS_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "GetPagedDashboardsByUserIDOrderByDateTimeDesc",
        "description": "Get paged dashboards by user ID order by datetime desc",
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

    SELECT
        *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_dashboard_id             AS 'dashboardID',
            i_user_id                  AS 'userID',
            vc_dashboard_hash_value    AS 'dashboardHashValue',
            vc_dashboard_name          AS 'dashboardName',
            vc_dashboard_short_name    AS 'dashboardShortName',
            vc_dashboard_description   AS 'dashboardDescription',
            i_dashboard_type           AS 'dashboardType',
            x_dashboard_setting_xml    AS 'dashboardSettingXml',
            i_report_count             AS 'reportCount',
            b_dashboard_public         AS 'dashboardPublic',
            vc_updated_by              AS 'updatedBy',
            dt_inserted_datetime       AS 'insertedDateTime',
            dt_updated_datetime        AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_dashboards WITH (FORCESEEK)
        WHERE i_user_id   = @i_user_id
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_GET_PAGED_DASHBOARDS_BY_USER_ID_ORDER_BY_DATETIME_DESC})
    RETURN 0""",
    },
    {
        "spName": "SearchDashboardsBySearchCriteria",
        "description": "Search dashboards by search criteria",
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
        *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_dashboard_id             AS 'dashboardID',
            i_user_id                  AS 'userID',
            vc_dashboard_hash_value    AS 'dashboardHashValue',
            vc_dashboard_name          AS 'dashboardName',
            vc_dashboard_short_name    AS 'dashboardShortName',
            vc_dashboard_description   AS 'dashboardDescription',
            i_dashboard_type           AS 'dashboardType',
            x_dashboard_setting_xml    AS 'dashboardSettingXml',
            i_report_count             AS 'reportCount',
            b_dashboard_public         AS 'dashboardPublic',
            vc_updated_by              AS 'updatedBy',
            dt_inserted_datetime       AS 'insertedDateTime',
            dt_updated_datetime        AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_dashboards
        WHERE CONTAINS(vc_dashboard_name, @vc_search_criteria)
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_SEARCH_DASHBOARDS_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "SearchDashboardsByUserIDAndSearchCriteria",
        "description": "Search dashboards by user ID and search criteria",
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
        *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_dashboard_id             AS 'dashboardID',
            i_user_id                  AS 'userID',
            vc_dashboard_hash_value    AS 'dashboardHashValue',
            vc_dashboard_name          AS 'dashboardName',
            vc_dashboard_short_name    AS 'dashboardShortName',
            vc_dashboard_description   AS 'dashboardDescription',
            i_dashboard_type           AS 'dashboardType',
            x_dashboard_setting_xml    AS 'dashboardSettingXml',
            i_report_count             AS 'reportCount',
            b_dashboard_public         AS 'dashboardPublic',
            vc_updated_by              AS 'updatedBy',
            dt_inserted_datetime       AS 'insertedDateTime',
            dt_updated_datetime        AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_dashboards
        WHERE CONTAINS(vc_dashboard_name, @vc_search_criteria)
          AND i_user_id   = @i_user_id
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_SEARCH_DASHBOARDS_BY_USER_ID_AND_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "CountDashboardsByHashValue",
        "description": "Count dashboards by hash value",
        "inputParameters":
"""@vc_dashboard_hash_value           varchar(128)""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount' FROM config_dashboards WITH (FORCESEEK) WHERE vc_dashboard_hash_value = @vc_dashboard_hash_value

    CHKERR({ERROR_COUNT_DASHBOARDS_BY_HASH_VALUE})
    RETURN 0""",
    },
    {
        "spName": "CountDashboards",
        "description": "Count dashboards",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount'
    FROM config_dashboards

    CHKERR({ERROR_COUNT_DASHBOARDS})
    RETURN 0""",
    },
    {
        "spName": "CountDashboardsByUserID",
        "description": "Count dashboards by user ID",
        "inputParameters":
"""@i_user_id           int""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount' FROM config_dashboards WITH (FORCESEEK) WHERE i_user_id = @i_user_id

    CHKERR({ERROR_COUNT_DASHBOARDS_BY_USER_ID})
    RETURN 0""",
    },
    {
        "spName": "CountDashboardsBySearchCriteria",
        "description": "Count dashboards by search criteria",
        "inputParameters":
"""@vc_search_criteria           varchar(400)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    SELECT COUNT(1) AS 'rowcount'
    FROM config_dashboards
    WHERE CONTAINS(vc_dashboard_name, @vc_search_criteria)

    CHKERR({ERROR_COUNT_DASHBOARDS_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "CountDashboardsByUserIDAndSearchCriteria",
        "description": "Count dashboards by user ID and search criteria",
        "inputParameters":
"""@i_user_id                int,
    @vc_search_criteria       varchar(400)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    SELECT COUNT(1) AS 'rowcount'
    FROM config_dashboards
    WHERE CONTAINS(vc_dashboard_name, @vc_search_criteria)
      AND i_user_id   = @i_user_id

    CHKERR({ERROR_COUNT_DASHBOARDS_BY_USER_ID_AND_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "InsertDashboard",
        "description": "Insert dashboard",
        "inputParameters":
"""@i_user_id                         int,
    @vc_dashboard_hash_value           varchar(128),
    @vc_dashboard_name                 varchar(200),
    @vc_dashboard_short_name           varchar(30),
    @vc_dashboard_description          varchar(600),
    @i_dashboard_type                  int,
    @x_dashboard_setting_xml           xml,
    @i_report_count                    int,
    @b_dashboard_public                bit""",
    
        "sqlQuery":
"""CHECK_NOTNULL(@vc_dashboard_hash_value)
    CHECK_NOTNULL(@vc_dashboard_name)
    CHECK_NOTNULL(@vc_dashboard_short_name)
    CHECK_NOTNULL(@x_dashboard_setting_xml)

    TRANINIT
    
    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_dashboards WITH (FORCESEEK)
        WHERE vc_dashboard_hash_value = @vc_dashboard_hash_value
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        INSERT INTO config_dashboards
        (
            i_user_id,
            vc_dashboard_hash_value,
            vc_dashboard_name,
            vc_dashboard_short_name,
            vc_dashboard_description,
            i_dashboard_type,
            x_dashboard_setting_xml,
            i_report_count,
            b_dashboard_public,
            vc_updated_by,
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @i_user_id,
            @vc_dashboard_hash_value,
            @vc_dashboard_name,
            @vc_dashboard_short_name,
            @vc_dashboard_description,
            @i_dashboard_type,
            @x_dashboard_setting_xml,
            @i_report_count,
            @b_dashboard_public,
            SYSTEM_USER,
            GETUTCDATE(),
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END

    TRANCHKERR({ERROR_INSERT_DASHBOARD})
    TRANRETURN""",
    },
    {
        "spName": "UpdateDashboard",
        "description": "Update dashboard",
        "inputParameters": 
"""@i_dashboard_id                    int,
    @i_user_id                         int,
    @vc_dashboard_hash_value           varchar(128),
    @vc_dashboard_name                 varchar(200),
    @vc_dashboard_short_name           varchar(30),
    @vc_dashboard_description          varchar(600),
    @i_dashboard_type                  int,
    @x_dashboard_setting_xml           xml,
    @i_report_count                    int,
    @b_dashboard_public                bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_dashboard_hash_value)
    CHECK_NOTNULL(@vc_dashboard_name)
    CHECK_NOTNULL(@vc_dashboard_short_name)
    CHECK_NOTNULL(@x_dashboard_setting_xml)

    TRANINIT

    IF EXISTS
    (
        SELECT TOP 1 'x'
        FROM config_dashboards WITH (FORCESEEK)
        WHERE vc_dashboard_hash_value = @vc_dashboard_hash_value
          AND i_dashboard_id          <> @i_dashboard_id
    )
    BEGIN
        SELECT 0 AS 'rowcount'
    END
    ELSE
    BEGIN
        UPDATE config_dashboards
        SET
            i_user_id                        = @i_user_id,
            vc_dashboard_hash_value          = @vc_dashboard_hash_value,
            vc_dashboard_name                = @vc_dashboard_name,
            vc_dashboard_short_name          = @vc_dashboard_short_name,
            vc_dashboard_description         = @vc_dashboard_description,
            i_dashboard_type                 = @i_dashboard_type,
            x_dashboard_setting_xml          = @x_dashboard_setting_xml,
            i_report_count                   = @i_report_count,
            b_dashboard_public               = @b_dashboard_public,
            vc_updated_by                    = SYSTEM_USER,
            dt_updated_datetime              = GETUTCDATE()
        WHERE i_dashboard_id                 = @i_dashboard_id
        
        SELECT @@ROWCOUNT AS 'rowcount'
    END

    TRANCHKERR({ERROR_UPDATE_DASHBOARD})
    TRANRETURN""",
    },
    )