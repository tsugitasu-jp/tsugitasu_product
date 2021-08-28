# 環境構築(Django+mongo+vue)

## Cloneする
```git clone https://github.com/tsugitasu-jp/tsugitasu.git```

## 以下の環境変数ファイルをプロジェクト直下に置く
* .env
* drf-firebase-admin-firebase-adminsdk.json
* settings.ini

※ 上からdocker、firebase、djangoの環境変数

## Dockerイメージを作成 -> コンテナを起動
プロジェクト直下のパスで以下を実行
```docker-compose up -d```

## コンテナの確認
```docker ps -a```
* django-temp-app(port: 8000)
* mongo(port: 27017)
* tsugitasu_front(port: 8080)
上記コンテナのstatusがupになっていたらOK

## トップページにアクセスできるか検証
* "http://localhost:8000/" でAPIサーバトップにアクセス出来る
* "http://localhost:8080/" でルーティングサーバのトップページにアクセス出来る

## Dockerコンテナ内に入る
```
docker-compose exec app bash
```

## Vue.jsのプロジェクト作成
### 1.コンテナ内でプロジェクト作成
```
vue create <プロジェクト名>
```
### 2.プロジェクトのテスト
```
cd <プロジェクト名>
npm run serve
```

## DBの作成とコレクション(RDBのテーブルに当たる)を作成
Dockerコンテナ内のbashから以下を実行  
```
python manage.py migrate
```

## DBの中身をGUIで参照する
- mongo commpassをダウンロード  
- mongodb://<user>:<pass>@localhost:27017  

※ userとpassはsettings.iniファイルを参照  

## コンテナの停止
```
docker-compose down
```
