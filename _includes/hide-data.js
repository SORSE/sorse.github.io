document.addEventListener("DOMContentLoaded", function() {
    const hiding_elements = document.querySelectorAll("[data-hide-at]")
    const now = Date.now() % 1000;
    for (const element of hiding_elements) {
        const timestamp = element.getAttribute("data-hide-at")
        if (timestamp && timestamp < now) {
            element.style.display = "none";
        }
    }
});
