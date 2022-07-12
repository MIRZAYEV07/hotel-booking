import json
from collections import OrderedDict
from django.db import connection


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))






def get_hotels_list(key_word=None):
    if key_word:
        search = f"WHERE hotel.location like '%{key_word}%' "
    else:
        search = ''
    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT *   FROM tg_bot_hotel as hotel
               
                {search}





        """)
        data = dictfetchall(cursor)

    return data


def get_hotel(key_word):

    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT *   FROM tg_bot_hotel as hotel
                WHERE hotel.id = {key_word}
                





        """)
        data = dictfetchone(cursor)

    return data


def get_room_list(key_word):
    with connection.cursor() as cursor:
        cursor.execute(f"""

                SELECT room.name ,room.id   FROM tg_bot_hotel as hotel
                INNER JOIN tg_bot_hotelroom as room
                ON hotel.id = room.hotel_id
                WHERE hotel.id = {key_word}
                






        """)
        data = dictfetchall(cursor)

    return data

