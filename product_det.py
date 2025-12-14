import sys

def get_product_info(product_name, product_id, quantity, price):
  
    return (
        f"product Name:{product_name},"
        f"product ID:{product_id},"
        f"Quantity:{quantity},"
        f"price:{price:.2f}"
    )
if __name__ == "__main__":
    print("=== product details ===")
    print(get_product_info("smart watch","123","4",550))
