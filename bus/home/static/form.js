const validateForm =() => {
    const usernameInput = document.getElementById('username');
    const userInputLen=usernameInput.value.trim().length;
    const userAge = document.getElementById('age');
    const password=document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    
    if(userInputLen<=3||userInputLen>=20)
    {
        document.getElementById('username-len-error').style.display='block';
       usernameInput.style.borderColor='#ff0000';
    }
    
    else
    {
        document.getElementById('username-len-error').style.display ='none';
        usernameInput.style.borderColor='';
    }
    if(userAge.value==NaN||userAge.value<13)
    {
        document.getElementById('age-error').style.display='block';
        userAge.style.borderColor='#ff0000';
    }
    else{
        document.getElementById('age-error').style.display ='none';
        userAge.style.borderColor='';
    }
    
}