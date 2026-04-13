
async function getUserData(){
    const response = await fetch('/api/todos');
    return response.json();
}

function loadTable(todos){
    const table = document.querySelector('#result');
    for(let user of todos){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const todos = await getUserData();
    loadTable(todos);
}

main();