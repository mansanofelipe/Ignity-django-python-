//let botao = document.querySelector("#adicionar-link");
//botao.addEventListener("click", criaFormInput);

botaoApagar.addEventListener("click", function(event){ // chama a função de apagar, qdo clicado
			apagaFormInput(event);})


/*function criaFormInput(event){
		
		let topoLista=document.querySelector(".lista-links"); // pega o topo da lista, para posicionar o bloco
		
		let itemLista=document.createElement("li"); // cria uma li
		itemLista.classList.add("item-lista");  // cria a classe dentro da li, para css
		
		let formulario = document.createElement("form"); // cria formulario
		formulario.classList.add("form-signin");
		formulario.action=(""); //não está funcionando a chamada do python no JS {% url "registrar" %}
		formulario.method=("post");

		let campoUrl = document.createElement("input");
		campoUrl.id=("nomeUrl");
		campoUrl.name=("nomeUrl");
		campoUrl.type=("text");
		campoUrl.placeholder=("Título do site");
		campoUrl.classList.add("campoUrl","form-control");

		let linkUrl = document.createElement("input");
		linkUrl.id=("linkUrl");
		linkUrl.name=("linkUrl");
		linkUrl.type=("text");
		linkUrl.placeholder=("Http/Url do site");
		linkUrl.classList.add("linkUrl","form-control");

		let botaoAdicionar = document.createElement("button");
		botaoAdicionar.id=("botaoAdicionar");
		botaoAdicionar.textContent=("Salvar Link!");	
		botaoAdicionar.classList.add("botaoAdicionar","btn","btn-lg","btn-block");
		botaoAdicionar.type=("submit");
		
		let botaoApagar = document.createElement("button");
		botaoApagar.id=("botaoApagar");
		botaoApagar.textContent=("Apagar");	
		botaoApagar.classList.add("botaoApagar","btn","btn-lg","btn-block"); 

		formulario.appendChild(campoUrl); // coloca o campo de nome dentro do formulario
		formulario.appendChild(linkUrl); // coloca o campo de nome dentro do formulario
		formulario.appendChild(botaoAdicionar); // coloca o campo de nome dentro do formulario
		formulario.appendChild(botaoApagar); // coloca o botão de apagar dentro  do formulario
		itemLista.appendChild(formulario); // coloca o formulario dentro do item lista
		topoLista.appendChild(itemLista); // coloca o item lista dentro da ul 

		// comentei todo esse trecho da função, pois o formulário já aparecerá no HTML. Motivo disso é que
		// nao consigo chamar o python de dentro do JS (front nao enxerga o back), então farei a chamada
		// via HTML
		
		
		})

		
}*/ 

function apagaFormInput(event){
	event.preventDefault();
	event.target.parentNode.parentNode.parentNode.reset(); // apaga o node bisaavô no clique
}
