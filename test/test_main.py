from fastapi.testclient import TestClient
from src.main import api  # adjust if your file path is different

client = TestClient(api)


# Test home endpoint
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


# Test POST (Create Ticket)
def test_create_ticket():
    response = client.post("/ticket", json={
        "id": 1,
        "flight_name": "Air Asia",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Singapore"
    })
    assert response.status_code == 200
    assert response.json()["flight_name"] == "Air Asia"


# Test GET all tickets
def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


# Test PUT (Update Ticket)
def test_update_ticket():
    response = client.put("/ticket/1", json={
        "id": 1,
        "flight_name": "Air Asia Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:00",
        "destination": "Malaysia"
    })
    assert response.status_code == 200
    assert response.json()["flight_name"] == "Air Asia Updated"


# Test DELETE (Delete Ticket)
def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Air Asia Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:00",
        "destination": "Malaysia"
    }
