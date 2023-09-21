function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var button = document.querySelector(".dark-mode-toggle");
  if (element.classList.contains("dark-mode")) {
    button.textContent = "Modo Claro";
  } else {
    button.textContent = "Modo Escuro";
  }
  }