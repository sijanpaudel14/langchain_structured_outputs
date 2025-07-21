# LangChain Structured Outputs Learning Project

This repository contains examples and implementations of LangChain's structured output capabilities using Google's Gemini AI model. The project demonstrates different approaches to obtaining structured, predictable responses from language models.

## 🚀 Features

- **Basic LangChain Integration**: Simple prompt-response workflow
- **JSON Schema Structured Outputs**: Using JSON schema for output validation
- **Pydantic Model Structured Outputs**: Type-safe structured outputs with Pydantic
- **Review Analysis**: Practical example analyzing text reviews with sentiment, themes, and structured data extraction

## 📋 Prerequisites

- Python 3.8+
- Google AI API Key (Gemini)
- Required Python packages (see Installation)

## 🔧 Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd langchain_structured_outputs
```

2. Install required packages:

```bash
pip install langchain-google-genai python-dotenv pydantic
```

3. Set up environment variables:
   Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## 📁 Project Structure

```
├── .env                              # Environment variables (API keys)
├── test.py                           # Basic LangChain implementation
├── with_structured_output_json.py    # JSON schema structured outputs
├── with_structured_output_pydantic.py # Pydantic model structured outputs
└── README.md                         # This file
```

## 🎯 What You'll Learn

### 1. Basic LangChain Implementation (`test.py`)

Learn the fundamentals of:

- Setting up ChatGoogleGenerativeAI model
- Creating prompt templates
- Building runnable chains
- Basic model invocation

**Key Concepts:**

- `PromptTemplate` for structured prompts
- Chain composition with `|` operator
- Model configuration and temperature settings

### 2. JSON Schema Structured Outputs (`with_structured_output_json.py`)

Discover how to:

- Define JSON schemas for structured data
- Use `with_structured_output()` method
- Extract specific data fields with validation
- Handle optional and required fields

**Schema Features:**

- Array fields for lists (key_themes, pros, cons)
- Enum constraints for sentiment classification
- Optional fields with null handling
- Required field validation

### 3. Pydantic Model Structured Outputs (`with_structured_output_pydantic.py`)

Master advanced techniques:

- Type-safe data models with Pydantic
- Field validation and descriptions
- Literal types for constrained values
- Optional field handling with defaults

**Pydantic Advantages:**

- Automatic type validation
- Better IDE support and autocomplete
- Clear field documentation
- Runtime type checking

## 🔍 Review Analysis Use Case

Both structured output examples demonstrate a **review analysis** system that extracts:

- **Key Themes**: Important topics discussed in the review
- **Summary**: Brief overview of the review content
- **Sentiment**: Positive/Negative classification
- **Pros**: Listed advantages mentioned
- **Cons**: Listed disadvantages mentioned
- **Reviewer Name**: If mentioned in the text

## 🚀 Usage Examples

### Basic Usage

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
response = model.invoke("Your question here")
```

### Structured Output with Pydantic

```python
class MySchema(BaseModel):
    field1: str = Field(description="Description here")
    field2: Optional[list[str]] = Field(default=None)

structured_model = model.with_structured_output(MySchema)
result = structured_model.invoke("Your input text")
```

## 🎨 Key Learning Outcomes

After working through this project, you'll understand:

1. **LangChain Fundamentals**

   - Model initialization and configuration
   - Prompt engineering with templates
   - Chain composition and execution

2. **Structured Output Strategies**

   - JSON Schema vs Pydantic models
   - When to use each approach
   - Field validation and constraints

3. **Real-World Application**

   - Text analysis and data extraction
   - Sentiment analysis implementation
   - Handling optional and required data

4. **Best Practices**
   - Environment variable management
   - Error handling considerations
   - Model temperature and parameter tuning

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Google AI Studio](https://aistudio.google.com/)
- [JSON Schema Specification](https://json-schema.org/)

## 🤝 Contributing

Feel free to contribute improvements, additional examples, or documentation enhancements!

## 📄 License

This project is for educational purposes. Please ensure you comply with Google AI's terms of service when using their API.

---

**Happy Learning! 🎉**

_This project demonstrates the power of structured outputs in making AI responses more predictable, parseable, and useful for downstream applications._
