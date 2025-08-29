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
        self.rating: int = Book.UNRATED
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
        notes_counter: dict[int, int] = {}
        for note in self.notes:
            if note.page not in notes_counter:
                notes_counter[note.page] = 1
            else:
                notes_counter[note.page] += 1
        max_page, max_counter = -1 , 0
        for page, count in notes_counter.items():
            if count > max_counter:
                max_page, max_counter , = page, count
        return  max_page

    def __str__(self) -> str :
        ratings : dict[int,str] = {
            Book.EXCELLENT: "Excellent",
            Book.GOOD: "good",
            Book.BAD: "Bad",
            Book.UNRATED: "Unrated"
        }
        return f"ISBN: {self.isbn} \n Author: {self.author} \nPages: {self.pages} \n Rating: {ratings[self.rating]}]"


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn:str, title : str, author : str , pages : int ) -> bool:
        if isbn in  self.books:
            return True
        else:
            self.books[isbn] = Book(isbn,title,author,pages)
            return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        return self.books.get(isbn, None)
















































