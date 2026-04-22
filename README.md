# python-sqlite-practice

Python の標準ライブラリ `sqlite3` を使った、SQLite の基本操作練習用スクリプトです。

## 概要

`main.py` は次の処理を行います。

1. `sample.db` に接続
2. `users` テーブルを作成（存在しない場合のみ）
3. サンプルデータ `("Taro", 20)` を1件追加
4. `users` テーブルの全件を取得して表示

## 実行方法

```bash
python main.py
```

## 出力例

```text
(1, 'Taro', 20)
(2, 'Taro', 20)
```

実行するたびに `INSERT` が実行されるため、レコードは増えていきます。
