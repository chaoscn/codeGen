DECLARE @dashboardID                int
DECLARE @userID                     int
DECLARE @dashboardHashValue         varchar(max)
DECLARE @dashboardName              varchar(200)
DECLARE @dashboardShortName         varchar(30)
DECLARE @dashboardDescription       varchar(600)
DECLARE @dashboardSettingXml        varchar(max)
DECLARE @reportCount                int
DECLARE @dashboardPublic            bit
SET @dashboardID = 0
SET @userID = 2
WHILE (@userID <= 3)
BEGIN
    DECLARE @i    int
    SET @i = 1
    WHILE (@i <= 10)
    BEGIN
        SET @dashboardID = @dashboardID + 1
        SET @dashboardHashValue = CAST(@dashboardID AS varchar)
        SET @dashboardName = 'Dashboard Name ' + CAST(@dashboardID AS varchar)
        SET @dashboardShortName = 'Dashboard Short Name ' + CAST(@dashboardID AS varchar)
        SET @dashboardDescription = 'Dashboard Description ' + CAST(@dashboardID AS varchar)
        SET @dashboardSettingXml = 
            CASE @i
                WHEN 1 THEN '<DashboardSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DashboardItems><DashboardItem ReportID="1" DaySpan="1" HoursPerAggregatedValue="1" ChartTypeEnum="TEXT"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem><DashboardItem ReportID="1" DaySpan="1" HoursPerAggregatedValue="1" ChartTypeEnum="SPLINE"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem><DashboardItem ReportID="1" ViewReportTypeInt="1" DaySpan="2" HoursPerAggregatedValue="1" ChartTypeEnum="SPLINE"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem></DashboardItems></DashboardSettingRoot>'
                WHEN 2 THEN '<DashboardSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DashboardItems><DashboardItem ReportID="1" ViewReportTypeInt="1" DaySpan="2" HoursPerAggregatedValue="1" ChartTypeEnum="TEXT"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem><DashboardItem ReportID="1" ViewReportTypeInt="1" DaySpan="2" HoursPerAggregatedValue="1" ChartTypeEnum="SPLINE"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem></DashboardItems></DashboardSettingRoot>'
                WHEN 3 THEN '<DashboardSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DashboardItems><DashboardItem ReportID="1" ViewReportTypeInt="2" DaySpan="30" HoursPerAggregatedValue="1" ChartTypeEnum="TEXT"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem><DashboardItem ReportID="1" ViewReportTypeInt="2" DaySpan="30" HoursPerAggregatedValue="1" ChartTypeEnum="SPLINE"><DataCenterIDs><DataCenterID>1</DataCenterID><DataCenterID>2</DataCenterID></DataCenterIDs></DashboardItem></DashboardItems></DashboardSettingRoot>'
                ELSE '<DashboardSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DashboardItems><DashboardItem ReportID="' + CAST(@dashboardID AS varchar) + '" DaySpan="1" HoursPerAggregatedValue="1" ChartTypeEnum="TEXT"><DataCenterIDs><DataCenterID>1</DataCenterID></DataCenterIDs></DashboardItem></DashboardItems></DashboardSettingRoot>'
            END
        SET @reportCount = 
            CASE @i
                WHEN 1 THEN 3
                WHEN 2 THEN 2
                WHEN 3 THEN 2
                ELSE 1
            END
        SET @dashboardPublic = floor(rand()*2)
        EXEC spm_InsertDashboard{}VERSION_SUFFIX
            @i_user_id = @userID,
            @vc_dashboard_hash_value = @dashboardHashValue,
            @vc_dashboard_name = @dashboardName,
            @vc_dashboard_short_name = @dashboardShortName,
            @vc_dashboard_description = @dashboardDescription,
            @i_dashboard_type = 1,
            @x_dashboard_setting_xml = @dashboardSettingXml,
            @i_report_count = 1,
            @b_dashboard_public = @dashboardPublic

        SET @i = @i + 1
    END

    SET @userID = @userID + 1
END