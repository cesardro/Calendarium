document.addEventListener('DOMContentLoaded', function () {
  // Obtener la altura de la barra de navegación
  var navbar = document.querySelector('.navbar');
  var navbarHeight = navbar.offsetHeight;

  // Calcular el valor del margen superior
  var marginTopValue = navbarHeight + 20;

  // Aplicar el margen superior al contenedor debajo de la barra de navegación
  var container = document.querySelector('.contenedor');
  container.style.marginTop = marginTopValue + 'px';
});

function toggleDarkMode() {
  // Verificar el estado actual del modo
  var isDarkMode = localStorage.getItem('darkMode') === 'true';

  // Cambiar el estado del modo
  isDarkMode = !isDarkMode;

  // Actualizar el localStorage con el nuevo estado del modo
  localStorage.setItem('darkMode', isDarkMode);

  // Aplicar el tema correspondiente
  applyTheme();
}

function applyTheme() {
  // Verificar el estado actual del modo
  var isDarkMode = localStorage.getItem('darkMode') === 'true';

  // Obtener el elemento body
  var body = document.querySelector('body');

  // Aplicar el tema correspondiente
  if (isDarkMode) {
    body.classList.add('dark-mode');
  } else {
    body.classList.remove('dark-mode');
  }
}

// Al cargar la página, aplicar el tema correspondiente
document.addEventListener('DOMContentLoaded', function () {
  applyTheme();
});

// Función para borrar las cookies del navegador
function deleteAllCookies() {
  var cookies = document.cookie.split(";");

  for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i];
    var eqPos = cookie.indexOf("=");
    var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
  }
}

// Evento click para el botón de Log Out
var logoutButton = document.getElementById("logoutButton");
logoutButton.addEventListener("click", function () {
  deleteAllCookies();
});