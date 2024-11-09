// Função para fazer a requisição à API
async function fetchSpeciesNames() {
    try {
        const response = await fetch('/species-names');
        if (!response.ok) {
            throw new Error('Erro na rede');
        }

        const speciesNames = await response.json();
        const listElement = document.getElementById('species-list');
        
        speciesNames.forEach(name => {
            const listItem = document.createElement('li');
            listItem.textContent = name;
            listElement.appendChild(listItem);
        });
    } catch (error) {
        console.error('Erro:', error);
        const listElement = document.getElementById('species-list');
        listElement.innerHTML = 'Erro ao buscar dados';
    }
}

window.onload = fetchSpeciesNames;