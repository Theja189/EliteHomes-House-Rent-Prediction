// =========================
// BACK TO TOP BUTTON
// =========================

window.addEventListener("scroll", function () {

    const button = document.getElementById("backToTop");

    if (!button) return;

    if (window.scrollY > 300) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
});

function scrollToTop() {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// =========================
// ACTIVE NAVBAR LINK
// =========================

document.addEventListener("DOMContentLoaded", function () {

    const currentPage = window.location.pathname;

    document.querySelectorAll(".nav-link").forEach(link => {

        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }

    });

});