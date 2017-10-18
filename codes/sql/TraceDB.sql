USE master

IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'TraceDB')
BEGIN
    ALTER DATABASE TraceDB SET RESTRICTED_USER WITH ROLLBACK IMMEDIATE
    DROP DATABASE [TraceDB]
END
GO

CREATE DATABASE [TraceDB] ON  PRIMARY
( NAME = N'tracedb', FILENAME = N'$targetPath$\TraceDB.mdf' , SIZE = 10368KB , MAXSIZE = UNLIMITED, FILEGROWTH = 50%),
 FILEGROUP [INDEX_DATA]
( NAME = N'tracedb_Index', FILENAME = N'$targetPath$\TraceDB_1.ndf' , SIZE = 512KB , MAXSIZE = UNLIMITED, FILEGROWTH = 512KB )
 LOG ON
( NAME = N'tracedb_Log', FILENAME = N'$targetPath$\TraceDB_2.ldf' , SIZE = 2560KB , MAXSIZE = 2048GB , FILEGROWTH = 1024KB )
GO
EXEC dbo.sp_dbcmptlevel @dbname=N'TraceDB', @new_cmptlevel=90
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [TraceDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [TraceDB] SET ANSI_NULL_DEFAULT OFF
GO
ALTER DATABASE [TraceDB] SET ANSI_NULLS OFF
GO
ALTER DATABASE [TraceDB] SET ANSI_PADDING OFF
GO
ALTER DATABASE [TraceDB] SET ANSI_WARNINGS OFF
GO
ALTER DATABASE [TraceDB] SET ARITHABORT OFF
GO
ALTER DATABASE [TraceDB] SET AUTO_CLOSE OFF
GO
ALTER DATABASE [TraceDB] SET AUTO_CREATE_STATISTICS ON
GO
ALTER DATABASE [TraceDB] SET AUTO_SHRINK OFF
GO
ALTER DATABASE [TraceDB] SET AUTO_UPDATE_STATISTICS ON
GO
ALTER DATABASE [TraceDB] SET CURSOR_CLOSE_ON_COMMIT OFF
GO
ALTER DATABASE [TraceDB] SET CURSOR_DEFAULT  GLOBAL
GO
ALTER DATABASE [TraceDB] SET CONCAT_NULL_YIELDS_NULL OFF
GO
ALTER DATABASE [TraceDB] SET NUMERIC_ROUNDABORT OFF
GO
ALTER DATABASE [TraceDB] SET QUOTED_IDENTIFIER OFF
GO
ALTER DATABASE [TraceDB] SET RECURSIVE_TRIGGERS OFF
GO
ALTER DATABASE [TraceDB] SET  DISABLE_BROKER
GO
ALTER DATABASE [TraceDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO
ALTER DATABASE [TraceDB] SET DATE_CORRELATION_OPTIMIZATION OFF
GO
ALTER DATABASE [TraceDB] SET TRUSTWORTHY OFF
GO
ALTER DATABASE [TraceDB] SET ALLOW_SNAPSHOT_ISOLATION OFF
GO
ALTER DATABASE [TraceDB] SET PARAMETERIZATION SIMPLE
GO
ALTER DATABASE [TraceDB] SET  READ_WRITE
GO
ALTER DATABASE [TraceDB] SET RECOVERY SIMPLE
GO
ALTER DATABASE [TraceDB] SET  MULTI_USER
GO
ALTER DATABASE [TraceDB] SET PAGE_VERIFY TORN_PAGE_DETECTION
GO
ALTER DATABASE [TraceDB] SET DB_CHAINING OFF
GO

USE [TraceDB]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[GlobalComTracerConfig](
    [vc_scratch_server] [varchar](64) NOT NULL,
    [vc_scratch_db] [varchar](64) NOT NULL,
    [i_trace_id] [int] NOT NULL,
    [i_global_trace_id] [int] NULL,
 CONSTRAINT [PK_GlobalComTracerConfig] PRIMARY KEY CLUSTERED 
(
    [vc_scratch_server] ASC,
    [vc_scratch_db] ASC,
    [i_trace_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY],
 CONSTRAINT [IX_GlobalComTracerConfig] UNIQUE NONCLUSTERED 
(
    [i_global_trace_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO

DECLARE @i_trace_id int
SET @i_trace_id = 0
WHILE @i_trace_id < 5
BEGIN
    INSERT INTO [TraceDB].[dbo].[GlobalComTracerConfig]
               ([vc_scratch_server]
               ,[vc_scratch_db]
               ,[i_trace_id]
               ,[i_global_trace_id])
         VALUES
               ('localhost'
               ,'TestDB'
               ,@i_trace_id
               ,@i_trace_id)
    SET @i_trace_id = @i_trace_id + 1
END
GO

USE [TraceDB]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[BDKApiDetail_Y_2009](
    [i_id] [int] NOT NULL,
    [dt_time] [datetime] NOT NULL,
    [i_trace_id] [int] NOT NULL,
    [i_PUID_High] [int] NULL,
    [i_PUID_low] [int] NULL,
    [vc_partner_name] [varchar](32) NULL,
    [dt_API_start_time] [datetime] NULL,
    [vc_API_name] [varchar](64) NULL,
    [txt_error_desc] [ntext] NULL,
    [i_delegate_PUID_High] [int] NULL,
    [i_delegate_PUID_Low] [int] NULL,
    [vc_object_id] [varchar](32) NULL,
    [HRReturn] [int] NULL,
    [guid_tracking_id] [uniqueidentifier] NULL,
 CONSTRAINT [PK_BDKApiDetail_Y_2009] PRIMARY KEY CLUSTERED 
(
    [dt_time] ASC,
    [i_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
ALTER TABLE [dbo].[BDKApiDetail_Y_2009]  WITH CHECK ADD CHECK  (([dt_time]>='01-01-2003' AND [dt_time]<'01-01-2015'))

CREATE NONCLUSTERED INDEX [IX_BDKApiDetail_Y_2009_1] ON [dbo].[BDKApiDetail_Y_2009] 
(
    [dt_time] ASC,
    [i_trace_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
CREATE NONCLUSTERED INDEX [IX_BDKApiDetail_Y_2009_2] ON [dbo].[BDKApiDetail_Y_2009] 
(
    [dt_time] ASC,
    [vc_partner_name] ASC,
    [vc_API_name] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
CREATE NONCLUSTERED INDEX [IX_BDKApiDetail_Y_2009_3] ON [dbo].[BDKApiDetail_Y_2009] 
(
    [i_PUID_High] ASC,
    [i_PUID_low] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
CREATE NONCLUSTERED INDEX [IX_BDKApiDetail_Y_2009_4] ON [dbo].[BDKApiDetail_Y_2009] 
(
    [i_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[view_BDKAPIDetail] AS  SELECT * FROM BDKApiDetail_Y_2009
GO

DECLARE @i_id int
DECLARE @dt_time datetime
DECLARE @i_errorCount int
DECLARE @rowIndex int
DECLARE @i_error_code int

DECLARE @errorCodeTable TABLE
(
  i_error_code int
)

INSERT INTO @errorCodeTable(i_error_code) VALUES (1)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1038085882)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073449315)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073469429)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478608)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478609)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478610)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478611)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478612)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478613)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478614)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478615)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478616)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478617)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478618)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478619)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478620)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478621)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478624)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478625)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478626)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478627)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478628)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478629)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478630)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478631)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478632)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478633)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478634)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478635)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478636)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478637)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478638)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478639)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478640)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478641)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478642)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478643)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478644)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478645)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478646)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478647)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478648)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478649)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478650)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478651)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478652)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478653)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478654)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478655)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478656)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478657)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478658)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478659)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478660)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478661)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478662)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478663)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478664)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478665)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478666)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478667)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478668)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478669)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478670)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478671)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478672)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478673)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478674)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478675)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478676)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478677)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-1073478678)
INSERT INTO @errorCodeTable(i_error_code) VALUES (114)
INSERT INTO @errorCodeTable(i_error_code) VALUES (115)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1303)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1501)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1504)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1505)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1601)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1800)
INSERT INTO @errorCodeTable(i_error_code) VALUES (1900)
INSERT INTO @errorCodeTable(i_error_code) VALUES (2)
INSERT INTO @errorCodeTable(i_error_code) VALUES (2021)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2030043118)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2030043121)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2030043126)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147012865)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147012889)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147012894)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147024809)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161444)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161451)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161452)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161453)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161454)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161455)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161456)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161457)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161458)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161459)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161460)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161461)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161503)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147161504)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147171379)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147171384)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147171389)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177598)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177599)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177600)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177601)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177602)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147177603)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178734)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178739)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178744)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178754)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178779)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178794)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178799)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178974)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178979)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178984)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178989)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147178994)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147179004)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180379)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180384)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180389)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180394)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180399)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180404)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180409)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180414)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180419)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180424)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180429)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180434)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180534)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180639)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180659)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180665)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180667)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180669)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180699)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180724)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180729)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180854)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180859)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180884)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180909)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180949)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180954)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180959)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180973)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180974)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147180978)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181004)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181005)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181006)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181013)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181014)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181033)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181035)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181036)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181037)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181048)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181050)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181052)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181053)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181064)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181067)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181070)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181072)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181073)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181075)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181076)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181079)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181082)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181093)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181095)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181096)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181097)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181098)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181103)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181124)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181144)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181149)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181154)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181159)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181161)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181162)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181163)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181269)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181334)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181339)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181354)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181479)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181483)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181490)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181491)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147181503)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191164)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191169)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191204)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191224)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191249)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191269)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191394)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147191404)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147196484)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200534)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200539)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200554)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200579)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200854)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200869)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200879)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200893)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200894)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200934)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147200939)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201034)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201124)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201214)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201344)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201358)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201364)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201369)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201419)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201444)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201449)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147201479)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211246)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211247)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211248)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211249)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211250)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211251)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211252)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211269)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211274)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211279)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211284)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211289)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211294)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211295)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211296)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211300)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211301)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211303)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211314)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211324)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211334)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211344)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211354)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211364)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211369)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211371)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211372)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211373)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211375)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211377)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211378)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211379)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211384)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211389)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211394)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211399)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211404)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211414)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211424)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211429)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211444)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211450)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211459)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211464)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211475)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211476)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211477)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211478)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211479)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211480)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211482)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211484)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211485)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211486)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211487)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211488)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211489)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211494)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211496)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211497)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211499)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211500)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211502)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147211504)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147216394)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-2147467259)
INSERT INTO @errorCodeTable(i_error_code) VALUES (25)
INSERT INTO @errorCodeTable(i_error_code) VALUES (26)
--Comment following errorcode cause they excceed INT MAX limitation.
--INSERT INTO @errorCodeTable(i_error_code) VALUES (-3220953276) 
--INSERT INTO @errorCodeTable(i_error_code) VALUES (-3220953277)
--INSERT INTO @errorCodeTable(i_error_code) VALUES (-3220953278)
INSERT INTO @errorCodeTable(i_error_code) VALUES (4)
INSERT INTO @errorCodeTable(i_error_code) VALUES (45)
INSERT INTO @errorCodeTable(i_error_code) VALUES (53)
INSERT INTO @errorCodeTable(i_error_code) VALUES (55)
INSERT INTO @errorCodeTable(i_error_code) VALUES (86)
INSERT INTO @errorCodeTable(i_error_code) VALUES (92)
INSERT INTO @errorCodeTable(i_error_code) VALUES (970)
INSERT INTO @errorCodeTable(i_error_code) VALUES (971)
INSERT INTO @errorCodeTable(i_error_code) VALUES (972)
INSERT INTO @errorCodeTable(i_error_code) VALUES (975)
INSERT INTO @errorCodeTable(i_error_code) VALUES (976)
INSERT INTO @errorCodeTable(i_error_code) VALUES (984)
INSERT INTO @errorCodeTable(i_error_code) VALUES (985)
INSERT INTO @errorCodeTable(i_error_code) VALUES (-989855244)

SELECT @i_errorCount = count(*) FROM @errorCodeTable

SET @i_id = 0
WHILE @i_id < 10000
BEGIN
    SET @dt_time = DATEADD(mi, -60*24*RAND(), GETDATE())
    SET @rowIndex = CAST(floor(rand() * @i_errorCount) AS INT)
    SELECT TOP 1 
        @i_error_code= A.i_error_code
    FROM (SELECT TOP (@rowIndex) i_error_code FROM @errorCodeTable ORDER BY i_error_code ASC) A
    ORDER BY A.i_error_code DESC

    INSERT INTO [TraceDB].[dbo].[view_BDKAPIDetail]
               ([i_id]
               ,[dt_time]
               ,[i_trace_id]
               ,[i_PUID_High]
               ,[i_PUID_low]
               ,[vc_partner_name]
               ,[dt_API_start_time]
               ,[vc_API_name]
               ,[txt_error_desc]
               ,[i_delegate_PUID_High]
               ,[i_delegate_PUID_Low]
               ,[vc_object_id]
               ,[HRReturn]
               ,[guid_tracking_id])
         VALUES
               (@i_id
               ,@dt_time
               ,CAST(ROUND(RAND()*4, 0) AS int)
               ,CAST(ROUND(RAND()*9999999, 0) AS int)
               ,CAST(ROUND(RAND()*9999999, 0) AS int)
               ,'Partner ' + CAST(CAST(ROUND(RAND()*4, 0) AS int) AS varchar)
               ,DATEADD(ms, -2*60*1000*RAND(), @dt_time)
               ,CASE WHEN RAND()<0.5 THEN 'API' + CAST(CAST(ROUND(RAND()*4, 0) AS int) AS varchar) ELSE 'PgwAPI' + CAST(CAST(ROUND(RAND()*4, 0) AS int) AS varchar) END
               ,NULL
               ,CAST(ROUND(RAND()*9999999, 0) AS int)
               ,CAST(ROUND(RAND()*9999999, 0) AS int)
               ,NULL
               ,CASE WHEN RAND()<0.2 THEN @i_error_code  ELSE NULL END
               ,NULL)
    SET @i_id = @i_id + 1
END
GO