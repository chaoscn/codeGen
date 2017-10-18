tableConfigDashboardGroups={
    "tableName": "config_dashboard_groups",
    "columns": (
        ("i_dashboard_group_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_dashboard_group_name", "varchar(200)", "NOT NULL"),
        ("vc_dashboard_group_description", "varchar(600)", "NOT NULL"),
        ("x_dashboard_group_setting_xml", "xml", "NOT NULL"),
        ("i_dashboard_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("i_user_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "xmlIgnores": (
        "x_dashboard_group_setting_xml",
        ),
    }

tables.append(tableConfigDashboardGroups)

tableConfigDashboardGroups["sps"]=(
    {
        "spName": "GetDashboardGroupByDashboardGroupID",
        "description": "Get dashboard group by dashboard group ID",
        "inputParameters":
"""@i_dashboard_group_id          int""",
        "sqlQuery":
"""SELECT
        i_dashboard_group_id             AS 'dashboardGroupID',
        vc_dashboard_group_name          AS 'dashboardGroupName',
        vc_dashboard_group_description   AS 'dashboardGroupDescription',
        x_dashboard_group_setting_xml    AS 'dashboardGroupSettingXml',
        i_dashboard_count                AS 'dashboardCount',
        i_user_count                     AS 'userCount',
        vc_updated_by                    AS 'updatedBy',
        dt_inserted_datetime             AS 'insertedDateTime',
        dt_updated_datetime              AS 'updatedDateTime'
    FROM config_dashboard_groups
    WHERE i_dashboard_group_id       = @i_dashboard_group_id
    
    CHKERR({ERROR_GET_DASHBOARD_GROUP_BY_DASHBOARD_GROUP_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertDashboardGroup",
        "description": "Insert dashboard group",
        "inputParameters":
"""@vc_dashboard_group_name                 varchar(200),
    @vc_dashboard_group_description          varchar(600),
    @x_dashboard_group_setting_xml           xml,
    @i_dashboard_count                       int""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_dashboard_group_setting_xml)

    TRANINIT
    
    INSERT INTO config_dashboard_groups
    (
        vc_dashboard_group_name,
        vc_dashboard_group_description,
        x_dashboard_group_setting_xml,
        i_dashboard_count,
        i_user_count,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @vc_dashboard_group_name,
        @vc_dashboard_group_description,
        @x_dashboard_group_setting_xml,
        @i_dashboard_count,
        0,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_INSERT_DASHBOARD_GROUP})
    TRANRETURN""",
    },
    {
        "spName": "UpdateDashboardGroup",
        "description": "Update dashboard group",
        "inputParameters": 
"""@i_dashboard_group_id                      int,
    @vc_dashboard_group_name                   varchar(200),
    @vc_dashboard_group_description            varchar(600),
    @x_dashboard_group_setting_xml             xml,
    @i_dashboard_count                         int""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_dashboard_group_setting_xml)

    TRANINIT

    UPDATE config_dashboard_groups
    SET
        vc_dashboard_group_name                = @vc_dashboard_group_name,
        vc_dashboard_group_description         = @vc_dashboard_group_description,
        x_dashboard_group_setting_xml          = @x_dashboard_group_setting_xml,
        i_dashboard_count                      = @i_dashboard_count,
        vc_updated_by                          = SYSTEM_USER,
        dt_updated_datetime                    = GETUTCDATE()
    WHERE i_dashboard_group_id                 = @i_dashboard_group_id

    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({ERROR_UPDATE_DASHBOARD_GROUP})
    TRANRETURN""",
    },
    )