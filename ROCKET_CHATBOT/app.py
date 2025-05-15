from flask import Flask, render_template, request, jsonify
from narrative_rag import generate_answer
from intent_handlers import handle_intent
from nlp_parser import classify_intent

# Set template and static folders explicitly
app = Flask(__name__, template_folder="templates", static_folder="static")

# ROUTE: Serve the chat UI
@app.route("/")
def index():
    return render_template("chat.html")

# ROUTE: Chat endpoint
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"answer": "Please enter a valid question."})

        print(f"🛰️  Received question: {question}")

        # NLP classification
        intent = classify_intent(question)
        print(f"🧠 Detected intent: {intent}")

        # If intent matches SQL logic
        if intent:
            answer = handle_intent(intent, question)
        else:
            # Fallback to RAG answer
            answer = generate_answer(question)

        return jsonify({"answer": answer})

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"answer": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
