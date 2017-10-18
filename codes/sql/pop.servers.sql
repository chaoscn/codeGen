DECLARE @serverRole varchar(200)
DECLARE @serverName varchar(200)
DECLARE @tempTable TABLE
(
  serverRole varchar(200),
  serverName varchar(200)
)
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Engine', 'BIMPFPRV11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Engine', 'BIMPFPRV12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Engine', 'BIMPFPRV13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Engine', 'BIMPFPRV14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Queue', 'BIMPFQMR01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Queue', 'BIMPFQMR02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Queue', 'BIMPFQMR03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Provisioning Queue', 'BIMPFQMR04')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Audit', 'BISQLAUD11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Batch Tool,Crypto Slave Servers', 'BISQLBAT01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B1 Final', 'BISQLBIP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B2 Final', 'BISQLBIP12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B3 Final', 'BISQLBIP13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B4 Final', 'BISQLBIP14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B1 Final Backup', 'BISQLBIS11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B2 Final Backup', 'BISQLBIS12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B3 Final Backup', 'BISQLBIS13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Databases B4 Final Backup', 'BISQLBIS14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Tools Databases Primary', 'BISQLBIT01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Tools Databases Backup', 'BISQLBIT02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Email Backup', 'BISQLCDF01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM1 Final', 'BISQLCOP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM2 Final', 'BISQLCOP02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM3 Final', 'BISQLCOP03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM4 Final', 'BISQLCOP04')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM1 Final Backup,Free Subscription Database 1', 'BISQLCOS01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM2 Final Backup,Free Subscription Database 2', 'BISQLCOS02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM3 Final Backup,Free Subscription Database 3', 'BISQLCOS03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Comment Databases CM4 Final Backup,Free Subscription Replica', 'BISQLCOS04')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C1 Final', 'BISQLCUP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C2 Final', 'BISQLCUP12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C3 Final', 'BISQLCUP13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C4 Final', 'BISQLCUP14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C1 Final Backup', 'BISQLCUS11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C2 Final Backup', 'BISQLCUS12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C3 Final Backup', 'BISQLCUS13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Customer Databases C4 Final Backup', 'BISQLCUS14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Email', 'BISQLEMP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Transaction', 'BISQLMPF11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Transaction', 'BISQLMPF12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Notification Queue Databases Primary', 'BISQLNOP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Notification Queue Databases Backup', 'BISQLNOS11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers,PaymentAuth Primary', 'BISQLPAP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('PaymentAuth Backup', 'BISQLPAS11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Replication Distributor D1', 'BISQLRED01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Replication Distributor D2', 'BISQLRED02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Replication Distributor D3', 'BISQLRED03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Replication Distributor D4', 'BISQLRED04')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Replication Distributor D5', 'BISQLRED05')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('BizOps QoS Reporting,BizOps Reporting,BizOps Reporting1,BizOps Reporting2,CDFDB,CleaningStation,Comment Standby1', 'BISQLREP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('BizOps Reporting,FinRpt Replica Two,SPS Replica Box', 'BISQLREP12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('BizOps Reporting,FinRpt Replica One,SPS Replica Box', 'BISQLREP13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('System Metric', 'BISQLTAK01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Master Clock Primary,Middleware Primary', 'BISQLTOP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Middleware Backup', 'BISQLTOS11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Aggregate Metric,DVT Reporting Machine', 'BISQLTQM01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Octopus Deployment Server', 'BIUTLOCT01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Passport Proxy Server: Locked Down', 'BIWEBPPG01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Passport Proxy Server: Locked Down', 'BIWEBPPG02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA12')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA13')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA14')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA15')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SOAP', 'BIWEBSOA16')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Test Tools', 'BIWEBSPK01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers,ToolsWeb', 'BIWEBTOL01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DistributionProgram DB 1,DMP Database 1', 'DMSQLAPP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DistributionProgram DB 2,DMP Database 2', 'DMSQLAPP02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Database 3', 'DMSQLAPP03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DistributionProgram DB DBR,DMP Replica,DMP Webstore Config Secondary', 'DMSQLREP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Tako Components PROD', 'DMSQLTAK01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DistributionProgram Webstore Config Primary,DMP Webstore Config Primary', 'DMSQLWSC01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP BProc', 'DMUTLBEP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Web Service', 'DMWEBSOA01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Web Service', 'DMWEBSOA02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Web Service', 'DMWEBSOA03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('DMP Web Service', 'DMWEBSOA04')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Primary File Server', 'FRFILP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Cluster File Server,Secondary File Server', 'FRFILS02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Modem Server', 'FRMODP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Primary Financial Reporting,Secondary Aggregation', 'FRSQLAGG01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Primary Aggregation,Secondary Financial Reporting', 'FRSQLAGG02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Terminal Server', 'FRTSVP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Terminal Server', 'FRTSVS02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Primary Reporting Web Server', 'FRWEBP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Secondary Reporting Web Server', 'FRWEBS02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('PaymentGateway Replica', 'PGSQLREP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers,PaymentGateway BProc', 'PGUTLBEP11')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Tools Utility 1,Crypto Slave Servers', 'PGUTLBIT01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Billing Tools Utility 2,Crypto Slave Servers', 'PGUTLBIT02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('SFTP Proxy', 'PGUTLFTP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers', 'PGUTLREM23')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers', 'PGUTLREM24')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Data Transfer Box,Data Transfer Box(Property Reference)', 'PRFILDTR01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Bizop Data Transfer Box,Bizop Data Transfer Box(Property Reference)', 'PRFILDTR02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Warehouse Box (Expanded)', 'PRSQLDWH01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Event Configuration and Control,Logshipping Monitor,Quarantine Server', 'PRSQLEVC01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('RASE Replica,Settlement History', 'PRSQLSEH01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Settlement History Secondary', 'PRSQLSEH02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Event Processor', 'PRUTLPRC01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Event Processor', 'PRUTLPRC02')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Event Processor', 'PRUTLPRC03')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('CP PS Database Replica', 'PTSQLREP01')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers', 'RKUTLREM21')
INSERT INTO @tempTable (serverRole, serverName) VALUES ('Crypto Slave Servers', 'RKUTLREM22')

DECLARE cursor1 CURSOR FOR
    SELECT
        serverRole,
        serverName
    FROM @tempTable
    ORDER BY serverName
OPEN cursor1
    FETCH NEXT FROM cursor1 INTO
        @serverRole,
        @serverName
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @serverName = 'TK2MP' + @serverName
        EXEC spm_InsertServer{}VERSION_SUFFIX
            @i_data_center_id  = 1,
            @vc_server_role    = @serverRole,
            @vc_server_name    = @serverName,
            @b_server_critical = 0,
            @b_server_enabled  = 1
        FETCH NEXT FROM cursor1 INTO
            @serverRole,
            @serverName
    END
CLOSE cursor1
DEALLOCATE cursor1

DECLARE cursor2 CURSOR FOR
    SELECT
        serverRole,
        serverName
    FROM @tempTable
    ORDER BY serverName
OPEN cursor2
    FETCH NEXT FROM cursor2 INTO
        @serverRole,
        @serverName
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @serverName = 'BLUMP' + @serverName
        EXEC spm_InsertServer{}VERSION_SUFFIX
            @i_data_center_id  = 2,
            @vc_server_role    = @serverRole,
            @vc_server_name    = @serverName,
            @b_server_critical = 0,
            @b_server_enabled  = 1
        FETCH NEXT FROM cursor2 INTO
            @serverRole,
            @serverName
    END
CLOSE cursor2
DEALLOCATE cursor2

DECLARE cursor3 CURSOR FOR
    SELECT
        serverRole,
        serverName
    FROM @tempTable
    ORDER BY serverName
OPEN cursor3
    FETCH NEXT FROM cursor3 INTO
        @serverRole,
        @serverName
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @serverName = 'CNPC' + @serverName
        EXEC spm_InsertServer{}VERSION_SUFFIX
            @i_data_center_id  = 3,
            @vc_server_role    = @serverRole,
            @vc_server_name    = @serverName,
            @b_server_critical = 0,
            @b_server_enabled  = 1
        FETCH NEXT FROM cursor3 INTO
            @serverRole,
            @serverName
    END
CLOSE cursor3
DEALLOCATE cursor3

SET @serverName = @@SERVERNAME
EXEC spm_InsertServer{}VERSION_SUFFIX
    @i_data_center_id  = 4,
    @vc_server_role    = 'Local Dev Box',
    @vc_server_name    = @@SERVERNAME,
    @b_server_critical = 0,
    @b_server_enabled  = 1