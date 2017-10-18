-- For the $tableName table
-- Index IX_$tableName$indexName

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_$tableName$indexName'
)
BEGIN
    PRINT 'Dropping index IX_$tableName$indexName.'
    DROP INDEX $tableName.IX_$tableName$indexName
END
GO

CREATE $unique INDEX [IX_$tableName$indexName] 
    ON [$tableName] (
        $indexColumns
        )
    ON [INDEX_DATA]
GO

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_$tableName$indexName'
)
BEGIN
    PRINT 'Successfully created index $tableName.IX_$tableName$indexName.'
END
ELSE
BEGIN
    PRINT 'Failed to create index $tableName.IX_$tableName$indexName!'
END
GO