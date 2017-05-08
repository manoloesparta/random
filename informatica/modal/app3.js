Parse.initialize("gpP78KnzSdCoqfgE1HpbxyT6HpXExyQ69r0g4gaK","259PLIB6Qn9xi9qK071t5DG1H0VahGc4tslfD8x6");
Parse.$ = jQuery;
Parse.User.enableRevocableSession();

$(document).ready(function(){

	getUser();

	$("#display-user").on("click", "a", function(event){
		event.preventDefault();

		var newMiles = Parse.Object.extend("newMiles");
		var id = $(this).attr("href");
		var q = new Parse.Query(newMiles);
		q.equalTo("objectId", id);
		q.find({
			success: function(results){
				console.log(results[0].get("user"));
				console.log(results[0].get("date"));
				console.log(results[0].get("currentMiles"));
				console.log(results[0].get("officeStartTime"));
				console.log(results[0].get("officeEndTime"));
				console.log(results[0].get("visitStartTime"));
				console.log(results[0].get("visitEndTime"));
				console.log(results[0].get("cancelDescription"));
				console.log(results[0].get("childName"));
				console.log(results[0].get("signatureImage"));
			}, error: function(error){
				console.log(error.message);
			}
		});
	});
});

var User = Parse.Object.extend("newMiles");

function getUser(){
	var query = new Parse.Query(User);
	query.find({
		success: function(results){
			var output = "";
			for(var i in results){
				var username = results[i].get("user");
				var id = results[i].id;
				output += "<tr class='usuarios'>";
				output += "<td><a href='"+ id +"' data-toggle='modal' data-target='#myModal'>";
				output += username + "</a></td>"
				output += "</tr>";
			}
			$("#display-user").html(output);
		},error: function(error){
			alert("Query error: " + error.message);
		}
	});
}