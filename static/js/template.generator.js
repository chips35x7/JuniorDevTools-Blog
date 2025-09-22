"use strict";
import { getImage } from "./utilities.js";
import { reverse } from "./utilities.js";

const servicesTemplate = document.getElementById("services-template");
const projectTemplate = document.getElementById("project-template");
const cardContainer = document.querySelector(".card-container");
const servicesContainer = document.querySelector(".services-container");

function generateService(
  fontawesomeClassType,
  fontawesomeIconType,
  name,
  tagline,
  descriptions,
  img,
  link = "#"
) {
  const clonedElement = servicesTemplate.content.cloneNode(true);

  clonedElement
    .querySelector(".icon")
    .classList.add(fontawesomeClassType, fontawesomeIconType);
  clonedElement.querySelector("h3").textContent = name;
  clonedElement.querySelector(".sub-header").textContent = tagline;

  let descriptionsContainer = clonedElement.querySelector(".content");
  for (let i = 0; i < descriptions.length; i++) {
    let listItem = document.createElement("li");
    listItem.textContent = descriptions[i];
    descriptionsContainer.append(listItem);
  }

  let serviceBtn = clonedElement.querySelector(".service-btn");
  serviceBtn.setAttribute("href", link);

  let serviceImage = clonedElement.querySelector(".service__img");
  serviceImage.setAttribute("src", img);

  servicesContainer.append(clonedElement);
}

function generateCard(img, title, link = "#") {
  const clonedElement = projectTemplate.content.cloneNode(true);
  let cardImage = clonedElement.querySelector(".card__img");
  cardImage.setAttribute("src", img);
  cardImage.setAttribute("alt", title + " Image");
  clonedElement.querySelector(".card__header").textContent = title;
  let cardBtn = clonedElement.querySelector(".card__btn");
  cardBtn.setAttribute("href", link);

  cardContainer.append(clonedElement);
}

fetch("data.json")
  .then((response) => response.json())
  .then((data) => {
    const services = data.services;
    const projects = data.projects;

    for (let i = 0; i < services.length; i++) {
      const service = services[i];
      const serviceSlug = service.slug;
      generateService(
        service.icons[0],
        service.icons[1],
        service.name,
        service.tagline,
        service.descriptions,
        getImage(service.illustration_image),
        reverse("service.php", "service", serviceSlug)
      );
    }
    for (let i = 0; i < projects.length; i++) {
      const project = projects[i];
      const projectSlug = project.slug;
      generateCard(
        getImage(project.image),
        project.name,
        reverse("project.php", "project", projectSlug)
      );
    }
  });
