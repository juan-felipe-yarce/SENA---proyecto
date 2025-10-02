// Igual al del acudiente: toggle + activo por URL
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const toggleIcon = document.getElementById('toggleIcon');

  sidebar.classList.toggle('collapsed');

  if (sidebar.classList.contains('collapsed')) {
    toggleIcon.classList.remove('bi-chevron-left');
    toggleIcon.classList.add('bi-chevron-right');
  } else {
    toggleIcon.classList.remove('bi-chevron-right');
    toggleIcon.classList.add('bi-chevron-left');
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const menuLinks = document.querySelectorAll('.menu-link');

  menuLinks.forEach(link => {
    if (link.href === window.location.href) {
      link.classList.add('active');
    }
    link.addEventListener('mouseenter', function () {
      this.style.transform = 'translateX(8px)';
    });
    link.addEventListener('mouseleave', function () {
      this.style.transform = 'translateX(0)';
    });
  });
});
