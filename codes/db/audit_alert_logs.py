tableAuditAlertLogs={
    "tableName": "audit_alert_logs",
    "columns": (
        ("bi_alert_log_id", "bigint", "NOT NULL", "IDENTITY(1, 1)"),
        ("i_alert_source_id", "int", "NOT NULL"),
        ("i_alert_rule_id", "int", "NOT NULL"),
        ("vc_alert_title", "varchar(200)", "NOT NULL"),
        ("t_alert_detail", "text"),
        ("vc_alert_link", "varchar(255)", "NOT NULL"),
        ("b_alert_enabled", "bit", "NOT NULL", "DEFAULT ((1))"),
        ("dt_inserted_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ("dt_updated_datetime", "datetime", "NOT NULL", "DEFAULT (GETUTCDATE())"),
        ),
    "indexs": (
        { "indexName": "alert_title_enabled", "unique": False, "columns": ("vc_alert_title", "b_alert_enabled", ) },
        { "indexName": "alert_source_id_enabled", "unique": False, "columns": ("i_alert_source_id", "b_alert_enabled", ) },
        { "indexName": "alert_rule_id_enabled", "unique": False, "columns": ("i_alert_rule_id", "b_alert_enabled", ) },
        { "indexName": "alert_enabled_datetime_enabled", "unique": False, "columns": ("dt_updated_datetime", "b_alert_enabled", ) },
        { "indexName": "datetime", "unique": False, "columns": ("dt_inserted_datetime", "dt_updated_datetime", ) },
        ),
    }
tables.append(tableAuditAlertLogs)