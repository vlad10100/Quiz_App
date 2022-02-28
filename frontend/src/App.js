import React from 'react'
import './App.css';


import QuizSelect from './components/QuizSelect'
import RandomQuiz from './components/RandomQuiz'
import {Route, Routes} from 'react-router-dom'
import { BrowserRouter as Router } from 'react-router-dom';



function App() {
    return(
        <Router>
            <Routes>
                <Route exact path="/" element={<QuizSelect/>} />
                <Route exact path="/r/:topic" element={<RandomQuiz/>} />
            </Routes>
        </Router>
    );
}

export default App;
