-- For the $tableName table
-- Full Text Index

IF EXISTS (
    SELECT 'X'
    FROM sys.tables t
    JOIN sys.fulltext_indexes i
      ON t.object_id    = i.object_id
     AND t.name         = '$tableName'
    JOIN sys.fulltext_catalogs c
      ON i.fulltext_catalog_id = c.fulltext_catalog_id
     AND c.name = 'monitoring_full_text_catalog')
BEGIN
    DROP FULLTEXT INDEX ON $tableName
    PRINT 'Fulltext index on $tableName was dropped successfully.'
END
GO

CREATE FULLTEXT INDEX
    ON [$tableName] (
        $indexColumns
        )
    KEY INDEX PK_$tableName$pkName
    ON monitoring_full_text_catalog

EXEC sp_fulltext_table '$tableName', 'activate'
GO

IF EXISTS (
    SELECT 'X'
    FROM sys.tables t
    JOIN sys.fulltext_indexes i
      ON t.object_id    = i.object_id
     AND t.name         = '$tableName'
    JOIN sys.fulltext_catalogs c
      ON i.fulltext_catalog_id = c.fulltext_catalog_id
     AND c.name = 'monitoring_full_text_catalog')
BEGIN
    PRINT 'Fulltext index on $tableName was created successfully.'
END
ELSE
BEGIN
    PRINT 'Error: fulltext index on $tableName was not created.'
END
GO

