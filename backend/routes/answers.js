const express = require('express');
const router = express.Router();
const Answer = require('../models/Answer');
const fetch = require('node-fetch'); // Install with `npm install node-fetch`

// Save an answer and score it
router.post('/', async (req, res) => {
    const { questionId, answer } = req.body;

    try {
        // Call the scoring API
        const response = await fetch('http://127.0.0.1:8000/score_answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answer }),
        });

        const { score } = await response.json();

        // Save the answer with the generated score
        const newAnswer = new Answer({ questionId, answer, score });
        await newAnswer.save();

        res.status(201).json({ message: 'Answer saved successfully', score });
    } catch (error) {
        res.status(500).json({ message: 'Error saving answer', error });
    }
});

module.exports = router;
