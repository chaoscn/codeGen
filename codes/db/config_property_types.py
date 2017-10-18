tableConfigPropertyTypes={
    "tableName": "config_property_types",
    "columns": (
        ("i_property_type_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_property_type_name", "varchar(200)", "NOT NULL"),
        ("i_property_type_value", "int", "NOT NULL"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "property_type_name", "unique": True, "columns": ("vc_property_type_name", ) },
        { "indexName": "property_type_value", "unique": True, "columns": ("i_property_type_value", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'PERFORMANCE_COUNTER'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'API_PARTNER'", "2", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'API_TEST'", "3", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigPropertyTypes)

tableConfigPropertyTypes["sps"]=(
    {
        "spName": "GetPropertyTypeByPropertyTypeValue",
        "description": "Get property type by property type value",
        "inputParameters": """@i_property_type_value           int""",
        "sqlQuery":
"""SELECT
        i_property_type_id      AS 'propertyTypeID',
        vc_property_type_name   AS 'propertyTypeName',
        i_property_type_value   AS 'propertyTypeValue',
        vc_updated_by           AS 'updatedBy',
        dt_inserted_datetime    AS 'insertedDateTime',
        dt_updated_datetime     AS 'updatedDateTime'
    FROM config_property_types WITH (FORCESEEK)
    WHERE i_property_type_value = @i_property_type_value
    
    CHKERR({ERROR_GET_PROPERTY_TYPE_BY_PROPERTY_TYPE_VALUE})
    RETURN 0""",
    },
    {
        "spName": "GetAllPropertyTypes",
        "description": "Get all property types",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_property_type_id      AS 'propertyTypeID',
        vc_property_type_name   AS 'propertyTypeName',
        i_property_type_value   AS 'propertyTypeValue',
        vc_updated_by           AS 'updatedBy',
        dt_inserted_datetime    AS 'insertedDateTime',
        dt_updated_datetime     AS 'updatedDateTime'
    FROM config_property_types
    ORDER BY i_property_type_id
    
    CHKERR({ERROR_GET_ALL_PROPERTY_TYPES})
    RETURN 0""",
    },
    {
        "spName": "InsertPropertyType",
        "description": "Insert property role",
        "inputParameters":
"""@vc_property_type_name           varchar(200),
    @i_property_type_value         int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_property_type_name)

    TRANINIT

    INSERT INTO config_property_types
    (
        vc_property_type_name,
        i_property_type_value,
        vc_updated_by,
        dt_inserted_datetime,
        dt_updated_datetime
    )
    VALUES
    (
        @vc_property_type_name,
        @i_property_type_value,
        SYSTEM_USER,
        GETUTCDATE(),
        GETUTCDATE()
    )
    
    SELECT @@IDENTITY AS 'identity'
    
    TRANCHKERR({ERROR_INSERT_PROPERTY_TYPE})
    TRANRETURN""",
    },
    )