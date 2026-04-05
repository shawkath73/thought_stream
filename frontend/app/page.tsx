'use client';
import { useState, useEffect } from 'react';

interface Thought {
  _id: string;
  text: string;
  timestamp: string;
  likes?: number; // Added likes to the interface
}

export default function Home() {
  const [thoughts, setThoughts] = useState<Thought[]>([]);
  const [newThought, setNewThought] = useState('');

  const fetchThoughts = async () => {
    const res = await fetch('https://thought-stream-backend.onrender.com/api/thoughts');
    const data = await res.json();
    setThoughts(data);
  };

  useEffect(() => { fetchThoughts(); }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newThought.trim()) return;
    await fetch('http://127.0.0.1:5000/api/thoughts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: newThought }),
    });
    setNewThought('');
    fetchThoughts();
  };

  // --- NEW ACTIONS ---
  const deleteThought = async (id: string) => {
    await fetch(`http://127.0.0.1:5000/api/thoughts/${id}`, { method: 'DELETE' });
    fetchThoughts();
  };

  const likeThought = async (id: string) => {
    await fetch(`http://127.0.0.1:5000/api/thoughts/${id}/like`, { method: 'PATCH' });
    fetchThoughts();
  };

  return (
    <main className="min-h-screen bg-gray-50 py-10 px-4 flex flex-col items-center">
      <h1 className="text-4xl font-extrabold text-indigo-600 mb-8">Stream of Thoughts</h1>

      <form onSubmit={handleSubmit} className="w-full max-w-md mb-10 flex gap-2">
        <input 
          className="flex-1 p-3 rounded-lg border-2 border-indigo-100 focus:border-indigo-500 outline-none text-black"
          value={newThought}
          onChange={(e) => setNewThought(e.target.value)}
          placeholder="What are you thinking?"
        />
        <button className="bg-indigo-600 text-white px-6 py-3 rounded-lg font-bold hover:bg-indigo-700">Post</button>
      </form>

      <div className="w-full max-w-md space-y-4">
        {thoughts.map((t) => (
          <div key={t._id} className="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 group relative">
            <p className="text-gray-800 text-lg mb-4">{t.text}</p>
            
            <div className="flex justify-between items-center text-sm">
              <button 
                onClick={() => likeThought(t._id)}
                className="text-gray-500 hover:text-pink-500 flex items-center gap-1 transition"
              >
                ❤️ {t.likes || 0}
              </button>
              
              <button 
                onClick={() => deleteThought(t._id)}
                className="text-gray-300 hover:text-red-500 transition"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}