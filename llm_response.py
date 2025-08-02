from transformers import pipeline

# Load the question-answering pipeline just once
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def generate_answer(context, question):
    """
    Generate an answer from the given context and question using the QA pipeline.

    Parameters:
    - context (str): Text extracted from the PDF
    - question (str): User's input question

    Returns:
    - str: Answer extracted from the context
    """
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
