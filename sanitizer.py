import re


class CodeSanitizer:

    def __init__(self):
        self.rules = [
            (r'password\s*=\s*".*?"', 'password="***"', re.IGNORECASE),
            (r'api[_-]?key\s*=\s*".*?"', 'api_key="***"', re.IGNORECASE),
            (r'token\s*=\s*".*?"', 'token="***"', re.IGNORECASE),
            (r'(jdbc:mysql://|https?://)[^\s"]+', '[URL_REMOVIDA]', 0),
            (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[EMAIL_REMOVIDO]', 0),
            (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP_REMOVIDO]', 0),
            (r'eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+', '[JWT_REMOVIDO]', 0),
            (r'AKIA[0-9A-Z]{16}', '[AWS_KEY_REMOVIDA]', 0)
        ]

    def sanitize(self, codigo: str) -> str:
        for padrao, substituto, flags in self.rules:
            codigo = re.sub(padrao, substituto, codigo, flags=flags)

        return codigo