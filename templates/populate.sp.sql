SPHEADER({spm_$spName{}VERSION_SUFFIX})
GO

----------------------------------------------------------------------------
-- FILE NAME: spm_$spName.sql
----------------------------------------------------------------------------
--
-- Target Database:     Monitoring
-- Description:         $description
--                      
--
-- VERSION: $$Id: spm_$spName.sql#1 2009-08-03 FAREAST\\yincao $$
--
-- CHANGE HISTORY:
-- Date        Author     Version     Description
-- ----------  ---------  ----------  ----------------------------------------
-- 2009-08-03  yincao     1           Create

--[SqlMethod]
CREATE PROCEDURE spm_$spName{}VERSION_SUFFIX
    $inputParameters
AS
BEGIN
    SPINIT({spm_$spName{}VERSION_SUFFIX}) 

    $sqlQuery

END
GO


SPFOOTER({spm_$spName{}VERSION_SUFFIX})
GO

