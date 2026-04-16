from transformers import pipeline
from guardrails import apply_guardrails

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

labels = ["fraude", "normal"]

def predict(text):
    result = classifier(text, candidate_labels=labels)

    prob = result["scores"][0]
    label = result["labels"][0]

    guard = apply_guardrails(prob)

    return {
        "texto": text,
        "classe": label,
        "confianca": prob,
        "guardrail": guard
    }

# teste
print(predict("Transação muito alta em outro país"))