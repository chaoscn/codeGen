tableConfigPartners={
    "tableName": "config_partners",
    "columns": (
        ("i_partner_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_partner_name", "varchar(200)", "NOT NULL"),
        ("vc_partner_description", "varchar(600)", "NULL", "DEFAULT ((NULL))"),
        ("i_api_count", "int", "not null", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "partner_name", "unique": True, "columns": ("vc_partner_name", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'A1'", "'A1'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Agent Desktop'", "'Agent Desktop'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'BAM'", "'BAM'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'bCentral'", "'bCentral'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CDF'", "'CDF'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'cm_RioWeb'", "'cm_RioWeb'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'cm_ssapi'", "'cm_ssapi'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CRMLive'", "'CRMLive'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CSS Consumer'", "'CSS Consumer'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Domain Services'", "'Domain Services'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Dynamics Live'", "'Dynamics Live'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GameZone'", "'GameZone'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'InComm'", "'InComm'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'IVR'", "'IVR'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'IWS Small Business (CM)'", "'IWS Small Business (CM)'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'LPO'", "'LPO'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Microsoft Learning Platform Grou'", "'Microsoft Learning Platform Grou'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'MPFServiceAcct'", "'MPFServiceAcct'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'MSN Direct'", "'MSN Direct'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'MSN Mobile'", "'MSN Mobile'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'MSNTV'", "'MSNTV'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'MSO Monitoring'", "'MSO Monitoring'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'NETWORK SERVICE'", "'NETWORK SERVICE'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'OEI'", "'OEI'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'PaymentService'", "'PaymentService'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Real Time Communications'", "'Real Time Communications'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SCS'", "'SCS'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SkyMarket'", "'SkyMarket'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SPG Signup'", "'SPG Signup'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'spsp_moonshot'", "'spsp_moonshot'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'spsp_MSOMonitoring '", "'spsp_MSOMonitoring '", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'spsp_signup'", "'spsp_signup'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Supportability'", "'Supportability'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'System Center Online'", "'System Center Online'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Texas'", "'Texas'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'WholesaleCSR'", "'WholesaleCSR'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Xbox Live'", "'Xbox Live'", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigPartners)

tableConfigPartners["sps"]=(
    {
        "spName": "GetPartnerByPartnerName",
        "description": "Get partner by partner name",
        "inputParameters": """@vc_partner_name           varchar(200)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_partner_name)

    SELECT
        i_partner_id            AS 'partnerID',
        vc_partner_name         AS 'partnerName',
        vc_partner_description  AS 'partnerDescription',
        i_api_count             AS 'apiCount',
        vc_updated_by           AS 'updatedBy',
        dt_inserted_datetime    AS 'insertedDateTime',
        dt_updated_datetime     AS 'updatedDateTime'
    FROM config_partners WITH (FORCESEEK)
    WHERE vc_partner_name        = @vc_partner_name
    
    CHKERR({ERROR_GET_PARTNER_BY_PARTNER_NAME})
    RETURN 0""",
    },
    {
        "spName": "GetAllPartners",
        "description": "Get all partners",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_partner_id            AS 'partnerID',
        vc_partner_name         AS 'partnerName',
        vc_partner_description  AS 'partnerDescription',
        i_api_count             AS 'apiCount',
        vc_updated_by           AS 'updatedBy',
        dt_inserted_datetime    AS 'insertedDateTime',
        dt_updated_datetime     AS 'updatedDateTime'
    FROM config_partners
    ORDER BY i_partner_id ASC
    
    CHKERR({ERROR_GET_ALL_PARTNERS})
    RETURN 0""",
    },
    {
        "spName": "GetPartnerByPartnerID",
        "description": "Get partner by partner ID",
        "inputParameters": """@i_partner_id           int""",
        "sqlQuery":
"""SELECT
        i_partner_id            AS 'partnerID',
        vc_partner_name         AS 'partnerName',
        vc_partner_description  AS 'partnerDescription',
        i_api_count             AS 'apiCount',
        vc_updated_by           AS 'updatedBy',
        dt_inserted_datetime    AS 'insertedDateTime',
        dt_updated_datetime     AS 'updatedDateTime'
    FROM config_partners
    WHERE i_partner_id           = @i_partner_id
    
    CHKERR({ERROR_GET_PARTNER_BY_PARTNER_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertPartner",
        "description": "Insert partner",
        "inputParameters":
"""@vc_partner_name           varchar(200),
    @vc_partner_description    varchar(600)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_partner_name)
    CHECK_NOTNULL(@vc_partner_description)

    TRANINIT

    INSERT INTO config_partners
    (
        vc_partner_name,
        vc_partner_description,
        i_api_count,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @vc_partner_name,
        @vc_partner_description,
        0,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_INSERT_PARTNER})
    TRANRETURN""",
    },
    )