tableUserReportSettings={
    "tableName": "user_report_settings",
    "columns": (
        ("i_user_report_setting_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_user_id", "int", "NOT NULL"),
        ("i_report_id", "int", "NOT NULL"),
        ("b_report_owner", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("b_alert_me", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("x_user_report_setting_xml", "xml", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_id_report_id", "unique": True, "columns": ("i_user_id", "i_report_id", ) },
        { "indexName": "report_id", "unique": False, "columns": ("i_report_id", ) },
        { "indexName": "user_id", "unique": False, "columns": ("i_user_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_user_id", "foreignTableName": "users", "foreignColumnName": "i_user_id", },
        { "columnName": "i_report_id", "foreignTableName": "config_reports", "foreignColumnName": "i_report_id", },
        ),
    "xmlIgnores": (
        "x_user_report_setting_xml",
        ),
    }

tables.append(tableUserReportSettings)

tableUserReportSettings["sps"]=(
    {
        "spName": "GetUserReportSettingByUserIDAndReportID",
        "description": "Get user report setting by user ID and report ID",
        "inputParameters":
"""@i_user_id          int,
    @i_report_id        int""",
        "sqlQuery":
"""SELECT
        i_user_report_setting_id    AS 'userReportSettingID',
        i_user_id                   AS 'userID',
        i_report_id                 AS 'reportID',
        b_report_owner              AS 'reportOwner',
        b_alert_me                  AS 'alertMe',
        x_user_report_setting_xml   AS 'userReportSettingXml',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM user_report_settings WITH (FORCESEEK)
    WHERE i_user_id                 = @i_user_id
      AND i_report_id               = @i_report_id

    CHKERR({ERROR_GET_USER_REPORT_SETTING_BY_USER_ID_AND_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "GetUserReportSettingsByUserID",
        "description": "Get user report settings by user ID",
        "inputParameters":
"""@i_user_id          int""",
        "sqlQuery":
"""SELECT
        i_user_report_setting_id    AS 'userReportSettingID',
        i_user_id                   AS 'userID',
        i_report_id                 AS 'reportID',
        b_report_owner              AS 'reportOwner',
        b_alert_me                  AS 'alertMe',
        x_user_report_setting_xml   AS 'userReportSettingXml',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM user_report_settings WITH (FORCESEEK)
    WHERE i_user_id                 = @i_user_id

    CHKERR({ERROR_GET_USER_REPORT_SETTINGS_BY_USER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetUserReportSettingsByReportID",
        "description": "Get user report settings by report ID",
        "inputParameters":
"""@i_report_id        int""",
        "sqlQuery":
"""SELECT
        i_user_report_setting_id    AS 'userReportSettingID',
        i_user_id                   AS 'userID',
        i_report_id                 AS 'reportID',
        b_report_owner              AS 'reportOwner',
        b_alert_me                  AS 'alertMe',
        x_user_report_setting_xml   AS 'userReportSettingXml',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM user_report_settings WITH (FORCESEEK)
    WHERE i_report_id               = @i_report_id

    CHKERR({ERROR_GET_USER_REPORT_SETTINGS_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertUserReportSetting",
        "description": "Insert user report setting",
        "inputParameters":
"""@i_user_id                   int,
    @i_report_id                 int,
    @b_report_owner              bit,
    @b_alert_me                  bit,
    @x_user_report_setting_xml   xml""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_user_report_setting_xml)

    TRANINIT
    IF NOT EXISTS (SELECT 'X' FROM users WITH (UPDLOCK) WHERE i_user_id = @i_user_id)
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        IF NOT EXISTS (SELECT 'X' FROM config_reports WITH (UPDLOCK) WHERE i_report_id = @i_report_id)
        BEGIN
            SELECT 0 AS 'identity'
        END
        ELSE
        BEGIN
            IF EXISTS (SELECT 'X' FROM user_report_settings WITH (UPDLOCK) WHERE i_user_id = @i_user_id AND i_report_id = @i_report_id)
            BEGIN
                SELECT 0 AS 'identity'
            END
            ELSE
            BEGIN
                INSERT INTO user_report_settings
                (
                    i_user_id,
                    i_report_id,
                    b_report_owner,
                    b_alert_me,
                    x_user_report_setting_xml,
                    dt_inserted_datetime,
                    dt_updated_datetime
                )
                VALUES
                (
                    @i_user_id,
                    @i_report_id,
                    @b_report_owner,
                    @b_alert_me,
                    @x_user_report_setting_xml,
                    GETUTCDATE(),
                    GETUTCDATE()
                )

                SELECT @@IDENTITY AS 'identity'

                UPDATE users SET i_report_count = i_report_count + 1 WHERE i_user_id = @i_user_id
                UPDATE config_reports SET i_user_count = i_user_count + 1 WHERE i_report_id = @i_report_id
            END
        END
    END

    TRANCHKERR({ERROR_INSERT_USER_REPORT_SETTING})
    TRANRETURN""",
    },
    {
        "spName": "UpdateUserReportSettingByUserIDAndReportID",
        "description": "Update user report setting by user ID and report ID",
        "inputParameters":
"""@i_user_id                   int,
    @i_report_id                 int,
    @b_report_owner              bit,
    @b_alert_me                  bit,
    @x_user_report_setting_xml   xml""",
        "sqlQuery":
"""CHECK_NOTNULL(@x_user_report_setting_xml)

    TRANINIT

    UPDATE user_report_settings
    SET
        b_report_owner              = @b_report_owner,
        b_alert_me                  = @b_alert_me,
        x_user_report_setting_xml   = @x_user_report_setting_xml,
        dt_updated_datetime         = GETUTCDATE()
    WHERE i_user_id                 = @i_user_id
      AND i_report_id               = @i_report_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_USER_REPORT_SETTING_BY_USER_ID_AND_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteUserReportSettingsByReportID",
        "description": "Delete user report settings by report ID",
        "inputParameters":
"""@i_report_id        int""",
        "sqlQuery":
"""TRANINIT

    UPDATE users
    SET i_report_count = i_report_count - 1
    WHERE i_user_id IN
    (
        SELECT
            i_user_id
        FROM user_report_settings WITH (UPDLOCK)
        WHERE i_report_id = @i_report_id
    )

    DELETE FROM user_report_settings
    WHERE i_report_id = @i_report_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_USER_REPORT_SETTINGS_BY_REPORT_ID})
    TRANRETURN""",
    },
    {
        "spName": "DeleteUserReportSettingByUserIDAndReportID",
        "description": "Delete user report setting by user ID and report ID",
        "inputParameters":
"""@i_user_id          int,
    @i_report_id        int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @b_found bit
    IF EXISTS (SELECT 'X' FROM user_report_settings WITH (UPDLOCK) WHERE i_user_id = @i_user_id AND i_report_id = @i_report_id AND b_report_owner = 0)
    BEGIN
        SET @b_found = 1

        DELETE FROM user_report_settings
        WHERE i_user_id      = @i_user_id
          AND i_report_id    = @i_report_id
          AND b_report_owner = 0

        SELECT @@ROWCOUNT AS 'rowcount'

        IF EXISTS (SELECT 'X' FROM users WITH (UPDLOCK) WHERE i_user_id = @i_user_id)
        BEGIN
            UPDATE users SET i_report_count = i_report_count - 1 WHERE i_user_id = @i_user_id
        END
        IF EXISTS (SELECT 'X' FROM config_reports WITH (UPDLOCK) WHERE i_report_id = @i_report_id)
        BEGIN
            UPDATE config_reports SET i_user_count = i_user_count - 1 WHERE i_report_id = @i_report_id
        END
    END
    ELSE
    BEGIN
        SET @b_found = 0
        SELECT 0 AS 'rowcount'
    END

    TRANCHKERR({ERROR_DELETE_USER_REPORT_SETTING_BY_USER_ID_AND_REPORT_ID})
    TRANRETURN""",
    },
    )