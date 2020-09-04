document.addEventListener("DOMContentLoaded", function() {
    const hiding_elements = document.querySelectorAll("[data-hide-at]")
    for (const element of hiding_elements) {
        const timestamp = element.getAttribute("data-hide-at")
        if (timestamp && timestamp < Date.now()) {
            element.style.display = "none";
        }
    }
});
