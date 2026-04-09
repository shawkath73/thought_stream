# ThoughtStream 🚀
A minimalist Full-Stack "Stream of Consciousness" application built to demonstrate modern web architecture, cloud integration, and agentic system foundations.

## 🏗 Architecture
This project follows a decoupled client-server architecture:
- **Frontend**: Next.js (React) hosted on Vercel.
- **Backend**: Flask (Python) hosted on Render.
- **Database**: MongoDB Atlas (NoSQL) for real-time data persistence.



## 🛠 Tech Stack
- **Frameworks**: Next.js 14, Flask
- **Styling**: Tailwind CSS
- **Database**: MongoDB (PyMongo)
- **Deployment**: Render (API), Vercel (UI), GitHub Actions

## 🚀 Features
- **Real-time Thoughts**: Post and view thoughts instantly.
- **Engagement**: Integrated "Like" system using MongoDB `$inc` atomicity.
- **Data Management**: Full CRUD capabilities with a focus on optimized API routing.
- **Responsive UI**: Fully mobile-responsive design using Tailwind.

## 🔧 Local Setup

### Backend
1. Navigate to `/backend`
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Add your `.env` file with `MONGO_URI`.
5. Run: `python run.py`

### Frontend
1. Navigate to `/frontend`
2. Install packages: `npm install`
3. Run development server: `npm run dev`

## 🌐 Deployment
The production API is hosted at: `https://thought-stream-backend.onrender.com/api/thoughts`

---
*Developed as part of an Engineering Research workflow into Agentic Systems and Production ML.*