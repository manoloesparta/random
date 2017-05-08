Parse.initialize("gpP78KnzSdCoqfgE1HpbxyT6HpXExyQ69r0g4gaK","259PLIB6Qn9xi9qK071t5DG1H0VahGc4tslfD8x6");
Parse.$ = jQuery;
Parse.User.enableRevocableSession();

LogInStatus();

$(document).ready(function(){

	LogInStatus();
	getUser();

	$("#logout").click(function(event){
		Parse.User.logOut();
		window.location.replace("index.html");
	});

});

function LogInStatus(){
	if(!Parse.User.current()){
		window.location.replace("index.html");
	}else{
		$("#current-user").html("Search here: " + Parse.User.current().get("username"));
	}
}

var User = Parse.Object.extend("User");

function getUser(){
	var query = new Parse.Query(User);
	query.find({
		success: function(results){
			var output = "";
			for(var i in results){
				var username = results[i].get("username");
				output += "<tr>";
				output += "<td>" + username + "</td>";
				output += "<td></td>";
				output += "<td></td>";
				output += "</tr>";
			}
			$("#display-user").html(output);
		},error: function(error){
			alert("Query error: " + error.message);
		}
	});
}