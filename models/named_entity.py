from sqlalchemy import Column, Integer, String

from db import Base, engine


class NamedEntity(Base):

    __tablename__ = "named_entity"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    entity_name = Column("entity_name", String(64), unique=True)
    standard_name = Column("standard_name", String(64))
    category = Column("category", String(32))


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

