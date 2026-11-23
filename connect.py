from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

def create_llm():
    llm=ChatGroq(
        model="openai/gpt-oss-120b"
    )
    return llm

def format_docs(docs):
    context="\n\n".join(
        doc.page_content for doc in docs
    )

    return context
def question_answer(question,retreiver,llm):
    retrieved_docs=retreiver.invoke(question)
    context=format_docs(retrieved_docs)

    prompt = PromptTemplate(
        template="""
You are an expert AI/ML interview preparation assistant.

Answer the user's question using the provided context.

If the answer is not available in the context,
clearly mention that the provided documents do not
contain enough information.

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )
    final_prompt = prompt.format(
        context=context,
        question=question
    )
    response = llm.invoke(final_prompt)
    return {
        "answer": response.content,
        "source_documents": retrieved_docs
    }

