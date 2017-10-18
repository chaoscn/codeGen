ALTER DATABASE Monitoring ADD FILEGROUP MonitoringPartition$partitionID
GO
ALTER DATABASE Monitoring
    ADD FILE
    (
        NAME       = MonitoringPartition$partitionID,
        FILENAME   = N'$$SQL_NET_TARGETPATH$$\MonitoringPartition$partitionID.ndf',
        SIZE       = 512KB,
        FILEGROWTH = 5MB
    )
    TO FILEGROUP MonitoringPartition$partitionID
GO
