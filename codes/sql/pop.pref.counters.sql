DECLARE @perfcRefID          int
SET @perfcRefID = 1
WHILE (@perfcRefID <= 216)
BEGIN
    EXEC spm_InsertPerfCounter{}VERSION_SUFFIX
        @i_perfc_ref_id  = @perfcRefID,
        @i_server_id     = 1,
        @i_property_id   = @perfcRefID,
        @b_perfc_enabled = 1
    SET @perfcRefID = @perfcRefID + 1
END