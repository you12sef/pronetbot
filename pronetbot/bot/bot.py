from config import ACCESS_TOKEN ,PAGE_ID
from messengerapi import SendApi
from messengerapi.components import PersistentMenu
from messengerapi.messenger_profile_api import ProfileApi
from templates.element import Menu
from responses import response

send = SendApi(ACCESS_TOKEN,PAGE_ID)
profile = ProfileApi(ACCESS_TOKEN)
res = response()

class bot:
    
    def Constants():
        welcome_screen =  [{"locale": "default", "text": f"مرحبا بكم في برونت"}]
        persistent_menu_buttons = Menu.get_button({'القائمة الرئيسية':'<MENUs>'})
        persistent_menu = PersistentMenu(persistent_menu_buttons).get_content()
        
        ############################################################
        profile.set_welcome_screen('<start_button>',welcome_screen)
        profile.set_persistent_menu(persistent_menu=persistent_menu)
        ############################################################
        
        return "DONE"

    def send_manage(data):

        id = data['id']
        text = data['text']
        type_ = data['type']
        payload = data['payload'] if 'payload' in data.keys() else None
        
        if type_ == 'text':
            send.typing_on_message(id)
            msg = res.txt_msg(text = text) 
            send.typing_off_message(id)   
            return send.send_text_message(msg,id)
            
        else:
            if payload:
                msg = res.postback_msg(payload)
                if 'button' in payload:
                    return send.send_buttons(msg[0],msg[1],id)
                else:
                    if type(msg) is tuple:
                        return send.send_generic_message(msg[0],id,"SQUARE",msg[1])
                    else:
                        return send.send_generic_message(msg,id,'SQUARE')

#bot.send_manage({'id': '6472442486117867', 'text': 'القائمة الرئيسية', 'type': 'postback', 'payload': '<maps>'})