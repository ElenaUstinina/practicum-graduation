import time

import data
import sender_stand_request


# Елена Устинина, 9-я когорта — Финальный проект. Инженер по тестированию плюс

def test_track_order():
    track = sender_stand_request.post_create_order(data.create_order_body).json()["track"]
    response = sender_stand_request.get_track_order(track)

    assert response.status_code == 200
