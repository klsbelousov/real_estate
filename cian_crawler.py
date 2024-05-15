import time
import os
import requests
import psycopg2

from random import randint





def get_offer(item):
    global offer
    offer = {}

    try:
        offer["cian_id"] = item["id"]
        offer["balcony"] = item["balconiesCount"]
        offer["floor_num"] = item["floorNumber"]
        offer["garage"] = item["garage"]
        offer["total_area"] = item["totalArea"]
        offer["kitchen_area"] = item["kitchenArea"]
        offer["rooms_count"] = item["roomsCount"]
        offer["living_area"] = item["livingArea"]
        offer["is_apartments"] = item["isApartments"]
        offer["bedrooms_count"] = item["bedroomsCount"]
        offer["year_built"] = item["building"]["buildYear"]
        offer["total_floor"] = item["building"]["floorsCount"]
        offer["district"] = item["geo"]["address"][1]["title"]
        offer["hood"] = item["geo"]["address"][2]["title"]
        offer["metro_name"] = item["geo"]["undergrounds"][0]["name"]
        offer["metro_transport_type"] = item["geo"]["undergrounds"][0]["transportType"]
        offer["metro_time"] = item["geo"]["undergrounds"][0]["time"]
        offer["description"] = item["description"] 
        offer["price"] = item["bargainTerms"]["priceRur"]
        insertion()
    except Exception:
        pass
    return offer


def get_offers(data):
    for item in data["data"]["offersSerialized"]:
        get_offer(item)


def get_json(page: int, rooms: int):
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }
    data = """{
        "jsonQuery": {
            "_type": "flatsale",
            "engine_version": {
                "type": "term",
                "value": 2
            },
            "region": {
                "type": "terms", 
                "value": [1]
            },
            "room": {
                "type": "terms", 
                "value": [%d]
            },
            "page": {
                "type": "term",
                "value": %d
            }
        }
    }""" % (rooms, page)
    
    response = requests.post('https://api.cian.ru/search-offers/v2/search-offers-desktop/', headers=headers, data=data)
    result = response.json()
    return result

def insertion():
    connection = psycopg2.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        database=os.getenv('DATABASE'),
        password=os.getenv('PASSWORD'),
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO real_estate (
                cian_id,
                balcony,
                floor_num,
                garage,
                total_area,
                kitchen_area,
                rooms_count,
                living_area,
                is_apartments,
                bedrooms_count,
                year_built,
                total_floor,
                district,
                hood,
                metro_name,
                metro_transport_type,
                metro_time,
                description,
                price
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (offer["cian_id"], offer["balcony"], offer["floor_num"], offer["garage"], offer["total_area"], offer["kitchen_area"], offer["rooms_count"], offer["living_area"], offer["is_apartments"], offer["bedrooms_count"], offer["year_built"], offer["total_floor"], offer["district"], offer["hood"], offer["metro_name"], offer["metro_transport_type"], offer["metro_time"], offer["description"], offer["price"])
        )
        connection.commit()
        print('[INFO] Data was successfully added')


def main():
    counter = 0
    rooms = [1,2,3,4,5,6,9]
    for j in rooms:
        for i in range(1, 40):
            data = get_json(i, j)
            counter += 1
            print(counter)
            get_offers(data) 
            time.sleep(30)

if __name__ == '__main__':
    main()

