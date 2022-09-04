let header = document.querySelector("header");
let sectionOne = document.querySelector(".home-intro");

let sectionOneOptions = {
  rootMargin: "-200px 0px 0px 0px"
};

let sectionOneObserver = new IntersectionObserver(function(
  entries,
  sectionOneObserver
) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      header.classList.add("nav-scrolled");
    } else {
      header.classList.remove("nav-scrolled");
    }
  });
},
sectionOneOptions);

sectionOneObserver.observe(sectionOne);

AOS.init({
  offset: 400,
  duration:1000,
})

