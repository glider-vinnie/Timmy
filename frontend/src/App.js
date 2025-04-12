import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message
    const userMessage = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    try {
      // Send message to backend
      const response = await axios.post('http://localhost:5000/analyze', {
        message: input
      });

      // Add bot response
      const botMessage = {
        text: response.data.response,
        sender: 'bot',
        sentiment: response.data.sentiment
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        text: 'Sorry, there was an error processing your message.',
        sender: 'bot',
        sentiment: 'neutral'
      };
      setMessages(prev => [...prev, errorMessage]);
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <div className="messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.sender}`}
              data-sentiment={message.sentiment}
            >
              {message.text}
            </div>
          ))}
        </div>
        <form onSubmit={handleSubmit} className="input-form">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
          />
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App; 