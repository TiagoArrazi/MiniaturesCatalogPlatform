from sqlalchemy import create_engine, Column, Integer, String, Boolean, MetaData, Table
from src.dao.filters.filters import *


ENGINE = create_engine("mysql+pymysql://root:12345678@localhost/miniatures", echo=True)
META = MetaData()

MINIATURES = Table(
    'miniatures_test_table', META,
    Column('id', primary_key=True),
    Column('manufacturer', String(40)),
    Column('model', String(40)),
    Column('color', String(20)),
    Column('miniature_manufacturer', String(20)),
    Column('pos_x', Integer),
    Column('pos_y', Integer),
    Column('section', Integer),
    Column('rubber_tires', Boolean),
)


def select(value='', field='', select_all=False):

    if select_all:
        expression = get_all(MINIATURES)
    else:
        expression = filter_by(MINIATURES, field, value)

    conn = ENGINE.connect()
    return conn.execute(expression)


if __name__ == '__main__':
    result = select(field='manufacturer', value='ferrari')
    for row in result:
        print(row)
