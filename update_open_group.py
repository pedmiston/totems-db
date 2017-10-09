#!/usr/bin/env python
import db
import pandas

con = db.connect_to_db()
groups = pandas.read_sql("""
SELECT *
FROM Table_Group
""", con)
groups.to_csv('Table_Group.csv', index=False)
