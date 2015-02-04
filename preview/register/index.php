<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge"> 
		<meta name="viewport" content="width=device-width, initial-scale=1"> 
		<title>Fullscreen Form Interface</title>
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<meta name="author" content="" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/normalize.css" />
		<link rel="stylesheet" type="text/css" href="css/demo.css" />
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		<link rel="stylesheet" type="text/css" href="css/cs-select.css" />
		<link rel="stylesheet" type="text/css" href="css/cs-skin-boxes.css" />
		<script src="js/modernizr.custom.js"></script>
	</head>
	<body>
	<?php
		$username = "root";
		$password = "Amsterdam";
		$hostname = "localhost"; 

		//connection to the database
		$dbhandle = mysql_connect($hostname, $username, $password)
		  or die("Unable to connect to MySQL");

		//select a database to work with
		$selected = mysql_select_db("creativePlaylist",$dbhandle)
		  or die("Could not select database");

		//execute the SQL query and return records
		$result = mysql_query("SELECT count(*) as total FROM User;");
		if (!$result) {
			echo "Back End Error";
		} else {
			$total = mysql_result($result, 0);
		}
				
		if(!isset($_GET['registered'])) {
		
			if($total<20) {

	?>
		<div class="container">
			<div class="fs-form-wrap" id="fs-form-wrap">
				<div class="fs-title">
					<h1>Register</h1>
					<div class="codrops-top">
					</div>
				</div>
				<form id="myform" class="fs-form fs-form-full" autocomplete="off" method="POST" action="register.php">
					<ol class="fs-fields">
						<li>
							<label class="fs-field-label fs-anim-upper" for="q1">What's your first name ?</label>
							<input class="fs-anim-lower" id="q1" name="first_name" type="text" placeholder="Lola" required/>
						</li>
						<li>
							<label class="fs-field-label fs-anim-upper" for="q2">What's your last name ?</label>
							<input class="fs-anim-lower" id="q2" name="last_name" type="text" placeholder="Dam" required/>
						</li>
						<li>
							<label class="fs-field-label fs-anim-upper" for="q3">Enter a username</label>
							<input class="fs-anim-lower" id="q3" name="username" type="text" placeholder="lolaDam" required/>
						</li>
						<li>
							<label class="fs-field-label fs-anim-upper" for="q4" data-info="We won't send you spam, we promise...">What's your email address ?</label>
							<input class="fs-anim-lower" id="q4" name="email" type="email" placeholder="lola.dam@gmail.com" required/>
						</li>

						<li>
							<label class="fs-field-label fs-anim-upper" for="q5">Enter your mail address</label>
							<textarea class="fs-anim-lower" id="q5" name="address" placeholder="Your address here" required></textarea>
						</li>
					</ol><!-- /fs-fields -->
					<button class="fs-submit" type="submit">Send answers</button>
				</form><!-- /fs-form -->
			</div><!-- /fs-form-wrap -->
		</div><!-- /container -->
		<?php 
				} else {
					echo "<div class='container'>
					<div class='fs-form-wrap' id='fs-form-wrap'>
					<div class='fs-title'>
						<h1>Sorry. Registration are closed.</h1>
					</div>
					</div>
					</div>";
				}
			} else { 
				if ($_GET['registered'] =='True') {
					echo "<div class='container'>
					<div class='fs-form-wrap' id='fs-form-wrap'>
					<div class='fs-title'>
						<h1>You've been registered. Thanks for your contribution.</h1>
					</div>
					</div>
					</div>";
				 } else {
				 
				 	echo "<div class='container'>
					<div class='fs-form-wrap' id='fs-form-wrap'>
					<div class='fs-title'>
						<h1>An error occured. Please try again.</h1>
						<br/>
						<button class='fs-submit' type='submit' onclick='reloc()' >Try Again</button>
					</div>
					</div>
					</div>";
				 
				 
				 } 
			
			}
		?> 
		<script src="js/classie.js"></script>
		<script src="js/selectFx.js"></script>
		<script src="js/fullscreenForm.js"></script>
		<script>
			function reloc() {
			    window.location = "/register/";
			}
		</script>
		<script>
			(function() {
				var formWrap = document.getElementById( 'fs-form-wrap' );

				[].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {	
					new SelectFx( el, {
						stickyPlaceholder: false,
						onChange: function(val){
							document.querySelector('span.cs-placeholder').style.backgroundColor = val;
						}
					});
				} );

				new FForm( formWrap, {
					onReview : function() {
						classie.add( document.body, 'overview' ); // for demo purposes only
					}
				} );
			})();
		</script>
	</body>
</html>