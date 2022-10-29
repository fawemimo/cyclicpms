let navButton = document.querySelector('.dropdown-btn');
let dropList = document.querySelector('#requestlist');
navButton.addEventListener('mouseup', display, false);
navButton.addEventListener('mouseover', none, false);

function display(e) {
    e.preventDefault();
    dropList.style.display = 'block';
};

function none(e) {
    e.preventDefault();
    dropList.style.display = 'none';
}

