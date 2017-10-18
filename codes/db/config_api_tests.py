tableConfigAPITests={
    "tableName": "config_api_tests",
    "columns": (
        ("i_api_test_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_api_name", "varchar(200)", "NOT NULL"),
        ("vc_api_description", "varchar(600)", "NULL", "DEFAULT ((NULL))"),
        ("vc_api_test_config_path", "varchar(600)", "NOT NULL"),
        ("vc_api_trouble_shooting_uri", "varchar(256)", "NULL", "DEFAULT ((NULL))"),
        ("i_data_center_id", "int", "NOT NULL"),
        ("i_max_error_count", "int", "NOT NULL", "DEFAULT ((1))"),
        ("b_send_recovery_email", "bit", "NOT NULL", "DEFAULT ((0))"),
        ("i_connectivity_property_id", "int", "NOT NULL", "DEFAULT ((0))"),
        ("i_latency_property_id", "int", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "api_name", "unique": False, "columns": ("vc_api_name", ) },
        { "indexName": "data_center_id", "unique": False, "columns": ("i_data_center_id", ) },
        { "indexName": "connectivity_property_id_latency_property_id", "unique": False, "columns": ("i_connectivity_property_id", "i_latency_property_id", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "fks": (
        { "columnName": "i_data_center_id", "foreignTableName": "config_data_centers", "foreignColumnName": "i_data_center_id", },
        ),
    "initialDataWhereIndex": (1, 5, ),
    "initialData": (
        { "dataLine": ("'GetAccountInfo'", "'GetAccountInfo'", "'..\Config\MonitoringAPITest\GetAccountInfo.xml'", "NULL", "1", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstruments'", "'GetPaymentInstruments'", "'..\Config\MonitoringAPITest\GetPaymentInstruments.xml'", "NULL", "1", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstrumentsEx'", "'GetPaymentInstrumentsEx'", "'..\Config\MonitoringAPITest\GetPaymentInstrumentsEx.xml'", "NULL", "1", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetSubscriptions'", "'GetSubscriptions'", "'..\Config\MonitoringAPITest\GetSubscriptions.xml'", "NULL", "1", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'TestConnection'", "'TestConnection'", "'..\Config\MonitoringAPITest\TestConnection.xml'", "NULL", "1", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetAccountInfo'", "'GetAccountInfo'", "'..\Config\MonitoringAPITest\GetAccountInfo.xml'", "NULL", "2", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstruments'", "'GetPaymentInstruments'", "'..\Config\MonitoringAPITest\GetPaymentInstruments.xml'", "NULL", "2", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstrumentsEx'", "'GetPaymentInstrumentsEx'", "'..\Config\MonitoringAPITest\GetPaymentInstrumentsEx.xml'", "NULL", "2", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetSubscriptions'", "'GetSubscriptions'", "'..\Config\MonitoringAPITest\GetSubscriptions.xml'", "NULL", "2", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'TestConnection'", "'TestConnection'", "'..\Config\MonitoringAPITest\TestConnection.xml'", "NULL", "2", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetAccountInfo'", "'GetAccountInfo'", "'..\Config\MonitoringAPITest\GetAccountInfo.xml'", "NULL", "3", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstruments'", "'GetPaymentInstruments'", "'..\Config\MonitoringAPITest\GetPaymentInstruments.xml'", "NULL", "3", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetPaymentInstrumentsEx'", "'GetPaymentInstrumentsEx'", "'..\Config\MonitoringAPITest\GetPaymentInstrumentsEx.xml'", "NULL", "3", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'GetSubscriptions'", "'GetSubscriptions'", "'..\Config\MonitoringAPITest\GetSubscriptions.xml'", "NULL", "3", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'TestConnection'", "'TestConnection'", "'..\Config\MonitoringAPITest\TestConnection.xml'", "NULL", "3", "3", "0", "0", "0", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigAPITests)

tableConfigAPITests["sps"]=(
    {
        "spName": "GetAllAPITests",
        "description": "Get all API tests",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_api_test_id               AS 'apiTestID',
        vc_api_name                 AS 'apiName',
        vc_api_description          AS 'apiDescription',
        vc_api_test_config_path     AS 'apiTestConfigPath',
        vc_api_trouble_shooting_uri AS 'apiTroubleShootingURI',
        i_data_center_id            AS 'dataCenterID',
        i_max_error_count           AS 'maxErrorCount',
        b_send_recovery_email       AS 'sendRecoveryEmail',
        i_connectivity_property_id  AS 'connectivityPropertyID',
        i_latency_property_id       AS 'latencyPropertyID',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM config_api_tests
    ORDER BY i_api_test_id

    CHKERR({ERROR_GET_ALL_API_TESTS})
    RETURN 0""",
    },
    {
        "spName": "GetAPITestsByDataCenterID",
        "description": "Get API tests by data center ID",
        "inputParameters":
"""@i_data_center_id int""",
        "sqlQuery":
"""SELECT
        i_api_test_id               AS 'apiTestID',
        vc_api_name                 AS 'apiName',
        vc_api_description          AS 'apiDescription',
        vc_api_test_config_path     AS 'apiTestConfigPath',
        vc_api_trouble_shooting_uri AS 'apiTroubleShootingURI',
        i_data_center_id            AS 'dataCenterID',
        i_max_error_count           AS 'maxErrorCount',
        b_send_recovery_email       AS 'sendRecoveryEmail',
        i_connectivity_property_id  AS 'connectivityPropertyID',
        i_latency_property_id       AS 'latencyPropertyID',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM config_api_tests WITH (FORCESEEK)
    WHERE i_data_center_id          = @i_data_center_id

    CHKERR({ERROR_GET_API_TESTS_BY_DATA_CENTER_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAPITestByAPITestID",
        "description": "Get API test by API test ID",
        "inputParameters":
"""@i_api_test_id int""",
        "sqlQuery":
"""SELECT
        i_api_test_id               AS 'apiTestID',
        vc_api_name                 AS 'apiName',
        vc_api_description          AS 'apiDescription',
        vc_api_test_config_path     AS 'apiTestConfigPath',
        vc_api_trouble_shooting_uri AS 'apiTroubleShootingURI',
        i_data_center_id            AS 'dataCenterID',
        i_max_error_count           AS 'maxErrorCount',
        b_send_recovery_email       AS 'sendRecoveryEmail',
        i_connectivity_property_id  AS 'connectivityPropertyID',
        i_latency_property_id       AS 'latencyPropertyID',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM config_api_tests
    WHERE i_api_test_id             = @i_api_test_id

    CHKERR({ERROR_GET_API_TEST_BY_API_TEST_ID})
    RETURN 0""",
    },
    {
        "spName": "GetFirstPropertyInsertedDateTimeByAPITestID",
        "description": "Get first property inserted datetime by API test ID",
        "inputParameters": """@i_api_test_id           int""",
        "sqlQuery":
"""SELECT TOP 1
        A.dt_inserted_datetime AS 'column'
    FROM config_properties A, config_api_tests B
    WHERE (A.i_property_id = B.i_connectivity_property_id OR A.i_property_id = B.i_latency_property_id)
      AND B.i_api_test_id = @i_api_test_id
    ORDER BY A.dt_inserted_datetime

    CHKERR({GET_FIRST_PROPERTY_INSERTED_DATETIME_BY_API_TEST_ID})
    RETURN 0""",
    },
    {
        "spName": "UpdateAPITest",
        "description": "Update API test",
        "inputParameters":
"""@i_api_test_id               int,
    @vc_api_name                 varchar(200),
    @vc_api_description          varchar(600),
    @vc_api_test_config_path     varchar(600),
    @vc_api_trouble_shooting_uri varchar(256),
    @i_data_center_id            int,
    @i_max_error_count           int,
    @b_send_recovery_email       bit,
    @i_connectivity_property_id  int,
    @i_latency_property_id       int""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_api_name)
    CHECK_NOTNULL(@vc_api_test_config_path)

    TRANINIT

    UPDATE config_api_tests
    SET
        vc_api_name                 = @vc_api_name,
        vc_api_description          = @vc_api_description,
        vc_api_test_config_path     = @vc_api_test_config_path,
        vc_api_trouble_shooting_uri = @vc_api_trouble_shooting_uri,
        i_data_center_id            = @i_data_center_id,
        i_max_error_count           = @i_max_error_count,
        b_send_recovery_email       = @b_send_recovery_email,
        i_connectivity_property_id  = @i_connectivity_property_id,
        i_latency_property_id       = @i_latency_property_id,
        vc_updated_by               = SYSTEM_USER,
        dt_updated_datetime         = GETUTCDATE()
    WHERE i_api_test_id             = @i_api_test_id

    SELECT @@ROWCOUNT AS 'rowcount'

    TRANCHKERR({ERROR_UPDATE_API_TEST})
    TRANRETURN""",
    },
    )