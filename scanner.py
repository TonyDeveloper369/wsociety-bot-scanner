class ProjectScanner:

    def scan(self, project_path: str) -> list[JavaFile]:
        arquivos_java = []

        for raiz, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]

            for file in files:
                if file in IGNORED_FILES or not file.endswith(".java"):
                    continue

                caminho = os.path.join(raiz, file)

                with open(caminho, "r", encoding="utf-8") as arquivo:
                    arquivos_java.append(
                        JavaFile(
                            nome=file,
                            caminho=caminho,
                            conteudo=arquivo.read()
                        )
                    )

        return arquivos_java