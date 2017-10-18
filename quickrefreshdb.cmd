sqlcmd -Q "ALTER DATABASE Monitoring SET RESTRICTED_USER WITH ROLLBACK IMMEDIATE"
cd /d %inetroot%\private\Monitoring\SQL\MonitoringDB\create
call build -cCP -m retail
cd /d %inetroot%\private\Monitoring\SQL\MonitoringDB\populate
call build -cCP -m retail
cd /d %inetroot%\private\Monitoring\CodeGen
sqlcmd -d Monitoring -i codes\sql\grant.permissions.to.network.service.sql
cd /d %inetroot%\private\Monitoring\SQL\MonitoringDB\populate\misc\data
call ImportData.cmd "%inetroot%\private\Monitoring\SQL\MonitoringDB\populate\misc\data\"
cd /d %inetroot%\private\Monitoring\CodeGen