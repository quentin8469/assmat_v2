slide_position = 0
size = 5

let slides = document.getElementsByClassName("item 1")
slide_length = slides.length
let afterButton = document.querySelector(".after")
let beforeButton = document.querySelector(".befor")

function update() {
    for (let slide of slides) {
        slide.classList.remove("shows")
        slide.classList.add("hidden")
    }

    for (let i = slide_position; i < slide_position + size; i++) {
        slides[i].classList.remove("hidden");
        slides[i].classList.add("shows");
    }
}

function nextSlide() {
    if (slide_position + size == slide_length) {
        slide_position = 0;
    } else {
        slide_position++;
    }

    update();
}

function beforeSlide() {
    if (slide_position == 0) {
        slide_position = slide_length - size;
    }
    else {
        slide_position--;
    }
    update();
}

update()
afterButton.addEventListener("click", nextSlide);
beforeButton.addEventListener("click", beforeSlide);