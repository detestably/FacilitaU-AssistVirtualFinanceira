import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [saldo, setSaldo] = useState(0);
  const [despesas, setDespesas] = useState([]);
  
  useEffect(() => {
    // Aqui você pode adicionar a lógica para buscar dados do backend, como saldo e despesas
    setSaldo(5000); // Exemplo
    setDespesas([
      { categoria: 'Alimentação', valor: 150 },
      { categoria: 'Transporte', valor: 50 },
    ]);
  }, []);

  return (
    <div id="dashboard">
      <h2>Saldo Atual: R${saldo}</h2>
      <h3>Despesas Recentes</h3>
      <ul>
        {despesas.map((despesa, index) => (
          <li key={index}>{despesa.categoria}: R${despesa.valor}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
