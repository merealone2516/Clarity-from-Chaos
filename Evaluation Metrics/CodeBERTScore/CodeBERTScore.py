from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

def calculate_codebertscore(paragraph1, paragraph2, model_name='microsoft/codebert-base'):
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Tokenize and encode the paragraphs
    inputs = tokenizer(paragraph1, paragraph2, return_tensors='pt', truncation=True, padding=True)

    # Get the model's output
    with torch.no_grad():
        outputs = model(**inputs)

    # Apply softmax to logits to get probabilities
    probabilities = F.softmax(outputs.logits, dim=1)

    # Assuming the first class (index 0) represents similarity
    similarity_score = probabilities[:, 0]

    return similarity_score.item()  # Convert to a single Python number

# Example paragraphs
paragraph1 = '''  Original Text  '''
paragraph2 = ''' Generated Text'''


# Calculate similarity
similarity_score = calculate_codebertscore(paragraph1, paragraph2)
print(similarity_score)
