from pydantic import BaseModel, Field

class ChatResponse(BaseModel):
    answer : str = Field(description = "Answer of the user's question")
    summary : str = Field(description = "A short summary of the answer")
    category : str = Field(description = "Category of the user's question")
    confidence : float = Field(gt = 0, lt = 1, description="Confidence score of the model , greather than 0 and less than 1")
    keywords : list[str] = Field(description = "Important keywords related to the question")