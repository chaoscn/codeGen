tableConfigDataCenters={
    "tableName": "config_data_centers",
    "columns": (
        ("i_data_center_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_data_center_name", "varchar(200)", "NOT NULL"),
        ("vc_data_center_pattern", "varchar(200)", "NOT NULL"),
        ("b_data_center_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "data_center_name", "unique": True, "columns": ("vc_data_center_name", ) },
        { "indexName": "data_center_name_enabled", "unique": False, "columns": ("vc_data_center_name", "b_data_center_enabled", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'PROD-TK2'", "'TK2MP*'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'PROD-BLU'", "'BLUMP*'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CNPC'", "'CNPC*'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigDataCenters)

tableConfigDataCenters["sps"]=(
    {
        "spName": "GetAllDataCenters",
        "description": "Get all data centers",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_data_center_id       AS 'dataCenterID',
        vc_data_center_name    AS 'dataCenterName',
        vc_data_center_pattern AS 'dataCenterPattern',
        b_data_center_enabled  AS 'dataCenterEnabled',
        vc_updated_by          AS 'updatedBy',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM config_data_centers
    ORDER BY i_data_center_id
    
    CHKERR({ERROR_GET_All_DATA_CENTERS})
    RETURN 0""",
    },
    {
        "spName": "InsertDataCenter",
        "description": "Insert data center",
        "inputParameters":
"""@vc_data_center_name        varchar(200),
    @vc_data_center_pattern     varchar(200),
    @b_data_center_enabled      bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_data_center_name)
    CHECK_NOTNULL(@vc_data_center_pattern)

    TRANINIT

    INSERT INTO config_data_centers
    (
        vc_data_center_name,
        vc_data_center_pattern,
        b_data_center_enabled,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @vc_data_center_name,
        @vc_data_center_pattern,
        @b_data_center_enabled,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )

    DECLARE @i_data_center_id int
    DECLARE @vc_server_name   varchar(200)
    SET @i_data_center_id = @@IDENTITY
    SET @vc_server_name   = 'DUMMY' + CAST(@i_data_center_id AS varchar)

    SELECT @i_data_center_id AS 'identity'

    IF (@i_data_center_id > 0)
    BEGIN
        EXEC spm_InsertServer{}VERSION_SUFFIX
            @i_data_center_id  = @i_data_center_id,
            @vc_server_role    = 'DUMMY',
            @vc_server_name    = @vc_server_name,
            @b_server_critical = 0,
            @b_server_enabled  = 1
    END

    TRANCHKERR({ERROR_INSERT_DATA_CENTER})
    TRANRETURN""",
    },
    )