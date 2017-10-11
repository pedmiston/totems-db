from invoke import task
from db import DB

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
def toggle_group_open(ctx, group_id):
    pass

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
        # db._engine.execute(line)
