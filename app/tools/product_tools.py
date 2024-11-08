import requests
from langchain.tools import BaseTool

class ProductUploadTool(BaseTool):
    name = "Product Upload Tool"
    description = "Uploads product data via FastAPI."

    def _run(self, query: str):
        # Extract product details from the query using a helper function
        product_data = extract_product_details(query)
        
        if not product_data:
            return {"error": "Failed to extract product details from the query."}
        
        # Send data to FastAPI product upload endpoint
        response = requests.post('http://localhost:8000/create-product', json=product_data)
        return response.json()

# Function to extract product details (e.g., for upload)
# def extract_product_details(query: str):
#     import re
#     product_name = re.search(r"called '([^']+)'", query)
#     product_cost = re.search(r"costing (\d+\.\d+|\d+)", query)
#     product_description = re.search(r"with a description '([^']+)'", query)
    
#     if product_name and product_cost and product_description:
#         return {
#             "product_name": product_name.group(1),
#             "product_cost": float(product_cost.group(1)),
#             "product_description": product_description.group(1)
#         }
#     return None

def extract_product_details(query: str):
    import re
    product_name = re.search(r"called '([^']+)'", query)
    product_cost = re.search(r"costing (\d+\.\d+|\d+)", query)
    product_description = re.search(r"with a description '([^']+)'", query)
    
    if product_name and product_cost and product_description:
        product = Product(
            product_name=product_name.group(1),
            product_cost=float(product_cost.group(1)),
            product_description=product_description.group(1)
        )
        return product.dict()  # Returns product details as a dictionary
    return None
