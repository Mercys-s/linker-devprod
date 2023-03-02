
// Кнопка 'Добавление работы' + Форма + Закрытие формы
const addWorkText = document.querySelector('.add-task-text');
const addWorkForm = document.querySelector('.add-task-form');
const addWorkClose = document.querySelector('#form-close');
const cardSet = document.querySelector('.card-set')


addWorkText.addEventListener('click' , function () {
    addWorkForm.classList.remove('element-hidden')
    addWorkText.classList.add('text-hidden')
    cardSet.classList.add('morphed')
});

addWorkClose.addEventListener('click', function () {
    addWorkForm.classList.add('element-hidden')
    addWorkText.classList.remove('text-hidden')
    cardSet.classList.remove('morphed')
});


// Работа с карточками

let subjectItem = document.querySelectorAll('.subject-item')

subjectItem.forEach (function(item) {
    console.log(item)
    if (item.innerText == "") {
        let notfoundedH1 = document.createElement('h1');
        notfoundedH1.setAttribute('class','notfoundedH1');
        notfoundedH1.innerText = 'Категория пока пуста';
        item.appendChild(notfoundedH1);
    }
} );


// Сообщение об ошибке
closeFormError = document.querySelector('.form-error');
closeFormErrorButton = document.querySelector('.close-button3');

closeFormErrorButton.addEventListener('click' , function () {
    closeFormError.classList.add('opacity-none');
});


