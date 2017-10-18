DECLARE @dashboardID                int
DECLARE @userID                     int
DECLARE @dashboardGroupName         varchar(200)
DECLARE @dashboardGroupDescription  varchar(600)
DECLARE @dashboardGroupSettingXml   varchar(max)
DECLARE @dashboardGroupItems        varchar(max)
SET @dashboardID = 0
SET @userID = 2
WHILE (@userID <= 3)
BEGIN
    SET @dashboardGroupItems = ''
    DECLARE @i    int
    SET @i = 1
    WHILE (@i <= 10)
    BEGIN
        SET @dashboardID = @dashboardID + 1
        SET @dashboardGroupItems = @dashboardGroupItems + '<DashboardGroupItem DashboardID="' + CAST(@dashboardID AS varchar) + '" />'

        SET @i = @i + 1
    END
    
    SET @dashboardGroupName = 'Test Dashboard Group Name for User ID ' + CAST(@userID AS varchar)
    SET @dashboardGroupDescription = 'Test Dashboard Group Description for User ID ' + CAST(@userID AS varchar)
    SET @dashboardGroupSettingXml = '<DashboardGroupSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><DashboardGroupItems>' + @dashboardGroupItems + '</DashboardGroupItems></DashboardGroupSettingRoot>'
    EXEC spm_InsertDashboardGroup{}VERSION_SUFFIX
        @vc_dashboard_group_name = @dashboardGroupName,
        @vc_dashboard_group_description = @dashboardGroupDescription,
        @x_dashboard_group_setting_xml = @dashboardGroupSettingXml,
        @i_dashboard_count = 10

    SET @userID = @userID + 1
END