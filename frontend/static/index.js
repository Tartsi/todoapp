'use strict';

function checkContent() {
    
    // Basic content check for login-form

    const username = document.querySelector("#username").value.trim();
    const password = document.querySelector("#password").value.trim();

    function resetValues() {
        document.querySelector("#username").value = "";
        document.querySelector("#password").value = "";
    }

    if (username.length < 4) {
        alert("Username not 4 characters!");
        resetValues();
        return false;
    }

    if (password.length < 4) {
        alert("Password not 4 characters!");
        resetValues();
        return false;
    }

    if (username.includes(";") || username.includes("'") || username.includes("--")) {
        alert("Invalid characters in username!");
        resetValues();
        return false;
    }

    return true;
}
