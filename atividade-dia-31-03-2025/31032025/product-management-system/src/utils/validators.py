def validate_product_name(name: str) -> str:
    if not name or len(name) < 3:
        raise ValueError("Product name must be at least 3 characters long.")
    return name

def validate_product_description(description: str) -> str:
    if not description or len(description) < 10:
        raise ValueError("Product description must be at least 10 characters long.")
    return description

def validate_product_price(price: float) -> float:
    if price <= 0:
        raise ValueError("Product price must be greater than zero.")
    return price