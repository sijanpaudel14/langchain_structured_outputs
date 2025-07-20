from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# schema


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list.")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["P", "N"] = Field(
        description="Return sentiment of the review negative, positive, or neutral"
    )
    pros: Optional[list[str]] = Field(default=None,
                                      description="List the pros mentioned in the review"
                                      )
    cons: Optional[list[str]] = Field(default=None,
                                      description="List the cons mentioned in the review"
                                      )
    name: Optional[str] = Field(default=None,
                                description="Name of the reviewer, if mentioned"
                                )  # Optional field for the reviewer's name


structured_model = model.with_structured_output(Review)

input_text = """Review sites often challenge businesses to showcase their personality and humanize their brand. However, when a review goes the extra mile and mentions a team member by name, it creates a genuine connection with potential customers. This personal touch greatly improves the likelihood of customers choosing your business over competitors.

This aspect holds even greater significance in agent-based organizations like salons or real estate companies, where personalized recommendations reassure customers that they will receive individualized care.

See the positive review example below that mentions team members. You can witness this approach’s remarkable impact on building customer trust and fostering satisfaction.

Review by Sijan Paudel
"""

result = structured_model.invoke(input_text)
print(result.name)
