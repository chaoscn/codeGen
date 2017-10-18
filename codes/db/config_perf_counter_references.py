tableConfigPerfCounterReferences={
    "tableName": "config_perf_counter_references",
    "columns": (
        ("i_perfc_ref_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_perfc_type_id", "int", "NOT NULL"),
        ("vc_perfc_category_name", "varchar(200)", "NOT NULL"),
        ("vc_perfc_instance_name", "varchar(200)", "NULL"),
        ("vc_perfc_name", "varchar(200)", "NOT NULL"),
        ("vc_full_text_index", "varchar(602)", "NOT NULL"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "perfc", "unique": True, "columns": ("vc_perfc_category_name", "vc_perfc_instance_name", "vc_perfc_name", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        { "indexName": "full_text_index", "fullText": True, "columns": ("vc_full_text_index", ) },
        ),
    "fks": (
        { "columnName": "i_perfc_type_id", "foreignTableName": "config_perf_counter_types", "foreignColumnName": "i_perfc_type_id", },
        ),
    "xmlIgnores": (
        "vc_full_text_index",
        ),
    }
tables.append(tableConfigPerfCounterReferences)

tableConfigPerfCounterReferences["sps"]=(
    {
        "spName": "CountPerfCounterReferencesBySearchCriteria",
        "description": "Count perf counter references by search criteria",
        "inputParameters":
"""@vc_search_criteria           varchar(400)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    SELECT COUNT(1) AS 'rowcount'
    FROM config_perf_counter_references
    WHERE CONTAINS(vc_full_text_index, @vc_search_criteria)

    CHKERR({ERROR_COUNT_PERF_COUNTER_REFERENCES_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "SearchPerfCounterReferencesBySearchCriteria",
        "description": "Search perf counter references by search criteria",
        "inputParameters":
"""@vc_search_criteria               varchar(400),
    @i_page_number                    int,
    @i_page_size                      int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_search_criteria)

    IF (@i_page_number <= 0)
        RAISERROR('Page number invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)
    IF (@i_page_size <= 0)
        RAISERROR('Page size invalid.', @DEFAULT_ERROR_LEVEL, @DEFAULT_ERROR_STATE, @ERROR_PREFIX)

    DECLARE @i_max_rowcount int
    SET @i_max_rowcount = @i_page_size * @i_page_number

    SELECT *
    FROM
    (
        SELECT TOP (@i_max_rowcount)
            i_perfc_ref_id               AS 'perfcRefID',
            i_perfc_type_id              AS 'perfcTypeID',
            vc_perfc_category_name       AS 'perfcCategoryName',
            vc_perfc_instance_name       AS 'perfcInstanceName',
            vc_perfc_name                AS 'perfcName',
            vc_full_text_index           AS 'fullTextIndex',
            vc_updated_by                AS 'updatedBy',
            dt_inserted_datetime         AS 'insertedDateTime',
            dt_updated_datetime          AS 'updatedDateTime',
            ROW_NUMBER() OVER (ORDER BY dt_inserted_datetime DESC) AS 'rowNumber'
        FROM config_perf_counter_references
        WHERE CONTAINS(vc_full_text_index, @vc_search_criteria)
        ORDER BY dt_inserted_datetime DESC
    ) A
    WHERE A.rowNumber > @i_max_rowcount - @i_page_size AND A.rowNumber <= @i_max_rowcount
    ORDER BY A.rowNumber

    CHKERR({ERROR_SEARCH_PERF_COUNTER_REFERENCES_BY_SEARCH_CRITERIA})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCounterReferenceByCategoryNameAndInstanceNameAndPerfcName",
        "description": "Get perf counter reference by category name and instance name and perfc name",
        "inputParameters":
"""@vc_perfc_category_name           varchar(200),
    @vc_perfc_instance_name           varchar(200),
    @vc_perfc_name                    varchar(200)""",
        "sqlQuery":
"""SELECT
        i_perfc_ref_id               AS 'perfcRefID',
        i_perfc_type_id              AS 'perfcTypeID',
        vc_perfc_category_name       AS 'perfcCategoryName',
        vc_perfc_instance_name       AS 'perfcInstanceName',
        vc_perfc_name                AS 'perfcName',
        vc_full_text_index           AS 'fullTextIndex',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counter_references WITH (FORCESEEK)
    WHERE vc_perfc_category_name = @vc_perfc_category_name
      AND vc_perfc_instance_name = @vc_perfc_instance_name
      AND vc_perfc_name          = @vc_perfc_name
    
    CHKERR({ERROR_GET_PERF_COUNTER_REFERENCE_BY_CATEGORY_NAME_AND_INSTANCE_NAME_AND_PERFC_NAME})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCounterReferencesByServerID",
        "description": "Get perf counter references by server ID",
        "inputParameters":
"""@i_server_id                  int""",
        "sqlQuery":
"""SELECT
        i_perfc_ref_id               AS 'perfcRefID',
        i_perfc_type_id              AS 'perfcTypeID',
        vc_perfc_category_name       AS 'perfcCategoryName',
        vc_perfc_instance_name       AS 'perfcInstanceName',
        vc_perfc_name                AS 'perfcName',
        vc_full_text_index           AS 'fullTextIndex',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counter_references
    WHERE i_perfc_ref_id IN
        (
            SELECT i_perfc_ref_id FROM config_perf_counters WITH (FORCESEEK) WHERE i_server_id = @i_server_id
        )
    
    CHKERR({ERROR_GET_PERF_COUNTER_REFERENCES_BY_SERVER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetPerfCounterReferenceByPerfCounterReferenceID",
        "description": "Get perf counter reference by perf counter reference ID",
        "inputParameters":
"""@i_perfc_ref_id                  int""",
        "sqlQuery":
"""SELECT
        i_perfc_ref_id               AS 'perfcRefID',
        i_perfc_type_id              AS 'perfcTypeID',
        vc_perfc_category_name       AS 'perfcCategoryName',
        vc_perfc_instance_name       AS 'perfcInstanceName',
        vc_perfc_name                AS 'perfcName',
        vc_full_text_index           AS 'fullTextIndex',
        vc_updated_by                AS 'updatedBy',
        dt_inserted_datetime         AS 'insertedDateTime',
        dt_updated_datetime          AS 'updatedDateTime'
    FROM config_perf_counter_references
    WHERE i_perfc_ref_id = @i_perfc_ref_id

    CHKERR({ERROR_GET_PERF_COUNTER_REFERENCE_BY_PERF_COUNTER_REFERENCE_ID})
    RETURN 0""",
    },
    {
        "spName": "InsertPerfCounterReference",
        "description": "Insert perf counter reference",
        "inputParameters":
"""@i_perfc_type_id                int,
    @vc_perfc_category_name         varchar(200),
    @vc_perfc_instance_name         varchar(200),
    @vc_perfc_name                  varchar(200)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_perfc_category_name)
    CHECK_NOTNULL(@vc_perfc_name)

    TRANINIT
    
    IF EXISTS
    (
        SELECT 'x'
        FROM config_perf_counter_references WITH (FORCESEEK)
        WHERE vc_perfc_category_name = @vc_perfc_category_name
          AND vc_perfc_instance_name = @vc_perfc_instance_name
          AND vc_perfc_name          = @vc_perfc_name
    )
    BEGIN
        SELECT 0 AS 'identity'
    END
    ELSE
    BEGIN
        INSERT INTO config_perf_counter_references
        (
            i_perfc_type_id,
            vc_perfc_category_name,
            vc_perfc_instance_name,
            vc_perfc_name,
            vc_full_text_index,
            vc_updated_by,
            dt_inserted_datetime,
            dt_updated_datetime
        )
        VALUES
        (
            @i_perfc_type_id,
            @vc_perfc_category_name,
            @vc_perfc_instance_name,
            @vc_perfc_name,
            @vc_perfc_category_name + ' ' + @vc_perfc_instance_name + ' ' + @vc_perfc_name,
            SYSTEM_USER,
            GETUTCDATE(),
            GETUTCDATE()
        )
        
        SELECT @@IDENTITY AS 'identity'
    END

    TRANCHKERR({ERROR_INSERT_PERF_COUNTER_REFERENCE})
    TRANRETURN""",
    },
    )