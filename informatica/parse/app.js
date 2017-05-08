Parse.initialize("gpP78KnzSdCoqfgE1HpbxyT6HpXExyQ69r0g4gaK","259PLIB6Qn9xi9qK071t5DG1H0VahGc4tslfD8x6");
Parse.$ = jQuery;
Parse.User.enableRevocableSession();

$(document).ready(function(){

	LogInStatus();

	$("#register-form").submit(function(event){
		event.preventDefault();

		var name = $("#register-user").val();
		var pass = $("#register-pass").val();
		var passconf = $("#register-password-confirm").val();

		if(pass === passconf)
		{

			var user = new Parse.User();
			user.set("username", name);
			user.set("password", md5(pass));

			user.signUp(null, {
				success: function(user){
					Parse.User.logIn(name, md5(pass), {
						success: function(user){
							console.log("Log in success");
							LogInStatus();
						}, error: function(user, error){
							console.log("Log in failed")
						}
					});
				}, error: function(user, error){
					alert("Sign Up Fail " + error.message);
				}
			});
		}
		else
		{
			alert("Password are not the same");
		}
	});

	$("#login-form").submit(function(event){
		event.preventDefault();

		var name = $("#login-user").val();
		var pass = $("#login-pass").val();

		Parse.User.logIn(name, md5(pass), {
			success: function(user){
				console.log("Log in success");
				LogInStatus();
			}, error: function(user, error){
				console.log("Log in failed")
			}
		});

	});

});

function LogInStatus(){
	if(Parse.User.current()){
		window.location.replace("home.html");
	}
}