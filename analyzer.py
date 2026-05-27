from openai import OpenAI
from prompts import JAVA_ANALYZER_PROMPT
from models import AnalysisResult
from config import OPENAI_MODEL

class OpenAIAnalyzer:

    def __init__(self):
        self.client = OpenAI()

    def analyze(self, chunk) -> AnalysisResult:
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            temperature=0.2,
            messages=[
                {"role": "system", "content": JAVA_ANALYZER_PROMPT},
                {"role": "user", "content": chunk.conteudo}
            ]
        )

        return AnalysisResult(
            arquivo=chunk.arquivo,
            analise=response.choices[0].message.content
        )