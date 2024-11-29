pythonを使ったバックエンドの習作
フロントエンドはこれをそのまま使える↓
https://github.com/violakatze/diary-study

起動
```
cd diary-study-python-backend
docker-compose up -d
```

テーブル作成
```
docker exec -it api bash
python db.py
```
