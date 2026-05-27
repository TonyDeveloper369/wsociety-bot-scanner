from dotenv import load_dotenv

from scanner import ProjectScanner
from sanitizer import CodeSanitizer
from chunker import JavaChunker
from analyzer import OpenAIAnalyzer
from report import ReportGenerator
from config import PROJECT_PATH

def main():

    print("Iniciando Java AI Analyzer...\n")
    load_dotenv()

    scanner = ProjectScanner()
    sanitizer = CodeSanitizer()
    chunker = JavaChunker()
    analyzer = OpenAIAnalyzer()
    report_generator = ReportGenerator()

    arquivos = scanner.scan(PROJECT_PATH)

    for arquivo in arquivos:
        arquivo.conteudo = sanitizer.sanitize(arquivo.conteudo)

    chunks = chunker.create_chunks(arquivos)

    resultados = [analyzer.analyze(chunk) for chunk in chunks]

    report_generator.generate(resultados)

if __name__ == "__main__":
    main()