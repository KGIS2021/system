#!/usr/bin/python3
#-*-coding:utf-8-*-
print("Content-type: text/html; charset=utf-8")

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(

"""
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>学生入力フォーム</title>
</head>

<body>
    入力フォーム<br> <br>
    <form name="form" method="post" action="confirm.py">
      学籍番号:<br>
        <input type="number" name="number" placeholder="半角数字" required>＊必須項目<br> <br>
      名前:<br>
        <input type="text" name="name"  required>＊必須項目 <br> <br>
      年齢:<br>
        <input type="number" name="age" placeholder="半角数字" required>＊必須項目<br> <br>
      備考:<br>
        <textarea name="note" value=""></textarea>
        <br> <br>
      <input type="submit" value="確認">
    </form>
</body>
</html>
"""
)