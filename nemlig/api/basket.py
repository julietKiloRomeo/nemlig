from . import webapi

def add_product_to_basket(product_id: int, quantity: int) -> dict:
    """
    Add a product to the basket.

    Args:
        product_id (int): The ID of the product to add.
        quantity (int): The quantity of the product to add.

    Returns:
        dict: The response from the API.

    Examples:
        >>> add_product_to_basket(123, 2)
        {'status': 'success', 'message': 'Product added to basket.'}
    """
    return webapi.post('/basket/AddToBasket', json={
        'productId': product_id,
        'quantity': quantity,
    })