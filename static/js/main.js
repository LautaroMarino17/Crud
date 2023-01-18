function quitar(){
    const elementoPadre = document.getElementById("div");
    const p = document.getElementById("p");
    elementoPadre.removeChild(p);
}
const btn = document.querySelectorAll(".delete");
if(btn){
   const btnArray = Array.from(btn);
   btnArray.forEach((btn)=>{
    btn.addEventListener('click', (e) =>{
        if(!confirm('Desea borrar el elemento? Se guardaran los cambios')) e.preventDefault();
    })
   })
}
