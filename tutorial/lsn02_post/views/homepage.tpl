<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>This is the home page</title>
</head>
<body>

<form action="/result" method="POST">
	<!--For more input type options, check: http://www.w3schools.com/tags/tag_input.asp-->
	<div>
		<strong>put a number here</strong>
		<input type="number" name="number_value" size="10" value="" />
	</div>
	<div>
		<strong>put some text here</strong>
		<input type="text" name="text_value" size="10" value="" />
	</div>
	<div>
		<strong>put a date here</strong>
		<input type="date" name="date_value" size="10" value="" />
	</div>
	<div>
		<strong>put a datetime here</strong>
		<input type="datetime" name="datetime_value" size="10" value="" />
	</div>

	<div> 
		<!--checkbox must have a default value, when it is checked, send value, if not, send None-->
		<strong>put a checkbox here</strong>
		<input type="checkbox" name="checkbox_value" size="10" value="checked" />
	</div>
	<div>
		<!--radio is a single choice, you can do the same thing in select-->
		<strong>put a radio here</strong>
		<input type="radio" name="radio_value" value="1" checked="checked" />True?
		<input type="radio" name="radio_value" value="0" />False?
	</div>
	<div>
		<!--select is a single choice, you can do the same thing in radio-->
		<strong>put a select here</strong>
		<select name="select_value">
			<option value="apple" selected>apple
			<option value="pear">pear
			<option value="orange">orange
		</select>
	</div>

	<div>
		<!---reset is a button you can reset the value already in form back to default-->
		<strong>put a reset here</strong>
		<input type="reset" name="reset_value" size="10" value="reset value">
	</div>

	<input type="submit" value="Submit">
</form>

</body>
</html>