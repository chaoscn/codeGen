VIEWHEADERFORALTER({view_$viewName{}VERSION_SUFFIX})

ALTER VIEW view_$viewName{}VERSION_SUFFIX
AS
    $sqlQuery
GO

VIEWFOOTER({view_$viewName{}VERSION_SUFFIX})

