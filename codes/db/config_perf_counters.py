tableConfigPerfCounters={
    "tableName": "config_perf_counters",
    "columns": (
        ("i_perfc_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_perfc_ref_id", "int", "NOT NULL"),
        ("i_server_id", "int", "NOT NULL"),
        ("i_property_id", "int", "NOT NULL"),
        ("i_refresh_config_interval_ms", "int", "NOT NULL", "DEFAULT ((0))"),
        ("i_probe_interval_ms", "int", "NOT NULL", "DEFAULT ((0))"),
        ("b_perfc_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "server_id_perfc_ref_id", "unique": True, "columns": ("i_server_id", "i_perfc_ref_id", ) },
        { "indexName": "perfc_ref_id", "unique": False, "columns": ("i_perfc_ref_id", ) },
        { "indexName": "server_id", "unique": False, "columns": ("i_server_id", ) },
        { "indexName": "property_id", "unique": True, "columns": ("i_property_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_server_id", "foreignTableName": "config_servers", "foreignColumnName": "i_server_id", },
        { "columnName": "i_perfc_ref_id", "foreignTableName": "config_perf_counter_references", "foreignColumnName": "i_perfc_ref_id", },
        { "columnName": "i_property_id", "foreignTableName": "config_properties", "foreignColumnName": "i_property_id", },
        ),
    }
tables.append(tableConfigPerfCounters)

tableConfigPerfCounters["sps"]=(
    {
        "spName": "GetPerfCountersByPerfcRefID",
        "description": "Get perf counters by pref counter reference ID",
        "inputParameters": """@i_perfc_ref_id           int""",
        "sqlQuery":
"""SELECT
        i_perfc_id                   AS 'perfcID',
        i_perfc_ref_id               AS 'perfcRefID',
        i_server_id                  AS 'serverID',
        i_property_id                AS 'propertyID',
        i_refresh_config_interval_ms AS 'refreshConfigIntervalMs',
        i_probe_interval_ms          AS 'probeIntervalMs',
        b_perfc_enabled              AS 'perfcEnabled',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counters WITH (FORCESEEK)
    WHERE i_perfc_ref_id             = @i_perfc_ref_id
    
    CHKERR({ERROR_GET_PERF_COUNTERS_BY_PERF_COUNTER_REFERENCE_ID})
    RETURN 0""",
    },
    {
        "spName": "GetFirstPropertyInsertedDateTimeByPerfcRefID",
        "description": "Get first property inserted datetime by perfc ref ID",
        "inputParameters": """@i_perfc_ref_id           int""",
        "sqlQuery":
"""SELECT TOP 1
        A.dt_inserted_datetime AS 'column'
    FROM config_properties A, config_perf_counters B WITH (FORCESEEK)
    WHERE A.i_property_id  = B.i_property_id
      AND B.i_perfc_ref_id = @i_perfc_ref_id
    ORDER BY A.dt_inserted_datetime

    CHKERR({GET_FIRST_PROPERTY_INSERTED_DATETIME_BY_PERFC_REF_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCountersByServerID",
        "description": "Get perf counters by server ID",
        "inputParameters": """@i_server_id           int""",
        "sqlQuery":
"""SELECT
        i_perfc_id                   AS 'perfcID',
        i_perfc_ref_id               AS 'perfcRefID',
        i_server_id                  AS 'serverID',
        i_property_id                AS 'propertyID',
        i_refresh_config_interval_ms AS 'refreshConfigIntervalMs',
        i_probe_interval_ms          AS 'probeIntervalMs',
        b_perfc_enabled              AS 'perfcEnabled',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counters WITH (FORCESEEK)
    WHERE i_server_id                = @i_server_id
    
    CHKERR({ERROR_GET_PERF_COUNTERS_BY_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCounterByPropertyID",
        "description": "Get perf counter by property ID",
        "inputParameters": """@i_property_id           int""",
        "sqlQuery":
"""SELECT
        i_perfc_id                   AS 'perfcID',
        i_perfc_ref_id               AS 'perfcRefID',
        i_server_id                  AS 'serverID',
        i_property_id                AS 'propertyID',
        i_refresh_config_interval_ms AS 'refreshConfigIntervalMs',
        i_probe_interval_ms          AS 'probeIntervalMs',
        b_perfc_enabled              AS 'perfcEnabled',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counters WITH (FORCESEEK)
    WHERE i_property_id              = @i_property_id
    
    CHKERR({ERROR_GET_PERF_COUNTER_BY_PROPERTY_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertPerfCounter",
        "description": "Insert perf counter",
        "inputParameters":
"""@i_perfc_ref_id                int,
    @i_server_id                    int,
    @i_property_id                  int,
    @b_perfc_enabled                bit""",
        "sqlQuery":
"""TRANINIT

    IF EXISTS (SELECT 'X' FROM config_perf_counter_references WHERE i_perfc_ref_id = @i_perfc_ref_id)
    BEGIN
        IF EXISTS (SELECT 'X' FROM config_servers WHERE i_server_id = @i_server_id)
        BEGIN
            IF EXISTS (SELECT 'X' FROM config_properties WHERE i_property_id = @i_property_id)
            BEGIN
                INSERT INTO config_perf_counters
                (
                    i_perfc_ref_id,
                    i_server_id,
                    i_property_id,
                    i_refresh_config_interval_ms,
                    i_probe_interval_ms,
                    b_perfc_enabled,
                    vc_updated_by,
                    dt_inserted_datetime,
                    dt_updated_datetime
                )
                VALUES
                (
                    @i_perfc_ref_id,
                    @i_server_id,
                    @i_property_id,
                    0,
                    0,
                    @b_perfc_enabled,
                    SYSTEM_USER,
                    GETUTCDATE(),
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

    TRANCHKERR({ERROR_INSERT_PERF_COUNTER})
    TRANRETURN""",
    }
    )