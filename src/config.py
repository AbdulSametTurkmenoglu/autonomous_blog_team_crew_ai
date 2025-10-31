import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY .env dosyasında bulunamadı")
if not SERPER_API_KEY:
    raise EnvironmentError("SERPER_API_KEY (SerperDevTool için) .env dosyasında bulunamadı")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

print("LLM Yapılandırması Yüklendi (gpt-4o-mini).")