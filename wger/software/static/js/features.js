jQuery(function($) {
	"use strict";
	// Author Code Here

	// Pricing Box Click Event
	$('.pricing .box-main').click(function() {
		$('.pricing .box-main').removeClass('active');
		$('.pricing .box-second').removeClass('active');
		$(this).addClass('active');
		$(this).next($('.box-second')).addClass('active');
		$('#pricing').css("background-image", "url(" + $(this).data('img') + ")");
		$('#pricing').css("background-size", "cover");
	});
});
