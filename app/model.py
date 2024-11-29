import datetime
from pydantic import BaseModel


# モデル定義
class Daily(BaseModel):
    id: int
    date: datetime.datetime
    content: str
    weather: int
