
const render_text = (node) => {
    fetch(`/api/node_data/${node['name']}`).then(resp => {
        resp.text().then(node_text => {
            var text_div = document.getElementById('text');
            var text_title = document.getElementById('text-title')
            console.log(node_text);
            text_div.innerHTML = node_text;
            text_title.innerHTML = node['title']
        })
    }) 
}

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
        .nodeAutoColorBy('type')
        
    });


}).catch(err => {
    console.log(err);
})