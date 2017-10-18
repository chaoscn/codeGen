IF NOT EXISTS
(
    SELECT 'X'
    FROM $tableName
    WHERE $where
)
BEGIN
    INSERT INTO $tableName
        ($columnLine)
        VALUES
        ($dataLine)
END

