"""empty message

Revision ID: 45557ab35630
Revises: 
Create Date: 2022-04-26 17:10:04.114690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45557ab35630'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
 
    op.create_table('flights',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('departureDate', sa.DateTime(), nullable=True),
    sa.Column('departureAirportName', sa.String(length=100), nullable=True),
    sa.Column('departureAirportCode', sa.String(length=100), nullable=True),
    sa.Column('departureCity', sa.String(length=100), nullable=True),
    sa.Column('departureLocate', sa.String(length=100), nullable=True),
    sa.Column('arrivalDate', sa.DateTime(), nullable=True),
    sa.Column('arrivalAirportName', sa.String(length=100), nullable=True),
    sa.Column('arrivalAirportCode', sa.String(length=100), nullable=True),
    sa.Column('arrivalCity', sa.String(length=100), nullable=True),
    sa.Column('arrivalLocate', sa.String(length=100), nullable=True),
    sa.Column('ticketprice', sa.Float(), nullable=True),
    sa.Column('flightNumber', sa.String(length=100), nullable=True),
    sa.Column('seatCapacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fullName', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('outboundFlight', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['outboundFlight'], ['flights.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')

    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('flights')
    op.drop_table('users')
    # ### end Alembic commands ###
