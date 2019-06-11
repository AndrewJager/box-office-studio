function runGraph(results){
    let resultsArray = results.replace('[','').replace(']','').split(",");
    console.log(resultsArray);
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: resultsArray,
            datasets: [{
                label: 'Daily gross',
                data: resultsArray,
                backgroundColor: '#082656',
                borderWidth: 4,
                fill: false,
            }],
            borderWidth: 1,
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            elements: {
                line: {
                    tension: 0,
                }
            }
        }
    });
}