var color_checkbox = document.getElementById("color_toggle");
var color_picker = document.getElementById("color_picker");

document.getElementById("bgcolor").style.backgroundColor = color_picker.value;
document.getElementById("bgtext").innerHTML = color_picker.value;

color_picker.addEventListener("input", function() {
    document.getElementById("bgtext").innerHTML = color_picker.value;
    if (color_checkbox.checked) {
        document.getElementById("bgcolor").style.backgroundColor = color_picker.value;
        sendMessage(color_picker.value);
    }
})

color_checkbox.addEventListener("change", function() {
    if (color_checkbox.checked) {
        document.getElementById("bgcolor").style.backgroundColor = color_picker.value;
        document.getElementById("bgtext").innerHTML = color_picker.value;
        sendMessage(color_picker.value);
    } else {
        document.getElementById("bgcolor").style.backgroundColor = "#242424";
        document.getElementById("bgtext").innerHTML = "OFF";
    }
})

const sendMessage = (text) => {
    fetch("/control", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: text }),
    });
  }