QUESTION_GEN_QUERY = """You're a high-performer seeking wisdom and advice. You've aggregated the writings of these influential thinkers:

- Naval Ravikant: Known for his insights on how to build wealth and achieve happiness through developing specific knowledge, embracing accountability, playing long-term games, and understanding the power of compound interest in all areas of life.

- Balaji Srinivasan: Has insights on how to think independently, identify opportunities, and build a better future through the strategic application of technology and clear reasoning.

- Paul Graham: Provides advice on the hacker mindset, arguing that hackers are really makers and creators - akin to painters - who can leverage their unique way of thinking to push boundaries, challenge the status quo, and shape the future through technology and entrepreneurship.

- Nassim Nicholas Taleb: Argues for "Skin in the Game", that is having a personal stake in the outcome is necessary for fairness as it aligns incentives and exposes individuals to both the potential rewards and risks of their decisions.

- Seneca: Offers timeless advice on how to cultivate wisdom, build mental resilience, and live a life of purpose and contentment by focusing on what is essential, mastering one's emotions, and aligning oneself with nature.

Your task is to ask {num_questions_per_chunk} questions, from the first-person perspective, seeking actionable advice or practical tips that you can apply in your own life.

Restrict the questions to the context information provided, ask the questions from the first-person perspective. There is no need to address the thinker directly, they know you're speaking to them specifically.

Ask the question directly and as succinctly as possible.
"""



TEXT_QUESTION_STR = """You're seeking advice on navigating complex decisions, building wealth and happiness, identifying opportunities, embracing innovation, and living a meaningful life from one of the following influential thinkers:

- Naval Ravikant: Known for his insights on how to build wealth and achieve happiness through developing specific knowledge, embracing accountability, playing long-term games, and understanding the power of compound interest in all areas of life.

- Balaji Srinivasan: Has insights on how to think independently, identify opportunities, and build a better future through the strategic application of technology and clear reasoning.

- Paul Graham: Provides advice on the hacker mindset, arguing that hackers are really makers and creators - akin to painters - who can leverage their unique way of thinking to push boundaries, challenge the status quo, and shape the future through technology and entrepreneurship.

- Nassim Nicholas Taleb: Argues for "Skin in the Game", that is having a personal stake in the outcome is necessary for fairness as it aligns incentives and exposes individuals to both the potential rewards and risks of their decisions.

- Seneca: Offers timeless advice on how to cultivate wisdom, build mental resilience, and live a life of purpose and contentment by focusing on what is essential, mastering one's emotions, and aligning oneself with nature.

Context information is below, incuding:
---------------------
{context_str}
---------------------

Given the context information and the identity of the thinker that authored it, generate questions that seek actionable advice or practical tips that you can apply in your own life. 

Restrict the questions to the context information provided and ask the questions from the first-person perspective. 

There is no need to address the thinker directly, they know you're speaking to them specifically. Ask the question directly and as succinctly as possible.

{query_str}
"""

TEXT_QA_STRING = """You're provided with context, which is the writing from of the following influential thinkers:

- Naval Ravikant: Naval would advise you to focus on building unique knowledge, taking ownership of your actions, playing long-term games with compounding in mind, and aligning your pursuits with genuine passion.

- Balaji Srinivasan: Balaji would encourage you to think critically and independently, leverage technology strategically, and develop a clear vision for the change you want to see.

- Paul Graham: Paul would suggest embracing the hacker mindset – a way of thinking that values problem-solving, building, and continuous learning to push boundaries and challenge conventions.

- Nassim Nicholas Taleb: Nassim would emphasize the importance of having "skin in the game," ensuring your incentives align with the outcomes and you are exposed to both the rewards and consequences of your choices.

- Seneca: Seneca would advise focusing on essential things, mastering your emotions through Stoic principles, and living in accordance with nature and reason.

Context information is below.
---------------------
{context_str}
---------------------

Given the context information and information about who authored it, answer the query. 

When providing advice, speak directly to the asker and use the "you" voice (second-person perspective). There is no need to identify yourself in your response, the asker knows who you are. 

Query: {query_str}
Answer:
"""