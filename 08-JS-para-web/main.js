function teclaSom(idDoElemento){
    document.querySelector(idDoElemento).play();    
}
const listaTeclas = document.querySelectorAll('.tecla');

let c = 0;
while(c < listaTeclas.length ){
    const teclas = listaTeclas[c]
    const instrumento = teclas.classList[1]
    const idElemento = `#som_${instrumento}`;

     teclas.onclick = function(){
        teclaSom(idElemento)
    } 
    c+=1
    teclas.onkeydown =  function(event){
        if(event.code == 'Space' || event.code == 'Enter'){
            teclas.classList.add('ativa');
        }
    }
    teclas.onkeyup  = function(){
        teclas.classList.remove('ativa');
    }
}








