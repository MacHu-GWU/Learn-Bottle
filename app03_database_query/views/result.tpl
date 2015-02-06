<!DOCTYPE html>
<html>
<head>
<title>result page</title>
</head>
<body>


<br>
<a href="/">Go back to index page</a>
<br>
<table frame="box" border="1" align="right" style="width:100%">
  	<tr>
	    <th>integer_type</th>
	    <th>real_type</th> 
	    <th>text_type</th>
	    <th>date_type</th>
	    <th>datetime_type</th>
  	</tr>

	%for record in records:
	<tr>
		%for item in record:
		<td>{{item}}</td>
		%end
	</tr>
	%end
</table>
<br>
<a href="/">Go back to index page</a>
</body>
</html>