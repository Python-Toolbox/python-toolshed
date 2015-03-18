"""empty message

Revision ID: d51bb5f40d
Revises: 2321e157a01
Create Date: 2015-03-18 14:41:31.908721

"""

# revision identifiers, used by Alembic.
revision = 'd51bb5f40d'
down_revision = '2321e157a01'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('contributors_url', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('current_version', sa.String(length=20), nullable=True))
    op.add_column('project', sa.Column('first_commit', sa.DateTime(), nullable=True))
    op.add_column('project', sa.Column('forks_url', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('mailing_list_url', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('number_of_contributors', sa.Integer(), nullable=True))
    op.add_column('project', sa.Column('open_issues_url', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('project_stub', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('starred_url', sa.String(), nullable=True))
    op.add_column('project', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('project', sa.Column('summary', sa.String(length=400), nullable=True))
    op.add_column('project', sa.Column('watchers_url', sa.String(), nullable=True))
    op.drop_column('project', 'issues_url')
    op.drop_column('project', 'version')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('version', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('project', sa.Column('issues_url', sa.VARCHAR(length=400), autoincrement=False, nullable=True))
    op.drop_column('project', 'watchers_url')
    op.drop_column('project', 'summary')
    op.drop_column('project', 'status')
    op.drop_column('project', 'starred_url')
    op.drop_column('project', 'project_stub')
    op.drop_column('project', 'open_issues_url')
    op.drop_column('project', 'number_of_contributors')
    op.drop_column('project', 'mailing_list_url')
    op.drop_column('project', 'forks_url')
    op.drop_column('project', 'first_commit')
    op.drop_column('project', 'current_version')
    op.drop_column('project', 'contributors_url')
    ### end Alembic commands ###
