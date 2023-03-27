import requests
def test_get_artists():
    response = requests.get('http://localhost:5000/artists')
    assert response.status_code == 200
    artists = response.json()
    assert len(artists) > 0
    
def test_get_events():
    response = requests.get('http://localhost:5000/events')
    assert response.status_code == 200
    events = response.json()
    assert len(events) > 0
