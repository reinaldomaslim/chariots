"""chariots table

Revision ID: a5757226e6fa
Revises: 
Create Date: 2019-08-19 15:22:15.841623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5757226e6fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehiclename', sa.String(length=10), nullable=True),
    sa.Column('capacity', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicle_vehiclename'), 'vehicle', ['vehiclename'], unique=True)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=140), nullable=True),
    sa.Column('load', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_timestamp'), 'order', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_timestamp'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_vehicle_vehiclename'), table_name='vehicle')
    op.drop_table('vehicle')
    # ### end Alembic commands ###