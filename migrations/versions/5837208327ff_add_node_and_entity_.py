"""Add node and entity models

Revision ID: 5837208327ff
Revises: 2018cb70b484
Create Date: 2013-09-23 15:06:14.583816

"""

# revision identifiers, used by Alembic.
revision = '5837208327ff'
down_revision = '2018cb70b484'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('remoteentity',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('type', sa.Enum(), nullable=True),
    sa.Column('provider', sa.String(length=128), nullable=True),
    sa.Column('remote_id', sa.String(length=128), nullable=False),
    sa.Column('internal_id', sa.GUID(), nullable=False),
    sa.Column('data', sa.JSONEncodedDict(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id'),
    sa.UniqueConstraint('provider','remote_id','type', name='remote_identifier')
    )
    op.create_table('node',
    sa.Column('id', sa.GUID(), nullable=False),
    sa.Column('label', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'step', sa.Column('node_id', sa.GUID(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'step', 'node_id')
    op.drop_table('node')
    op.drop_table('remoteentity')
    ### end Alembic commands ###
