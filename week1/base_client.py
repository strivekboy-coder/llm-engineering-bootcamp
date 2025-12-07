from typing import Optional, Any, Dict
from retry1 import retry
from timer import timer
class BaseClient:

    def __init__(self, base_url:str, timeout:float = 5.0,api_key :Optional[str] = None) -> None:

        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.api_key = api_key
    @retry(max_retries=3, delay=0.2, backoff=2.0)
    @timer
    def request(self, method: str, url: str, **kwargs: Any) -> Dict[str, Any]:
        url = f"{self.base_url}/{url.lstrip('/')}"
        return {
            "method": method,
            "url": url,
            "timeout": self.timeout,
            "sent_kwargs": kwargs,
        }
if __name__ == '__main__':
    client = BaseClient(
        base_url="https://api.example.com/",
        timeout = 10.0,
        api_key = "SECRET-KEY-123"
    )
    print("base_url:", client.base_url)
    print("timeout:", client.timeout)
    print("api_key:", client.api_key)

if __name__ == "__main__":
    client = BaseClient("https://api.test.com", timeout=3.0)
    resp = client.request("GET", "/users", q="alice")
    print(resp)

client.request("GET", "/users", q="alice")
