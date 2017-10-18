----------------------------------------------------------------------------
-- FILE NAME: $tableName.sql
----------------------------------------------------------------------------
--
-- Target Database:     Monitoring
-- Description:         Creates the $tableName table.
--                     
--
-- Author:              yincao
-- Original Date:       07/31/2009

TABLEHEADER({$tableName})

CREATE TABLE dbo.$tableName (
    $columnDefinations

    CONSTRAINT PK_$tableName$pkName PRIMARY KEY CLUSTERED (
        $pkColumn
    )
) ON [$fileGroupName]
GO

TABLEFOOTER({$tableName})
