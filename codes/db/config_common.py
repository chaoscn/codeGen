tableConfigCommon={
    "tableName": "config_common",
    "columns": (
        ("i_config_id", "int", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_config_name", "varchar(200)", "NOT NULL"),
        ("vc_config_value", "varchar(8000)", "NOT NULL"),
        ("b_config_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("vc_updated_by", "varchar(100)", "NOT NULL"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "config_name", "unique": True, "columns": ("vc_config_name", ) },
        { "indexName": "config_name_enabled", "unique": False, "columns": ("vc_config_name", "b_config_enabled", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    "initialDataWhereIndex": (1, ),
    "initialData": (
        { "dataLine": ("'Global.Default Connection String'", "'Integrated Security=SSPI;persist security info=False;'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Default Refresh Config Interval'", "24*3600*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Default Web Server'", "'localhost'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Perf Counter.Default Probe Interval'", "15*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Perf Counter.Default Scan Server Interval'", "12*3600*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Perf Counter.Max Sleep At First Time'", "5*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Perf Counter.Sleep Time Every N Rounds'", "100", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Perf Counter.N Rounds'", "1", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Dashboard.Default Dashboard Group Name'", "'Default'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Dashboard.Default Dashboard Group Description'", "'Default'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Look Back Days'", "14", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Wait For Next Round Offset'", "15*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Tako Server Name'", "'localhost'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Trace DB Catalog Name'", "'TraceDB'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Tako BDK API SQL Query'", getSQLCompatibleString("""
SELECT
    A.vc_api_name AS 'apiName',
    A.vc_partner_name AS 'partnerName',
    (
        SELECT TOP 1
            B.vc_machine_name
        FROM TraceDBTransfer.dbo.TraceConfig B (NOLOCK)
        WHERE B.i_trace_id =
        (
            SELECT TOP 1
                C.i_trace_id
            FROM TraceDB.dbo.GlobalComTracerConfig C (NOLOCK)
            WHERE C.i_global_trace_id = A.i_trace_id
        )
    ) AS 'serverName',
    CASE
        WHEN A.HRReturn IS NULL OR A.HRReturn = 0 THEN 0
        WHEN UPPER(substring(vc_api_name, 1, 3)) = 'PGW' AND A.HRReturn IN ([1]) THEN 1
        WHEN vc_api_name in ('[0]') AND A.HRReturn IN ([2]) THEN 1
        ELSE 2
    END AS 'takoAPIPartnerStatus',
    SUM(CASE WHEN DATEDIFF(ms, A.dt_API_start_time, A.dt_time) BETWEEN 0 AND 120000 THEN DATEDIFF(ms, A.dt_API_start_time, A.dt_time) ELSE 0 END) AS 'latency',
    COUNT(CASE WHEN DATEDIFF(ms, A.dt_API_start_time, A.dt_time) BETWEEN 0 AND 120000 THEN 1 ELSE 0 END) AS 'count'
FROM TraceDB.dbo.view_BDKAPIDetail A (NOLOCK)
WHERE A.dt_time >= @dt_time_from AND A.dt_time < @dt_time_to
GROUP BY A.vc_api_name,
    A.vc_partner_name,
    A.i_trace_id,
    CASE
        WHEN A.HRReturn IS NULL OR A.HRReturn = 0 THEN 0
        WHEN UPPER(substring(vc_api_name, 1, 3)) = 'PGW' AND A.HRReturn IN ([1]) THEN 1
        WHEN vc_api_name in ('[0]') AND A.HRReturn IN ([2]) THEN 1
        ELSE 2
    END
ORDER BY A.vc_api_name, A.vc_partner_name, A.i_trace_id
"""), "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Check Trace DB SQL Query'", getSQLCompatibleString("""
IF EXISTS
(
    SELECT name FROM sys.databases WHERE name = N'TraceDB'
)
BEGIN
    SELECT 1 AS 'boolean'
END
ELSE
BEGIN
    SELECT 0 AS 'boolean'
END
"""), "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Tako BDK API SCS API Name List'", "'ActivateToken,ActivateTokenEx,AddComment,AddPaymentInstrument,AddRoleAssignment,AddViolation,AdjustGotoBAMDate,AdjustResourceBalance,AdjustSubscription,BanPaymentInstrument,BanUser,BlacklistToken,CalculateTax,CancelConversion,CancelPayment,CancelRenewal,CancelSubscription,CancelSubscriptionEx,CancelTransaction,ChargePaymentInstrument,CheckCDAvailability,CheckProvisioningStatus,CloseAccount,CloseBalance,CompleteConversion,ConsumeToken,ConvertSubscription,ConvertSubscriptionEx,ConvertSubscriptionEx2,ConvertSubscriptionEx3,CreateAccount,CreditPaymentInstrument,CreditPaymentInstrumentEx,DeactivateToken,DeactivateTokenEx,DeliverToken,DeprovisionServices,ExtendSubscription,FixExistingAddress,GetAccountIdFromAdminPUID,GetAccountIdFromPaymentInstrumentInfo,GetAccountIdFromPuid,GetAccountIdFromToken,GetAccountIdFromTokenId,GetAccountInfo,GetAccountStatus,GetAdjustments,GetBaseOfferings,GetBaseOfferingsEx,GetBillingPeriods,GetBillingReference,GetComments,GetEligibleOfferings,GetEligibleOfferingsEx,GetEligibleSwitchPITypes,GetExistingAccountsByCriteria,GetKey,GetLineItemHistory,GetPartnerConfiguration,GetPaymentInstruments,GetPaymentInstrumentsEx,GetPaymentMethodTypeProperties,GetPermitHistoryForObjectId,GetPermitsForObjectId,GetPermitsForPUID,GetPolicy,GetProductClasses,GetProvisioningInfo,GetReferralData,GetReferralEvents,GetReplacementToken,GetReplacementTokenFromPuid,GetResourceBalances,GetResourcePrices,GetServiceComponents,GetStatement,GetStatementEx,GetSubscriptionHistory,GetSubscriptions,GetSubscriptionStatus,GetTokenClasses,GetTokenClassRestrictionInfoForPUID,GetTokenInfo,GetTokenInfoEx,GetTransactions,GetUnconditionalReplacementToken,GetUserProfile,ImportSettledBillingItem,IsPaymentInstrumentBanned,IssueTokenTrusted,LoadTokenInstance,MapAddress,MarkTokenDistributionStatus,MatchPaymentInstrumentInfo,MigrateOffer,OffsetLineItem,OffsetLineItem2,OffsetOrder,OffsetSingleUsageEvent,OrderCDforAccount,OrderCDforAnonymous,PayUser,ProcessChargeback,ProvisionServices,PurchaseItem,PurchaseItemEx,PurchaseOffering,PurchaseOfferingEx,PurchaseOfferingEx2,PurchaseOfferingEx3,ReconcileTokenTrusted,RefundTaxForAccount,RegisterPaymentInstrument,ReinstateSubscription,RemoveBillingReference,RemovePaymentInstrument,RemovePMNBasedServices,RemoveRoleAssignment,RemoveViolation,ReportSingleUsageEvent,ReportTransactionEvent,ReportUsageEvent,ReschedulePayment,SearchAccounts,SearchAccountsEx,SearchBillingInfo,SendHCI,SendValidationTokenInfo,SetBillingReference,SetPartnerConfiguration,SettleBalance,SettleOrder,SetUserProfile,SignAgreement,StopPayments,SubmitOrder,SwitchPaymentInstruments,SyncUPSCacheForPUID,TestConnection,TokenRedemption,TransferBalance,UnbanPaymentInstrument,UnbanUser,UnIssueTokenTrusted,UpdateAccountInfo,UpdatePaymentInstrumentInfo,UpdateSubscriptionInfo,ValidateProvisioningData,ValidateToken'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Tako BDK API PGW System Error Code List'", "'1,2,4,25,26,45,53,55,86,92,114,115,970,971,972,975,976,984,985,1303,1501,1504,1505,1601,1800,1900,2021'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Partner.Tako BDK API SCS System Error Code List'", "'-3220953278,-3220953277,-3220953276,-2147467259,-2147216394,-2147211504,-2147211502,-2147211500,-2147211499,-2147211497,-2147211496,-2147211494,-2147211489,-2147211488,-2147211487,-2147211486,-2147211485,-2147211484,-2147211482,-2147211480,-2147211479,-2147211478,-2147211477,-2147211476,-2147211475,-2147211464,-2147211459,-2147211450,-2147211444,-2147211429,-2147211424,-2147211414,-2147211404,-2147211399,-2147211394,-2147211389,-2147211384,-2147211379,-2147211378,-2147211377,-2147211375,-2147211373,-2147211372,-2147211371,-2147211369,-2147211364,-2147211354,-2147211344,-2147211334,-2147211324,-2147211314,-2147211303,-2147211301,-2147211300,-2147211296,-2147211295,-2147211294,-2147211289,-2147211284,-2147211279,-2147211274,-2147211269,-2147211252,-2147211251,-2147211250,-2147211249,-2147211248,-2147211247,-2147211246,-2147201479,-2147201449,-2147201444,-2147201419,-2147201369,-2147201364,-2147201358,-2147201344,-2147201214,-2147201124,-2147201034,-2147200939,-2147200934,-2147200894,-2147200893,-2147200879,-2147200869,-2147200854,-2147200579,-2147200554,-2147200539,-2147200534,-2147196484,-2147191404,-2147191394,-2147191269,-2147191249,-2147191224,-2147191204,-2147191169,-2147191164,-2147181503,-2147181491,-2147181490,-2147181483,-2147181479,-2147181354,-2147181339,-2147181334,-2147181269,-2147181163,-2147181162,-2147181161,-2147181159,-2147181154,-2147181149,-2147181144,-2147181124,-2147181103,-2147181098,-2147181097,-2147181096,-2147181095,-2147181093,-2147181082,-2147181079,-2147181076,-2147181075,-2147181073,-2147181072,-2147181070,-2147181067,-2147181064,-2147181053,-2147181052,-2147181050,-2147181048,-2147181037,-2147181036,-2147181035,-2147181033,-2147181014,-2147181013,-2147181006,-2147181005,-2147181004,-2147180978,-2147180974,-2147180973,-2147180959,-2147180954,-2147180949,-2147180909,-2147180884,-2147180859,-2147180854,-2147180729,-2147180724,-2147180699,-2147180669,-2147180667,-2147180665,-2147180659,-2147180639,-2147180534,-2147180434,-2147180429,-2147180424,-2147180419,-2147180414,-2147180409,-2147180404,-2147180399,-2147180394,-2147180389,-2147180384,-2147180379,-2147179004,-2147178994,-2147178989,-2147178984,-2147178979,-2147178974,-2147178799,-2147178794,-2147178779,-2147178754,-2147178744,-2147178739,-2147178734,-2147177603,-2147177602,-2147177601,-2147177600,-2147177599,-2147177598,-2147171389,-2147171384,-2147171379,-2147161504,-2147161503,-2147161461,-2147161460,-2147161459,-2147161458,-2147161457,-2147161456,-2147161455,-2147161454,-2147161453,-2147161452,-2147161451,-2147161444,-2147024809,-2147012894,-2147012889,-2147012865,-2030043126,-2030043121,-2030043118,-1073478678,-1073478677,-1073478676,-1073478675,-1073478674,-1073478673,-1073478672,-1073478671,-1073478670,-1073478669,-1073478668,-1073478667,-1073478666,-1073478665,-1073478664,-1073478663,-1073478662,-1073478661,-1073478660,-1073478659,-1073478658,-1073478657,-1073478656,-1073478655,-1073478654,-1073478653,-1073478652,-1073478651,-1073478650,-1073478649,-1073478648,-1073478647,-1073478646,-1073478645,-1073478644,-1073478643,-1073478642,-1073478641,-1073478640,-1073478639,-1073478638,-1073478637,-1073478636,-1073478635,-1073478634,-1073478633,-1073478632,-1073478631,-1073478630,-1073478629,-1073478628,-1073478627,-1073478626,-1073478625,-1073478624,-1073478621,-1073478620,-1073478619,-1073478618,-1073478617,-1073478616,-1073478615,-1073478614,-1073478613,-1073478612,-1073478611,-1073478610,-1073478609,-1073478608,-1073469429,-1073449315,-1038085882,-989855244'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Test Runner.Scan Interval'", "5*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.API Test Runner.Max Calls Count In History'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Aggregator.Page Size'", "5000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Aggregator.Thread Pool Size'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Page Size'", "5000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Thread Pool Size'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Property Latest Days'", "-7", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Property Hourly Days'", "-367", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Property Daily Days'", "-10*365-5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Report Hourly Days'", "-367", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Report Daily Days'", "-10*365-5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Audit Extractor Log Days'", "-30", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Clean Up.Report Alert Days'", "-367", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Alert Mail.Check New Task Interval'", "60000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Background Job.Alert Mail.Thread Pool Size'", "5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.SMTP Server.Address'", "'localhost'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.SMTP Server.Port'", "25", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.SMTP Server.EnableSSL'", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.SMTP Server.Timeout'", "30000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.Default Address Template'", "'{0}@dummy.com'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.SMTP Test From'", "'ctp_mnr'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.SMTP Test To'", "'ctp_smtp'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.API Test Notification From'", "'ctp_mnr'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.API Test Notification To'", "'ctp_apin'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.API Test Alert From'", "'ctp_mnr'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.API Test Alert To'", "'ctp_apia'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.Report Alert From'", "'ctp_mnr'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Address.Report Alert To'", "'ctp_repa'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Failure Notification Title'", "'..\\Templates\\Emails\\APITestFailureNotificationTitle.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Recovery Notification Title'", "'..\\Templates\\Emails\\APITestRecoveryNotificationTitle.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Failure Detail Title'", "'..\\Templates\\Emails\\APITestFailureDetailTitle.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Recovery Detail Title'", "'..\\Templates\\Emails\\APITestRecoveryDetailTitle.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Failure Notification Body'", "'..\\Templates\\Emails\\APITestFailureNotificationBody.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Recovery Notification Body'", "'..\\Templates\\Emails\\APITestRecoveryNotificationBody.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Failure Detail Body'", "'..\\Templates\\Emails\\APITestFailureDetailBody.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.API Test Recovery Detail Body'", "'..\\Templates\\Emails\\APITestRecoveryDetailBody.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.Report Alert Title'", "'..\\Templates\\Emails\\ReportAlertTitle.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Email.Template.Report Alert Body'", "'..\\Templates\\Emails\\ReportAlertBody.xslt'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Default'", "60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.UserDO'", "6*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigReportDO'", "1*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ReportValueLatestDO'", "10*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ReportValueHourlyDO'", "20*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ReportValueDailyDO'", "1*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigAPIDO'", "3*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigAPITestDO'", "24*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigPerfCounterReferenceDO'", "3*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigDashboardDO'", "1*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.ConfigDashboardGroupDO'", "1*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Cache.Duration.Dummy.Monitoring.MonitoringLib.DO.UserDashboardGroupSettingDO'", "1*60*60*1000", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Search.Default Items Per Page'", "20", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Search.Max Items Per Page'", "200", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Search.Max Pages Count In Whole Pagination'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Search.Max Pages Count In Each Side Of Pagination'", "5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Create.Max Report Alert Comment Length'", "300", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Create.Max Report Cell Theme Comment Length'", "300", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.Action.Wait Seconds'", "3", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View.Default Day Span'", "0", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View.Max Day Span'", "60", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Bar Colors'", "'FF418CF0,FFE0400A,FF87CEEB,FFBA55D3,FF4682B4,FF40E0D0,FFF0E68C,FF8FBC8B'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Border Color'", "'FFCCCCCC'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Border Line Color'", "'FFFD9F0C'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Title Color'", "'FF800000'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Back Color'", "'FFF8EBDA'", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Default Image Width'", "800", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Max Image Width'", "2048", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Min Image Width'", "200", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Default Image Height'", "480", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Max Image Height'", "2048", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Min Image Height'", "200", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Default Moving Average Days'", "7", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Max Moving Average Days'", "30", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart.Min Moving Average Days'", "5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Default Image Width'", "800", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Max Image Width'", "2048", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Min Image Width'", "200", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Default Image Height'", "480", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Max Image Height'", "2048", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Report.View Chart For Dashboard.Min Image Height'", "100", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.Search.Default Items Per Page'", "4", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.Search.Max Items Per Page'", "50", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.Search.Max Pages Count In Whole Pagination'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.Search.Max Pages Count In Each Side Of Pagination'", "5", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Dashboard Width'", "400", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Dashboard Height'", "300", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Dashboard Separator Height'", "2", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Report Title Line Height'", "20", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Report Text Line Height'", "20", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Default Day Span'", "1", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Dashboard.View.Max Day Span'", "60", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Json Service.Search Property.Default Items Per Page'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Json Service.Search Property.Max Items Per Page'", "50", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Json Service.Search Report.Default Items Per Page'", "10", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Json Service.Search Report.Max Items Per Page'", "50", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Json Service.Update Dashboard Group Setting Xml.Max Dashboards In Dashboard Group'", "30", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Admin.Logs.Extractor.Default Items Per Page'", "20", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        { "dataLine": ("'Global.Web.Admin.Logs.Service.Default Items Per Page'", "20", "1", "SYSTEM_USER", "GETUTCDATE()", "GETUTCDATE()") },
        ),
    }
tables.append(tableConfigCommon)

tableConfigCommon["sps"]=(
    {
        "spName": "GetConfigByName",
        "description": "Get config by name",
        "inputParameters": """@vc_config_name           varchar(200)""",
        "sqlQuery":
"""CHECK_NOTNULL(@vc_config_name)

    SELECT
        i_config_id          AS 'configID',
        vc_config_name       AS 'configName',
        vc_config_value      AS 'configValue',
        b_config_enabled     AS 'configEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_common WITH (FORCESEEK)
    WHERE vc_config_name     = @vc_config_name
    
    CHKERR({ERROR_GET_CONFIG_BY_NAME})
    RETURN 0""",
    },
    {
        "spName": "GetAllConfigs",
        "description": "Get all configs",
        "inputParameters": """""",
        "sqlQuery":
"""SELECT
        i_config_id          AS 'configID',
        vc_config_name       AS 'configName',
        vc_config_value      AS 'configValue',
        b_config_enabled     AS 'configEnabled',
        vc_updated_by        AS 'updatedBy',
        dt_inserted_datetime AS 'insertedDateTime',
        dt_updated_datetime  AS 'updatedDateTime'
    FROM config_common
    ORDER BY i_config_id
    
    CHKERR({ERROR_GET_All_CONFIGS})
    RETURN 0""",
    },
    )

# IGlobalConfiguration.cs
createDir(targetInterfaceConfigurationsPath)
propertyLines=[]
for initialData in tableConfigCommon["initialData"]:
    name, value=initialData["dataLine"][0], initialData["dataLine"][1]
    propertyType="int"
    if value[0]=="'":
        propertyType="string"
    propertyLines.append("        %s %s { get; }" % (propertyType, getCleanText(name)))
parameters={}
parameters["iGlobalConfiguration"]="\n".join(propertyLines)
createFile(os.path.join(targetInterfaceConfigurationsPath, "IGlobalConfiguration.cs"), templateMonitoringInterfaceConfigurationsIGlobalConfiguration.substitute(parameters))

# GlobalConfiguration.cs
createDir(targetInterfaceImplementsConfigurationsPath)
propertyLines, updateLines=[], []
for initialData in tableConfigCommon["initialData"]:
    name, value=initialData["dataLine"][0], initialData["dataLine"][1]
    parameters={}
    parameters["propertyName"]=getCleanText(name)
    parameters["propertyKey"]=name.strip("'")
    parameters["defaultValue"]=value.strip("'").replace("\\", "\\\\")
    if value[0]=="'":
        propertyLines.append(templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationPropertyString.substitute(parameters))
    else:
        propertyLines.append(templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationPropertyInt.substitute(parameters))
    updateLines.append(templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfigurationUpdate.substitute(parameters))
parameters={}
parameters["globalConfiguration"]="\n\n".join(propertyLines)
parameters["updateGlobalConfiguration"]="\n".join(updateLines)
createFile(os.path.join(targetInterfaceImplementsConfigurationsPath, "GlobalConfiguration.cs"), templateMonitoringLibModelsInterfaceImplementsConfigurationsGlobalConfiguration.substitute(parameters))