import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prediction, setPrediction] = useState(null);

  const handlePredict = async () => {
    const response = await axios.post('http://localhost:8000/api/predict/', {
      feeling: 75,
      study_hours: 7
    });
    setPrediction(response.data.prediction);
  };

  return (
    <div>
      <h1>Exam Score Predictor</h1>
      <button onClick={handlePredict}>Predict Score</button>
      {prediction && <p>Predicted Score: {prediction}</p>}
    </div>
  );
}

export default App;
