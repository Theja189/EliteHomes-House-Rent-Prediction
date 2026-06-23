const ctx = document.getElementById("predictionChart");

if (ctx) {

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: [
                "Hyderabad",
                "Bangalore",
                "Mumbai",
                "Pune",
                "Chennai"
            ],

            datasets: [{

                label: "Predictions",

                data: [
                    15,
                    12,
                    8,
                    10,
                    6
                ],

                backgroundColor: [
                    "#6C63FF",
                    "#8B5CF6",
                    "#A855F7",
                    "#7C3AED",
                    "#9333EA"
                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {
                    display: false
                }

            }

        }

    });

}