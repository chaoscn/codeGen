DECLARE @serverID           int
DECLARE @extractorTypeID    int
DECLARE @extractorActionID  int
DECLARE @dateTime           datetime

SET @serverID    = 1
WHILE (@serverID <= 100)
BEGIN
    SET @extractorTypeID    = rand() * 4 + 1
    SET @extractorActionID  = rand() * 2 + 1
    SET @dateTime           = DATEADD(hh, @serverID - 101, GETUTCDATE())
    EXEC spm_InsertExtractorLog{}VERSION_SUFFIX
        @i_server_id               = @serverID,
        @i_extractor_type_id       = @extractorTypeID,
        @i_extractor_action_id     = @extractorActionID,
        @t_extractor_message       = 'test lksjdflwejf test',
        @dt_inserted_datetime      = @dateTime
    SET @serverID = @serverID + 1
END