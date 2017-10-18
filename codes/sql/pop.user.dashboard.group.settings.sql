EXEC spm_InsertUserDashboardGroupSetting{}VERSION_SUFFIX
    @i_user_id = 2,
    @i_dashboard_group_id = 1,
    @b_dashboard_group_owner = 1,
    @x_user_dashboard_group_setting_xml = '<UserDashboardGroupSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" />'
    
EXEC spm_InsertUserDashboardGroupSetting{}VERSION_SUFFIX
    @i_user_id = 3,
    @i_dashboard_group_id = 2,
    @b_dashboard_group_owner = 1,
    @x_user_dashboard_group_setting_xml = '<UserDashboardGroupSettingRoot xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" />'