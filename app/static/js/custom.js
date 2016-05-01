// Read More

// $(document).ready(function(){
// 	$('#bio_btn').toggle(function(){
// 		$('#bio').css({'display:block'});
// 	}, function() {
// 		$('#bio').css({'display:none'});
// 	},
// 	});

$(document).ready(function(){
	$('#hist_btn').click(function(){
		$('#history').toggle("slow");
		if ($(this).text() == "Read More") {
			$(this).text("Read Less");
		}
		else {
			$(this).text('Read More');
		}
	});
	$('#reviews_btn').click(function(){
		$('#reviews').toggle("slow");
		if ($(this).text() == "Read More") {
			$(this).text("Read Less");
		}
		else {
			$(this).text('Read More');
		}
	});

	});