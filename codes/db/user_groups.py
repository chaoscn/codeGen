tableUserGroups={
    "tableName": "user_groups",
    "columns": (
        ("i_user_group_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_user_group_name", "varchar(200)", "NOT NULL"),
        ("vc_user_group_description", "varchar(600)", "NOT NULL"),
        ("i_user_count", "int", "NOT NULL", "DEFAULT ((0))"),
        ("bi_user_group_flags", "bigint", "NOT NULL", "DEFAULT ((0))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_group_name", "unique": True, "columns": ("vc_user_group_name", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'Administrators'", "'M&R system administrators'", "'1'", "1|2|4", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Users'", "'M&R system users'", "'0'", "2|4", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Guests'", "'M&R system guests'", "'0'", "4", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
"""
FLAG_SYSTEM_ADMIN: 0x01
FLAG_REPORT_USER: 0x02
FLAG_REPORT_GUEST: 0x04
"""
tables.append(tableUserGroups)

tableUserGroups["dataObjectExtra"]="""
        protected static readonly long FLAG_SYSTEM_ADMIN = 0x01;
        protected static readonly long FLAG_REPORT_USER = 0x02;
        protected static readonly long FLAG_REPORT_GUEST = 0x04;

        [XmlElement]
        public bool IsSystemAdmin
        {
            get { return (UserGroupFlags & FLAG_SYSTEM_ADMIN) == FLAG_SYSTEM_ADMIN; }
            set { UserGroupFlags |= FLAG_SYSTEM_ADMIN; }
        }

        [XmlElement]
        public bool IsReportUser
        {
            get { return (UserGroupFlags & FLAG_REPORT_USER) == FLAG_REPORT_USER; }
            set { UserGroupFlags |= FLAG_REPORT_USER; }
        }

        [XmlElement]
        public bool IsReportGuest
        {
            get { return (UserGroupFlags & FLAG_REPORT_GUEST) == FLAG_REPORT_GUEST; }
            set { UserGroupFlags |= FLAG_REPORT_GUEST; }
        }
"""

tableUserGroups["sps"]=(
    {
        "spName": "GetUserGroupByGroupID",
        "description": "Get user group by group ID",
        "inputParameters":
"""@i_user_group_id          int""",
        "sqlQuery":
"""SELECT
        i_user_group_id             AS 'userGroupID',
        vc_user_group_name          AS 'userGroupName',
        vc_user_group_description   AS 'userGroupDescription',
        i_user_count                AS 'userCount',
        bi_user_group_flags         AS 'userGroupFlags',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM user_groups
    WHERE i_user_group_id       = @i_user_group_id
    
    CHKERR({ERROR_GET_USER_GROUP_BY_GROUP_ID})
    RETURN 0""",
    },
    {
        "spName": "GetAllUserGroups",
        "description": "Get all user groups",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_user_group_id             AS 'userGroupID',
        vc_user_group_name          AS 'userGroupName',
        vc_user_group_description   AS 'userGroupDescription',
        i_user_count                AS 'userCount',
        bi_user_group_flags         AS 'userGroupFlags',
        vc_updated_by               AS 'updatedBy',
        dt_inserted_datetime        AS 'insertedDateTime',
        dt_updated_datetime         AS 'updatedDateTime'
    FROM user_groups
    ORDER BY vc_user_group_name ASC
    
    CHKERR({ERROR_GET_ALL_USER_GROUPS})
    RETURN 0""",
    },
    {
        "spName": "UpdateUserGroup",
        "description": "Update user group",
        "inputParameters":
"""@i_user_group_id             int,
    @vc_user_group_name          varchar(200),
    @vc_user_group_description   varchar(600),
    @bi_user_group_flags         bigint""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_user_group_name)
    CHECK_NOTNULL(@vc_user_group_description)

    TRANINIT

    UPDATE user_groups
    SET
        vc_user_group_name          = @vc_user_group_name,
        vc_user_group_description   = @vc_user_group_description,
        bi_user_group_flags         = @bi_user_group_flags,
        vc_updated_by               = SYSTEM_USER,
        dt_updated_datetime         = GETUTCDATE()
    WHERE i_user_group_id           = @i_user_group_id
    
    SELECT @@ROWCOUNT AS 'rowcount'
    
    TRANCHKERR({ERROR_UPDATE_USER_GROUP})
    TRANRETURN""",
    },
    )