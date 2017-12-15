from invoke import task
import pandas
import db
from db import DB
from models import Group, Player

@task
def verify_tom_participant_ids(ctx):
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

@task
def install(ctx):
    """Install the totems database on a remote server."""
    ctx.run('ansible-playbook install.yml')

@task
def snapshot(ctx):
    """Take a snapshot of the totems database."""
    ctx.run('ansible-playbook snapshot.yml')

@task
def restore(ctx, dump):
    """Restore the totems database from a snapshot."""
    cmd = 'ansible-playbook restore.yml -e dump={dump}'
    ctx.run(cmd.format(dump=dump))

@task
def verify_player(ctx, player_id):
    db = DB()
    exists = db.verify_player(player_id)
    print('ID_Player={}: {}'.format(player_id, exists))

@task
def print_player_details(self, player_id):
    db = DB()
    player = db._query_player(player_id)
    print(player)

@task
def print_team_details(self, group_id):
    db = DB()
    team = db._query_team(group_id)
    print(team)

@task
def print_diachronic_teams(self):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Group)
                      .filter_by(Treatment='Diachronic'))
    for r in results:
        print('{}\t\t{}\t\t{}'.format(r.ID_Group, r.Size, r.Open))

@task
def print_synchronic_teams(self):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Group)
                      .filter_by(Treatment='Synchronic'))
    print('ID_Group\t\tSize\t\tOpen')
    for r in results:
        print('{}\t\t{}\t\t{}'.format(r.ID_Group, r.Size, r.Open))

@task
def print_players_in_team(self, group_id):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Player)
                      .filter_by(ID_Group=group_id))
    for r in results:
        print(r)

@task
def open_teams(self, group_ids):
    db = DB()
    session = db._sessionmaker()
    for group_id in open(group_ids).readlines():
        team = db._query_team(group_id.strip(), session)
        team.Open = True
    session.commit()

@task
def toggle_open_group(ctx, group_id):
    db = DB()
    db.toggle_group_open(group_id)

@task
def set_group_size(ctx, group_id, size):
    pass

@task
def delete_player(ctx, player_id):
    pass

@task
def run_sql(ctx, command_file):
    """Run arbitrary SQL commands from a file."""
    db = DB()
    cmds = [line.strip() for line in open(command_file).readlines()]
    for line in open(command_file).readlines():
        line = line.strip()
        print('Executing: {}'.format(line))
        db._engine.execute(line)
