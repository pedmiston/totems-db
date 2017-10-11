#!/usr/bin/env python
import pandas
import db

con = db.connect_to_db()
player_info = pandas.read_sql("""
    SELECT ID_Player, Table_Player.ID_Group as ID_Group
    FROM Table_Player
    LEFT JOIN Table_Group
    ON Table_Player.ID_Group = Table_Group.ID_Group
    WHERE Treatment='Isolated' AND BuildingTime=25
""", con)

def enumerate_sessions(chunk):
    chunk['SessionIX'] = range(1, len(chunk)+1)
    return chunk

player_info = player_info.groupby('ID_Group').apply(enumerate_sessions)
tom_subj_info = player_info.pivot('ID_Group', 'SessionIX')
tom_subj_info = tom_subj_info.reset_index()

tom_subj_info.to_csv('tom_subj_info.csv', index=False)
