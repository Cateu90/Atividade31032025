def validate_product_name(name: str) -> str:
    if not name or len(name) < 3:
        raise ValueError("Product name must be at least 3 characters long.")
    return name

def validate_product_price(price: float) -> float:
    if price < 0:
        raise ValueError("Product price must be a non-negative value.")
    return price

def validate_product_stock(stock: int) -> int:
    if stock < 0:
        raise ValueError("Product stock must be a non-negative integer.")
    return stock