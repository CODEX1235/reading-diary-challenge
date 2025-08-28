from datetime import datetime

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
       return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating:int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool :
        if page > self.pages:
            return False
        else:
            self.notes.append(Note(text, page, date))
            return True

    def set_rating(self, rating: int) -> bool :
        if rating in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            self.rating : int = rating
            return True
        else:
            return False

    def get_notes_of_page(self, page: int)-> list[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self)-> int:
        if not self.notes:
            return -1

        notas_por_pagina = {}
        for note in self.notes:
            notas_por_pagina[note.page] = notas_por_pagina.get(note.page,0) + 1

        return max(notas_por_pagina, key= notas_por_pagina.get)



<




























