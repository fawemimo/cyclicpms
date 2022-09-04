// window.onclick = function(e) {
//     e.preventDefault();
//     openclose(event)
  
// }
let clickEvent = document.getElementsByClassName('.dropdown-expand');

clickEvent.addEventListener('click',openclose,false);
let content = document.getElementById('toggle');
// console.log(clickEvent)
function close() {
    let dropdowns = document.querySelectorAll('.dropdown-expand')
    for (let i = 0;  i< dropdowns.length; i++) {
        dropdowns[i].classList.remove('dropdown-expand')
        
    }
}

function openclose(event) {
    
    if (!event.target.matches('.dropdown-toggle')){
        close();

    } else {
        let toggle = event.target.dataset.toggle
        let content = document.getElementById(toggle)
        if (content.classList.contains('dropdown-expand')){
            content.classList.remove('dropdown-expand');
            close();
        } else {
            close();
            content.classList.add('dropdown-expand')
        }
    }
}



let bars = document.querySelector('ul li i');
let body = document.querySelector('body')
bars.addEventListener('click',collapse,false);
function collapse(e) {
    e.preventDefault();
  
        body.classList.toggle('sidebar-expand')
      
   
}


// form 

// let form = document.querySelector('#filter')
// form.addEventListener('keyup',search,false)

// function search(e) {
//     e.preventDefault();
//     let text = e.target.value.toLowerCase();
//     let content = document.querySelector('body');
//     let body = content.querySelector('.wrapper');
//     Array.from(content).forEach(function(item){
//         let search = item.firstChild.textContent;
//         if(search.toLowerCase().indexOf(text != -1)) {
//         item.style.display = 'block';
//     } else {
//         item.style.display = 'none';
//     }
//     })
    
// }

