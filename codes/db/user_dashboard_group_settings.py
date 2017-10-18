tableUserDashboardGroupSettings={
    "tableName": "user_dashboard_group_settings",
    "columns": (
        ("i_user_dashboard_group_setting_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_user_id", "int", "NOT NULL"),
        ("i_dashboard_group_id", "int", "NOT NULL"),
        ("b_dashboard_group_owner", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("x_user_dashboard_group_setting_xml", "xml", "NOT NULL"),
        ("i_dashboard_group_order_id", "int", "NOT NULL", "DEFAULT ((1))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_id_dashboard_group_id", "unique": True, "columns": ("i_user_id", "i_dashboard_group_id", ) },
        { "indexName": "user_id_dashboard_group_order_id", "unique": True, "columns": ("i_user_id", "i_dashboard_group_order_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_user_id", "foreignTableName": "users", "foreignColumnName": "i_user_id", },
        { "columnName": "i_dashboard_group_id", "foreignTableName": "config_dashboard_groups", "foreignColumnName": "i_dashboard_group_id", },
        ),
    "xmlIgnores": (
        "x_user_dashboard_group_setting_xml",
        ),
    }

tables.append(tableUserDashboardGroupSettings)

tableUserDashboardGroupSettings["sps"]=(
    {
        "spName": "GetDefaultUserDashboardGroupSettingByUserID",
        "description": "Get default user dashboard group setting by user ID",
        "inputParameters":
"""@i_user_id          int""",
        "sqlQuery":
"""SELECT TOP 1
        i_user_dashboard_group_setting_id    AS 'userDashboardGroupSettingID',
        i_user_id                            AS 'userID',
        i_dashboard_group_id                 AS 'dashboardGroupID',
        b_dashboard_group_owner              AS 'dashboardGroupOwner',
        x_user_dashboard_group_setting_xml   AS 'userDashboardGroupSettingXml',
        i_dashboard_group_order_id           AS 'dashboardGroupOrderID',
        dt_inserted_datetime                 AS 'insertedDateTime',
        dt_updated_datetime                  AS 'updatedDateTime'
    FROM user_dashboard_group_settings WITH (FORCESEEK)
    WHERE i_user_id                 = @i_user_id
    ORDER BY i_dashboard_group_order_id ASC

    CHKERR({ERROR_GET_DEFAULT_USER_DASHBOARD_GROUP_SETTING_BY_USER_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertUserDashboardGroupSetting",
        "description": "Insert user dashboard group setting",
        "inputParameters":
"""@i_user_id                            int,
    @i_dashboard_group_id                 int,
    @b_dashboard_group_owner              bit,
    @x_user_dashboard_group_setting_xml   xml""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_user_dashboard_group_setting_xml)

    TRANINIT
    
    IF NOT EXISTS (SELECT 'X' FROM users WHERE i_user_id = @i_user_id)
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        IF NOT EXISTS (SELECT 'X' FROM config_dashboard_groups WITH (UPDLOCK) WHERE i_dashboard_group_id = @i_dashboard_group_id)
        BEGIN
            SELECT 0 AS 'identity'
        END
        ELSE
        BEGIN
            IF EXISTS (SELECT 'X' FROM user_dashboard_group_settings WITH (FORCESEEK) WHERE i_user_id = @i_user_id AND i_dashboard_group_id = @i_dashboard_group_id)
            BEGIN
                SELECT 0 AS 'identity'
            END
            ELSE
            BEGIN
                DECLARE @i_dashboard_group_order_id int
                SELECT
                    @i_dashboard_group_order_id = ISNULL(MAX(i_dashboard_group_order_id), 0) + 1
                FROM user_dashboard_group_settings WITH (FORCESEEK)
                WHERE i_user_id = @i_user_id
                
                INSERT INTO user_dashboard_group_settings
                (
                    i_user_id,
                    i_dashboard_group_id,
                    b_dashboard_group_owner,
                    x_user_dashboard_group_setting_xml,
                    i_dashboard_group_order_id,
                    dt_inserted_datetime,
                    dt_updated_datetime
                )
                VALUES
                (
                    @i_user_id,
                    @i_dashboard_group_id,
                    @b_dashboard_group_owner,
                    @x_user_dashboard_group_setting_xml,
                    @i_dashboard_group_order_id,
                    GETUTCDATE(),
                    GETUTCDATE()
                )

                SELECT @@IDENTITY AS 'identity'

                UPDATE config_dashboard_groups SET i_user_count = i_user_count + 1 WHERE i_dashboard_group_id = @i_dashboard_group_id
            END
        END
    END

    TRANCHKERR({ERROR_INSERT_USER_DASHBOARD_GROUP_SETTING})
    TRANRETURN""",
    },
    {
        "spName": "UpdateUserDashboardGroupSettingByUserDashboardGroupSettingID",
        "description": "Update user dashboard group setting by user dashboard group setting ID",
        "inputParameters":
"""@i_user_dashboard_group_setting_id    int,
    @b_dashboard_group_owner              bit,
    @x_user_dashboard_group_setting_xml   xml""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_user_dashboard_group_setting_xml)

    TRANINIT

    UPDATE user_dashboard_group_settings
    SET
        b_dashboard_group_owner              = @b_dashboard_group_owner,
        x_user_dashboard_group_setting_xml   = @x_user_dashboard_group_setting_xml,
        dt_updated_datetime                  = GETUTCDATE()
    WHERE i_user_dashboard_group_setting_id  = @i_user_dashboard_group_setting_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_USER_DASHBOARD_GROUP_SETTING_BY_USER_DASHBOARD_GROUP_SETTING_ID})
    TRANRETURN""",
    },
    {
        "spName": "UpdateDashboardGroupOrderIDByUserDashboardGroupSettingID",
        "description": "Update dashboard group order ID by user dashboard group setting ID",
        "inputParameters":
"""@i_user_dashboard_group_setting_id    int,
    @i_dashboard_group_order_id           int""",
        "sqlQuery":
"""TRANINIT

    UPDATE user_dashboard_group_settings
    SET
        i_dashboard_group_order_id           = @i_dashboard_group_order_id,
        dt_updated_datetime                  = GETUTCDATE()
    WHERE i_user_dashboard_group_setting_id  = @i_user_dashboard_group_setting_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_DASHBOARD_GROUP_ORDER_ID_BY_USER_DASHBOARD_GROUP_SETTING_ID})
    TRANRETURN""",
    },
    )