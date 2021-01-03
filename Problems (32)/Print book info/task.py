def print_book_info(title, author=None, year=None):
    info = f'"{title}"'
    if author is not None or year is not None:
        info += " was written"
    if author:
        info += f" by {author}"
    if year:
        info += f" in {year}"
    print(info)


# print_book_info('War and Peace', "Leo Tolstoy", 1869)
# print_book_info('Crime and Punishment', 1866)