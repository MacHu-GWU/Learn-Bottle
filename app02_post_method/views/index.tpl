<!DOCTYPE html>
<html>
<head>
<title>This is the home page</title>
</head>
<body>

<form action="/result" method="POST">
Calculate the sum of two numbers
<br>
<input type="number" name="value1" size="10" value="{{default_value1}}"> +
<input type="number" name="value2" size="10" value="{{default_value2}}">
<br>
<input type="submit" value="Submit">
<br>
</form>

<form action="/" method="POST">
<input type="submit" value="Assign random value">
</form>

</body>
</html>