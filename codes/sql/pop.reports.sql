DECLARE @dateTime datetime
SET @dateTime = DATEADD(dd, -1, GETUTCDATE())
EXEC spm_InsertReport{}VERSION_SUFFIX
    @vc_report_hash_value           = '0000000000000000000',
    @vc_report_name                 = 'API GetAccountInfo abcdefg hijklmn',
    @vc_report_short_name           = 'GetAccountInfo',
    @vc_report_description          = 'GetAccountInfo GetAccountInfo GetAccountInfo GetAccountInfo',
    @i_report_type                  = 2,
    @x_report_data_source_xml       = '<ReportSourceRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportFormula><NumeratorValues><ReportFormulaValue Factor="5"><PropertyTypeAndID Type="PERFORMANCE_COUNTER" ID="1" /></ReportFormulaValue></NumeratorValues><DenominatorValues /></ReportFormula></ReportSourceRoot>',
    @x_report_setting_xml           = '<ReportSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" IsAverage="true" IsPercentage="true"><CellThemes><CellTheme LowerBoundEquals="true" UpperBoundEquals="true" LowerBound="50" UpperBound="100" ThemeIndex="1" /><CellTheme LowerBoundEquals="true" UpperBoundEquals="true" LowerBound="0" UpperBound="20" ThemeIndex="2" /><CellTheme LowerBoundEquals="true" UpperBoundEquals="true" LowerBound="30" UpperBound="40" ThemeIndex="3" /></CellThemes></ReportSettingRoot>',
    @x_report_alert_xml             = '<ReportAlertRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportAlerts><ReportAlert LowerBound="1" UpperBound="50"><WithinHours /><WithinWeekdays /><WithinDays /><WithinMonths /></ReportAlert></ReportAlerts></ReportAlertRoot>',
    @dt_hourly_aggregated_datetime  = @dateTime,
    @dt_daily_aggregated_datetime   = @dateTime,
    @b_report_public                = 1,
    @b_report_ready                 = 1

EXEC spm_InsertReport{}VERSION_SUFFIX
    @vc_report_hash_value           = '0000000000000000001',
    @vc_report_name                 = 'API GetPaymentInstruments abcdefg hijklmn',
    @vc_report_short_name           = 'GetPaymentInstruments',
    @vc_report_description          = 'GetPaymentInstruments GetPaymentInstruments GetPaymentInstruments GetPaymentInstruments',
    @i_report_type                  = 1,
    @x_report_data_source_xml       = '<ReportSourceRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportFormula><NumeratorValues><ReportFormulaValue Factor="5"><PropertyTypeAndID Type="PERFORMANCE_COUNTER" ID="1" /></ReportFormulaValue></NumeratorValues><DenominatorValues /></ReportFormula></ReportSourceRoot>',
    @x_report_setting_xml           = '<ReportSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" IsAverage="false" IsPercentage="false"><CellThemes></CellThemes></ReportSettingRoot>',
    @x_report_alert_xml             = '<ReportAlertRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportAlerts><ReportAlert LowerBound="1" UpperBound="50"><WithinHours /><WithinWeekdays /><WithinDays /><WithinMonths /></ReportAlert></ReportAlerts></ReportAlertRoot>',
    @dt_hourly_aggregated_datetime  = @dateTime,
    @dt_daily_aggregated_datetime   = @dateTime,
    @b_report_public                = 1,
    @b_report_ready                 = 1

DECLARE @index      int
DECLARE @hashValue  varchar(200)
DECLARE @reportType int
DECLARE @isPublic   int
DECLARE @isReady    int
SET @index = 0
WHILE (@index < 200)
BEGIN
    SET @hashValue  = 'abcdef' + CAST(@index AS varchar)
    SET @reportType = 1 + floor(rand()*2)
    SET @isPublic   = floor(rand()*2)
    SET @isReady    = floor(rand()*2)
    EXEC spm_InsertReport{}VERSION_SUFFIX
        @vc_report_hash_value           = @hashValue,
        @vc_report_name                 = 'API GetPaymentInstruments abcdefg hijklmn',
        @vc_report_short_name           = 'GetPaymentInstruments',
        @vc_report_description          = 'GetPaymentInstruments GetPaymentInstruments GetPaymentInstruments GetPaymentInstruments',
        @i_report_type                  = @reportType,
        @x_report_data_source_xml       = '<ReportSourceRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportFormula><NumeratorValues><ReportFormulaValue Factor="5"><PropertyTypeAndID Type="PERFORMANCE_COUNTER" ID="1" /></ReportFormulaValue></NumeratorValues><DenominatorValues /></ReportFormula></ReportSourceRoot>',
        @x_report_setting_xml           = '<ReportSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" IsAverage="true" IsPercentage="true" />',
        @x_report_alert_xml             = '<ReportAlertRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><ReportAlerts><ReportAlert LowerBound="1" UpperBound="50"><WithinHours /><WithinWeekdays /><WithinDays /><WithinMonths /></ReportAlert></ReportAlerts></ReportAlertRoot>',
        @dt_hourly_aggregated_datetime  = @dateTime,
        @dt_daily_aggregated_datetime   = @dateTime,
        @b_report_public                = @isPublic,
        @b_report_ready                 = @isReady
    SET @index = @index + 1
END