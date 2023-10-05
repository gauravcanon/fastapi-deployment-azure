from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()


# Add uvicorn start command


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/me")
def read_user_me():
    # generate a fake username for demo purposes
    return {"username": "fakecurrentuser"}


if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0",
                port=8000,
                proxy_headers=True,
                forwarded_allow_ips="*",
                )

