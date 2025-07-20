from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# schema


Review = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(Review)

input_text = """Review sites often challenge businesses to showcase their personality and humanize their brand. However, when a review goes the extra mile and mentions a team member by name, it creates a genuine connection with potential customers. This personal touch greatly improves the likelihood of customers choosing your business over competitors.

This aspect holds even greater significance in agent-based organizations like salons or real estate companies, where personalized recommendations reassure customers that they will receive individualized care.

See the positive review example below that mentions team members. You can witness this approach’s remarkable impact on building customer trust and fostering satisfaction.

Review by Sijan Paudel
"""

result = structured_model.invoke(input_text)
print(result)
