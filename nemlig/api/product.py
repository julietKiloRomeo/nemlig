from . import webapi
from typing import Dict, Any

def search_products(query: str = '', take: int = 10) -> Dict[str, Any]:
    """
    Search for products based on the given query.

    Args:
        query (str): The search query string (default: '').
        take (int): The maximum number of products to retrieve (default: 10).

    Returns:
        dict: A dictionary containing the search results.

    Example:
        nemlig.api.search_products("agurk")

        Returns:
        {
            'Products': {
                'Products': [
                    {
                        'TemplateName': 'productlistitem',
                        'PrimaryImage': 'https://www.nemlig.com/scommerce/images/agurk-oeko.jpg?i=h0XZ3ZP4/106593',
                        'Availability': {
                            'IsDeliveryAvailable': True,
                            'IsAvailableInStock': True,
                            'ReasonMessageKeys': []
                        },
                        'Id': '106593',
                        'Name': 'Agurk øko.',
                        'Category': 'Grønt',
                        'SubCategory': 'Agurk / Tomat',
                        'Url': 'agurk-oeko-106593',
                        'UnitPrice': '10,00 kr./Stk.',
                        'UnitPriceCalc': 10.0,
                        'UnitPriceLabel': 'kr./Stk.',
                        'DiscountItem': True,
                        'Description': '1 stk. / Spanien / Klasse 1',
                        'SaleBeforeLastSalesDate': 0,
                        'Price': 10.0,
                        'Campaign': None,
                        'Labels': ['Øko (europæisk)', 'Discount'],
                        'Favorite': True,
                        'ProductSubGroupNumber': '6200100007',
                        'ProductSubGroupName': 'Agurk',
                        'ProductCategoryGroupNumber': '6200100000',
                        'ProductCategoryGroupName': 'Grønt',
                        'ProductMainGroupNumber': '6200000000',
                        'ProductMainGroupName': 'Frugt og grønt'
                    }
                ]
            }
        }
    """
    return webapi.get('/s/0/1/0/Search/Search', params={
        'query': query,
        'take': take,
    })

def search_results_as_html(results):
    """
    Converts the results from a search into "cards" with info about each result
    and an image of the product.

    Args:
        results (dict): A dictionary containing the search results.

    Returns:
        str: A markdown representation of the search results.

    Example:
        search_results_as_markdown({
            'Products': {
                'Products': [
                    {
                        'TemplateName': 'productlistitem',
                        'PrimaryImage': 'https://www.nemlig.com/scommerce/images/agurk-oeko.jpg?i=h0XZ3ZP4/106593',
                        'Availability': {
                            'IsDeliveryAvailable': True,
                            'IsAvailableInStock': True,
                            'ReasonMessageKeys': []
                        },
                        'Id': '106593',
                        'Name': 'Agurk øko.',
                        'Category': 'Grønt',
                        'SubCategory': 'Agurk / Tomat',
                        'Url': 'agurk-oeko-106593',
                        'UnitPrice': '10,00 kr./Stk.',
                        'UnitPriceCalc': 10.0,
                        ...
                        'ProductMainGroupName': 'Frugt og grønt'
                    }
                ]
            }
        })

    Returns:
        [![Agurk øko.](https://www.nemlig.com/scommerce/images/agurk-oeko.jpg?i=h0XZ3ZP4/106593)](https://www.nemlig.com/agurk-oeko-106593)
        
        **Name:** Agurk øko.
        **Unit Price:** 10,00 kr./Stk.
        **Description:** 1 stk. / Spanien / Klasse 1
    """

    html = ""
    for product in results['Products']['Products']:
        html += f"<div class='card' style='width: 18rem;'>\n"
        html += f"  <img src='{product['PrimaryImage']}' class='card-img-top' style='width: 120px;'>\n"
        html += f"  <div class='card-body'>\n"
        html += f"    <h5 class='card-title'>{product['Name']}</h5>\n"
        html += f"    <p class='card-text'>Unit Price: {product['UnitPrice']}</p>\n"
        html += f"    <p class='card-text'>Description: {product['Description']}</p>\n"
        html += f"  </div>\n"
        html += f"</div>\n"
    return html
