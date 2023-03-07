document.body.onload = function() {
    setTimeout (function() {
        let preloader = document.getElementById ('page-preloader');
        if ( !preloader.classList.contains('done') ) {
            preloader.classList.add('done');
        };
    }, 1000);
};


// Обработка авторизации и регистрации
const authRegisterText = document.querySelector('.user-name');
const loginForm = document.querySelector('.login-form');
const registerForm = document.querySelector('.register-form');
const closeFormButton = document.querySelector('.form-close');
const closeFormButton2 = document.querySelector('.form-close2');
const backgroundBlackout = document.querySelector('.background-blackout');
const haventAccount = document.querySelector('.h3-text');
const haveAccount = document.querySelector('.h3-text-reg');


if (authRegisterText.innerText == 'Регистрация / Авторизация') {
    authRegisterText.addEventListener ('click', function () {
        loginForm.classList.remove('element-hidden');
        backgroundBlackout.classList.remove('opacity-none');
    });
    
    closeFormButton.addEventListener ('click', function () {
        loginForm.classList.add('element-hidden');
        registerForm.classList.add('element-hidden');
        backgroundBlackout.classList.add('opacity-none');
    });
    
    closeFormButton2.addEventListener ('click', function () {
        loginForm.classList.add('element-hidden');
        registerForm.classList.add('element-hidden');
        backgroundBlackout.classList.add('opacity-none');
    });
    
    haventAccount.addEventListener ('click', function () {
        registerForm.classList.remove('element-hidden');
        loginForm.classList.add('element-hidden');
    });
    
    haveAccount.addEventListener ('click', function () {
        registerForm.classList.add('element-hidden');
        loginForm.classList.remove('element-hidden');
    });
} else {
    /* Слайдбар при нажатии на ник */
};



// Обработка ошибок
closeFormError = document.querySelector('.form-error');
closeFormErrorButton = document.querySelector('.close-button3');

closeFormErrorButton.addEventListener('click' , function () {
    closeFormError.classList.add('opacity-none');
});


