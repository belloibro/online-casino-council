import os
import ollama

def load_persona(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

persona_cards = load_persona("references/personas.md")

def consult_council(decision_topic):
    system_prompt = f"""
    You are managing the Online Casino Council. 
    A decision goes in: {decision_topic}
    A panel of opinionated casino operators each attacks it. 
    Here are the persona cards and rules:
    {persona_cards}
    
    Reconcile the disagreement into one final recommendation with a bet/action attached.
    """
    
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system', 
            'content': system_prompt
        },
        {
            'role': 'user', 
            'content': f"Evaluate this decision/proposal: {decision_topic}"
        },
    ])
    
    return response['message']['content']

if __name__ == "__main__":
    topic = input("Enter the casino business decision to stress-test: ")
    print("\n[Council Convening...]\n")
    verdict = consult_council(topic)
    print(verdict)
