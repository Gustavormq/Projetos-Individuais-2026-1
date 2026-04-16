def apply_guardrails(prob):
    if prob < 0.6:
        return "Baixa confiança - revisão manual recomendada"
    
    if prob > 0.9:
        return "Alta probabilidade de fraude - verificar imediatamente"
    
    return "Confiança moderada"