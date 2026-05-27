from dataclasses import dataclass

@dataclass
class JavaFile:
    nome: str
    caminho: str
    conteudo: str

@dataclass
class Chunk:
    arquivo: str
    conteudo: str

@dataclass
class AnalysisResult:
    arquivo: str
    analise: str