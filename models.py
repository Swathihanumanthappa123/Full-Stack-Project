from pydantic import BaseModel

class Author(BaseModel):
    id: int
    name: str
    email: str
    date_of_birth: str

class Book(BaseModel):
    id: int
    author_id: int
    isbn: str

class SaleItem(BaseModel):
    id: int
    book_id: int
    customer_name: str
    item_price: float
    quantity: int
