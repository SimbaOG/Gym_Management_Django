$(document).on('submit', '#master-login', function(e) {
    e.preventDefault();
    if (!$('#username').val()) {
        alert('Enter your name!');
    }
    else if (!$('#password').val()) {
        alert('Enter your password!');
    }
});