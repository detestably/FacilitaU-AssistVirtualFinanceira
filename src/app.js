import React from 'react';
import './App.css';
import Header from './components/header';
import Dashboard from './components/dashboard';
import TransactionForm from './components/TransactionForm';
import Chatbot from './components/Chatbot';

function App() {
  return (
    <div className="App">
      <Header />
      <Dashboard />
      <TransactionForm />
      <Chatbot />
    </div>
  );
}

export default App;
