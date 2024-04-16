QUESTION_GEN_QUERY = """Your task is to write a factoid question given a context.

The questions you generate should be answerable with a specific, concise piece of factual information from the context.  Restrict the questions to the context information provided and ask the questions from the first-person perspective. 

There is no need to address the thinker directly, they know you're speaking to them specifically. Ask the question directly and as succinctly as possible. Your question MUST NOT mention something like "according to the passage" or "context".

"""

TEXT_QUESTION_STR = """ Your task is to write a factoid question given a context.

Context information is below.

---------------------
{context_str}
---------------------

You're seeking wisdom and advice. Given the context information, generate questions that seek actionable advice or practical tips that you can apply in your own life. 

The questions you generate should be answerable with a specific, concise piece of factual information from the context.  Restrict the questions to the context information provided and ask the questions from the first-person perspective. 

There is no need to address the thinker directly, they know you're speaking to them specifically. Ask the question directly and as succinctly as possible. Your question MUST NOT mention something like "according to the passage" or "context".
"""

TEXT_QA_STRING = """Context information is below.

---------------------
{context_str}
---------------------

You are the author of the context. Given the context information provide advice that answers the query. Use only the given context to provide advice. 

When providing advice, speak directly to the asker and use the "you" voice (second-person perspective). There is no need to identify yourself in your response, the asker knows who you are. 

Query: {query_str}
Answer:
"""