<?php
include 'config.php';
$conn = @mysqli_connect($servername, $username, $password);
@mysqli_select_db($conn, "sqli");
$query = "SELECT name FROM users";
$result = @mysqli_query($conn, $query);
if(empty($result)) {
                $query = "CREATE TABLE users (
                          name varchar(255) NOT NULL,
                          `1` varchar(255),
                          `2` varchar(255),
                          `3` varchar(255),
													`4` varchar(255),
													`5` varchar(255),
													`6` varchar(255),
													`7` varchar(255),
													`8` varchar(255),
													`9` varchar(255)
                          )";
                $result = @mysqli_query($conn, $query);
}
if ($_POST && $_POST["user"]) {
	setcookie("user", $_POST["user"]);
	@mysqli_query($conn, "INSERT INTO users (name, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`) VALUES ('custom-".@mysqli_real_escape_string($conn, $_POST["user"])."', '', '', '', '', '', '', '', '', '');");
}
if ($_POST && $_POST["action"]) {
	if ($_POST["action"] == "Create") {
		if (!($_POST["number"]!="1" && $_POST["number"]!="2" && $_POST["number"]!="3" && $_POST["number"]!="4" && $_POST["number"]!="5" && $_POST["number"]!="6" && $_POST["number"]!="7" && $_POST["number"]!="8" && $_POST["number"]!="9")) {
			@mysqli_query($conn, "UPDATE users SET `".$_POST["number"]."` = '".@mysqli_real_escape_string($conn, $_POST["value"])."' WHERE name = 'custom-".@mysqli_real_escape_string($conn, $_COOKIE["user"])."';");
		}
		else {echo "plz dont hack our database thank you";}
	}
	if ($_POST["action"] == "Read") {
		echo "SELECT `".$_POST["number"]."` FROM users WHERE name = 'custom-".@mysqli_real_escape_string($conn, $_COOKIE["user"])."';<br>";
		$result = @mysqli_query($conn, "SELECT `".$_POST["number"]."` FROM users WHERE name = 'custom-".@mysqli_real_escape_string($conn, $_COOKIE["user"])."';");
		echo "Result: ".@mysqli_fetch_row($result)[0];
	}
}
echo "<h1>Welcome to manager!</h1>";
if ($_COOKIE["user"]) {
	echo "Hello, ".$_COOKIE["user"]."!<br>";
	echo "Please select your number: <br>";
	echo "<form method='post'><select name='number'><option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option>
	<option value='5'>5</option><option value='6'>6</option><option value='7'>7</option><option value='8'>8</option><option value='9'>9</option></select><br>
	Value (if creating): <input type='text' name='value'></input><br>
	<input type='submit' value='Read' name='action'></input><input type='submit' value='Create' name='action'></input>";
}
else {
	echo "<form method='post'>Please enter your username: <input name='user' type='text'></input>";
	echo "<input type='submit' value='Login'></input></form>";
}
