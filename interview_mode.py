
from langchain_core.prompts import PromptTemplate
def generate_question(topic,retriever,llm):
    retrieved_docs = retriever.invoke(
        f"Important interview concepts and questions about {topic}"
    )

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = PromptTemplate(
        template="""
You are an experienced AI/ML technical interviewer.

Generate ONE interview question about {topic}.

Use the following context to understand the topic:
{context}

Requirements:
- Ask only one question.
- Make it suitable for a technical interview.
- Do not provide the answer.

Interview Question:
""",
        input_variables=["topic", "context"]
    )
    final_prompt=prompt.format(
        topic=topic,
        context=context
    )
    response=llm.invoke(final_prompt)
    return response.content


def evaluate_answer(question, candidate_answer, retriever, llm):
    retrieved_docs = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )
    prompt = PromptTemplate(
        template="""
You are an experienced AI/ML technical interviewer.

Evaluate the candidate's answer based on the question
and the provided reference context.

Question:
{question}

Candidate's Answer:
{candidate_answer}

Reference Context:
{context}

Evaluate the answer based on:
1. Technical correctness
2. Conceptual understanding
3. Completeness

Provide your evaluation in this format:

Score: X/10

What was correct:
Explain the correct points.

What was missing:
Explain the missing or incorrect concepts.

Improvement:
Explain how the candidate can improve the answer.
""",
        input_variables=[
            "question",
            "candidate_answer",
            "context"
        ]
    )

    final_prompt = prompt.format(
        question=question,
        candidate_answer=candidate_answer,
        context=context
    )

    response = llm.invoke(final_prompt)
    return response.content

def generate_followup_question(
    question,
    candidate_answer,
    feedback,
    retriever,
    llm
):
    retrieved_docs = retriever.invoke(
        question + " " + candidate_answer
    )

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = PromptTemplate(
        template="""
You are an experienced AI/ML technical interviewer.

The candidate was asked:
{question}

Candidate's answer:
{candidate_answer}

Evaluation feedback:
{feedback}

Reference context:
{context}

Your task:
- Generate ONE relevant follow-up interview question.
- Focus on a concept the candidate missed or did not explain clearly.
- If the candidate answered everything correctly, ask a deeper conceptual question.
- Do not provide the answer.
- Ask only one question.

Follow-up Question:
""",
        input_variables=[
            "question",
            "candidate_answer",
            "feedback",
            "context"
        ]
    )
    final_prompt = prompt.format(
        question=question,
        candidate_answer=candidate_answer,
        feedback=feedback,
        context=context
    )
    response = llm.invoke(final_prompt)
    return response.content


