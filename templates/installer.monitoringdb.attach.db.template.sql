CREATE DATABASE $$dbName$$
ON PRIMARY 
    (FILENAME = N'$$mdfPath$$$$dbFilePrefix$$.mdf'),
    (FILENAME = N'$$ndfPath$$$$dbFilePrefix$$.ndf'),
$partitionContents
LOG ON
    (FILENAME = N'$$ldfPath$$$$dbFilePrefix$$.ldf')
FOR ATTACH
GO