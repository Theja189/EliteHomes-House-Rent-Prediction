// =========================
// RENT PREDICTION LOADER
// =========================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector(".predict-btn");

    if (!form || !button) return;

    form.addEventListener("submit", function () {

        button.disabled = true;

        button.innerHTML = `
            <span class="spinner-border spinner-border-sm"></span>
            Predicting...
        `;

    });

});