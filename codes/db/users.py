tableUsers={
    "tableName": "users",
    "columns": (
        ("i_user_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_user_domain", "varchar(100)", "NOT NULL"),
        ("vc_user_alias", "varchar(100)", "NOT NULL"),
        ("vc_user_emails", "varchar(8000)", "NULL"),
        ("i_report_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("i_user_group_id", "int", "NOT NULL"),
        ("b_user_disabled", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_domain_user_alias", "unique": True, "columns": ("vc_user_domain", "vc_user_alias", ) },
        { "indexName": "user_group_id", "unique": False, "columns": ("i_user_group_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_user_group_id", "foreignTableName": "user_groups", "foreignColumnName": "i_user_group_id", },
        ),
    "initialDataWhereIndex": (1, 2, ),
    "initialData": (
        { "dataLine": ("'PHX'", "'yincao'", "'yincao'", "'0'", "1", "0", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'FAREAST'", "'yincao'", "'yincao'", "'0'", "1", "0", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableUsers)

tableUsers["sps"]=(
    {
        "spName": "GetAllUsers",
        "description": "Get all users",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_user_id              AS 'userID',
        vc_user_domain         AS 'userDomain',
        vc_user_alias          AS 'userAlias',
        vc_user_emails         AS 'userEmails',
        i_report_count         AS 'reportCount',
        i_user_group_id        AS 'userGroupID',
        b_user_disabled        AS 'userDisabled',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM users
    ORDER BY vc_user_domain, vc_user_alias

    CHKERR({ERROR_GET_ALL_USERS})
    RETURN 0""",
    },
    {
        "spName": "GetUserByUserID",
        "description": "Get user by user ID",
        "inputParameters":
"""@i_user_id               int""",
        "sqlQuery":
"""SELECT
        i_user_id              AS 'userID',
        vc_user_domain         AS 'userDomain',
        vc_user_alias          AS 'userAlias',
        vc_user_emails         AS 'userEmails',
        i_report_count         AS 'reportCount',
        i_user_group_id        AS 'userGroupID',
        b_user_disabled        AS 'userDisabled',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM users
    WHERE i_user_id            = @i_user_id
    
    CHKERR({ERROR_GET_USER_BY_USER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetUserByDomainAndAlias",
        "description": "Get user by domain and alias",
        "inputParameters":
"""@vc_user_domain          varchar(100),
    @vc_user_alias           varchar(100)""",
        "sqlQuery":
"""SELECT
        i_user_id              AS 'userID',
        vc_user_domain         AS 'userDomain',
        vc_user_alias          AS 'userAlias',
        vc_user_emails         AS 'userEmails',
        i_report_count         AS 'reportCount',
        i_user_group_id        AS 'userGroupID',
        b_user_disabled        AS 'userDisabled',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM users WITH (FORCESEEK)
    WHERE vc_user_domain       = UPPER(@vc_user_domain)
      AND vc_user_alias        = LOWER(@vc_user_alias)
    
    CHKERR({ERROR_GET_USER_BY_DOMAIN_AND_ALIAS})
    RETURN 0""",
    },
    {
        "spName": "GetUsersByReportID",
        "description": "Get users by report ID",
        "inputParameters":
"""@i_report_id          int""",
        "sqlQuery":
"""SELECT
        i_user_id              AS 'userID',
        vc_user_domain         AS 'userDomain',
        vc_user_alias          AS 'userAlias',
        vc_user_emails         AS 'userEmails',
        i_report_count         AS 'reportCount',
        i_user_group_id        AS 'userGroupID',
        b_user_disabled        AS 'userDisabled',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM users
    WHERE i_user_id IN (SELECT i_user_id FROM user_report_settings WITH (FORCESEEK) WHERE i_report_id = @i_report_id)
    
    CHKERR({ERROR_GET_USERS_BY_REPORT_ID})
    RETURN 0""",
    },
    {
        "spName": "GetUsersByReportIDAndOwner",
        "description": "Get users by report ID and owner",
        "inputParameters":
"""@i_report_id          int,
    @b_report_owner       bit""",
        "sqlQuery":
"""SELECT
        i_user_id              AS 'userID',
        vc_user_domain         AS 'userDomain',
        vc_user_alias          AS 'userAlias',
        vc_user_emails         AS 'userEmails',
        i_report_count         AS 'reportCount',
        i_user_group_id        AS 'userGroupID',
        b_user_disabled        AS 'userDisabled',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM users
    WHERE i_user_id IN (SELECT i_user_id FROM user_report_settings WITH (FORCESEEK) WHERE i_report_id = @i_report_id AND b_report_owner = @b_report_owner)
    
    CHKERR({ERROR_GET_USERS_BY_REPORT_ID_AND_OWNER})
    RETURN 0""",
    },
    {
        "spName": "CountUsers",
        "description": "Count users",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT COUNT(1) AS 'rowcount'
    FROM users

    CHKERR({ERROR_COUNT_USERS})
    RETURN 0""",
    },
    {
        "spName": "InsertUser",
        "description": "Insert user",
        "inputParameters":
"""@vc_user_domain          varchar(100),
    @vc_user_alias           varchar(100),
    @vc_user_emails          varchar(8000),
    @i_user_group_id         int,
    @b_user_disabled         bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_user_domain)
    CHECK_NOTNULL(@vc_user_alias)

    TRANINIT
    
    IF NOT EXISTS (SELECT 'X' FROM user_groups WITH (UPDLOCK) WHERE i_user_group_id = @i_user_group_id)
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        IF EXISTS (SELECT 'X' FROM users WITH (FORCESEEK) WHERE vc_user_domain = @vc_user_domain AND vc_user_alias = @vc_user_alias)
        BEGIN
            SELECT 0 AS 'identity'
        END
        ELSE
        BEGIN
            INSERT INTO users
            (
                vc_user_domain,
                vc_user_alias,
                vc_user_emails,
                i_report_count,
                i_user_group_id,
                b_user_disabled,
                dt_inserted_datetime,
                dt_updated_datetime
            )
            VALUES
            (
                UPPER(@vc_user_domain),
                LOWER(@vc_user_alias),
                @vc_user_emails,
                0,
                @i_user_group_id,
                @b_user_disabled,
                GETUTCDATE(),
                GETUTCDATE()
            )
            
            SELECT @@IDENTITY AS 'identity'
            
            UPDATE user_groups
            SET i_user_count      = i_user_count + 1
            WHERE i_user_group_id = @i_user_group_id
        END
    END
    
    TRANCHKERR({ERROR_INSERT_USER})
    TRANRETURN""",
    },
    {
        "spName": "UpdateUser",
        "description": "Update user",
        "inputParameters":
"""@i_user_id               int,
    @vc_user_domain          varchar(100),
    @vc_user_alias           varchar(100),
    @vc_user_emails          varchar(8000),
    @i_user_group_id         int,
    @b_user_disabled         bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_user_domain)
    CHECK_NOTNULL(@vc_user_alias)

    TRANINIT
    
    DECLARE @i_original_user_group_id int
    SET @i_original_user_group_id = (SELECT TOP 1 i_user_group_id FROM users WHERE i_user_id = @i_user_id)
    IF (@i_original_user_group_id IS NULL OR @i_original_user_group_id = 0)
    BEGIN
        SELECT 0 AS 'rowcount'
    END
    ELSE
    BEGIN
        IF NOT EXISTS (SELECT 'X' FROM user_groups WITH (UPDLOCK) WHERE i_user_group_id = @i_original_user_group_id)
        BEGIN
            SELECT 0 AS 'rowcount'
        END
        ELSE
        BEGIN
            IF NOT EXISTS (SELECT 'X' FROM user_groups WITH (UPDLOCK) WHERE i_user_group_id = @i_user_group_id)
            BEGIN
                SELECT 0 AS 'rowcount'
            END
            ELSE
            BEGIN
                UPDATE users
                SET
                    vc_user_domain              = UPPER(@vc_user_domain),
                    vc_user_alias               = LOWER(@vc_user_alias),
                    vc_user_emails              = @vc_user_emails,
                    i_user_group_id             = @i_user_group_id,
                    b_user_disabled             = @b_user_disabled,
                    dt_updated_datetime         = GETUTCDATE()
                WHERE i_user_id                 = @i_user_id
                
                SELECT @@ROWCOUNT AS 'rowcount'
                
                IF (@i_original_user_group_id <> @i_user_group_id)
                BEGIN
                    UPDATE user_groups SET i_user_count = i_user_count - 1 WHERE i_user_group_id = @i_original_user_group_id
                    UPDATE user_groups SET i_user_count = i_user_count + 1 WHERE i_user_group_id = @i_user_group_id
                END
            END
        END
    END
    
    TRANCHKERR({ERROR_UPDATE_USER})
    TRANRETURN""",
    },
    )