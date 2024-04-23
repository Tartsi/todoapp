'use strict';

function userCreated() {
    alert("User created successfully");
}

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

    let maliciousCharacters = /[<>!;,'"]/;

    if (maliciousCharacters.test(username)) {
        alert("Invalid characters in username!");
        resetValues();
        return false;
    }

    return true;
}
