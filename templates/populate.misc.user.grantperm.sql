------------------------------------------------------------------------------
-- WARNING: Do NOT grant excessive permissions to any entity in this file. Every
-- permission grant here must be required and accounted for!
-- Contact AnoopA with questions. 
------------------------------------------------------------------------------

if not exists (select name from sysusers where issqlrole = 1 and name = 'MonitorOperators')
BEGIN
    EXEC sp_addrole 'MonitorOperators'
END
GO

$grantPermLines

GO
