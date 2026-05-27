class ReportGenerator:

    def generate(self, resultados: list):
        print("\n" + "=" * 70)
        print("RELATÓRIO FINAL")
        print("=" * 70)

        for resultado in resultados:
            print(f"\nArquivo: {resultado.arquivo}")
            print("-" * 70)
            print(resultado.analise)
            print("\n")