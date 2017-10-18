FNALTHEADER({fnm_$fnName{}VERSION_SUFFIX}, {$fnType})

ALTER FUNCTION fnm_$fnName{}VERSION_SUFFIX (
    $inputParameters
)
RETURNS $returnType
AS
BEGIN
    $sqlQuery
END
GO

FNFOOTER({fnm_$fnName{}VERSION_SUFFIX})