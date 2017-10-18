tableConfigAPIPartnerServers={
    "tableName": "config_api_partner_servers",
    "columns": (
        ("i_api_partner_server_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_api_partner_id", "int", "NOT NULL"),
        ("i_server_id", "int", "NOT NULL"),
        ("i_property_id", "int", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "api_partner_id_server_id", "unique": True, "columns": ("i_api_partner_id", "i_server_id", ) },
        { "indexName": "api_partner_id", "unique": False, "columns": ("i_api_partner_id", ) },
        { "indexName": "server_id", "unique": False, "columns": ("i_server_id", ) },
        { "indexName": "property_id", "unique": True, "columns": ("i_property_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_api_partner_id", "foreignTableName": "config_api_partners", "foreignColumnName": "i_api_partner_id", },
        { "columnName": "i_server_id", "foreignTableName": "config_servers", "foreignColumnName": "i_server_id", },
        { "columnName": "i_property_id", "foreignTableName": "config_properties", "foreignColumnName": "i_property_id", },
        ),
    }
tables.append(tableConfigAPIPartnerServers)

tableConfigAPIPartnerServers["sps"]=(
    {
        "spName": "GetAPIPartnerServerByPropertyID",
        "description": "Get API partner server by property ID",
        "inputParameters": """@i_property_id           int""",
        "sqlQuery":
"""SELECT
        i_api_partner_server_id AS 'apiPartnerServerID',
        i_api_partner_id        AS 'apiPartnerID',
        i_server_id             AS 'serverID',
        i_property_id           AS 'propertyID',
        dt_inserted_datetime    AS 'insertedDateTime'
    FROM config_api_partner_servers WITH (FORCESEEK)
    WHERE i_property_id         = @i_property_id
    
    CHKERR({ERROR_GET_API_PARTNER_SERVER_BY_PROPERTY_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnerServerByAPIPartnerIDAndServerID",
        "description": "Get API partner server by API partner ID and server ID",
        "inputParameters":
"""@i_api_partner_id           int,
    @i_server_id                int""",
        "sqlQuery":
"""SELECT
        i_api_partner_server_id AS 'apiPartnerServerID',
        i_api_partner_id        AS 'apiPartnerID',
        i_server_id             AS 'serverID',
        i_property_id           AS 'propertyID',
        dt_inserted_datetime    AS 'insertedDateTime'
    FROM config_api_partner_servers WITH (FORCESEEK)
    WHERE i_api_partner_id      = @i_api_partner_id
      AND i_server_id           = @i_server_id
    
    CHKERR({ERROR_GET_API_PARTNER_SERVER_BY_API_PARTNER_ID_AND_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnerServersByServerID",
        "description": "Get API partner servers by server ID",
        "inputParameters": """@i_server_id         int""",
        "sqlQuery":
"""SELECT
        i_api_partner_server_id AS 'apiPartnerServerID',
        i_api_partner_id        AS 'apiPartnerID',
        i_server_id             AS 'serverID',
        i_property_id           AS 'propertyID',
        dt_inserted_datetime    AS 'insertedDateTime'
    FROM config_api_partner_servers WITH (FORCESEEK)
    WHERE i_server_id           = @i_server_id
    
    CHKERR({ERROR_GET_API_PARTNER_SERVERS_BY_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnerServersByAPIID",
        "description": "Get API partner servers by API ID",
        "inputParameters": """@i_api_id         int""",
        "sqlQuery":
"""SELECT
        caps.i_api_partner_server_id AS 'apiPartnerServerID',
        caps.i_api_partner_id        AS 'apiPartnerID',
        caps.i_server_id             AS 'serverID',
        caps.i_property_id           AS 'propertyID',
        caps.dt_inserted_datetime    AS 'insertedDateTime'
    FROM config_api_partner_servers caps,
         config_api_partners cap
    WHERE cap.i_api_id               = @i_api_id
      AND cap.i_api_partner_id       = caps.i_api_partner_id
    
    CHKERR({ERROR_GET_API_PARTNER_SERVERS_BY_API_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnerServersWithPartnerIDByAPIID",
        "description": "Get API partner servers with partner ID by API ID",
        "inputParameters": """@i_api_id         int""",
        "sqlQuery":
"""SELECT
        caps.i_api_partner_server_id AS 'apiPartnerServerID',
        caps.i_api_partner_id        AS 'apiPartnerID',
        cap.i_partner_id             AS 'partnerID',
        caps.i_server_id             AS 'serverID',
        caps.i_property_id           AS 'propertyID',
        caps.dt_inserted_datetime    AS 'insertedDateTime'
    FROM config_api_partner_servers caps,
         config_api_partners cap
    WHERE cap.i_api_id               = @i_api_id
      AND cap.i_api_partner_id       = caps.i_api_partner_id
    
    CHKERR({ERROR_GET_API_PARTNER_SERVERS_WITH_PARTNER_ID_BY_API_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertAPIPartnerServer",
        "description": "Insert API partner server",
        "inputParameters":
"""@i_api_partner_id      int,
    @i_server_id           int,
    @i_property_id         int""",
        "sqlQuery":
"""TRANINIT

    IF EXISTS (SELECT 'X' FROM config_api_partners WHERE i_api_partner_id = @i_api_partner_id)
    BEGIN
        IF EXISTS (SELECT 'X' FROM config_servers WHERE i_server_id = @i_server_id)
        BEGIN
            IF EXISTS (SELECT 'X' FROM config_properties WHERE i_property_id = @i_property_id)
            BEGIN
                INSERT INTO config_api_partner_servers
                (
                    i_api_partner_id,
                    i_server_id,
                    i_property_id,
                    dt_inserted_datetime
                )
                VALUES
                (
                    @i_api_partner_id,
                    @i_server_id,
                    @i_property_id,
                    GETUTCDATE()
                )
                
                SELECT @@IDENTITY AS 'identity'
            END
            ELSE
            BEGIN
                SELECT 0 AS 'identity'
            END
        END
        ELSE
        BEGIN
            SELECT 0 AS 'identity'
        END
    END
    ELSE
    BEGIN
        SELECT 0 AS 'identity'
    END
    
    TRANCHKERR({ERROR_INSERT_API_PARTNER_SERVER})
    TRANRETURN""",
    },
    )