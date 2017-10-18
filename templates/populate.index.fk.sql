-- For the $tableName table
-- Index FK_$tableName$foreignKeyName

IF EXISTS
(
    SELECT name FROM dbo.sysobjects WHERE id = OBJECT_ID(N'FK_$foreignKeyName') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1
)
ALTER TABLE [$tableName] DROP CONSTRAINT FK_$tableName$foreignKeyName
GO

ALTER TABLE [$tableName]
    ADD CONSTRAINT [FK_$tableName$foreignKeyName]
    FOREIGN KEY (
        [$columnName]
    ) REFERENCES [$foreignTableName] (
        [$foreignColumnName]
    ) NOT FOR REPLICATION
GO