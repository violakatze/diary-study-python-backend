from sqlalchemy import create_engine, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

host = "db:3306"
db_name = "db"
user = "db"
password = "password"

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(DATABASE, echo=True)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE, checkfirst=False)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

Base = declarative_base()
Base.query = session.query_property()


# テーブル定義
class DailyTable(Base):
    __tablename__ = "daily"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(timezone=True), unique=True, nullable=False)
    content = Column(String(100), nullable=False)
    weather = Column(Integer, nullable=False)


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
