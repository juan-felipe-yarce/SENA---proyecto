// Igual al del acudiente: toggle + activo por URL

// === FUNCIÓN PARA COLAPSAR O EXPANDIR EL SIDEBAR ===
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');    // Obtiene el aside por su ID
  const toggleIcon = document.getElementById('toggleIcon'); // Obtiene el ícono de toggle por su ID

  sidebar.classList.toggle('collapsed'); // Alterna la clase "collapsed" (añade o quita)

  // Cambia el ícono según el estado del sidebar
  if (sidebar.classList.contains('collapsed')) {
    toggleIcon.classList.remove('bi-chevron-left');  // Quita flecha izquierda
    toggleIcon.classList.add('bi-chevron-right');    // Pone flecha derecha
  } else {
    toggleIcon.classList.remove('bi-chevron-right'); // Quita flecha derecha
    toggleIcon.classList.add('bi-chevron-left');     // Pone flecha izquierda
  }
}

// === EJECUTA CUANDO EL DOM ESTÁ LISTO ===
document.addEventListener("DOMContentLoaded", function () {
  const menuLinks = document.querySelectorAll('.menu-link'); // Selecciona todos los enlaces del menú lateral

  // Recorre cada enlace
  menuLinks.forEach(link => {
    // Marca como "activo" el enlace cuya URL coincida con la actual
    if (link.href === window.location.href) {
      link.classList.add('active');
    }

    // Animación al pasar el mouse: se mueve un poco a la derecha
    link.addEventListener('mouseenter', function () {
      this.style.transform = 'translateX(8px)';
    });

    // Vuelve a su posición cuando el mouse se va
    link.addEventListener('mouseleave', function () {
      this.style.transform = 'translateX(0)';
    });
  });
});
