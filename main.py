from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calculate")
async def calculate_y(x: float):
    # バリデーション: xが整数または小数点でない場合はエラーを返す
    if not isinstance(x, (int, float)):
        raise HTTPException(status_code=400, detail="Input value must be an integer or float")

    # 一次関数の計算: y = 10x + 5
    y = 10 * x + 5

    return {"result": y}