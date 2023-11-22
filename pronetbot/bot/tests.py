from templates.element import*
from messengerapi import SendApi
from messengerapi.messenger_profile_api import ProfileApi
from messengerapi.components import (QuickReplies,QuickReply,
                                     Buttons,Button)
from messengerapi.components import PersistentMenu,Elements,Elements
from messengerapi.constants import MessagingType,MessageTag,ButtonType,WebViewRatio,QuickReplyType
from config import*
from responses import response
import data


id = "6472442486117867"
send_api = SendApi(ACCESS_TOKEN,'107043698928404')
profile = ProfileApi(ACCESS_TOKEN)


#send_api.send_text_message('text', id)
image_url2 = 'https://cpmr-islands.org/wp-content/uploads/sites/4/2019/07/test.png'

#menu = Menu.get_menu([
#                    {('title1','subtitle1',image_url2):['button1<my_payload>']}, 
#                    {('title2','subtitle2',image_url2):['button1','button2']}
#                ])
'''
class a:
    def get():
        gree = ''
        welcome_screen =  [{"locale": "default", "text": f"مرحبا , {{user_first_name}} {gree} "}]
        profile.set_welcome_screen('start', welcome_screen)
        #print (a)
        return "DONE"
    def sas():
        return True

a.get()

class bot:
    
    def Constants():
        gree = ''
        welcome_screen =  [{"locale": "default", "text": f"مرحبا , {{user_first_name}} {gree} "}]
        profile.set_welcome_screen('start', welcome_screen)
        #persistent_menu_buttons = Menu.get_button(['القائمة الرئيسية<MENUs>'])
        #persistent_menu = PersistentMenu(persistent_menu_buttons).get_content()
        ############################################################
        #profile.set_welcome_screen('start',welcome_screen)
        #profile.set_persistent_menu(persistent_menu=persistent_menu)
        ############################################################
        return "DONE"
    
bot.Constants()
''' 
    
    
    
#prmenu = PersistentMenu(Menu.get_button(['القائمة الرئيسية<MENUs>'])).get_content()
#profile.set_persistent_menu(persistent_menu=prmenu)

#Menu.get_button(buttons=['1','1','2'])
#ss = response().postback_msg('<MENUs>')
#s = send_api.send_generic_message(ss,id,image_aspect_ratio="SQUARE")
#print (s)
#send_api.send_generic_message(menu,id,image_aspect_ratio="horizontal")
 
#send_api.mark_seen_message(id)

#d= send_api.typing_on_message(id)
#print (d)
#send_api.typing_off_message(id)


q = QuickReplies()
q1 = [QuickReply('1','<WWW>',content_type=QuickReplyType.TEXT).get_content()]
q2 = QuickReply(content_type=QuickReplyType.USER_PHONE_NUMBER,image_url=image_url2).get_content()
q3 = QuickReply(content_type=QuickReplyType.USER_EMAIL).get_content()
q.add_quick_reply(q1)
q.add_quick_reply(q2)
q.add_quick_reply(q3)
replies = q.get_content()

output = send_api.send_quick_replies('4',q1,id)

#output = send_api.send_generic_message(menu,id,quick_replies=replies)
print(output)

#output = send_api.send_quick_replies('send your phone number',replies,id)
#output = send_api.send_text_message('test',id,MessagingType.MESSAGE_TAG,tag=MessageTag.ACCOUNT_UPDATE  )
#print (output)
'''
b = Buttons()
b1 = Button(ButtonType.WEB_URL,'TEST')
#b1.set_phone_number('+218924482907')
b1.set_url("https://finch-resolved-indirectly.ngrok-free.app")
b1.set_webview(webview=WebViewRatio.COMPACT)
b.add_button(b1.get_content())
b = b.get_content()

c = Elements()
c1 = Element(image_url=image_url2)
c1.set_default_action_url(image_url2)

c.add_element(c1.get_content())
#c.get_content()
#c.add_element(Element(image_url=image_url2).get_content())
c = c.get_content()
'''
x= Menu.get_menu([
                
                {('LiteBeam 5AC','470$ LYD',image_url2):None},
                {('PowerBeam M5','590$ LYD',image_url2):None},
                {('PowerBeam 5AC','730$ LYD',image_url2):None},
                {(' ',' ',image_url2):{'الرجوع':'<MENUs>'}}
                
            ])
'''
output = send_api.send_generic_message(c,id)
print (output)

'''
