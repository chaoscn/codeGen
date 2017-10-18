USE master

IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'TraceDBTransfer')
BEGIN
    ALTER DATABASE TraceDBTransfer SET RESTRICTED_USER WITH ROLLBACK IMMEDIATE
    DROP DATABASE [TraceDBTransfer]
END
GO

CREATE DATABASE [TraceDBTransfer] ON PRIMARY
( NAME = N'TraceDBTransfer', FILENAME = N'$targetPath$\TraceDBTransfer.mdf' , SIZE = 22528KB , MAXSIZE = UNLIMITED, FILEGROWTH = 20480KB ),
 FILEGROUP [INDEX_DATA]
( NAME = N'TraceDBTransfer_Index', FILENAME = N'$targetPath$\TraceDBTransfer_1.ndf' , SIZE = 2048KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10240KB )
 LOG ON
( NAME = N'TraceDBTransfer_Log', FILENAME = N'$targetPath$\TraceDBTransfer_2.ldf' , SIZE = 17408KB , MAXSIZE = UNLIMITED, FILEGROWTH = 15360KB )
GO
EXEC dbo.sp_dbcmptlevel @dbname=N'TraceDBTransfer', @new_cmptlevel=80
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [TraceDBTransfer].[dbo].[sp_fulltext_database] @action = 'disable'
end
GO
ALTER DATABASE [TraceDBTransfer] SET ANSI_NULL_DEFAULT OFF
GO
ALTER DATABASE [TraceDBTransfer] SET ANSI_NULLS OFF
GO
ALTER DATABASE [TraceDBTransfer] SET ANSI_PADDING OFF
GO
ALTER DATABASE [TraceDBTransfer] SET ANSI_WARNINGS OFF
GO
ALTER DATABASE [TraceDBTransfer] SET ARITHABORT OFF
GO
ALTER DATABASE [TraceDBTransfer] SET AUTO_CLOSE OFF
GO
ALTER DATABASE [TraceDBTransfer] SET AUTO_CREATE_STATISTICS ON
GO
ALTER DATABASE [TraceDBTransfer] SET AUTO_SHRINK OFF
GO
ALTER DATABASE [TraceDBTransfer] SET AUTO_UPDATE_STATISTICS ON
GO
ALTER DATABASE [TraceDBTransfer] SET CURSOR_CLOSE_ON_COMMIT OFF
GO
ALTER DATABASE [TraceDBTransfer] SET CURSOR_DEFAULT  GLOBAL
GO
ALTER DATABASE [TraceDBTransfer] SET CONCAT_NULL_YIELDS_NULL OFF
GO
ALTER DATABASE [TraceDBTransfer] SET NUMERIC_ROUNDABORT OFF
GO
ALTER DATABASE [TraceDBTransfer] SET QUOTED_IDENTIFIER OFF
GO
ALTER DATABASE [TraceDBTransfer] SET RECURSIVE_TRIGGERS OFF
GO
ALTER DATABASE [TraceDBTransfer] SET DISABLE_BROKER
GO
ALTER DATABASE [TraceDBTransfer] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO
ALTER DATABASE [TraceDBTransfer] SET DATE_CORRELATION_OPTIMIZATION OFF
GO
ALTER DATABASE [TraceDBTransfer] SET TRUSTWORTHY OFF
GO
ALTER DATABASE [TraceDBTransfer] SET ALLOW_SNAPSHOT_ISOLATION OFF
GO
ALTER DATABASE [TraceDBTransfer] SET PARAMETERIZATION SIMPLE
GO
ALTER DATABASE [TraceDBTransfer] SET  READ_WRITE
GO
ALTER DATABASE [TraceDBTransfer] SET RECOVERY SIMPLE
GO
ALTER DATABASE [TraceDBTransfer] SET  MULTI_USER
GO
ALTER DATABASE [TraceDBTransfer] SET PAGE_VERIFY TORN_PAGE_DETECTION
GO
ALTER DATABASE [TraceDBTransfer] SET DB_CHAINING OFF
GO

USE [TraceDBTransfer]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[TraceConfig](
	[vc_machine_name] [varchar](256) NOT NULL,
	[vc_logname] [varchar](256) NOT NULL,
	[i_trace_id] [int] NOT NULL,
	[i_polling_interval] [int] NOT NULL,
	[vc_directory] [varchar](256) NULL,
	[vc_type] [varchar](32) NULL,
	[vc_pattern] [varchar](64) NULL,
	[dt_last_updated] [datetime] NULL,
 CONSTRAINT [PK_TraceConfig] PRIMARY KEY CLUSTERED 
(
	[i_trace_id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY],
 CONSTRAINT [IX_TraceConfig] UNIQUE NONCLUSTERED 
(
	[vc_machine_name] ASC,
	[vc_logname] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO

DECLARE @i_trace_id int
SET @i_trace_id = 0
WHILE @i_trace_id < 5
BEGIN
    INSERT INTO [TraceDBTransfer].[dbo].[TraceConfig]
               ([vc_machine_name]
               ,[vc_logname]
               ,[i_trace_id]
               ,[i_polling_interval]
               ,[vc_directory]
               ,[vc_type]
               ,[vc_pattern]
               ,[dt_last_updated])
         VALUES
               ('TK2MPBISQL0' + CAST(@i_trace_id AS varchar)
               ,'Log0' + CAST(@i_trace_id AS varchar)
               ,@i_trace_id
               ,30000
               ,''
               ,'ComTracer'
               ,'Test*'
               ,GETUTCDATE())
    SET @i_trace_id = @i_trace_id + 1
END
GO