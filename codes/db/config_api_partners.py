tableConfigAPIPartners={
    "tableName": "config_api_partners",
    "columns": (
        ("i_api_partner_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_api_id", "int", "NOT NULL"),
        ("i_partner_id", "int", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "api_id_partner_id", "unique": True, "columns": ("i_api_id", "i_partner_id", ) },
        { "indexName": "partner_id", "unique": False, "columns": ("i_partner_id", ) },
        { "indexName": "api_id", "unique": False, "columns": ("i_api_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_api_id", "foreignTableName": "config_apis", "foreignColumnName": "i_api_id", },
        { "columnName": "i_partner_id", "foreignTableName": "config_partners", "foreignColumnName": "i_partner_id", },
        ),
    }
tables.append(tableConfigAPIPartners)

tableConfigAPIPartners["sps"]=(
    {
        "spName": "GetAPIPartnersByAPIID",
        "description": "Get API partners by API ID",
        "inputParameters": """@i_api_id           int""",
        "sqlQuery":
"""SELECT
        i_api_partner_id     AS 'apiPartnerID',
        i_api_id             AS 'apiID',
        i_partner_id         AS 'partnerID',
        dt_inserted_datetime AS 'insertedDateTime'
    FROM config_api_partners WITH (FORCESEEK)
    WHERE i_api_id           = @i_api_id
    
    CHKERR({ERROR_GET_API_PARTNERS_BY_API_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnersByPartnerID",
        "description": "Get API partners by partner ID",
        "inputParameters": """@i_partner_id         int""",
        "sqlQuery":
"""SELECT
        i_api_partner_id     AS 'apiPartnerID',
        i_api_id             AS 'apiID',
        i_partner_id         AS 'partnerID',
        dt_inserted_datetime AS 'insertedDateTime'
    FROM config_api_partners WITH (FORCESEEK)
    WHERE i_partner_id       = @i_partner_id
    
    CHKERR({ERROR_GET_API_PARTNERS_BY_PARTNER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPIPartnerByAPIIDAndPartnerID",
        "description": "Get API partner by API ID and partner ID",
        "inputParameters":
"""@i_api_id               int,
    @i_partner_id           int""",
        "sqlQuery":
"""SELECT
        i_api_partner_id     AS 'apiPartnerID',
        i_api_id             AS 'apiID',
        i_partner_id         AS 'partnerID',
        dt_inserted_datetime AS 'insertedDateTime'
    FROM config_api_partners WITH (FORCESEEK)
    WHERE i_api_id           = @i_api_id
      AND i_partner_id       = @i_partner_id
    
    CHKERR({ERROR_GET_API_PARTNER_BY_API_ID_AND_PARTNER_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertAPIPartner",
        "description": "Insert API partner",
        "inputParameters":
"""@i_api_id               int,
    @i_partner_id           int""",
        "sqlQuery":
"""TRANINIT

    IF EXISTS (SELECT 'X' FROM config_apis WITH (UPDLOCK) WHERE i_api_id = @i_api_id)
    BEGIN
        IF EXISTS (SELECT 'X' FROM config_partners WITH (UPDLOCK) WHERE i_partner_id = @i_partner_id)
        BEGIN
            IF NOT EXISTS (SELECT 'X' FROM config_api_partners WITH (FORCESEEK) WHERE i_api_id = @i_api_id AND i_partner_id = @i_partner_id)
            BEGIN
                INSERT INTO config_api_partners
                (
                    i_api_id,
                    i_partner_id,
                    dt_inserted_datetime
                )
                VALUES
                (
                    @i_api_id,
                    @i_partner_id,
                    GETUTCDATE()
                )
                
                SELECT @@IDENTITY AS 'identity'
                
                UPDATE config_apis SET i_partner_count = i_partner_count + 1 WHERE i_api_id = @i_api_id
                UPDATE config_partners SET i_api_count = i_api_count + 1 WHERE i_partner_id = @i_partner_id
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
    
    TRANCHKERR({ERROR_INSERT_API_PARTNER})
    TRANRETURN""",
    },
    )