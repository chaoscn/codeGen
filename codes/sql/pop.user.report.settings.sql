TRUNCATE TABLE user_report_settings

DECLARE @maxUserID int
DECLARE @maxReportID int
SET @maxUserID   = 7
SET @maxReportID = 200

DECLARE @userID int
DECLARE @reportID int
SET @userID      = 1
SET @reportID    = 1

DECLARE @reportOwner int
DECLARE @alertMe int

WHILE (@reportID <= @maxReportID AND @userID <= @maxUserID)
BEGIN
    SET @reportOwner = floor(rand()*2)
    SET @alertMe     = floor(rand()*2)
    EXEC spm_InsertUserReportSetting{}VERSION_SUFFIX
        @i_user_id                  = @userID,
        @i_report_id                = @reportID,
        @b_report_owner             = @reportOwner,
        @b_alert_me                 = @alertMe,
        @x_user_report_setting_xml  = '<UserReportSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" />'
    SET @userID = @userID + 1
    IF (@userID > @maxUserID)
    BEGIN
        SET @userID   = 1
        SET @reportID = @reportID + 1
    END
END