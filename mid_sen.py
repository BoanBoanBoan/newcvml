import os
import pypdf
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


# Example usage
root_directories = {
    'Senior Specialist': "generator_pos/middle_specialist_pdfs",
    'Middle Specialist': "generator_pos/middle_specialist_pdfs",
}

resume_data_common = []
for role, directory in root_directories.items():
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(resume_path)
            resume_data_common.append((text, role))

# Train Doc2Vec model using resume_data_common
tagged_data = [TaggedDocument(words=text.split(), tags=[role]) for text, role in resume_data_common]
model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=20)
model.build_vocab(tagged_data)
model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

# Example usage for predicting category
new_cv_path = "Profile.pdf"
new_cv_text = extract_text_from_pdf(new_cv_path)

# Remove newline characters and extra spaces
new_cv_text = ' '.join(new_cv_text.split())

# Check if the word "senior" is present in the new CV
if "senior" in new_cv_text.lower():
    most_similar_tag = 'Senior Specialist'
    confidence_percentage = 100.0
else:
    # Infer vector for the new CV
    new_vector = model.infer_vector(new_cv_text.split())

    # Find the most similar documents and their cosine similarity scores
    similar_documents = model.dv.most_similar([new_vector], topn=len(model.dv))
    similarity_scores = {tag: score for tag, score in similar_documents}

    # Get the predicted category with the highest similarity score
    most_similar_tag = max(similarity_scores, key=similarity_scores.get)
    confidence_percentage = similarity_scores[most_similar_tag] * 100

print(f"The predicted category for the new CV is: {most_similar_tag} with confidence: {confidence_percentage:.2f}%")
