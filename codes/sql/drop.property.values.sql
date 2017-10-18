DECLARE @tableName varchar(200)
DECLARE @sqlQuery nvarchar(max)

SET @sqlQuery = ''
DECLARE cursor1 CURSOR FOR
    SELECT name
    FROM sys.tables
    WHERE type_desc = 'USER_TABLE'
      AND name LIKE 'property_value%'
    ORDER BY NAME
OPEN cursor1
    FETCH NEXT FROM cursor1 INTO @tableName
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @sqlQuery = @sqlQuery + 'DROP TABLE ' + @tableName + ' '
        FETCH NEXT FROM cursor1 INTO @tableName
    END
CLOSE cursor1
DEALLOCATE cursor1
EXEC sp_executesql @sqlQuery