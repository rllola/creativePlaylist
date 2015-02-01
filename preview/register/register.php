<?php 
	
	$servername = "localhost";
	$username = "root";
	$password = "Amsterdam";
	$dbname = "creativePlaylist";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
		  
	function sanitize_string($str) {
		if (get_magic_quotes_gpc()) {
			$sanitize = mysqli_real_escape_string(stripslashes($str));	 
		} else {
			$sanitize = mysqli_real_escape_string($str);	
		} 
		return $sanitize;
	}
	
	$first_name = $conn->real_escape_string($_POST['first_name']);
	$last_name = $conn->real_escape_string($_POST['last_name']);
	$username = $conn->real_escape_string($_POST['username']);
	$email = $conn->real_escape_string($_POST['email']);
	$address = $conn->real_escape_string($_POST['address']);
	
	echo $first_name;
	echo $last_name;
	echo $username;
	echo $email;
	echo $address;

	if ( isset($first_name) && !empty($first_name) &&
	 isset($last_name) && !empty(last_name) &&
	 isset($username) && !empty($username) &&
	 isset($email) && !empty($email) &&
	 isset($address) && !empty($address)) {
	 
	 	echo "All good so far";
	 	
	 	$sql = "INSERT INTO User (Id_user, username, email, first_name, last_name, address)
		VALUES (null, '$username', '$email', '$first_name', '$last_name', '$address')";

		if ($conn->query($sql) === TRUE) {
		    echo "New record created successfully";
		    header('Location:/register/?registered=True');
		} else {
		    echo "Error: " . $sql . "<br>" . $conn->error;
		    header('Location:/register/?registered=False');
		}
		
	}		  
		  
?>