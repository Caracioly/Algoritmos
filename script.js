function darkMode() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var image = document.getElementById("image-btn");

  if (element.classList.contains("dark-mode")) {
    image.src = "to-light.png";
  } else {
    image.src = "to-dark.png";
  }
  }