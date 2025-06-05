import { useState, useEffect, useRef } from 'react';

export const useCreditUpdates = () => {
  const [creditData, setCreditData] = useState({ available: 0, used: 0, limit: 0 });
  const [history, setHistory] = useState([]);
  const [error, setError] = useState(null);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(`ws://${window.location.host}/ws/credit_updates`);

    ws.current.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setCreditData(data);
        setHistory(prev => [...prev.slice(-49), { time: new Date(), ...data }]);
      } catch (err) {
        setError('Failed to parse credit update');
      }
    };

    ws.current.onerror = () => setError('WebSocket error');

    return () => {
      if (ws.current) ws.current.close();
    };
  }, []);

  return { creditData, history, error };
};
