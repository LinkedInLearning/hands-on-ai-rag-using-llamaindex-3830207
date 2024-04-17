QUESTION_GEN_PROMPT = """Your task is to write a question given a context. Your question must be in the form of an adult mentee seeking advice 
from a trusted mentor. Formulate your question in the same style as questions users could ask in a search engine. Your question must be 
answerable with a specific, concise piece of information from the context. 

The context is below:
----------------------
{context}
----------------------

Your question MUST be short, clear, and based on the essence of the context. DO NOT use any qualifiers, relative clauses, or introductory modifiers.  
Keep your question short and to the point. Ask your question using the first person perspective, in the form of a student seeking advice from a trusted mentor.
"""

ANSWER_GEN_PROMPT = """You're a trusted mentor to an adult mentee. Your mentee is seeking advice in the form of a question.

Below is your mentee's question:

----------------------
{question}
----------------------

You've previously done some thinking and writing on the exact question your mentee has asked. Your answer MUST be actionable
yet concise. It must be based on your thinking and writing, which is below:

----------------------
{context}
----------------------

DO NOT use any qualifiers, relative clauses, or introductory modifiers in your answer. Provide your answer question using the second person
perspective, speaking directly to your mentee, in the form of a trusted mentor providing actionable advice.
"""

GROUNDEDNESS_PROMPT = """You are given context and a question. Provide a 'total rating' from 1 to 5 indicating 
the extent to which the question can be answered clearly using the context. 1 = not answerable, 5 = clearly answerable

Format your response as:

Evaluation: (rationale)
Total rating: (a number in the range 1-5)

Content and question are below:
----------------------
Context: {context}
Question: {question}
----------------------
"""