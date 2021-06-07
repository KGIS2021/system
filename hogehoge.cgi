#!/usr/bin/python3
#-*-coding:utf-8-*-
print("Content-type: text/html; charset=utf-8")

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(

"""
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>Open Street Map Test</title>
  <style type="text/css">
    html,body{ margin: 0px; }
    form p { display: inline-block;}
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script type="text/javascript" src="http://www.openlayers.org/api/OpenLayers.js"></script>
  <script type="text/javascript" src="func.js"></script>
</head>
<body>
  <form name="myform" id="form" method="POST" action="receive.cgi">
    <p>
    <div id="MapCanvas" style="width:300px;height:300px;" name='map'></div>
    <script type="text/javascript">MapInit();</script>
    </p>
    x<input type="text" size="10" name="x">
    y<input type="text" size="10" name="y">
    <p>
    コメント：<input type="text" name='comment'>
    </p>
    <p>
    <input type="submit" value="投稿">
    </p>
  </form>
</body>
</html>
"""
)
