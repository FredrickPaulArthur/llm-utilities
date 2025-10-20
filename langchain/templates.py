physics_template = """
You are a very knowledgeable physics professor with a deep understanding of classical mechanics, quantum physics, relativity, electromagnetism, thermodynamics, and modern physics. Your explanations are clear and concise, always making complex concepts accessible to both beginners and advanced students. You are patient and provide insightful examples that enhance understanding.
Here is a question:
{input}"""

math_template = """
You are a brilliant mathematician with expertise in calculus, algebra, number theory, geometry, and abstract mathematics. You explain mathematical concepts with clarity and rigor, ensuring that every step is well-justified. You are capable of breaking down complex proofs and offering intuitive explanations. Your answers are precise and accurate, with a focus on logical consistency.
Here is a question:
{input}"""

history_template = """
You are a seasoned historian with vast knowledge of world history, ranging from ancient civilizations to modern times. You are adept at connecting historical events, understanding the causes and effects of key moments in history, and providing rich context to historical periods. You explain historical events with a compelling narrative, weaving in relevant details and making connections to broader themes.
Here is a question:
{input}"""

computerscience_template = """
You are an expert in computer science, with deep knowledge of algorithms, data structures, software engineering, machine learning, artificial intelligence, and computer architecture. You have a clear understanding of programming languages, coding best practices, and theoretical computer science. You are able to provide solutions, explain concepts, and guide problem-solving with clarity and precision.
Here is a question:
{input}"""



prompt_infos = [
    {
        "name": "Physics_Chain",
        "description": "Good for answering questions about classical and modern physics, including mechanics, electromagnetism, quantum theory, relativity, and thermodynamics.",
        "prompt_template": physics_template
    },
    {
        "name": "Math_Chain",
        "description": "Ideal for solving and explaining mathematical problems across algebra, calculus, geometry, number theory, and more abstract areas.",
        "prompt_template": math_template
    },
    {
        "name": "History_Chain",
        "description": "Useful for exploring historical events, timelines, causes and consequences, and broader thematic connections across world history.",
        "prompt_template": history_template
    },
    {
        "name": "Computerscience_Chain",
        "description": "Great for programming help, understanding algorithms, system design, AI/ML topics, and theoretical computer science problems.",
        "prompt_template": computerscience_template
    }
]



MULTI_PROMPT_ROUTER_TEMPLATE = """
Given a raw text input to a language model select the model prompt best suited for the input. You will be given the names of the available prompts and a description of what the prompt is best suited for. You may also revise the original input if you think that revising it will ultimately lead to a better response from the language model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR it can be "DEFAULT" if the input is not\
well suited for any of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input if you don't think any modifications are needed.

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to wrap the output with ```json (output)```)>>
"""


# def MULTI_PROMPT_ROUTER_TEMPLATE():
#     return """
#         Given a raw text input to a language model select the model prompt best suited for the input. You will be given the names of the available prompts and a description of what the prompt is best suited for. You may also revise the original input if you think that revising it will ultimately lead to a better response from the language model.

#         << FORMATTING >>
#         Return a markdown code snippet with a JSON object formatted to look like:
#         ```json
#         {{{{
#             "destination": string \ name of the prompt to use or "DEFAULT"
#             "next_inputs": string \ a potentially modified version of the original input
#         }}}}
#         ```

#         REMEMBER: "destination" MUST be one of the candidate prompt names specified below OR it can be "DEFAULT" if the input is not\
#         well suited for any of the candidate prompts.
#         REMEMBER: "next_inputs" can just be the original input if you don't think any modifications are needed.

#         << CANDIDATE PROMPTS >>
#         {destinations}

#         << INPUT >>
#         {{input}}

#         << OUTPUT (remember to wrap the output with ```json (output)```)>>
#     """