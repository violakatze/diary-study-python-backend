from sqlalchemy.orm import Session
from dateutil import tz
from datetime import datetime
from model import Daily
from db import DailyTable

UTC = tz.gettz("UTC")


def convert(value: DailyTable) -> Daily:
    """モデル変換"""
    date: datetime = value.date
    result: Daily = {
        "id": value.id,
        "date": date.astimezone(UTC),  # DBの値をUTCとみなしてフラグをつける
        "content": value.content,
        "weather": value.weather,
    }
    return result


def get_all(session: Session) -> list[Daily]:
    """全件取得"""
    results = list(
        map(
            lambda x: convert(x),
            session.query(DailyTable).order_by(DailyTable.date).all(),
        )
    )
    return results


def get(session: Session, id: int) -> Daily:
    """1件取得"""
    item = (
        session.query(DailyTable).filter(DailyTable.id == id).first()
    )  # TODO:エラー処理
    result = convert(item)
    return result


def add(session: Session, daily: Daily):
    """登録"""
    # TODO:エラー処理
    item = DailyTable(date=daily.date, content=daily.content, weather=daily.weather)
    session.add(item)
    session.commit()
    session.refresh(item)


def update(session: Session, daily: Daily):
    """更新"""
    # TODO:エラー処理
    item = session.query(DailyTable).filter(DailyTable.id == daily.id).first()
    item.date = daily.date
    item.content = daily.content
    item.weather = daily.weather
    session.commit()
    session.refresh(item)
    return item


def remove(session: Session, daily: Daily):
    """削除"""
    # TODO:エラー処理
    session.query(DailyTable).filter(DailyTable.id == daily.id).delete()
    session.commit()
