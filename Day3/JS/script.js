const menuOpen = document.getElementById("open");
const menuClose = document.getElementById("close");

const container = document.querySelector(".container");

console.log(container);

menuOpen.addEventListener("click", () => {
  console.log("Click");
  container.classList.add("show-nav");
});

menuClose.addEventListener("click", () => {
  console.log("Click");
  container.classList.remove("show-nav");
});
