<!DOCTYPE html>
<html>
<head>
<title>This is the home page</title>
</head>
<body>

<form action="/upload" method="post" enctype="multipart/form-data">
  Category:      <input type="text" name="category" />
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>

</body>
</html>