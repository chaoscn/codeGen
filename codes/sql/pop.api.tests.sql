IF NOT EXISTS
(
    SELECT 'X'
    FROM config_api_tests
    WHERE vc_api_name = 'GetAccountInfo' AND i_data_center_id = 4
)
BEGIN
    INSERT INTO config_api_tests
        (vc_api_name, vc_api_description, vc_api_test_config_path, vc_api_trouble_shooting_uri, i_data_center_id, i_max_error_count, b_send_recovery_email, i_connectivity_property_id, i_latency_property_id, vc_updated_by, dt_inserted_datetime, dt_updated_datetime)
        VALUES
        ('GetAccountInfo', 'GetAccountInfo', '..\Config\MonitoringAPITest\GetAccountInfo.xml', NULL, 4, 3, 0, 0, 0, SYSTEM_USER, GETUTCDATE(), GETUTCDATE())
END

IF NOT EXISTS
(
    SELECT 'X'
    FROM config_api_tests
    WHERE vc_api_name = 'GetPaymentInstruments' AND i_data_center_id = 4
)
BEGIN
    INSERT INTO config_api_tests
        (vc_api_name, vc_api_description, vc_api_test_config_path, vc_api_trouble_shooting_uri, i_data_center_id, i_max_error_count, b_send_recovery_email, i_connectivity_property_id, i_latency_property_id, vc_updated_by, dt_inserted_datetime, dt_updated_datetime)
        VALUES
        ('GetPaymentInstruments', 'GetPaymentInstruments', '..\Config\MonitoringAPITest\GetPaymentInstruments.xml', NULL, 4, 3, 0, 0, 0, SYSTEM_USER, GETUTCDATE(), GETUTCDATE())
END

IF NOT EXISTS
(
    SELECT 'X'
    FROM config_api_tests
    WHERE vc_api_name = 'GetPaymentInstrumentsEx' AND i_data_center_id = 4
)
BEGIN
    INSERT INTO config_api_tests
        (vc_api_name, vc_api_description, vc_api_test_config_path, vc_api_trouble_shooting_uri, i_data_center_id, i_max_error_count, b_send_recovery_email, i_connectivity_property_id, i_latency_property_id, vc_updated_by, dt_inserted_datetime, dt_updated_datetime)
        VALUES
        ('GetPaymentInstrumentsEx', 'GetPaymentInstrumentsEx', '..\Config\MonitoringAPITest\GetPaymentInstrumentsEx.xml', NULL, 4, 3, 0, 0, 0, SYSTEM_USER, GETUTCDATE(), GETUTCDATE())
END

IF NOT EXISTS
(
    SELECT 'X'
    FROM config_api_tests
    WHERE vc_api_name = 'GetSubscriptions' AND i_data_center_id = 4
)
BEGIN
    INSERT INTO config_api_tests
        (vc_api_name, vc_api_description, vc_api_test_config_path, vc_api_trouble_shooting_uri, i_data_center_id, i_max_error_count, b_send_recovery_email, i_connectivity_property_id, i_latency_property_id, vc_updated_by, dt_inserted_datetime, dt_updated_datetime)
        VALUES
        ('GetSubscriptions', 'GetSubscriptions', '..\Config\MonitoringAPITest\GetSubscriptions.xml', NULL, 4, 3, 0, 0, 0, SYSTEM_USER, GETUTCDATE(), GETUTCDATE())
END

IF NOT EXISTS
(
    SELECT 'X'
    FROM config_api_tests
    WHERE vc_api_name = 'TestConnection' AND i_data_center_id = 4
)
BEGIN
    INSERT INTO config_api_tests
        (vc_api_name, vc_api_description, vc_api_test_config_path, vc_api_trouble_shooting_uri, i_data_center_id, i_max_error_count, b_send_recovery_email, i_connectivity_property_id, i_latency_property_id, vc_updated_by, dt_inserted_datetime, dt_updated_datetime)
        VALUES
        ('TestConnection', 'TestConnection', '..\Config\MonitoringAPITest\TestConnection.xml', NULL, 4, 3, 0, 0, 0, SYSTEM_USER, GETUTCDATE(), GETUTCDATE())
END