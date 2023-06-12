onload = principal;

const mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Dicimebre']
const diaSemanaEntero = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
const diaSemanaCorto = ['D','L','M','X','J','V','S']
function principal() {
    const fecha = new Date();
    const mesActual = mes[fecha.getMonth()];
    const anioActual = fecha.getFullYear();
    document.getElementById('mes').innerHTML = mesActual + " " + anioActual;
    diaTabs(fecha, fecha.getDate())
    diaCard(fecha, fecha.getDate())
}

function diaTabs(fecha, diaAct){
    document.getElementById('diaT1').innerHTML = diaSemanaCorto[fecha.getDay()%7]+" "+diaAct +"/"+(fecha.getMonth()+1);
    document.getElementById('diaT2').innerHTML = diaSemanaCorto[(fecha.getDay()+1)%7] +" "+(diaAct +1)+"/"+(fecha.getMonth()+1);
    document.getElementById('diaT3').innerHTML = diaSemanaCorto[(fecha.getDay()+2)%7] +" "+(diaAct +2)+"/"+(fecha.getMonth()+1);
    document.getElementById('diaT4').innerHTML = diaSemanaCorto[(fecha.getDay()+3)%7] +" "+(diaAct +3)+"/"+(fecha.getMonth()+1);
    document.getElementById('diaT5').innerHTML = diaSemanaCorto[(fecha.getDay()+4)%7] +" "+(diaAct +4)+"/"+(fecha.getMonth()+1);
    document.getElementById('diaT6').innerHTML = diaSemanaCorto[(fecha.getDay()+5)%7] +" "+(diaAct +5)+"/"+(fecha.getMonth()+1);
    document.getElementById('diaT7').innerHTML = diaSemanaCorto[(fecha.getDay()+6)%7] +" "+(diaAct +6)+"/"+(fecha.getMonth()+1);
}

function diaCard(fecha, diaAct) {
    document.getElementById('dia1').innerHTML = diaSemanaEntero[fecha.getDay()]+" "+diaAct +" de "+ mes[fecha.getMonth()];
    document.getElementById('dia2').innerHTML = diaSemanaEntero[(fecha.getDay()+1)%7] +" "+(diaAct +1)+" de "+mes[fecha.getMonth()];
    document.getElementById('dia3').innerHTML = diaSemanaEntero[(fecha.getDay()+2)%7] +" "+(diaAct +2)+" de "+mes[fecha.getMonth()];
    document.getElementById('dia4').innerHTML = diaSemanaEntero[(fecha.getDay()+3)%7] +" "+(diaAct +3)+" de "+mes[fecha.getMonth()];
    document.getElementById('dia5').innerHTML = diaSemanaEntero[(fecha.getDay()+4)%7] +" "+(diaAct +4)+" de "+mes[fecha.getMonth()];
    document.getElementById('dia6').innerHTML = diaSemanaEntero[(fecha.getDay()+5)%7] +" "+(diaAct +5)+" de "+mes[fecha.getMonth()];
    document.getElementById('dia7').innerHTML = diaSemanaEntero[(fecha.getDay()+6)%7] +" "+(diaAct +6)+" de "+mes[fecha.getMonth()];
}
function showCard(cardId) {
    var card = document.getElementById(cardId);
    card.style.display = "block";
    document.getElementById("overlay").classList.add("show");
  }
  
  function hideCard(cardId) {
    var card = document.getElementById(cardId);
    card.style.display = "none";
    document.getElementById("overlay").classList.remove("show");
  }

  