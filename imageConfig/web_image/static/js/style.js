#Author Name - Mohamed Imran
#Date - 11-10-2019 -  12-10-2019
#purpose - Jquery file for web app 
$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
                email : $('#emailInput').val(),
                Confirmpassword : $('#Confirmpassword').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data["client_token"]).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

    });
    

	$('#login').on('click', function(event) {

		$.ajax({
			data : {
				name : $('#nameInputlog').val(),
                email : $('#emailInputlog').val(),
			},
			type : 'POST',
			url : '/login'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlertlog').text(data.error).show();
				$('#successAlertlog').hide();
			}
			else {
				$('#successAlertlog').text(data["client_token"]).show();
				$('#errorAlertlog').hide();
			}

		});

		event.preventDefault();

	});

	$('#createAcc').on('click',function(){
		$('#efg').show();
		$('#abc').hide();
	});
	$('#loginAcc').on('click',function(){
		$('#abc').show();
		$('#efg').hide();
	});
});
