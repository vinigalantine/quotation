from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from alpha_vantage import AlphaVantage

app = FastAPI()

"""
 I suffered with CORS problems :/
 Thats why I'm allowing "*" (All) origins, I know it's not secure but this is a "silly project"
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Here is the only route we have
@app.get("/quotes")
def quotes(symbol: Optional[str] = None):
    av = AlphaVantage()

    if symbol is None or symbol == "":
        # Here raise an Exception when no "symbol" is provided
        raise HTTPException(status_code=400, detail="You need to inform a symbol!")

    return av.quotation(symbol)