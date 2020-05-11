

class Book:

    def __init__(self, path: str, language: str, tokenizer):
        self.path = path
        self.language = language
        self.tokenizer = tokenizer
        self.tokens = tokenizer.tokenize(self.read_book(path))

    def read_book(self, path, encoding='utf-8'):
        with open(path, 'r+', encoding=encoding) as book_file:
            return book_file.read()
