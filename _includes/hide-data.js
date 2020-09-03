document.addEventListener("DOMContentLoaded", function() {
    const hiding_elements = document.querySelectorAll("[data-hide-at]")
    for (const element of hiding_elements) {
        if (element.getAttribute("data-hide-at") < Date.now()) {
            element.style.display = "none";
        }
    }
});
