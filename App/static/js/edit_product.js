document.getElementById("editForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userId = document.getElementById("id").value;

    // Dados organizados
    const data = {
        "nome": document.getElementById("nome").value,
        "marca": document.getElementById("marca").value,
        "preco": document.getElementById("preco").value,
        "estoque": document.getElementById("estoque").value,
    }

    // Envio dos dados para a route de edicao, passando o id por url
    const response = await fetch(`/edit_product/${userId}`, {
        method: "PUT",
        headers: { "Content-Type": "Application/json" },
        body: JSON.stringify(data)
    });

    // Aguardando a resposta da route
    const result = await response.json();

    // Notifica se deu certo ou não
    if (response.ok) {
        alert(result.message);
        window.location.href = "/product_list";
    } else {
        alert(result.error || "Erro ao atualizar!");
    }
});