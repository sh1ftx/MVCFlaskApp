document.getElementById("editForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userId = document.getElementById("id").value;

    // Dados organizados
    const data = {
        "nome": document.getElementById("nome").value,
        "email": document.getElementById("email").value,
        "telefone": document.getElementById("telefone").value,
        "cidade": document.getElementById("cidade").value,
        "data_nascimento": document.getElementById("data_nascimento").value,
    }

    // Envio dos dados para a route de edicao, passando o id por url
    const response = await fetch(`/edit_user/${userId}`, {
        method: "POST",
        headers: { "Content-Type": "Application/json" },
        body: JSON.stringify(data)
    });

    // Aguardando a resposta da route
    const result = await response.json();

    // Notifica se deu certo ou não
    if (response.ok) {
        alert(result.message);
        window.location.href = "/user_list";
    } else {
        alert(result.error || "Erro ao atualizar!");
    }
});