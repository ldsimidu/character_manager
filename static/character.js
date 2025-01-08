document.addEventListener("DOMContentLoaded", function() {
    // Pegando todas as divs de skill
    const skillElements = document.querySelectorAll('.attribute-value');

    skillElements.forEach(function(skillElement) {
        const skillValue = parseInt(skillElement.innerText, 10);

        // Verificando o valor da habilidade e aplicando a classe correspondente
        if (skillValue >= 1) {
            skillElement.closest('.attribute-card').classList.add('green');
        } else if (skillValue < 0) {
            skillElement.closest('.attribute-card').classList.add('red');
        }
    });
});
