DELETE FROM datos
        WHERE rowid  NOT IN (
            SELECT MIN(rowid)
            FROM datos
            GROUP BY data
        );