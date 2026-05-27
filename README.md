# 💻 wsociety-bot-scanner

O **wsociety-bot-scanner** é um agente autônomo inteligente desenvolvido em Python, inspirado na cultura hacker de auditoria e monitoramento de bastidores. Ele foi projetado para realizar varreduras automatizadas e revisões arquiteturais profundas em sistemas Java. Utilizando engenharia de prompts avançada integrada ao modelo `gpt-4o-mini` da OpenAI, o bot expõe falhas críticas e vulnerabilidades estruturais antes que o código chegue ao ambiente de produção.

O projeto foi construído sob os pilares do **Clean Code**, garantindo alta performance através de estruturas matematicamente limpas como `dataclasses`, processamento linearizado por matrizes de Expressões Regulares (RegEx) e fatiamento lógico de strings em saltos controlados.

---

## 🚀 Funcionalidades

* **Scanner de Perímetro:** Varre recursivamente o diretório do projeto Java ignorando pastas e arquivos desnecessários ou gerados pelo sistema (como `.git`, `target`, `.idea`, `__pycache__`).
* **Sanitização de Segurança (Data Protection):** Passa o código-fonte por uma matriz rigorosa de RegEx para ofuscar dados confidenciais (senhas, chaves AWS, tokens, chaves JWT, IPs e e-mails) antes do envio para a API externa, blindando o ecossistema.
* **Fatiamento de Código (Chunking):** Fragmenta arquivos extensos através de saltos matemáticos exatos no tamanho máximo configurado, otimizando o consumo de tokens e evitando quebras nos limites de contexto da IA.
* **Auditoria de Vulnerabilidades:** Detecta cirurgicamente anomalias no código Java como:
  * Injeção de SQL (SQL Injection)
  * Alto acoplamento e baixa coesão estrutural
  * Classes Deus (God Classes) e violações dos princípios SOLID
  * Má gestão ou vazamento de recursos JDBC
* **Terminal Report Generator:** Consolida as respostas assíncronas enviadas pela IA e renderiza um relatório técnico limpo e formatado diretamente no console.

---

## 📂 Estrutura do Projeto

A arquitetura do sistema é estritamente modular, mapeada por responsabilidades únicas:

```text
├── app.py              # Fluxo principal (Orquestrador do Pipeline)
├── config.py           # Configurações globais e limites do sistema
├── models.py           # Modelos de dados puros (Python Dataclasses)
├── scanner.py          # Mecanismo de varredura de arquivos do projeto Java
├── sanitizer.py        # Sistema de ofuscação e segurança baseada em RegEx
├── chunker.py          # Divisor de arquivos por fatiamento de strings
├── analyzer.py         # Client de comunicação direta com a OpenAI
├── prompts.py          # Engenharia de prompt (Perfil do Arquiteto Sênior)
├── report.py           # Formatador e exibidor do relatório em terminal
└── .env                # Arquivo protegido de credenciais (Chave da API)
