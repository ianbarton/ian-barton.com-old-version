$(document).ready(function(){

        $("#toc").append('<p>On this page:</p>')
            $("div.outline-2 h2, div.outline-3 h3").each(function(i) {
                    //if ( $(this).is("h2")) {
                    var current = $(this);
                    current.attr("id", "title" + i);
                    $("#toc").append("<li><a id='link" + i + "' href='#title" +
                                     i + "' title='" + current.attr("tagName") + "'>" + 
        current.html() + "</a>" + "</li>");

                    //}


});

        });