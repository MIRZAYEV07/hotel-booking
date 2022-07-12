from django.shortcuts import render
from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from geopy.geocoders import Nominatim
from .models import UserRegister ,HotelRoom
from .services import get_hotels_list , get_room_list,get_hotel


geolocator = Nominatim(user_agent="example app")



def geo(l,m):

    return geolocator.reverse(f'{l}, {m}').raw


def make_button(button,holat):
    btn1 = []
    b1 = []
    for a in button:
        b1.append(InlineKeyboardButton(f"{a['name']}",callback_data=f"{holat}_{a['id']}"))
        if len(b1) == 2:
            btn1.append(b1)
            b1 = []
    if b1:
        btn1.append(b1)
    return btn1



def start(update ,context):

    user_name = update.message.from_user.first_name

    buttons = [

        [ KeyboardButton("Register")],

    ]
    update.message.reply_text(f"SALOM {user_name}",reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True))
    return 'main_part'



def user_firstname(update ,context):
    update.message.reply_text("Ismingiz: ")

    return 1

def user_lastname(update ,context):
    global first_name
    first_name = update.message.text
    update.message.reply_text("Familiya: : ")

    return 2
def user_phonenumber(update ,context):
    global last_name
    last_name = update.message.text
    update.message.reply_text("Telefon raqam: ")

    return 3

def user_register(update,context):
    phone_number = update.message.text
    user = UserRegister()
    user.first_name = first_name
    user.last_name = last_name
    user.phone_number = phone_number
    user.user_tgID = update.message.from_user.id
    user.save()
    buttons = [

        [KeyboardButton("Submit")],

    ]
    update.message.reply_text(f"Register", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    return 'main_part'


def hotel_choice(update ,context):
    user_name = update.message.from_user.first_name

    buttons = [

        [KeyboardButton("Hotels"),KeyboardButton("Hotels in my area", request_location=True)],

    ]
    update.message.reply_text(f" {user_name} maqul tugmani bosing", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def hotel_list(update , context):
    print('>>>>>>>>>>')
    if update.message.location:

        location = update.message.location

        my_area = geo(location.latitude,location.longitude)["display_name"]
        my_area = my_area.split(',')
        print(my_area[-3])

        hotel_list = get_hotels_list(my_area[-3])
        print(hotel_list)


    else:
        hotel_list = get_hotels_list()




    if hotel_list:
        btn = make_button(hotel_list, "hotel")
        print(btn)

        update.message.reply_text("Hotels List: ", reply_markup=InlineKeyboardMarkup(btn))
    else:
        update.message.reply_text("Error 404 !")


    return 'inline_query'

def inline_query(update , context):
    query = update.callback_query
    data = query.data
    data1 = data.split('_')
    print(data1)

    if data1[0] == 'hotel':
        btn = make_button(get_room_list(data1[1]),'rooms')
        query.message.delete()
        query.message.reply_photo(photo= open(f"{get_hotel(data1[1])['image']}",'rb'),caption=f" Name :{get_hotel(data1[1])['name']}\n\n Description:{get_hotel(data1[1])['description']}\n\n Location : {get_hotel(data1[1])['location']}", reply_markup=InlineKeyboardMarkup(btn))

    # if data1[0] == 'rooms':
    #     query_data = HotelRoom.objects.filter(data1[1])
    #     query.message.delete()
    #
    #     query.message.reply_text(f"{query_data['name']}")















