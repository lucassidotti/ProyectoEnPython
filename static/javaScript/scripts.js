const overlay=document.getElementById("overlay");
const form=document.getElementById("form");
const msjNombre=document.getElementById('msjNombre');
const msjTel=document.getElementById('msjTel');
const msjMail=document.getElementById('msjMail');
const msjFechaNac=document.getElementById('msjFechaNac');

form.addEventListener("submit",function(e){
    e.preventDefault();

    msjNombre.innerText='';
    msjTel.innerText='';
    msjMail.innerText='';
    msjFechaNac.innerText='';

    const formName=document.getElementById("formName").value.trim();
    const formMail=document.getElementById("formMail").value.trim();
    const formTel=document.getElementById("formTel").value.trim();
    const formEdad=document.getElementById("formEdad").value;
    let formError=false;

    if(formName===''){
        msjNombre.innerText='Ingrese su nombre'
        msjNombre.style.color='red'
        formError=true
    };

    const mailRegex=/^[^\s@]+@[^\s@]+.[^\s@]+$/;
    if(formMail===''){
        msjMail.innerText='Ingrese su correo'
        msjMail.style.color='red'
        formError=true
    }else if(!mailRegex.test(formMail)){
        msjMail.innerText='Su mail es invalido.'
        msjMail.style.color='red'
        formError=true
    };

    if(!/^\d{7,15}$/.test(formTel)){
        msjTel.innerText='Ingrese su telefono'
        msjTel.style.color='red'
        formError=true
    };

    if(formEdad===''){
        msjFechaNac.innerText='Seleccione su fecha de nacimiento';
        msjFechaNac.style.color='red';
        formError=true;
    }else{
        const fechaIngr=new Date(formEdad);
        const fechaHoy=new Date();
        let edad=fechaHoy.getFullYear() - fechaIngr.getFullYear();
        const mes=fechaHoy.getMonth() - fechaIngr.getMonth();
        const dia=fechaHoy.getDate() - fechaIngr.getDate();
        if (mes < 0 || (mes === 0 && dia < 0)){
             edad--; 
            };
        
        if (edad < 18) {
            msjFechaNac.innerText = 'Debe ser mayor de 18 años para registrarse';
            msjFechaNac.style.color = 'red';
            formError= true;
        };
    };
    if(!formError){
        overlay.style.display="none";
        form.submit();
    }
});

const btnMenor=document.getElementById("btnMenor");
btnMenor.addEventListener('click',()=>{
    window.location.href="https://www.youtube.com/@BlueyEspanol";
})

