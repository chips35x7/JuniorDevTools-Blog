"use strict";

const secBtns = document.querySelectorAll(".control");
const sections = document.querySelectorAll(".section");

function checkActiveBtn(referenceAttribute) {
  for (let y = 0; y < secBtns.length; y++) {
    if (secBtns[y].getAttribute("href").slice(2) == referenceAttribute) {
      secBtns[y].classList.add("active-btn");
    } else {
      secBtns[y].classList.remove("active-btn");
    }
  }
}

for (let i = 0; i < secBtns.length; i++) {
  const currentBtn = secBtns[i];
  currentBtn.addEventListener("click", () => {
    let referenceAttribute = currentBtn
      .getAttribute("href")
      .slice(2, currentBtn.length);
    for (let x = 0; x < sections.length; x++) {
      let sectionClassList = sections[x].classList;
      sectionClassList.remove("active-el");
      if (sectionClassList.contains(referenceAttribute)) {
        checkActiveBtn(referenceAttribute);
        sectionClassList.add("active-el");
      }
    }
  });
}

window.addEventListener("load", () => {
  const hash = window.location.hash.slice(1);
  console.log(hash);
  if (hash) {
    for (let x = 0; x < sections.length; x++) {
      let sectionClassList = sections[x].classList;
      sectionClassList.remove("active-el");
      if (sectionClassList.contains(hash)) {
        checkActiveBtn(hash);
        sectionClassList.add("active-el");
      }
    }
  }
});
