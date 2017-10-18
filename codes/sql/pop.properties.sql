DECLARE @index          int
DECLARE @propertyValue  varchar(200)
DECLARE @dateTime       datetime
SET @dateTime = DATEADD(dd, -1, GETUTCDATE())
SET @index = 1
WHILE (@index <= 216)
BEGIN
    SET @propertyValue = 'Perf ' + CAST(@index AS varchar)
    EXEC spm_InsertProperty{}VERSION_SUFFIX
        @i_property_type_id             = 1,
        @i_server_id                    = 1,
        @vc_property_name               = @propertyValue,
        @b_property_enabled             = 1,
        @dt_hourly_aggregated_datetime  = @dateTime,
        @dt_daily_aggregated_datetime   = @dateTime
    SET @index = @index + 1
END
SET @index = 1
WHILE (@index <= 436)
BEGIN
    SET @propertyValue = 'API ' + CAST(@index AS varchar)
    EXEC spm_InsertProperty{}VERSION_SUFFIX
        @i_property_type_id             = 2,
        @i_server_id                    = 1,
        @vc_property_name               = @propertyValue,
        @b_property_enabled             = 1,
        @dt_hourly_aggregated_datetime  = @dateTime,
        @dt_daily_aggregated_datetime   = @dateTime
    SET @index = @index + 1
END