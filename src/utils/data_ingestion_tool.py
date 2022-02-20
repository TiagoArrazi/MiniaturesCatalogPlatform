import sqlalchemy.engine
from numbers_parser import Document
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


def load_data() -> pd.DataFrame:
    doc = Document("/Users/tiagocostaarrazi/Documents/Catálogo Carrinhos.numbers")
    sheets = doc.sheets()  # Each sheet represents a cataloged section (Section A, Section B, etc.)
    tables = [sheet.tables() for sheet in sheets]
    data = [table[0].rows(values_only=True) for table in tables]

    df_list = [pd.DataFrame(d[1:], columns=d[0]) for d in data]

    df_miniatures = pd.concat(df_list)

    return df_miniatures


def create_table(db_engine: sqlalchemy.engine.Engine) -> None:
    base = declarative_base()

    class Miniature(base):
        __tablename__ = 'miniatures_test_table'

        id = Column(Integer, primary_key=True)
        manufacturer = Column(String(40))
        model = Column(String(40))
        color = Column(String(20))
        miniature_manufacturer = Column(String(20))
        pos_x = Column(Integer)
        pos_y = Column(Integer)
        section = Column(Integer)
        rubber_tires = Column(Boolean)

    base.metadata.create_all(db_engine)


def bulk_insert(data_df: pd.DataFrame, db_engine: sqlalchemy.engine.Engine) -> None:
    with db_engine.begin() as conn:
        data_df.to_sql("miniatures_test_table", con=conn, if_exists="append", index=False)


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:12345678@localhost/miniatures", echo=True)
    # data = load_data()
    # create_table(engine)
    # bulk_insert(data, engine)
