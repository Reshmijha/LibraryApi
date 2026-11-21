def validate_book(data):
    errors = []

    if not data:
        return ["Request body must be JSON"]

    title = data.get("title")
    if not title or not str(title).strip():
        errors.append("title is required")
    elif len(title) > 100:
        errors.append("title must be at most 100 characters")

    author = data.get("author")
    if not author or not str(author).strip():
        errors.append("author is required")

    year = data.get("published_year")
    if not isinstance(year, int) or year < 1450 or year > 2100:
        errors.append("published_year must be a number between 1450 and 2100")

    price = data.get("price", 0)
    if not isinstance(price, (int, float)) or price < 0:
        errors.append("price must be a positive number")

    if "available" in data and not isinstance(data["available"], bool):
        errors.append("available must be true or false")

    return errors
