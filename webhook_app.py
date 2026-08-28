from fastapi import FastAPI
app = FastAPI()

@app.post("/webhook/pocketoption")
async def on_alert(data: dict):
    print("Executing Pocket Option trade from TradingView signal:", data)
    return {"status": "trade_executed"}
