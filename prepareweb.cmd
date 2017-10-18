@echo off
cd /d %inetroot%\private\Monitoring\CodeGen
set SQL_SPIL_VERSION=_13_6

copy codes\sql\pop.data.centers.sql codes\sql\_pop.data.centers.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.data.centers.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.data.centers.sql -o codes\sql\_pop.data.centers.log

copy codes\sql\pop.servers.sql codes\sql\_pop.servers.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.servers.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.servers.sql -o codes\sql\_pop.servers.log

copy codes\sql\pop.users.sql codes\sql\_pop.users.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.users.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.users.sql -o codes\sql\_pop.users.log

copy codes\sql\pop.api.tests.sql codes\sql\_pop.api.tests.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.api.tests.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.api.tests.sql -o codes\sql\_pop.api.tests.log

copy codes\sql\pop.reports.sql codes\sql\_pop.reports.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.reports.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.reports.sql -o codes\sql\_pop.reports.log

copy codes\sql\pop.recommended.reports.sql codes\sql\_pop.recommended.reports.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.recommended.reports.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.recommended.reports.sql -o codes\sql\_pop.recommended.reports.log

copy codes\sql\pop.pref.counter.references.sql codes\sql\_pop.pref.counter.references.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.pref.counter.references.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.pref.counter.references.sql -o codes\sql\_pop.pref.counter.references.log

copy codes\sql\pop.user.report.settings.sql codes\sql\_pop.user.report.settings.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.user.report.settings.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.user.report.settings.sql -o codes\sql\_pop.user.report.settings.log

copy codes\sql\pop.audit.extractor.logs.sql codes\sql\_pop.audit.extractor.logs.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.audit.extractor.logs.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.audit.extractor.logs.sql -o codes\sql\_pop.audit.extractor.logs.log

copy codes\sql\pop.audit.service.logs.sql codes\sql\_pop.audit.service.logs.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.audit.service.logs.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.audit.service.logs.sql -o codes\sql\_pop.audit.service.logs.log

copy codes\sql\pop.properties.sql codes\sql\_pop.properties.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.properties.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.properties.sql -o codes\sql\_pop.properties.log

copy codes\sql\pop.pref.counters.sql codes\sql\_pop.pref.counters.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.pref.counters.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.pref.counters.sql -o codes\sql\_pop.pref.counters.log

copy codes\sql\pop.api.partners.sql codes\sql\_pop.api.partners.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.api.partners.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.api.partners.sql -o codes\sql\_pop.api.partners.log

copy codes\sql\pop.api.partner.servers.sql codes\sql\_pop.api.partner.servers.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.api.partner.servers.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.api.partner.servers.sql -o codes\sql\_pop.api.partner.servers.log

copy codes\sql\pop.report.value.latest.sql codes\sql\_pop.report.value.latest.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.value.latest.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.value.latest.sql -o codes\sql\_pop.report.value.latest.log

copy codes\sql\pop.report.value.hourly.sql codes\sql\_pop.report.value.hourly.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.value.hourly.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.value.hourly.sql -o codes\sql\_pop.report.value.hourly.log

copy codes\sql\pop.report.value.daily.sql codes\sql\_pop.report.value.daily.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.value.daily.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.value.daily.sql -o codes\sql\_pop.report.value.daily.log

copy codes\sql\pop.report.api.partner.value.latest.sql codes\sql\_pop.report.api.partner.value.latest.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.api.partner.value.latest.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.api.partner.value.latest.sql -o codes\sql\_pop.report.api.partner.value.latest.log

copy codes\sql\pop.report.api.partner.value.hourly.sql codes\sql\_pop.report.api.partner.value.hourly.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.api.partner.value.hourly.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.api.partner.value.hourly.sql -o codes\sql\_pop.report.api.partner.value.hourly.log

copy codes\sql\pop.report.api.partner.value.daily.sql codes\sql\_pop.report.api.partner.value.daily.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.report.api.partner.value.daily.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.report.api.partner.value.daily.sql -o codes\sql\_pop.report.api.partner.value.daily.log

copy codes\sql\pop.dashboards.sql codes\sql\_pop.dashboards.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.dashboards.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.dashboards.sql -o codes\sql\_pop.dashboards.log

copy codes\sql\pop.dashboard.groups.sql codes\sql\_pop.dashboard.groups.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.dashboard.groups.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.dashboard.groups.sql -o codes\sql\_pop.dashboard.groups.log

copy codes\sql\pop.user.dashboard.group.settings.sql codes\sql\_pop.user.dashboard.group.settings.sql /y
rep {}VERSION_SUFFIX %SQL_SPIL_VERSION% codes\sql\_pop.user.dashboard.group.settings.sql
timer sqlcmd -d Monitoring -i codes\sql\_pop.user.dashboard.group.settings.sql -o codes\sql\_pop.user.dashboard.group.settings.log