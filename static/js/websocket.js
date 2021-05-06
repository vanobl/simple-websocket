window.onload = function() {
    // создадим подключение
    let socket = new WebSocket("ws://localhost:8080/ws");

    // отправим сообщение из формы
    document.forms.publish.onsubmit = function() {
        let outgoingMessage = this.message.value;

        socket.send(createJSON(outgoingMessage));
        return false;
    }

    // обработчик входящих сообщений
    socket.onmessage = function(event) {
        let incomingMessage = event.data;
        let json_message = JSON.parse(incomingMessage);
        showMessage(json_message["text"], json_message["last_number"]);
    }

    // метод показа сообщений
    function showMessage(message, number) {
        let p =document.createElement('p');
        p.innerHTML = "<strong>" + number + ". " + message + "</strong>";

        let target = document.querySelector('#forMessages');
        target.insertAdjacentElement('beforeend', p);
    }

    // метод формирования JSON
    function createJSON(message) {
        let json_object = JSON.stringify({"text": message})
        return json_object
    }
}