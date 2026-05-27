from models import Chunk
from config import MAX_CHUNK_SIZE

class JavaChunker:

    def create_chunks(self, arquivos: list) -> list[Chunk]:

        return [
            Chunk(arquivo=arquivo.nome, conteudo=parte)
            for arquivo in arquivos
            for parte in self._split_content(arquivo.conteudo)
        ]

    def _split_content(self, conteudo: str) -> list[str]:

        return [
            conteudo[i : i + MAX_CHUNK_SIZE]
            for i in range(0, len(conteudo), MAX_CHUNK_SIZE)
        ]