import React, { useState } from 'react';

function TransactionForm() {
  const [categoria, setCategoria] = useState('');
  const [valor, setValor] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aqui você pode adicionar a lógica para enviar os dados ao backend
    alert(`Transação adicionada: ${categoria} - R$${valor}`);
  };

  return (
    <div id="transactions">
      <h2>Adicionar Nova Transação</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Categoria:
          <input 
            type="text" 
            value={categoria} 
            onChange={(e) => setCategoria(e.target.value)} 
          />
        </label>
        <label>
          Valor:
          <input 
            type="number" 
            value={valor} 
            onChange={(e) => setValor(e.target.value)} 
          />
        </label>
        <button type="submit">Adicionar</button>
      </form>
    </div>
  );
}

export default TransactionForm;
