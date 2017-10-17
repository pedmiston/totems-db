#!/usr/bin/env python
import pandas
import db

con = db.connect_to_db()
player_info = pandas.read_sql("""
    SELECT ID_Player, Table_Player.ID_Group as ID_Group, Size, Open, Status_Start, Status_End, Ancestor, Score
    FROM Table_Player
    LEFT JOIN Table_Group
    ON Table_Player.ID_Group = Table_Group.ID_Group
    WHERE Treatment='Isolated'
""", con)

def enumerate_sessions(chunk):
    chunk['SessionIX'] = range(1, len(chunk)+1)
    return chunk

(player_info.groupby('ID_Group')
            .apply(enumerate_sessions)
            .sort_values(by=['ID_Group', 'ID_Player'])
            .to_csv('isolated_players.csv', index=False))
