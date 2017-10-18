tableConfigProperties={
    "tableName": "config_properties",
    "columns": (
        ("i_property_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_property_type_id", "int", "NOT NULL"),
        ("i_server_id", "int", "NOT NULL"),
        ("vc_property_name", "varchar(600)", "NOT NULL"),
        ("b_property_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("dt_hourly_aggregated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_daily_aggregated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "property_name_server_id", "unique": True, "columns": ("vc_property_name", "i_server_id", ) },
        { "indexName": "server_id", "unique": False, "columns": ("i_server_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_property_type_id", "foreignTableName": "config_property_types", "foreignColumnName": "i_property_type_id", },
        { "columnName": "i_server_id", "foreignTableName": "config_servers", "foreignColumnName": "i_server_id", },
        ),
    }
tables.append(tableConfigProperties)

tableConfigProperties["sps"]=(
    {
        "spName": "GetPropertyByServerIDAndPropertyName",
        "description": "Get property by server ID and property name",
        "inputParameters": 
"""@i_server_id           int,
    @vc_property_name      varchar(600)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_property_name)

    SELECT
        i_property_id                 AS 'propertyID',
        i_property_type_id            AS 'propertyTypeID',
        i_server_id                   AS 'serverID',
        vc_property_name              AS 'propertyName',
        b_property_enabled            AS 'propertyEnabled',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDatetime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDatetime',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_properties WITH (FORCESEEK)
    WHERE i_server_id           = @i_server_id
      AND vc_property_name      = @vc_property_name
    
    CHKERR({ERROR_GET_PROPERTY_BY_SERVER_ID_AND_PROPERTY_NAME})
    RETURN 0""",
    },
    {
        "spName": "GetPropertyByPropertyID",
        "description": "Get property by property ID",
        "inputParameters": 
"""@i_property_id           int""",
        "sqlQuery":
"""SELECT
        i_property_id                 AS 'propertyID',
        i_property_type_id            AS 'propertyTypeID',
        i_server_id                   AS 'serverID',
        vc_property_name              AS 'propertyName',
        b_property_enabled            AS 'propertyEnabled',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDatetime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDatetime',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_properties
    WHERE i_property_id           = @i_property_id
    
    CHKERR({ERROR_GET_PROPERTY_BY_PROPERTY_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPropertiesByServerID",
        "description": "Get properties by server ID",
        "inputParameters": 
"""@i_server_id           int""",
        "sqlQuery":
"""SELECT
        i_property_id                 AS 'propertyID',
        i_property_type_id            AS 'propertyTypeID',
        i_server_id                   AS 'serverID',
        vc_property_name              AS 'propertyName',
        b_property_enabled            AS 'propertyEnabled',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDatetime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDatetime',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_properties WITH (FORCESEEK)
    WHERE i_server_id                 = @i_server_id
    ORDER BY i_property_id ASC
    
    CHKERR({ERROR_GET_PROPERTIES_BY_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAllPropertiesByPropertyIDAndPageSize",
        "description": "Get all properties by property ID and page size",
        "inputParameters": 
"""@i_property_id           int,
    @i_page_size             int""",
        "sqlQuery":
"""IF (@i_page_size<0 OR @i_page_size>5000)
        RAISERROR('Page size is invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    SELECT TOP (@i_page_size)
        i_property_id                 AS 'propertyID',
        i_property_type_id            AS 'propertyTypeID',
        i_server_id                   AS 'serverID',
        vc_property_name              AS 'propertyName',
        b_property_enabled            AS 'propertyEnabled',
        dt_hourly_aggregated_datetime AS 'hourlyAggregatedDatetime',
        dt_daily_aggregated_datetime  AS 'dailyAggregatedDatetime',
        vc_updated_by                 AS 'updatedBy',
        dt_inserted_datetime          AS 'insertedDateTime',
        dt_updated_datetime           AS 'updatedDateTime'
    FROM config_properties
    WHERE i_property_id               > @i_property_id
    ORDER BY i_property_id ASC

    CHKERR({ERROR_GET_ALL_PROPERTIES_BY_PROPERTY_ID_AND_PAGE_SIZE})
    RETURN 0""",
    },
    {
        "spName": "InsertProperty",
        "description": "Insert property",
        "inputParameters":
"""@i_property_type_id            int,
    @i_server_id                   int,
    @vc_property_name              varchar(600),
    @b_property_enabled            bit,
    @dt_hourly_aggregated_datetime datetime,
    @dt_daily_aggregated_datetime  datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_property_name)
    CHECK_NOTNULL(@dt_hourly_aggregated_datetime)
    CHECK_NOTNULL(@dt_daily_aggregated_datetime)

    TRANINIT

    INSERT INTO config_properties
    (
        i_property_type_id,
        i_server_id,
        vc_property_name,
        b_property_enabled,
        dt_hourly_aggregated_datetime,
        dt_daily_aggregated_datetime,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @i_property_type_id,
        @i_server_id,
        @vc_property_name,
        @b_property_enabled,
        @dt_hourly_aggregated_datetime,
        @dt_daily_aggregated_datetime,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    EXEC spm_CreateTablePropertyValue{}VERSION_SUFFIX
        @ti_table_type = 0,
        @i_server_id   = @i_server_id
    EXEC spm_CreateTablePropertyValue{}VERSION_SUFFIX
        @ti_table_type = 1,
        @i_server_id   = @i_server_id
    EXEC spm_CreateTablePropertyValue{}VERSION_SUFFIX
        @ti_table_type = 2,
        @i_server_id   = @i_server_id
    
    TRANCHKERR({ERROR_INSERT_PROPERTY})
    TRANRETURN""",
    },
    {
        "spName": "UpdateProperty",
        "description": "Update property",
        "inputParameters":
"""@i_property_id                      int,
    @i_property_type_id                 int,
    @i_server_id                        int,
    @vc_property_name                   varchar(600),
    @b_property_enabled                 bit,
    @dt_hourly_aggregated_datetime      datetime,
    @dt_daily_aggregated_datetime       datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_property_name)

    TRANINIT

    UPDATE config_properties
    SET
        i_property_type_id              = @i_property_type_id,
        i_server_id                     = @i_server_id,
        vc_property_name                = @vc_property_name,
        b_property_enabled              = @b_property_enabled,
        dt_hourly_aggregated_datetime   = @dt_hourly_aggregated_datetime,
        dt_daily_aggregated_datetime    = @dt_daily_aggregated_datetime,
        vc_updated_by                   = SYSTEM_USER,
        dt_updated_datetime             = GETUTCDATE()
    WHERE i_property_id                 = @i_property_id
    
    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({ERROR_UPDATE_PROPERTY})
    TRANRETURN""",
    },
    {
        "spName": "DeletePropertyByPropertyID",
        "description": "Delete property by property ID",
        "inputParameters":
"""@i_property_id                      int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @i_server_id int
    SELECT
        @i_server_id    = i_server_id
    FROM config_properties
    WHERE i_property_id = @i_property_id

    EXEC spm_DeletePropertyValuesByPropertyID{}VERSION_SUFFIX
        @ti_table_type = 0,
        @i_server_id   = @i_server_id,
        @i_property_id = @i_property_id
    EXEC spm_DeletePropertyValuesByPropertyID{}VERSION_SUFFIX
        @ti_table_type = 1,
        @i_server_id   = @i_server_id,
        @i_property_id = @i_property_id
    EXEC spm_DeletePropertyValuesByPropertyID{}VERSION_SUFFIX
        @ti_table_type = 2,
        @i_server_id   = @i_server_id,
        @i_property_id = @i_property_id

    DELETE config_perf_counters
    WHERE i_property_id = @i_property_id

    DELETE config_properties
    WHERE i_property_id = @i_property_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_DELETE_PROPERTY_BY_PROPERTY_ID})
    TRANRETURN""",
    },
    {
        "spName": "CreateTablePropertyValue",
        "description": "Create table property value",
        "inputParameters":
"""@ti_table_type       tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id         int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name = dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF NOT EXISTS
    (
        SELECT  *
        FROM    sysobjects
        WHERE   id = object_id(@vc_table_name) and OBJECTPROPERTY(id, N'IsUserTable') = 1
    )
    BEGIN
        SET @nvc_sql_query = '
            CREATE TABLE ' + @vc_table_name + '
            (
                bi_sequence_id bigint NOT NULL IDENTITY(1, 1),
                i_property_id int NOT NULL,
                f_property_value float NOT NULL DEFAULT ((0)),
                b_failed bit NOT NULL DEFAULT ((0)),
                dt_inserted_datetime datetime NOT NULL DEFAULT (GETUTCDATE())
                CONSTRAINT PK_sequence_id_' + CAST(@ti_table_type AS varchar) + CAST(@i_server_id AS varchar) + '
                PRIMARY KEY CLUSTERED (bi_sequence_id ) ON ' + dbo.fnm_GetFileGroupName{}VERSION_SUFFIX (@i_server_id) + '
            )
            CREATE UNIQUE INDEX [IX_property_id_datetime_' + CAST(@ti_table_type AS varchar) + CAST(@i_server_id AS varchar) + ']
                ON ' + @vc_table_name + '(i_property_id, dt_inserted_datetime)
                ON [INDEX_DATA]'
        EXEC sp_executesql @nvc_sql_query
    END

    TRANCHKERR({ERROR_CREATE_TABLE_PROPERTY_VALUE})
    TRANRETURN""",
    },
    {
        "spName": "TruncateTablePropertyValue",
        "description": "Truncate table property value",
        "inputParameters":
"""@ti_table_type       tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id         int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name = dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF EXISTS
    (
        SELECT  *
        FROM    sysobjects
        WHERE   id = object_id(@vc_table_name) and OBJECTPROPERTY(id, N'IsUserTable') = 1
    )
    BEGIN
        SET @nvc_sql_query = 'TRUNCATE TABLE ' + @vc_table_name + ''
        EXEC sp_executesql @nvc_sql_query
    END

    TRANCHKERR({ERROR_TRUNCATE_TABLE_PROPERTY_VALUE})
    TRANRETURN""",
    },
    {
        "spName": "DeletePropertyValuesByPropertyID",
        "description": "Delete property values by property ID",
        "inputParameters":
"""@ti_table_type       tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id         int,
    @i_property_id       int""",
        "sqlQuery":
"""TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name = dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF EXISTS
    (
        SELECT  *
        FROM    sysobjects
        WHERE   id = object_id(@vc_table_name) and OBJECTPROPERTY(id, N'IsUserTable') = 1
    )
    BEGIN
        SET @nvc_sql_query = '
            DELETE ' + @vc_table_name + '
            WHERE i_property_id = @i_property_id
            SELECT @@ROWCOUNT AS ''rowcount'''
        EXEC sp_executesql @nvc_sql_query,
            N'@i_property_id int',
            @i_property_id = @i_property_id
    END
    ELSE
    BEGIN
        SELECT 0 AS 'rowcount'
    END

    TRANCHKERR({ERROR_DELETE_PROPERTY_VALUES_BY_PROPERTY_ID})
    TRANRETURN""",
    },
    {
        "spName": "InsertPropertyValue",
        "description": "Insert property value",
        "inputParameters":
"""@ti_table_type          tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id            int,
    @i_property_id          int,
    @f_property_value       float,
    @b_failed               bit,
    @dt_inserted_datetime   datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name = dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@dt_inserted_datetime IS NULL)
        SET @dt_inserted_datetime = GETUTCDATE()

    SET @nvc_sql_query = '
        IF EXISTS
        (
            SELECT ''X''
            FROM ' + @vc_table_name + '
            WHERE i_property_id        = @i_property_id
              AND dt_inserted_datetime = @dt_inserted_datetime
        )
        BEGIN
            SELECT 0 AS ''identity''
        END
        ELSE
        BEGIN
            INSERT INTO ' + @vc_table_name + '
            (
                i_property_id,
                f_property_value,
                b_failed,
                dt_inserted_datetime
            )
            VALUES
            (
                @i_property_id,
                @f_property_value,
                @b_failed,
                @dt_inserted_datetime
            )
            SELECT @@IDENTITY AS ''identity''
        END'
    EXEC sp_executesql @nvc_sql_query,
        N'  @i_property_id          int,
            @f_property_value       float,
            @b_failed               bit,
            @dt_inserted_datetime   datetime',
        @i_property_id        = @i_property_id,
        @f_property_value     = @f_property_value,
        @b_failed             = @b_failed,
        @dt_inserted_datetime = @dt_inserted_datetime

    TRANCHKERR({ERROR_INSERT_PROPERTY_VALUE})
    TRANRETURN""",
    },
    {
        "spName": "GetPropertyValuesByPropertyIDAndDateTime",
        "description": "Get property values by property ID and dateTime.",
        "inputParameters":
"""@ti_table_type          tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id                 int,
    @i_property_id               int,
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name=dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    SET @nvc_sql_query='
        SELECT
            bi_sequence_id          AS ''sequenceID'',
            i_property_id           AS ''propertyID'',
            f_property_value        AS ''propertyValue'',
            b_failed                AS ''failed'',
            dt_inserted_datetime    AS ''insertedDateTime''
        FROM ' + @vc_table_name + ' WITH (FORCESEEK)
        WHERE i_property_id = @i_property_id'
    IF (@dt_inserted_datetime_from IS NULL AND @dt_inserted_datetime_to IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime < @dt_inserted_datetime_to, 21) ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'  @i_property_id               int,
                @dt_inserted_datetime_to   datetime',
            @i_property_id              = @i_property_id,
            @dt_inserted_datetime_to    = @dt_inserted_datetime_to
    END
    ELSE IF (@dt_inserted_datetime_to IS NULL AND @dt_inserted_datetime_from IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime >= @dt_inserted_datetime_from ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'  @i_property_id               int,
                @dt_inserted_datetime_from   datetime',
            @i_property_id              = @i_property_id,
            @dt_inserted_datetime_from  = @dt_inserted_datetime_from
    END
    ELSE IF (@dt_inserted_datetime_from IS NOT NULL AND @dt_inserted_datetime_to IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime >= @dt_inserted_datetime_from AND dt_inserted_datetime < @dt_inserted_datetime_to ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'  @i_property_id               int,
                @dt_inserted_datetime_from   datetime,
                @dt_inserted_datetime_to     datetime',
            @i_property_id              = @i_property_id,
            @dt_inserted_datetime_from  = @dt_inserted_datetime_from,
            @dt_inserted_datetime_to    = @dt_inserted_datetime_to
    END

    TRANCHKERR({ERROR_GET_PROPERTY_VALUES_BY_PROPERTY_ID_AND_DATETIME})
    TRANRETURN""",
    },
    {
        "spName": "GetPropertyValuesByPropertyIDsAndDateTime",
        "description": "Get property values summed by property IDs and dateTime.",
        "inputParameters":
"""@ti_table_type          tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id                 int,
    @vc_property_ids             varchar(8000),
    @dt_inserted_datetime_from   datetime,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_property_ids)
    SET @vc_property_ids = dbo.fnm_GetFilteredString{}VERSION_SUFFIX (@vc_property_ids)

    TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name=dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    SET @nvc_sql_query='
        SELECT
            bi_sequence_id AS ''sequenceID'',
            i_property_id AS ''propertyID'',
            f_property_value AS ''propertyValue'',
            b_failed AS ''failed'',
            dt_inserted_datetime AS ''insertedDateTime''
        FROM ' + @vc_table_name + ' WITH (FORCESEEK)
        WHERE i_property_id IN (' + @vc_property_ids + ')'
    IF (@dt_inserted_datetime_from IS NULL AND @dt_inserted_datetime_to IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime < @dt_inserted_datetime_to ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'@dt_inserted_datetime_to   datetime',
            @dt_inserted_datetime_to    = @dt_inserted_datetime_to
    END
    ELSE IF (@dt_inserted_datetime_to IS NULL AND @dt_inserted_datetime_from IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime >= @dt_inserted_datetime_from ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'@dt_inserted_datetime_from   datetime',
            @dt_inserted_datetime_from  = @dt_inserted_datetime_from
    END
    ELSE IF (@dt_inserted_datetime_from IS NOT NULL AND @dt_inserted_datetime_to IS NOT NULL)
    BEGIN
        SET @nvc_sql_query = @nvc_sql_query + ' AND dt_inserted_datetime >= @dt_inserted_datetime_from AND dt_inserted_datetime < @dt_inserted_datetime_to ORDER BY dt_inserted_datetime'
        EXEC sp_executesql @nvc_sql_query,
            N'  @dt_inserted_datetime_to   datetime,
                @dt_inserted_datetime_from datetime',
            @dt_inserted_datetime_to    = @dt_inserted_datetime_to,
            @dt_inserted_datetime_from  = @dt_inserted_datetime_from
    END

    TRANCHKERR({ERROR_GET_PROPERTY_VALUES_SUMMED_BY_PROPERTY_IDS_AND_DATETIME})
    TRANRETURN""",
    },
    {
        "spName": "DeletePropertyValuesByDateTime",
        "description": "Delete property values by dateTime.",
        "inputParameters":
"""@ti_table_type          tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id                 int,
    @dt_inserted_datetime_to     datetime""",
        "sqlQuery":
"""CHECK_NOTNULL(@dt_inserted_datetime_to)

    TRANINIT

    DECLARE @vc_table_name       varchar(200),
            @nvc_sql_query       nvarchar(4000)

    SET @vc_table_name=dbo.fnm_GetPropertyValueTableName{}VERSION_SUFFIX (@ti_table_type, @i_server_id)
    IF (@vc_table_name IS NULL)
        RAISERROR('Can not get property value table name.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF EXISTS
    (
        SELECT  *
        FROM    sysobjects
        WHERE   id = object_id(@vc_table_name) and OBJECTPROPERTY(id, N'IsUserTable') = 1
    )
    BEGIN
        SET @nvc_sql_query = '
            DELETE FROM ' + @vc_table_name + '
            WHERE dt_inserted_datetime < @dt_inserted_datetime_to
            SELECT @@ROWCOUNT AS ''rowcount'''
        EXEC sp_executesql @nvc_sql_query,
            N'@dt_inserted_datetime_to datetime',
            @dt_inserted_datetime_to = @dt_inserted_datetime_to
    END
    ELSE
    BEGIN
        SELECT 0 AS 'rowcount'
    END

    TRANCHKERR({ERROR_DELETE_PROPERTY_VALUES_BY_DATETIME})
    TRANRETURN""",
    },
    )

tableConfigProperties["fns"]=(
    {
        "fnName": "GetPropertyValueTableName",
        "fnType": "ScalarFunction",
        "inputParameters":
"""@ti_table_type           tinyint, -- 0 = latest, 1 = hourly, 2 = daily
    @i_server_id             int""",
        "returnType": "varchar(200)",
        "sqlQuery":
"""
    DECLARE @vc_table_name varchar(200)
    IF (@ti_table_type < 0 OR @ti_table_type > 2)
        SET @vc_table_name = NULL
    ELSE IF (@ti_table_type = 0)
        SET @vc_table_name = 'property_value_' + CAST(@i_server_id AS varchar) + '_latest'
    ELSE IF (@ti_table_type = 1)
        SET @vc_table_name = 'property_value_' + CAST(@i_server_id AS varchar) + '_hourly'
    ELSE IF (@ti_table_type = 2)
        SET @vc_table_name = 'property_value_' + CAST(@i_server_id AS varchar) + '_daily'
    RETURN @vc_table_name
""",
    },
    )
