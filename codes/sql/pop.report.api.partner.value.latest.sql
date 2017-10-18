DECLARE @reportID       int
DECLARE @serverID       int
DECLARE @partnerID      int
DECLARE @currentHour    int
DECLARE @dateTime       datetime
DECLARE @floatValue0    float
DECLARE @floatValue1    float
DECLARE @floatValue2    float
DECLARE @floatValue3    float
DECLARE @floatValue4    float
DECLARE @floatValue5    float
DECLARE @floatValue6    float
DECLARE @floatValue7    float
DECLARE @floatValue8    float
DECLARE @floatValue9    float
DECLARE @floatValue10   float
DECLARE @floatValue11   float
DECLARE @floatValue12   float
DECLARE @floatValue13   float
DECLARE @floatValue14   float
DECLARE @floatValue15   float
DECLARE @floatValue16   float
DECLARE @floatValue17   float
DECLARE @floatValue18   float
DECLARE @floatValue19   float
DECLARE @floatValue20   float
DECLARE @floatValue21   float
DECLARE @floatValue22   float
DECLARE @floatValue23   float
DECLARE @bitValue0      bit
DECLARE @bitValue1      bit
DECLARE @bitValue2      bit
DECLARE @bitValue3      bit
DECLARE @bitValue4      bit
DECLARE @bitValue5      bit
DECLARE @bitValue6      bit
DECLARE @bitValue7      bit
DECLARE @bitValue8      bit
DECLARE @bitValue9      bit
DECLARE @bitValue10     bit
DECLARE @bitValue11     bit
DECLARE @bitValue12     bit
DECLARE @bitValue13     bit
DECLARE @bitValue14     bit
DECLARE @bitValue15     bit
DECLARE @bitValue16     bit
DECLARE @bitValue17     bit
DECLARE @bitValue18     bit
DECLARE @bitValue19     bit
DECLARE @bitValue20     bit
DECLARE @bitValue21     bit
DECLARE @bitValue22     bit
DECLARE @bitValue23     bit
SET @reportID = 1
WHILE (@reportID <= 2)
BEGIN
    SET @serverID = 5
    WHILE (@serverID <= 20)
    BEGIN
        SET @dateTime = DATEADD(hh, 0 - floor(rand() * 3), GETDATE())
        SET @dateTime = DATEADD(dd, -1, @dateTime)
        SET @dateTime = DATEADD(mi, 0 - DATEPART(mi, @dateTime), @dateTime)
        SET @dateTime = DATEADD(ss, 0 - DATEPART(ss, @dateTime), @dateTime)
        SET @dateTime = DATEADD(ms, 0 - DATEPART(ms, @dateTime), @dateTime)
        SET @currentHour  = DATEPART(hh, @dateTime)
        SET @partnerID = 1
        WHILE (@partnerID <= 10)
        BEGIN
            SET @floatValue0  = rand()*100
            SET @floatValue1  = rand()*100
            SET @floatValue2  = rand()*100
            SET @floatValue3  = rand()*100
            SET @floatValue4  = rand()*100
            SET @floatValue5  = rand()*100
            SET @floatValue6  = rand()*100
            SET @floatValue7  = rand()*100
            SET @floatValue8  = rand()*100
            SET @floatValue9  = rand()*100
            SET @floatValue10 = rand()*100
            SET @floatValue11 = rand()*100
            SET @floatValue12 = rand()*100
            SET @floatValue13 = rand()*100
            SET @floatValue14 = rand()*100
            SET @floatValue15 = rand()*100
            SET @floatValue16 = rand()*100
            SET @floatValue17 = rand()*100
            SET @floatValue18 = rand()*100
            SET @floatValue19 = rand()*100
            SET @floatValue20 = rand()*100
            SET @floatValue21 = rand()*100
            SET @floatValue22 = rand()*100
            SET @floatValue23 = rand()*100
            SET @bitValue0    = floor(rand()*2)
            SET @bitValue1    = floor(rand()*2)
            SET @bitValue2    = floor(rand()*2)
            SET @bitValue3    = floor(rand()*2)
            SET @bitValue4    = floor(rand()*2)
            SET @bitValue5    = floor(rand()*2)
            SET @bitValue6    = floor(rand()*2)
            SET @bitValue7    = floor(rand()*2)
            SET @bitValue8    = floor(rand()*2)
            SET @bitValue9    = floor(rand()*2)
            SET @bitValue10   = floor(rand()*2)
            SET @bitValue11   = floor(rand()*2)
            SET @bitValue12   = floor(rand()*2)
            SET @bitValue13   = floor(rand()*2)
            SET @bitValue14   = floor(rand()*2)
            SET @bitValue15   = floor(rand()*2)
            SET @bitValue16   = floor(rand()*2)
            SET @bitValue17   = floor(rand()*2)
            SET @bitValue18   = floor(rand()*2)
            SET @bitValue19   = floor(rand()*2)
            SET @bitValue20   = floor(rand()*2)
            SET @bitValue21   = floor(rand()*2)
            SET @bitValue22   = floor(rand()*2)
            SET @bitValue23   = floor(rand()*2)
            EXEC spm_InsertOrUpdateReportAPIPartnerValueLatest{}VERSION_SUFFIX
                @i_report_id                = @reportID,
                @i_server_id                = @serverID,
                @i_partner_id               = @partnerID,
                @ti_current_hour            = @currentHour,
                @f_report_value_0           = @floatValue0,
                @f_report_value_1           = @floatValue1,
                @f_report_value_2           = @floatValue2,
                @f_report_value_3           = @floatValue3,
                @f_report_value_4           = @floatValue4,
                @f_report_value_5           = @floatValue5,
                @f_report_value_6           = @floatValue6,
                @f_report_value_7           = @floatValue7,
                @f_report_value_8           = @floatValue8,
                @f_report_value_9           = @floatValue9,
                @f_report_value_10          = @floatValue10,
                @f_report_value_11          = @floatValue11,
                @f_report_value_12          = @floatValue12,
                @f_report_value_13          = @floatValue13,
                @f_report_value_14          = @floatValue14,
                @f_report_value_15          = @floatValue15,
                @f_report_value_16          = @floatValue16,
                @f_report_value_17          = @floatValue17,
                @f_report_value_18          = @floatValue18,
                @f_report_value_19          = @floatValue19,
                @f_report_value_20          = @floatValue20,
                @f_report_value_21          = @floatValue21,
                @f_report_value_22          = @floatValue22,
                @f_report_value_23          = @floatValue23,
                @b_failed_0                 = @bitValue0,
                @b_failed_1                 = @bitValue1,
                @b_failed_2                 = @bitValue2,
                @b_failed_3                 = @bitValue3,
                @b_failed_4                 = @bitValue4,
                @b_failed_5                 = @bitValue5,
                @b_failed_6                 = @bitValue6,
                @b_failed_7                 = @bitValue7,
                @b_failed_8                 = @bitValue8,
                @b_failed_9                 = @bitValue9,
                @b_failed_10                = @bitValue10,
                @b_failed_11                = @bitValue11,
                @b_failed_12                = @bitValue12,
                @b_failed_13                = @bitValue13,
                @b_failed_14                = @bitValue14,
                @b_failed_15                = @bitValue15,
                @b_failed_16                = @bitValue16,
                @b_failed_17                = @bitValue17,
                @b_failed_18                = @bitValue18,
                @b_failed_19                = @bitValue19,
                @b_failed_20                = @bitValue20,
                @b_failed_21                = @bitValue21,
                @b_failed_22                = @bitValue22,
                @b_failed_23                = @bitValue23,
                @dt_updated_datetime        = @dateTime
            SET @partnerID = @partnerID + 1
        END
        SET @serverID = @serverID + 1
    END
    SET @reportID = @reportID + 1
END