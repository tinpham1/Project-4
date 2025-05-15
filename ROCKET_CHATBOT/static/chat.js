// Purpose: Sends user question to Flask backend and displays answer

function askQuestion() {
    const question = document.getElementById("question").value.trim();
    const responseEl = document.getElementById("response");

    if (!question) {
        responseEl.innerText = "Please enter a question.";
        return;
    }

    responseEl.innerText = "🤖 Thinking...";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    })
    .then(res => res.json())
    .then(data => {
        responseEl.innerText = data.answer || "No answer received.";
    })
    .catch(err => {
        console.error("Error:", err);
        responseEl.innerText = "⚠️ Error fetching response. Please try again.";
    });
}

// Optional: Trigger askQuestion on Enter key
document.getElementById("question").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        askQuestion();
    }
});
