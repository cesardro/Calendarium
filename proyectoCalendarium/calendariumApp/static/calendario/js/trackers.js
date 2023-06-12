document.addEventListener('DOMContentLoaded', function() {
  // Obtener la altura de la barra de navegación
  var navbar = document.querySelector('.navbar');
  var navbarHeight = navbar.offsetHeight;

  // Calcular el valor del margen superior
  var marginTopValue = navbarHeight + 20;

  // Aplicar el margen superior al contenedor debajo de la barra de navegación
  var container = document.querySelector('.container');
  container.style.marginTop = marginTopValue + 'px';
});