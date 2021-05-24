$(document).on('submit', '#add-owner', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'confowner/add/',
        data: {
            username:$('#username').val(),
            password:$('#password').val(),
            email:$('#email').val(),
            ph_number:$('#phnumber').val(),
            c_code:$('#c_code').val(),
            loc:$('#loc').val(),
            gym_id:$('#gym_id').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert("User created!");
        },
        error:function(){
            alert("Value Error!");
        }
    });
});