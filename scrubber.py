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
        assert self.verify_player(player_id)
        session = self._sessionmaker()
        (session.query(models.Player)
                .filter_by(ID_Player=player_id)
                .delete())

    def verify_player(self, player_id):
        session = self._sessionmaker()
        player = (session.query(models.Player)
                         .filter_by(ID_Player=player_id)
                         .first())
        return player != None

    def _query_player(player_id):
        session = self._sessionmaker()


if __name__ == '__main__':
    scrubber = Scrubber()
    fire.Fire(scrubber)
