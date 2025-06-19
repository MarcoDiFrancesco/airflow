from airflow.sdk import dag, task
import requests

# {Symbol: Name}
SYMBOLS = {
    "VWCE.DE": "VWCE",
    "AYEM.DE": "AYEM",
    "^GSPC": "GSPC",    
}


@dag(schedule="0 2 * * *")  # Daily at 2:00
def finance_api_update():
    """
    # Download Finance data from API
    
    First update database:
    e.g.
    `https://finance.difra.me/api/update/%5EGSPC`

    Then test if it has current month data:
    e.g.
    `https://finance.difra.me/api/price/%5EGSPC/2025-01`
    """

    @task()
    def update(symbol):
        api_url = f"https://finance.difra.me/api/update/{symbol}"
        response = requests.get(api_url)
        response.raise_for_status()
        return symbol

    @task()
    def price(symbol):
        api_url = f"https://finance.difra.me/api/price/{symbol}/2025-01"
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()

    for symbol, name in SYMBOLS.items():
        update_t = update.override(task_id=f"update_{name}")(symbol)
        price_t = price.override(task_id=f"price_{name}")(symbol)
        update_t >> price_t


finance_api_update()
