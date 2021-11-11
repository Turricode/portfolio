fetch('/api/graph_data').then(response => {
    if(response.status !== 200){
        console.log('Error connecting to graph api');
        return;
    }

    response.json().then(data => {
        const Graph = ForceGraph()
        (document.getElementById('graph'))
        .graphData(data)
        .nodeId('name')
    })


}).catch(err => {
    console.log(err)
})