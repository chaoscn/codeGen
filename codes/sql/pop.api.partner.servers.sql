DECLARE @apiPartnerID          int
DECLARE @propertyID          int
SET @apiPartnerID = 1
WHILE (@apiPartnerID <= 436)
BEGIN
    SET @propertyID = 216 + @apiPartnerID
    EXEC spm_InsertAPIPartnerServer{}VERSION_SUFFIX
        @i_api_partner_id   = @apiPartnerID,
        @i_server_id        = 1,
        @i_property_id      = @propertyID
    SET @apiPartnerID = @apiPartnerID + 1
END