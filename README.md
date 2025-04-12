# Sentiment Analysis Chatbot

A simple chatbot that can understand basic user messages and respond based on sentiment (positive, negative, neutral).

## Project Structure
- `backend/`: Flask API with sentiment analysis model
- `frontend/`: React application for the chat interface

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the Flask server: `python app.py`

### Frontend Setup
1. Navigate to the frontend directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

## Features
- Real-time sentiment analysis of user messages
- Simple and intuitive chat interface
- Basic response generation based on sentiment