'use strict';

function checkRegister() {
    
    // Basic content check for new users

    const username = document.querySelector("#new_username").value.trim();
    const password = document.querySelector("#new_password").value.trim();
    const confirm_password = document.querySelector("#confirm_password").value.trim();

    function resetValues() {
        document.querySelector("#new_username").value = "";
        document.querySelector("#new_password").value = "";
        document.querySelector("#confirm_password").value = "";
    }

    if (username.length < 4) {
        alert("Username must be atleast 4 characters long!");
        resetValues();
        return false;
    }

    if (password.length < 6) {
        alert("Password must be atleast 6 characters long!");
        resetValues();
        return false;
    }

    let hasNumber = /\d/;

    if (!hasNumber.test(password)) {
        alert("Password must include atleast 1 number!")
        resetValues();
        return false;
    }
    
    let specialCharacters = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;

    if (!specialCharacters.test(password)) {
        alert("Password must include atleast 1 special character!");
        resetValues();
        return false;
    }

    if (password !== confirm_password) {
        alert("Passwords do not match!");
        resetValues();
        return false;
    }

    let maliciousCharacters = /[<>!;,'"]/;

    if (maliciousCharacters.test(username)) {
        alert("Invalid characters in username!");
        resetValues();
        return false;
    }

    return true;
}
