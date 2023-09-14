const closemodalBtn = document.querySelector(".modal-close-button");

closemodalBtn.addEventListener("click", () => {
  document.querySelector(".modal-container").classList.toggle("modal-container-close");
})

const openmodalbtn = document.querySelector(".navigation-link-buttom");

openmodalbtn.addEventListener("click", (e) => {
  e.preventDefault();
  document.querySelector(".modal-container").classList.toggle("modal-container-close");
})
