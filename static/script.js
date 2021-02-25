


window.onload = function () {
    document.getElementById("str_user").setAttribute("value", salutation[random]);

    input = document.getElementById("str_user");

    input.addEventListener("keyup", function (event) {
        
        if (event.keyCode == 13) {
            
            console.log(str_input_user)
            print_user();
            request_ajax("str_user", str_input_user, callback_json);
            //Send request
            spinner.style.display = "block";
        }

    });
    
}

