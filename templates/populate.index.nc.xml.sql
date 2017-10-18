SET QUOTED_IDENTIFIER ON

-- For the $tableName table
-- Index IX_primary_$tableName$indexName

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_primary_$tableName$indexName'
)
BEGIN
    PRINT 'Dropping index IX_primary_$tableName$indexName.'
    DROP INDEX IX_primary_$tableName$indexName ON $tableName
END
GO

CREATE PRIMARY XML INDEX [IX_primary_$tableName$indexName] 
    ON [$tableName] (
        $indexColumns
        )
GO

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_primary_$tableName$indexName'
)
BEGIN
    PRINT 'Successfully created index $tableName.IX_primary_$tableName$indexName.'
END
ELSE
BEGIN
    PRINT 'Failed to create index $tableName.IX_primary_$tableName$indexName!'
END
GO

-- For the $tableName table
-- Index IX_secondary_$tableName$indexName

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_secondary_$tableName$indexName'
)
BEGIN
    PRINT 'Dropping index IX_secondary_$tableName$indexName.'
    DROP INDEX IX_secondary_$tableName$indexName ON $tableName
END
GO

CREATE XML INDEX [IX_secondary_$tableName$indexName] 
    ON [$tableName] (
        $indexColumns
        )
    USING XML INDEX IX_primary_$tableName$indexName FOR PATH
GO

IF EXISTS
(
    SELECT name FROM sys.indexes WHERE object_id = OBJECT_ID(N'[dbo].[$tableName]') AND name = N'IX_secondary_$tableName$indexName'
)
BEGIN
    PRINT 'Successfully created index $tableName.IX_secondary_$tableName$indexName.'
END
ELSE
BEGIN
    PRINT 'Failed to create index $tableName.IX_secondary_$tableName$indexName!'
END
GO

SET QUOTED_IDENTIFIER OFF
GO