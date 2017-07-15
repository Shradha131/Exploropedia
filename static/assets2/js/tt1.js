$(".readmore").on('click touchstart', function(event) {
        var txt = $(".more-content").is(':visible') ? 'Show more (+)' : 'Less (–)';
        $(this).parent().prev(".more-content").toggleClass("visible");
        $(this).html(txt);
        event.preventDefault();
    });