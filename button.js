$(function() {
    $('#find').click(function() {
 
        $.ajax({
            url: '/signUp',
            data:  
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
