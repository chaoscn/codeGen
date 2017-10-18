tableAuditUserActivityLogs={
    "tableName": "audit_user_activity_logs",
    "columns": (
        ("bi_user_activity_log_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("vc_user_name", "varchar(200)", "NOT NULL"),
        ("vc_user_action_name", "varchar(200)", "NOT NULL"),
        ("t_user_action_detail", "text"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "user_name", "unique": False, "columns": ("vc_user_name", "dt_inserted_datetime", ) },
        ),
    }
tables.append(tableAuditUserActivityLogs)