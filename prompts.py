from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

#Programming Prompt
programming_prompt = PromptTemplate(
    template = """
     You are an expert and 15 years experienced Programmer.
     Answer the user's programming question clearly and accurately
     with coding example and explanation should be beginner-friendly.
     User Question : {question}
     {format_instructions}
""",
   input_variables = ["question", "format_instructions"]
)

#Mathmatics prompt
math_prompt = PromptTemplate(
    template = """
    Your are a university Professor of Mathmatics.
    Solve the user's math problem step by step with explanation in a simple manner.
    User Question : {question}
    {format_instructions}
""",
   input_variables = ["question", "format_instructions"]
)

#General Prompt
general_prompt = PromptTemplate(
    template = """
    You are a helpful Reply Assistant.
    Answer the user's question clearly without unnecessary information.
    If the explanation required, explain in a understandable way.
    User Question : {question}
    {format_instructions}
""",
    input_variables = ["question", "format_instructions"]
)

#follow-up prompt
followup_prompt = ChatPromptTemplate.from_template(
    """ 
    Based on the following user's question, suggest 3 short follow-up questions they might want to ask next.
    Rules:
    - Return ONLY the 3 questions.
    - Put each question on a separate line.
    - Do NOT write any introduction.
    Question : {question}
    """
)