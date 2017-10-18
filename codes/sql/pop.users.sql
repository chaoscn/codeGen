DECLARE @domainName varchar(200)
DECLARE @userName varchar(200)
SET @domainName = SUBSTRING(SYSTEM_USER, 0, CHARINDEX('\', SYSTEM_USER))
SET @userName = SUBSTRING(SYSTEM_USER, LEN(@domainName)+2, LEN(SYSTEM_USER)-LEN(@domainName)-1)

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = @userName,
    @vc_user_emails  = @userName,
    @i_user_group_id = 2,
    @b_user_disabled =0

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = 'tester',
    @vc_user_emails  = 'tester',
    @i_user_group_id = 2,
    @b_user_disabled =0

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = 'haha',
    @vc_user_emails  = 'haha',
    @i_user_group_id = 2,
    @b_user_disabled =0

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = 'heihei',
    @vc_user_emails  = 'heihei',
    @i_user_group_id = 2,
    @b_user_disabled =0

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = 'god',
    @vc_user_emails  = 'god',
    @i_user_group_id = 2,
    @b_user_disabled =0

EXEC spm_InsertUser{}VERSION_SUFFIX
    @vc_user_domain  = @domainName,
    @vc_user_alias   = 'buddha',
    @vc_user_emails  = 'buddha',
    @i_user_group_id = 2,
    @b_user_disabled =0
