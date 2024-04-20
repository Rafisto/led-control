var color_checkbox = document.getElementById("color_toggle");
var color_picker = document.getElementById("color_picker");
var color_state = false;

document.getElementById("bgcolor").style.backgroundColor = color_picker.value;
document.getElementById("bgtext").innerHTML = color_picker.value;

const receiveInput = () => {
    document.getElementById("bgtext").innerHTML = color_picker.value;
    if (color_checkbox.checked) {
        document.getElementById("bgcolor").style.backgroundColor =
            color_picker.value;
        sendMessage(color_picker.value);
    }
};

const switchState = async () => {
    if (color_checkbox.checked) {
        color_state = true;
        document.getElementById("bgcolor").style.backgroundColor =
            color_picker.value;
        document.getElementById("bgtext").innerHTML = color_picker.value;
        sendMessage("on");
        await new Promise((r) => setTimeout(() => r(), 2000));
        sendMessage(color_picker.value);
    } else {
        color_state = false;
        document.getElementById("bgcolor").style.backgroundColor = "#242424";
        document.getElementById("bgtext").innerHTML = "OFF";
        sendMessage("off");
        await new Promise((r) => setTimeout(() => r(), 2000));
    }
};

color_picker.addEventListener("input", () => receiveInput());
color_checkbox.addEventListener("change", () => switchState());

const sendMessage = (() => {
    let lastExecutionTime = 0;
    const delay = 500;

    return (text) => {
        const currentTime = Date.now();
        if (currentTime - lastExecutionTime >= delay) {
            fetch("/control", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query: text }),
            });
            lastExecutionTime = currentTime;
        }
    };
})();
