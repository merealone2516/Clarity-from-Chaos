from sentence_transformers import SentenceTransformer, util
import nltk


def compute_embeddings(text):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    return model.encode(text, convert_to_tensor=True)


def split_into_sentences(paragraph):
    nltk.download('punkt')
    return nltk.tokenize.sent_tokenize(paragraph)


def calculate_overall_similarity(paragraph1, paragraph2):

    sentences1 = split_into_sentences(paragraph1)
    sentences2 = split_into_sentences(paragraph2)

    embeddings1 = compute_embeddings(sentences1)
    embeddings2 = compute_embeddings(sentences2)

    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
    max_scores = cosine_scores.max(dim=1).values
    return max_scores.mean().item()

paragraph1 = '''     '''
paragraph2 = '''   '''

overall_similarity = calculate_overall_similarity(paragraph1, paragraph2)
print("Overall Similarity:", overall_similarity)
