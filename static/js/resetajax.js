$(document).on('submit', '#page-confirmation', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'userdata/validate/',
        data: {
            email:$('#email').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){

            var modal = document.getElementById("SuccessModal");


            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close2")[0];


            modal.style.display = "block";


            // When the user clicks on <span> (x), close the modal
            span.onclick = function() {
            modal.style.display = "none";
            }

            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
            }
            
        },
        error:function(){

            var modal = document.getElementById("FailedModal");

            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close")[0];

            modal.style.display = "block";
            

            // When the user clicks on <span> (x), close the modal
            span.onclick = function() {
            modal.style.display = "none";
            }

            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
            }
        }
    });
});