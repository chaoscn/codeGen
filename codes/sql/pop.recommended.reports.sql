DECLARE @reportID int
SET @reportID = 1
WHILE @reportID <= 100
BEGIN
    EXEC spm_InsertRecommendedReport{}VERSION_SUFFIX
        @i_report_id = @reportID
    SET @reportID = @reportID + 1
END