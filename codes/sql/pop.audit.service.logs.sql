DECLARE @i                  int
DECLARE @serviceTypeID      int
DECLARE @serviceActionID    int
DECLARE @dateTime           datetime

SET @i    = 1
WHILE (@i <= 100)
BEGIN
    SET @serviceTypeID    = rand() * 4 + 1
    SET @serviceActionID  = rand() * 3 + 1
    SET @dateTime           = DATEADD(hh, @i - 101, GETUTCDATE())
    EXEC spm_InsertServiceLog{}VERSION_SUFFIX
        @i_service_type_id          = @serviceTypeID,
        @i_service_action_id        = @serviceActionID,
        @t_service_message          = 'test lksjdflwejf test',
        @dt_inserted_datetime       = @dateTime
    SET @i = @i + 1
END