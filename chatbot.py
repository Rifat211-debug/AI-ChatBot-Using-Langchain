from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableBranch, RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

from prompts import programming_prompt, math_prompt, general_prompt, followup_prompt
from schemas import ChatResponse

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = PydanticOutputParser(
    pydantic_object = ChatResponse
)

#chains
programming_chain = programming_prompt | model | parser
math_chain = math_prompt | model | parser
general_chain = general_prompt | model | parser


#runnable branch
prog_keywords = ["python", "programming", "coding", "code", "java", "javascript", "sql", "function", "class", "algorithm", "machine learning", "deep learning", "langchain", "c++", "html"]
math_keywords = ["math", "mathematics", "calculate", "equation", "derivative", "integral", "algebra", "geometry", "probability", "statistics", "solve"]


conditional_chain = RunnableBranch(
    (
        lambda x : any(word in x["question"].strip().lower() for word in prog_keywords),
        programming_chain
    ),
    (
        lambda x : any(word in x["question"].strip().lower() for word in math_keywords),
        math_chain
    ),
    general_chain
)

#runnable parallel
parallel_chain = RunnableParallel(
    {
        "answer" : conditional_chain,
        "follow_up" : followup_prompt | model | StrOutputParser()
    }
)


#final response of chatbot 
def get_response(question):
    result = parallel_chain.invoke({
        "question" : question,
        "format_instructions" : parser.get_format_instructions()
        })

    response = result["answer"]
    followup_questions = result["follow_up"].splitlines()

    return response, followup_questions

