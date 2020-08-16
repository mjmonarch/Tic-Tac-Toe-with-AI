def print_book_info(title, author=None, year=None):
    #  Write your code here
    result = f'"{title}"'
    if author or year:
        result += " was written"
    if author:
        result += f" by {author}"
    if year:
        result += f" in {year}"
    print(result)


# print_book_info("War and Peace", "Leo Tolstoy", 1869)
# print_book_info("Crime and Punishment", year=1866)
# print_book_info("The Chonicles of Narnia", "C.S. Lewis")
# print_book_info("Harry Potter")