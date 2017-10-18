tableConfigServers={
    "tableName": "config_servers",
    "columns": (
        ("i_server_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_data_center_id", "int", "not null"),
        ("vc_server_role", "varchar(400)", "NOT NULL"),
        ("vc_server_name", "varchar(200)", "NOT NULL"),
        ("b_server_critical", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_server_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "server_name", "unique": True, "columns": ("vc_server_name", ) },
        { "indexName": "data_center_server_role_name", "unique": True, "columns": ("i_data_center_id", "vc_server_role", "vc_server_name", ) },
        { "indexName": "server_id_server_critical", "unique": True, "columns": ("i_server_id", "b_server_critical", ) },
        { "indexName": "server_role_name_enabled", "unique": False, "columns": ("vc_server_role", "vc_server_name", "b_server_enabled", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_data_center_id", "foreignTableName": "config_data_centers", "foreignColumnName": "i_data_center_id", },
        ),
    "initialDataWhereIndex": (3, ),
    "initialData": (
        { "dataLine": ("1", "'DUMMY'", "'TK2MPDUMMY'", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("2", "'DUMMY'", "'BLUMPDUMMY'", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("3", "'DUMMY'", "'CNPCDUMMY'", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigServers)

tableConfigServers["sps"]=(
    {
        "spName": "GetServersByServerRole",
        "description": "Get servers by server role",
        "inputParameters": """@vc_server_role           varchar(200)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_role)

    SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers WITH (FORCESEEK)
    WHERE vc_server_role     = @vc_server_role
    
    CHKERR({ERROR_GET_SERVERS_BY_SERVER_ROLE})
    RETURN 0""",
    },
    {
        "spName": "GetAllServers",
        "description": "Get all servers",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers
    ORDER BY i_server_id ASC
    
    CHKERR({ERROR_GET_ALL_SERVERS})
    RETURN 0""",
    },
    {
        "spName": "GetServerByServerID",
        "description": "Get server by server ID",
        "inputParameters": """@i_server_id           int""",
        "sqlQuery":
"""SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers
    WHERE i_server_id        = @i_server_id
    
    CHKERR({ERROR_GET_SERVER_BY_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetServerByNameAndDataCenterID",
        "description": "Get server by name and data center ID",
        "inputParameters":
"""@vc_server_name             varchar(200),
    @i_data_center_id           int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_name)

    SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers WITH (FORCESEEK)
    WHERE i_data_center_id   = @i_data_center_id
      AND vc_server_name     = @vc_server_name
    
    CHKERR({ERROR_GET_SERVER_BY_NAME_AND_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetServersByDataCenterID",
        "description": "Get servers by data center ID",
        "inputParameters":
"""@i_data_center_id           int""",
        "sqlQuery":
"""SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers WITH (FORCESEEK)
    WHERE i_data_center_id   = @i_data_center_id
    
    CHKERR({ERROR_GET_SERVERS_BY_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetServersByServerRoleAndDataCenterID",
        "description": "Get servers by server role and data center ID",
        "inputParameters":
"""@vc_server_role             varchar(200),
    @i_data_center_id           int""",
        "sqlQuery":
"""SELECT
        i_server_id          AS 'serverID',
        i_data_center_id     AS 'dataCenterID',
        vc_server_role       AS 'serverRole',
        vc_server_name       AS 'serverName',
        b_server_critical    AS 'serverCritical',
        b_server_enabled     AS 'serverEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_servers WITH (FORCESEEK)
    WHERE i_data_center_id   = @i_data_center_id
      AND vc_server_role     = @vc_server_role
    
    CHKERR({ERROR_GET_SERVERS_BY_SERVER_ROLE_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertServer",
        "description": "Insert server",
        "inputParameters":
"""@i_data_center_id         int,
    @vc_server_role           varchar(200),
    @vc_server_name           varchar(200),
    @b_server_critical        bit,
    @b_server_enabled         bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_role)
    CHECK_NOTNULL(@vc_server_name)

    TRANINIT

    INSERT INTO config_servers
    (
        i_data_center_id,
        vc_server_role,
        vc_server_name,
        b_server_critical,
        b_server_enabled,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @i_data_center_id,
        @vc_server_role,
        @vc_server_name,
        @b_server_critical,
        @b_server_enabled,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_INSERT_SERVER})
    TRANRETURN""",
    },
    {
        "spName": "UpdateServer",
        "description": "Update server",
        "inputParameters":
"""@i_server_id              int,
    @i_data_center_id         int,
    @vc_server_role           varchar(200),
    @vc_server_name           varchar(200),
    @b_server_critical        bit,
    @b_server_enabled         bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_server_role)
    CHECK_NOTNULL(@vc_server_name)

    TRANINIT

    UPDATE config_servers
    SET
        i_data_center_id     = @i_data_center_id,
        vc_server_role       = @vc_server_role,
        vc_server_name       = @vc_server_name,
        b_server_critical    = @b_server_critical,
        b_server_enabled     = @b_server_enabled,
        vc_updated_by        = SYSTEM_USER,
        dt_updated_datetime  = GETUTCDATE()
    WHERE i_server_id        = @i_server_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_SERVER})
    TRANRETURN""",
    },
    )