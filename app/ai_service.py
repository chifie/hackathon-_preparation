from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_stock(product_name, quantity, sales_last_7_days):

    prompt = f"""
    Analyze this inventory information.

    Product: {product_name}
    Current stock: {quantity}
    Sales in last 7 days: {sales_last_7_days}

    Give a short explanation of:
    1. Whether the stock may need attention.
    2. Why.
    3. One recommendation for the business owner.
    """

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text