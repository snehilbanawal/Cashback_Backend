// Scrolling Navbar
var nav = document.querySelector("nav");
window.addEventListener("scroll", () => {
  nav.classList.toggle("nav-scrolling", window.scrollY > 0);
});
