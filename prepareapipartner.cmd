@echo off
cd /d %inetroot%\private\Monitoring\CodeGen
copy codes\sql\TraceDBTransfer.sql codes\sql\_build_TraceDBTransfer.sql /y
copy codes\sql\TraceDB.sql codes\sql\_build_TraceDB.sql /y
rep $targetPath$ %inetroot%\target\retail codes\sql\_build_TraceDBTransfer.sql
rep $targetPath$ %inetroot%\target\retail codes\sql\_build_TraceDB.sql
sqlcmd -i codes\sql\_build_TraceDBTransfer.sql
sqlcmd -i codes\sql\_build_TraceDB.sql