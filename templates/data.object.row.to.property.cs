
            columnName = GetColumnNameWithPrefix(prefix, "$dataObjectPropertyInLowerCase");
            $dataObjectPropertyInUpperCase = GetCellValue<$dataObjectDataType>(columnName, row, $dataObjectPropertyDefaultValue);
            if (!row.Table.Columns.Contains(columnName)) allFieldsMet = false;
