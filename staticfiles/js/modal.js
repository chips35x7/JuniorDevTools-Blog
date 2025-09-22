"use strict";

const modalBg = document.querySelector(".modal-bg");
const modal = document.querySelector(".custom-modal");
const openModal = document.querySelector(".open-custom-modal");
const closeModal = document.getElementById("close-custom-modal");
const body = document.querySelector("body");

openModal.addEventListener("click", () => {
  console.log("Button Clicked");
  modalBg.style.display = "block";
  body.style.overflowY = "hidden";
  modal.classList.add("animate");
});

closeModal.addEventListener("click", () => {
  // modalBg.classList.remove("custom-modal--active");
  modalBg.style.display = "none";
  body.style.overflowY = "visible";
  modal.classList.remove("animate");
});
