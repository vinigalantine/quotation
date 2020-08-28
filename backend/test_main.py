from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Here are all the tests

# This tests an normal response
def test_get_quotation():
    response = client.get("/quotes?symbol=PETR4.SA")

    data = response.json()
    
    assert response.status_code == 200
    assert type(data["price"]) is float
    assert data["symbol"] == "PETR4.SA"

# This tests an requisition where no parameter is provided
def test_get_quotation_null_symbol():
    response = client.get("/quotes")
    
    assert response.status_code == 400
    assert response.json() == {"detail":"You need to inform a symbol!"}

# This tests an requisition where the "symbol" parameter is None
def test_get_quotation_null_symbol():
    response = client.get("/quotes?symbol=")
    
    assert response.status_code == 400
    assert response.json() == {"detail":"You need to inform a symbol!"}

# This tests an requisition of a nonexistent symbol
def test_get_quotation_nonexistent_symbol():
    response = client.get("/quotes?symbol=ABCDEF")
    
    assert response.status_code == 404
    assert response.json() == {"detail":"Looks like this symbol doesn't exists... :/"}