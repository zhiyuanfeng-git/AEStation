
function Highlight(query_content){
    window.addEventListener('DOMContentLoaded', (event) => {
        const activeLink = document.querySelector(query_content);
        if (activeLink) {
            activeLink.style.fontWeight = 'bold';
        }
    });
}

Highlight(highlight_query)