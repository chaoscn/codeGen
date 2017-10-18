@echo off
cd /d %inetroot%\private\Monitoring\CodeGen
md %inetroot%\target\Config
md %inetroot%\target\Config\MonitoringAPITest
copy /y %inetroot%\private\Monitoring\MonitoringAPITest\APIConfigs\*.xml %inetroot%\target\Config\MonitoringAPITest
md %inetroot%\target\Logs\APITest
md %inetroot%\target\Logs\APITest\Subscriptions
md %inetroot%\target\Logs\APITest\Subscriptions\GetAccountInfo
md %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstruments
md %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstrumentsEx
md %inetroot%\target\Logs\APITest\Subscriptions\GetSubscriptions
md %inetroot%\target\Logs\APITest\Subscriptions\TestConnection
del %inetroot%\target\Logs\APITest\Subscriptions\GetAccountInfo\*.log
del %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstruments\*.log
del %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstrumentsEx\*.log
del %inetroot%\target\Logs\APITest\Subscriptions\GetSubscriptions\*.log
del %inetroot%\target\Logs\APITest\Subscriptions\TestConnection\*.log
for /l %%d in (1,1,9) do echo %%d >> %inetroot%\target\Logs\APITest\Subscriptions\GetAccountInfo\GetAccountInfo.2010.0%%d.log
for /l %%d in (1,1,9) do echo %%d >> %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstruments\GetPaymentInstruments.2010.0%%d.log
for /l %%d in (1,1,9) do echo %%d >> %inetroot%\target\Logs\APITest\Subscriptions\GetPaymentInstrumentsEx\GetPaymentInstrumentsEx.2010.0%%d.log
for /l %%d in (1,1,9) do echo %%d >> %inetroot%\target\Logs\APITest\Subscriptions\GetSubscriptions\GetSubscriptions.2010.0%%d.log
for /l %%d in (1,1,9) do echo %%d >> %inetroot%\target\Logs\APITest\Subscriptions\TestConnection\TestConnection.2010.0%%d.log