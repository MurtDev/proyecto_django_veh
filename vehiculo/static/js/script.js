// Esperar que el documento esté listo
document.addEventListener("DOMContentLoaded", function() {
  // Seleccionar todos los mensajes
  const messages = document.querySelectorAll('.message');

  // Definir el tiempo de visualización del mensaje (por ejemplo, 3000 ms)
  const messageDisplayTime = 2000;

  // Iterar sobre cada mensaje
  messages.forEach(function(message) {
    // Desvanecer el mensaje después de un cierto tiempo
    setTimeout(function() {
      message.classList.add('fade-out'); // Agregar clase de desvanecimiento
      setTimeout(() => {
        message.style.display = 'none'; // Ocultar el mensaje después del desvanecimiento
      }, 1000); // Tiempo de desvanecimiento (1 segundo)
    }, messageDisplayTime);
  });
});