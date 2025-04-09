document.getElementById("cadastroForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = {
        "nome": document.getElementById("nome").value,
        "email": document.getElementById("email").value,
        "telefone": document.getElementById("telefone").value,
        "cidade": document.getElementById("cidade").value,
        "data_nascimento": document.getElementById("data_nascimento").value
    };

    const response = await fetch("/user_register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    const result = await response.json();

    if (response.ok) {
        alert(result.message);
        window.location.href = "/user_list";
    } else {
        alert(result.error || "Erro ao cadastrar!");
    }
});