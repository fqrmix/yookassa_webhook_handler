from fastapi import FastAPI, Request, Response, status

app = FastAPI()

@app.post("/webhook/apiv3/error_example")
async def handle_error(request: Request, response: Response):
    headers = request.headers
    payload = await request.json()
    print(f"Headers:\n{headers}\n\nBody:\n{payload}")
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


@app.post("/webhook/apiv3/success_example")
async def handle_success(request: Request, response: Response):
    headers = request.headers
    payload = await request.json()
    print(f"Headers:\n{headers}\n\nBody:\n{payload}")
    response.status_code = status.HTTP_200_OK
