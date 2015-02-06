<!DOCTYPE html>
<html>
<head>
<title>This is the home page</title>
</head>
<body>

<form action="/result" method="POST">
Query From Database

<br>
integer_value between
<br>
<input type="number" name="integer_lowerbound" size="10" value="{{integer_lowerbound}}"> and <input type="number" name="integer_upperbound" size="10" value="{{integer_upperbound}}">

<br>
real_value between
<br>
<input type="number" name="real_lowerbound" size="10" value="{{real_lowerbound}}"> and <input type="number" name="real_upperbound" size="10" value="{{real_upperbound}}">

<br>
text_value contains
<br>
<input type="text" name="text_pattern" size="10" value="{{text_pattern}}">

<br>
date_value between
<br>
<input type="date" name="date_lowerbound" size="10" value="{{date_lowerbound}}"> and <input type="date" name="date_upperbound" size="10" value="{{date_upperbound}}">

<br>
datetime_value between
<br>
<input type="datetime" name="datetime_lowerbound" size="10" value="{{datetime_lowerbound}}"> and <input type="datetime" name="datetime_upperbound" size="10" value="{{datetime_upperbound}}">

<br>
<input type="submit" value="Submit">
</form>

<form action="/" method="POST">
<input type="submit" value="clear all value">
</form>
</body>
</html>