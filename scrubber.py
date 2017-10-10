#!/usr/bin/env python
import fire
import pandas
import db

class Scrubber:
    def __init__(self):
        self._con = db.connect_to_db()

    def remove_participant(self, participant_id):
        assert self.verify_participant(participant_id)
        con.execute(
            db.Group.update()
                 .values(Status = 'E')
                 .where(db.Group.c.ID_Group.in_(group_ids))
        )

    def verify_participant(self, participant_id):
        participants = pandas.read_sql("SELECT ID_Player FROM Table_Player",
                                       self._con)
        return participant_id in participants.ID_Player


if __name__ == '__main__':
    scrubber = Scrubber()
    fire.Fire(scrubber)
