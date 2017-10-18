tableConfigPerfCounterTypes={
    "tableName": "config_perf_counter_types",
    "columns": (
        ("i_perfc_type_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_perfc_type_name", "varchar(200)", "NOT NULL"),
        ("i_perfc_type_value", "int", "NOT NULL"),
        ("b_accumulate", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("b_percentage", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "perfc_type_name", "unique": True, "columns": ("vc_perfc_type_name", ) },
        { "indexName": "perfc_type_value", "unique": True, "columns": ("i_perfc_type_value", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'NumberOfItemsHEX32'", "0", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'NumberOfItemsHEX64'", "256", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'NumberOfItems32'", "65536", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'NumberOfItems64'", "65792", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterDelta32'", "4195328", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterDelta64'", "4195584", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SampleCounter'", "4260864", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CountPerTimeInterval32'", "4523008", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CountPerTimeInterval64'", "4523264", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'RateOfCountsPerSecond32'", "272696320", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'RateOfCountsPerSecond64'", "272696576", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'RawFraction'", "537003008", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterTimer'", "541132032", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Timer100Ns'", "542180608", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SampleFraction'", "549585920", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterTimerInverse'", "557909248", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Timer100NsInverse'", "558957824", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterMultiTimer'", "574686464", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterMultiTimer100Ns'", "575735040", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterMultiTimerInverse'", "591463680", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterMultiTimer100NsInverse'", "592512256", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'AverageTimer32'", "805438464", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'ElapsedTime'", "807666944", "1", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'AverageCount64'", "1073874176", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'SampleBase'", "1073939457", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'AverageBase'", "1073939458", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'RawBase'", "1073939459", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'CounterMultiBase'", "1107494144", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'542573824'", "542573824", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'537003264'", "537003264", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'1073939712'", "1073939712", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'5571840'", "5571840", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigPerfCounterTypes)

tableConfigPerfCounterTypes["sps"]=(
    {
        "spName": "GetAllPerfCounterTypes",
        "description": "Get all perf counter types",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_perfc_type_id        AS 'perfcTypeID',
        vc_perfc_type_name     AS 'perfcTypeName',
        i_perfc_type_value     AS 'perfcTypeValue',
        b_accumulate           AS 'accumulate',
        b_percentage           AS 'percentage',
        vc_updated_by          AS 'updatedBy',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM config_perf_counter_types
    ORDER BY i_perfc_type_id
    
    CHKERR({ERROR_GET_All_PERF_COUNTER_TYPES})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCounterTypeByRefID",
        "description": "Get perf counter type by ref ID",
        "inputParameters": """@i_perfc_ref_id           int""",
        "sqlQuery":
"""SELECT
        i_perfc_type_id        AS 'perfcTypeID',
        vc_perfc_type_name     AS 'perfcTypeName',
        i_perfc_type_value     AS 'perfcTypeValue',
        b_accumulate           AS 'accumulate',
        b_percentage           AS 'percentage',
        vc_updated_by          AS 'updatedBy',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM config_perf_counter_types
    WHERE i_perfc_type_id = 
        (
            SELECT TOP 1 i_perfc_type_id
            FROM config_perf_counter_references
            WHERE i_perfc_ref_id = @i_perfc_ref_id
        )
    
    CHKERR({ERROR_GET_PERF_COUNTER_TYPE_BY_REF_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertPerfCounterType",
        "description": "Insert perf counter type",
        "inputParameters":
"""@vc_perfc_type_name   varchar(200),
    @i_perfc_type_value   int,
    @b_accumulate         bit, 
    @b_percentage         bit""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_perfc_type_name)

    TRANINIT

    IF EXISTS
    (
        SELECT 'x'
        FROM config_perf_counter_types WITH (FORCESEEK)
        WHERE vc_perfc_type_name = @vc_perfc_type_name
           OR i_perfc_type_value = @i_perfc_type_value
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        INSERT INTO config_perf_counter_types
        (
            vc_perfc_type_name,
            i_perfc_type_value,
            b_accumulate,
            b_percentage,
            vc_updated_by,
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @vc_perfc_type_name,
            @i_perfc_type_value,
            @b_accumulate,
            @b_percentage,
            SYSTEM_USER,
            GETUTCDATE(),
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END

    TRANCHKERR({ERROR_INSERT_PERF_COUNTER_TYPE})
    TRANRETURN""",
    },
    {
        "spName": "GetPerfCounterTypeByTypeValue",
        "description": "Get perf counter type by perf counter type value",
        "inputParameters": """@i_perfc_type_value           int""",
        "sqlQuery":
"""SELECT
        i_perfc_type_id        AS 'perfcTypeID',
        vc_perfc_type_name     AS 'perfcTypeName',
        i_perfc_type_value     AS 'perfcTypeValue',
        b_accumulate           AS 'accumulate',
        b_percentage           AS 'percentage',
        vc_updated_by          AS 'updatedBy',
        dt_inserted_datetime   AS 'insertedDateTime',
        dt_updated_datetime    AS 'updatedDateTime'
    FROM config_perf_counter_types
    WHERE i_perfc_type_value = @i_perfc_type_value
    
    CHKERR({ERROR_GET_PERF_COUNTER_TYPE_BY_TYPE_VALUE})
    RETURN 0""",
    },    
    )