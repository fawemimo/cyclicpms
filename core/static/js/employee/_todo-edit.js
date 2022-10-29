let isSelected = document.querySelector('input[type=checkbox]');
console.log(isSelected);
isSelected.addEventListener('click', checked, false);

function checked(e){
    e.preventDefault();
    let isChecked = document.querySelector('label p#checked');
    console.log(isChecked);
    isChecked.classList.add('checked');
}