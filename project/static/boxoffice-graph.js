function runGraph(results, titles){
    console.log(results);
    console.log(titles);
    let resultsArray = results.replace('[','').replace(']','').split(",");
    let titleArray = titles.replace('[','').replace(']','').replace(/\'/g, "").split(",");
    console.log(resultsArray);
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: titleArray,
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