import mlflow
from transformers import pipeline

mlflow.set_experiment("fraud_detection")

# modelo pré-treinado
classifier = pipeline("zero-shot-classification")

labels = ["fraude", "normal"]

texts = [
    "Transação de alto valor em país estrangeiro",
    "Compra comum em horário comercial",
    "Valor muito alto fora do padrão",
    "Compra pequena recorrente"
]

true_labels = ["fraude", "normal", "fraude", "normal"]

with mlflow.start_run():
    preds = []

    for text in texts:
        result = classifier(text, candidate_labels=labels)
        preds.append(result["labels"][0])

    # avaliação simples
    accuracy = sum([p == t for p, t in zip(preds, true_labels)]) / len(true_labels)

    mlflow.log_param("model", "facebook/bart-large-mnli")
    mlflow.log_metric("accuracy", accuracy)

    # salva modelo como artefato (pipeline)
    mlflow.log_text("Modelo zero-shot Hugging Face usado", "model_info.txt")

    print("Execução com modelo pré-treinado concluída!")