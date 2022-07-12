from django.core.management.base import BaseCommand
from telegram.ext import CommandHandler, Updater, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from ...views import( start,user_register,user_firstname,user_phonenumber,user_lastname,hotel_choice,hotel_list ,inline_query)

TOKEN = "5420058689:AAFYdmLGty31txO_zAFvBZAbXFJMCjDb3vc"


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(TOKEN)

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                'main_part': [MessageHandler(Filters.regex('Register'),user_firstname),MessageHandler(Filters.regex('Submit'),hotel_choice),MessageHandler(Filters.regex('Hotels'),hotel_list),MessageHandler(Filters.location,hotel_list)
                   ],
                1  : [MessageHandler(Filters.text,user_lastname)
                   ],
                2  : [MessageHandler(Filters.text,user_phonenumber)
                   ],
                3  : [MessageHandler(Filters.text,user_register)
                   ],


                'inline_query': [CallbackQueryHandler(inline_query), CommandHandler('start', start),
                    ],


            },
            fallbacks=[]
        )

        updater.dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
