console.log('Hello world')

let header = document.querySelector('header');
let sectionOne = document.querySelector('body');
let sectionOneOptions = {
    rootMargin: '200px 0px 0px 0px'
};
let sectionOneObserver = new IntersectionObserver(function(entries,sectionOneObserver) {
    entries.forEach(entry => {
        // console.log(entry.target)
        if(!entry.isIntersecting) {
            header.classList.add('nav-scroll');            
        } else {
            header.classList.remove(nav-scroll)
        }
    }) 
}, sectionOneOptions);

sectionOneObserver.observe(sectionOne);