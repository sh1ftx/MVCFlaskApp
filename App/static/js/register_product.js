document.getElementById("cadastroForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        "nome": document.getElementById("nome").value,
        "marca": document.getElementById("marca").value,
        "preco": document.getElementById("preco").value,
        "estoque": document.getElementById("estoque").value,
    };

    const response = await fetch("/register_product", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
    } else {
        alert(result.error || "Erro ao cadastrar!");
    }
});