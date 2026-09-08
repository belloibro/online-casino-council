from flask import Flask, render_template_string, request
import ollama

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Online Casino Council</title>
    <style>
        body { font-family: monospace; background: #121212; color: #00ff66; padding: 20px; max-width: 800px; margin: auto; }
        textarea { width: 100%; height: 100px; background: #1e1e1e; color: #fff; border: 1px solid #333; padding: 10px; font-size: 16px; }
        button { background: #00ff66; color: #121212; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        pre { background: #1e1e1e; padding: 15px; border: 1px solid #333; white-space: pre-wrap; word-wrap: break-word; color: #fff; }
    </style>
</head>
<body>
    <h1>Online Casino Council</h1>
    <form method="POST">
        <textarea name="topic" placeholder="Enter casino business decision to stress-test...">{{ topic }}</textarea><br>
        <button type="submit">Conven Council</button>
    </form>
    {% if verdict %}
        <h3>Council Verdict:</h3>
        <pre>{{ verdict }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    verdict = ""
    topic = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        try:
            with open("references/personas.md", "r") as f:
                persona_cards = f.read()
        except FileNotFoundError:
            persona_cards = "Standard iGaming Operator Personas"

        system_prompt = f"""
        You are managing the Online Casino Council.
        A decision goes in: {topic}
        A panel of opinionated casino operators each attacks it.
        Here are the persona cards and rules:
        {persona_cards}
        Reconcile the disagreement into one final recommendation with a bet/action attached.
        """

        response = ollama.chat(
            model='llama3',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f"Evaluate this decision/proposal: {topic}"}
            ]
        )
        verdict = response['message']['content']

    return render_template_string(HTML_TEMPLATE, verdict=verdict, topic=topic)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
