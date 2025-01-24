const mongoose = require('mongoose');

const answerSchema = new mongoose.Schema({
    questionId: { type: Number, required: true },
    answer: { type: String, required: true },
    score: { type: Number, required: false }, // New field for storing the score
});

module.exports = mongoose.model('Answer', answerSchema);
