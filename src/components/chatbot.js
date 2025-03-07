import React, { useState } from 'react';

function Chatbot() {
  const [mensagem, setMensagem] = useState('');
  const [resposta, setResposta] = useState('');

  const handleSendMessage = async () => {
    // Lógica para enviar a mensagem ao backend (onde a IA responderá)
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: mensagem }),
    });
    const data = await res.json();
    setResposta(data.response);
  };

  return (
    <div id="chatbot">
      <h2>Assistente Virtual</h2>
      <div>
        <textarea 
          value={mensagem} 
          onChange={(e) => setMensagem(e.target.value)} 
          placeholder="Digite sua mensagem..." 
        />
        <button onClick={handleSendMessage}>Enviar</button>
      </div>
      <div>
        {resposta && <p><strong>Resposta:</strong> {resposta}</p>}
      </div>
    </div>
  );
}

export default Chatbot;
