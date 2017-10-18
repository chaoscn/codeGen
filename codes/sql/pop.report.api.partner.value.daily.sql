DECLARE @reportID         int
DECLARE @serverID         int
DECLARE @partnerID        int
DECLARE @dailyPartitionID int
DECLARE @currentDay       int
DECLARE @dateTime         datetime
DECLARE @floatValue       float
DECLARE @bitValue         bit
SET @reportID = 1
WHILE (@reportID <= 2)
BEGIN
    SET @dailyPartitionID = @reportID - 1
    SET @serverID = 5
    WHILE (@serverID <= 20)
    BEGIN
        SET @partnerID = 1
        WHILE (@partnerID <= 10)
        BEGIN
            SET @currentDay = 0
            WHILE (@currentDay <= 60)
            BEGIN
                SET @dateTime   = DATEADD(dd, @currentDay - 61, GETDATE())
                SET @floatValue = rand()*100
                SET @bitValue   = floor(rand()*2)
                EXEC spm_InsertOrUpdateReportAPIPartnerValuedaily{}VERSION_SUFFIX
                    @i_daily_partition_id       = @dailyPartitionID,
                    @i_report_id                = @reportID,
                    @i_server_id                = @serverID,
                    @i_partner_id               = @partnerID,
                    @f_report_value             = @floatValue,
                    @b_failed                   = @bitValue,
                    @dt_inserted_datetime       = @dateTime
                SET @currentDay = @currentDay + 1
            END
            SET @partnerID = @partnerID + 1
        END
        SET @serverID = @serverID + 1
    END
    SET @reportID = @reportID + 1
END