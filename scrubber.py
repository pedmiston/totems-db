#!/usr/bin/env python
import fire
import pandas
from sqlalchemy.orm import sessionmaker
import models
import db


class Scrubber:
    def __init__(self):
        self._engine = db.connect_to_db()
        self._sessionmaker = sessionmaker(bind=self._engine)

    def remove_player(self, player_id):
        session = self._sessionmaker()
        player = self._query_player(player_id, _session=session)
        player.delete()
        session.commit()

    def verify_player(self, player_id):
        return self._query_player(player_id) != None

    def set_group_open(self, group_id, open=False):
        session = self._sessionmaker()
        group = self._query_team(group_id, _session=session)
        group.Open = open
        session.commit()

    def set_group_size(self, group_id, size):
        session = self._sessionmaker()
        group = self._query_team(group_id, _session=session)
        group.Size = Size
        session.commit()

    def _query_player(self, player_id, _session=None):
        session = _session or self._sessionmaker()
        player = (session.query(models.Player)
                         .filter_by(ID_Player=player_id)
                         .first())
        return player

    def _query_team(self, group_id, _session=None):
        session = _session or self._sessionmaker()
        group = (session.query(models.Group)
                        .filter_by(ID_Group=group_id)
                        .first())
        return group

if __name__ == '__main__':
    scrubber = Scrubber()
    fire.Fire(scrubber)
