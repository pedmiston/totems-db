from invoke import task
import pandas
import db
from db import DB
from models import Group, Player, Workshop, PlayerObs, Totem, WorkShopObs

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
def print_player_details(ctx, player_id):
    db = DB()
    player = db._query_player(player_id)
    print(player)

@task
def print_team_details(ctx, group_id):
    db = DB()
    team = db._query_team(group_id)
    print(team)

@task
def print_diachronic_teams(ctx):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Group)
                      .filter_by(Treatment='Diachronic'))
    for r in results:
        print('{}\t\t{}\t\t{}'.format(r.ID_Group, r.Size, r.Open))

@task
def print_isolated_teams(ctx):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Group)
                      .filter_by(Treatment='Isolated'))
    for r in results:
        print('{}\t\t{}\t\t{}'.format(r.ID_Group, r.Size, r.Open))

@task
def print_synchronic_teams(ctx):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Group)
                      .filter_by(Treatment='Synchronic'))
    print('ID_Group\t\tSize\t\tOpen')
    for r in results:
        print('{}\t\t{}\t\t{}'.format(r.ID_Group, r.Size, r.Open))

@task
def print_players_in_team(ctx, group_id):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Player)
                      .filter_by(ID_Group=group_id))
    for r in results:
        print(r)

@task
def print_team_of_player(ctx, player_id):
    db = DB()
    session = db._sessionmaker()
    player = db._query_player(player_id)
    results = (session.query(Player)
                      .filter_by(ID_Group=player.ID_Group))
    for r in results:
        print(r)


@task
def print_team_playerobs(ctx, group_id):
    db = DB()
    session = db._sessionmaker()
    player_ids = [r.ID_Player for r in session.query(Player).filter_by(ID_Group=group_id)]
    for player_id in player_ids:
        results = session.query(PlayerObs).filter_by(ID_Player=player_id)
        for r in results:
            print(r)

@task
def print_team_totems(ctx, group_id):
    db = DB()
    session = db._sessionmaker()
    player_ids = [r.ID_Player for r in session.query(Player).filter_by(ID_Group=group_id)]

    for player_id in player_ids:
        results = session.query(Totem).filter_by(ID_Player=player_id)
        for r in results:
            print(r)

@task
def print_totems(ctx, player_id):
    db = DB()
    session = db._sessionmaker()
    results = session.query(Totem).filter_by(ID_Player=player_id)
    for r in results:
        print(r)


@task
def print_workshopobs(ctx, player_id):
    db = DB()
    session = db._sessionmaker()
    results = session.query(WorkShopObs).filter_by(ID_Player=player_id)
    for r in results:
        print(r)


@task
def print_team_workshopobs(ctx, group_id):
    db = DB()
    session = db._sessionmaker()
    player_ids = [r.ID_Player for r in session.query(Player).filter_by(ID_Group=group_id)]

    for player_id in player_ids:
        results = session.query(WorkShopObs).filter_by(ID_Player=player_id)
        for r in results:
            print(r)


@task
def open_teams(ctx, group_ids):
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
def run_sql(ctx, command_file):
    """Run arbitrary SQL commands from a file."""
    db = DB()
    cmds = [line.strip() for line in open(command_file).readlines()]
    for line in open(command_file).readlines():
        line = line.strip()
        print('Executing: {}'.format(line))
        db._engine.execute(line)


@task
def print_workshop(ctx, player_id):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Workshop)
                      .filter_by(ID_Player=player_id))
    for r in results:
        print(r)


@task
def print_n_trials(ctx, player_id):
    db = DB()
    session = db._sessionmaker()
    results = (session.query(Workshop)
                      .filter_by(ID_Player=player_id))
    print(len(list(results)))


@task
def clone_tom_participants(ctx):
    db = DB()
    session = db._sessionmaker()
    ids = [int(participant_id) for participant_id in open("tom-ids.txt")]
    values = []
    for participant_id in ids:
        player = db._query_player(participant_id, session=session)
        clone_id = int(str(player.ID_Player) + str(player.Ancestor))
        clone_group = player.ID_Group + "-" + str(player.Ancestor)
        values.append(dict(ancestor_id=player.ID_Player, ancestor_group=player.ID_Group, clone_id=clone_id, clone_group=clone_group))
    data = pandas.DataFrame(values).sort_values(by=["ancestor_group", "ancestor_id"])
    print(data)

@task
def clone_player(ctx, player_id):
    """Clone a player's data to a new group."""
    db = DB()
    session = db._sessionmaker()
    orig_player = db._query_player(player_id, session=session)
    orig_group = db._query_team(orig_player.ID_Group, session=session)

    cloned_group = Group(
        ID_Group=orig_group.ID_Group + "-" + str(orig_player.Ancestor),
        Size=1,
        Open=False,
        Treatment="Isolated",
        BuildingTime=orig_group.BuildingTime,
        Status=orig_group.Status,
    )
    session.add(cloned_group)
    session.flush()
    print(f"Cloned group: {cloned_group}")

    cloned_player = Player(
        ID_Player=int(str(orig_player.ID_Player) + str(orig_player.Ancestor)),
        Sex=orig_player.Sex,
        Age=orig_player.Age,
        # ID_Number
        # Status_Start
        # Status_End
        # ID_Call
        # Gain
        Score=orig_player.Score,
        BestTotem=orig_player.BestTotem,
        # Knowledge
        Ancestor=orig_player.Ancestor,
        ID_Group=cloned_group.ID_Group
    )
    session.add(cloned_player)
    session.flush()  # creates new ID_Player

    cloned_player.ID_Number = cloned_player.ID_Player
    print(f"Cloned player: {cloned_player}")

    results = session.query(Workshop).filter_by(ID_Player=orig_player.ID_Player)
    for orig_workshop in results:
        w = Workshop(
            WorkShop1 = orig_workshop.WorkShop1,
            WorkShop2 = orig_workshop.WorkShop2,
            WorkShop3 = orig_workshop.WorkShop3,
            WorkShop4 = orig_workshop.WorkShop4,
            WorkShopString = orig_workshop.WorkShopString,
            WorkShopResult = orig_workshop.WorkShopResult,
            Success = orig_workshop.Success,
            Innov = orig_workshop.Innov,
            TrialTime = orig_workshop.TrialTime,
            ID_Player = cloned_player.ID_Player
        )
        session.add(w)
        session.flush()

    results = session.query(Totem).filter_by(ID_Player=orig_player.ID_Player)
    for orig_totem in results:
        t = Totem(
            Totem1 = orig_totem.Totem1,
            Totem2 = orig_totem.Totem2,
            Totem3 = orig_totem.Totem3,
            ScoreTotem = orig_totem.ScoreTotem,
            TotemTime = orig_totem.TotemTime,
            ID_Player = cloned_player.ID_Player
        )
        session.add(t)
        session.flush()

    session.commit()
