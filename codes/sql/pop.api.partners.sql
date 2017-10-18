DECLARE @apiID          int
SET @apiID = 1
WHILE (@apiID <= 436)
BEGIN
    EXEC spm_InsertAPIPartner{}VERSION_SUFFIX
        @i_api_id       = @apiID,
        @i_partner_id   = 1
    SET @apiID = @apiID + 1
END