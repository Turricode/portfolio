
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
        .nodeCanvasObject((node, ctx, globalScale) => {
            const label = node.name;
            const fontSize = 12/globalScale;
            ctx.font = `${fontSize}px Sans-Serif`;
            const textWidth = ctx.measureText(label).width;
            const bckgDimensions = [textWidth, fontSize].map(n => n + fontSize * 0.2); // some padding
  
            ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
            ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);
  
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = node.color;
            ctx.fillText(label, node.x, node.y);
  
            node.__bckgDimensions = bckgDimensions; // to re-use in nodePointerAreaPaint
          })
          .nodePointerAreaPaint((node, color, ctx) => {
            ctx.fillStyle = color;
            const bckgDimensions = node.__bckgDimensions;
            bckgDimensions && ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);
          })
          .linkDirectionalParticles(1);
    });


}).catch(err => {
    console.log(err);
})