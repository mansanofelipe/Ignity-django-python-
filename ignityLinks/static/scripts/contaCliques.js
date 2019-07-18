
var botoes=document.querySelectorAll(".item-lista");

botoes.forEach(function(botao){

	botao.addEventListener("click", function(){
		clique=this.children[1].children[0].children[0]; // péssimo código: reescrever!
		clique.textContent++;
})
})	
