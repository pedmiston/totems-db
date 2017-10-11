#!/usr/bin/env python
from os import environ

import sqlalchemy
from sqlalchemy.orm import sessionmaker

import ansible_vault
from unipath import Path
import fire
import pandas

from models import Group, Player


PROJ = Path(__file__).absolute().parent

class DB:
    def __init__(self):
        self._engine = connect_to_db()
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
        player = (session.query(Player)
                         .filter_by(ID_Player=player_id)
                         .first())
        return player

    def _query_team(self, group_id, _session=None):
        session = _session or self._sessionmaker()
        group = (session.query(Group)
                        .filter_by(ID_Group=group_id)
                        .first())
        return group


def connect_to_db():
    url = "mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}".format(
        user='experimenter',
        password=get_from_vault('experimenter_password'),
        host='128.104.130.116',
        port='3306',
        dbname='Totems',
    )
    con = sqlalchemy.create_engine(url)
    return con


def get_from_vault(key=None, vault_file='vars/secrets.yml'):
    try:
        ansible_vault_password_file = environ['ANSIBLE_VAULT_PASSWORD_FILE']
    except KeyError:
        raise AssertionError('Set the ANSIBLE_VAULT_PASSWORD_FILE environment variable')
    ansible_vault_password = open(ansible_vault_password_file).read().strip()
    vault = ansible_vault.Vault(ansible_vault_password)
    secrets_yaml = Path(PROJ, vault_file)
    data = vault.load(open(secrets_yaml).read())
    if key is None:
        return data
    else:
        return data.get(key)
