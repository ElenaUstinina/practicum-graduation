import requests
import config
import data


def post_create_order(body):
    return requests.post(config.MAIN_URL + config.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_track_order(track_id):
    return requests.get(config.MAIN_URL + config.TRACK_ORDER_PATH,
                        params={"t": track_id},
                        headers=data.headers)
