document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('character-form');
    const characterList = document.getElementById('character-list');

    // Função para buscar personagens existentes e renderizá-los
    const fetchCharacters = () => {
        fetch('/characters')
            .then((response) => response.json())
            .then((characters) => {
                characterList.innerHTML = ''; // Limpa a lista de personagens

                characters.forEach((character) => {
                    const charDiv = document.createElement('div');
                    charDiv.className = 'character-card';
                    charDiv.style.overflow = 'hidden';  // Desabilita o overflow
                    charDiv.style.whiteSpace = 'nowrap';  // Impede quebra de linha
                    charDiv.style.cursor = 'pointer'; // Adiciona o cursor pointer para mostrar que é clicável

                    // Criação do link para a página de detalhes do personagem
                    const charLink = document.createElement('a');
                    charLink.href = `/character/${character.id}`;
                    charLink.style.textDecoration = 'none'; // Remove underline
                    charLink.style.color = 'inherit'; // Garante que o texto dentro do link tenha a mesma cor da div

                    // Adiciona conteúdo com nome, classe e nível dentro do link
                    charLink.innerHTML = `
                        <h3>${character.name}</h3>
                        <p>Classe: ${character.character_class}</p>
                        <p>Nível: ${character.level}</p>
                    `;
                    
                    // Adiciona o link à div do personagem
                    charDiv.appendChild(charLink);

                    // Adiciona a div à lista de personagens
                    characterList.appendChild(charDiv);
                });
            })
            .catch((error) => console.error('Erro ao buscar personagens:', error));
    };

    // Chamando a função para renderizar a lista de personagens
    fetchCharacters();

    // Função para enviar novo personagem
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Evita o comportamento padrão do envio do formulário

        const formData = new FormData(form);
        const newCharacter = Object.fromEntries(formData.entries());

        fetch('/create_character', {  // Altere aqui para o novo endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newCharacter),
        })
            .then((response) => {
                console.log(response); // Verifique a resposta do servidor
                return response.json(); // Tente converter para JSON
            })
            .then((data) => {
                console.log(data); // Se for um JSON válido
                form.reset();
                fetchCharacters(); // Atualiza a lista de personagens
            })
            .catch((error) => {
                console.error('Erro ao adicionar personagem:', error);
            });
    });
});

// Função para buscar personagens e renderizar em outra parte, se necessário
async function fetchCharacters() {
    const response = await fetch('/api/characters');
    const characters = await response.json();

    const characterList = document.getElementById('character-list');
    characterList.innerHTML = ''; // Limpa a lista

    characters.forEach(character => {
        const listItem = document.createElement('div');
        listItem.className = 'character-card';
        listItem.style.overflow = 'hidden';  // Desabilita o overflow
        listItem.style.whiteSpace = 'nowrap';  // Impede quebra de linha
        listItem.style.cursor = 'pointer'; // Adiciona o cursor pointer para mostrar que é clicável

        // Criação do link para a página de detalhes do personagem
        const charLink = document.createElement('a');
        charLink.href = `/character/${character.id}`;
        charLink.style.textDecoration = 'none'; // Remove underline
        charLink.style.color = 'inherit'; // Garante que o texto dentro do link tenha a mesma cor da div

        // Estrutura do conteúdo do personagem
        charLink.innerHTML = `
            <h3>${character.name}</h3>
            <p>Classe: ${character.character_class}</p>
            <p>Nível: ${character.level}</p>
        `;
        
        // Adiciona o link à div e a div à lista
        listItem.appendChild(charLink);
        characterList.appendChild(listItem);
    });
}
fetchCharacters();
