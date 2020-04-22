$(document).ready(function() {
	(function(){
	  var newscript = document.createElement('script');
	     newscript.type = 'text/javascript';
	     newscript.async = true;
	     newscript.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js';
	  (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(newscript);
	})();
	$('.LikesButton').on('click', function(event) {

		$.ajax({
			data : {
				post_id : $(this).attr('post_id')
			},
			type : 'POST',
			url : '/post/like'
		})
		.done(function(data) {
			$('#nOfLikes'+data.post_id).text(data.nOfLikes).show();

		});

	});

});