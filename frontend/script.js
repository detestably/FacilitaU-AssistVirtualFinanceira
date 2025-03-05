function handleKeyPress(event) {
    if (event.key === 'Enter') {
        const userInput = document.getElementById('user-input');
        const chatBox = document.getElementById('chat-box');

        const userMessage = userInput.value;
        chatBox.innerHTML += `<div><strong>Você:</strong> ${userMessage}</div>`;
        userInput.value = '';

        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage, user_id: 1 }), // user_id deve ser dinâmico
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<div><strong>Assistente:</strong> ${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }
}