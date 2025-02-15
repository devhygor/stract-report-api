import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Testa o endpoint raiz"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Home</h1>" in response.data

def test_plataforma(client):
    response = client.get('/meta_ads')
    assert response.status_code == 200
    assert b"de meta_ads" in response.data

def test_plataforma_resumo(client):
    """Testa o endpoint de resumo de uma plataforma"""
    response = client.get('/meta_ads/resumo')
    assert response.status_code == 200
    assert b"Resumo de meta_ads" in response.data

def test_geral(client):
    """Testa o endpoint geral"""
    response = client.get('/geral')
    assert response.status_code == 200
    assert b"Geral" in response.data

def test_geral_resumo(client):
    """Testa o endpoint de resumo geral"""
    response = client.get('/geral/resumo')
    assert response.status_code == 200
    assert b"Resumo Geral" in response.data

if __name__ == "__main__":
    pytest.main()