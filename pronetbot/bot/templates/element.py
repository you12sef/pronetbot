from messengerapi.components import (
    Elements,
    Element,
    Buttons,
    Button,
    ButtonType,
)


class Menu:    
    def list_menu(menu: list) -> dict: 
        '''
        menu -> [
                    {('title1','subtitle1','image_url1'):{'button1':"button_type",'button2':"button_type"}}, 
                    {('title2','subtitle2','image_url2'):{'button1':"button_type"}}
                ]
        '''
        return Menu.get_menu(menu)
    
            
    def get_menu(menu):
        elements = Elements()
        
        for __menu__ in menu:
            buttons = list(__menu__.values())[0]
            data_of_menu = list(  list( __menu__.keys() )[0]  )
            if buttons:
                elements.add_element(Element(
                                                title=data_of_menu[0],
                                                subtitle=data_of_menu[1],
                                                image_url=data_of_menu[2],
                                                buttons=Menu.get_button(buttons),
                                                ).get_content())
            else:
                elements.add_element(Element(
                                                title=data_of_menu[0],
                                                subtitle=data_of_menu[1],
                                                image_url=data_of_menu[2],
                                                ).get_content())                
        return elements.get_content()


    def get_button(buttons:dict) -> dict:
        
        '''Creat Buttons
                buttons = {'button1':"button_type",'button2':"button_type"}
        
            to Creat Url Button
                buttons = {'button2':"url"}              
                !The link must start with http OR https!
                
            to creat phone number Button
                buttons = {'button2':"phone_number"}              
       
            set payload 
                buttons = {'button1':"payload",'button2':"button_type"}

                '''
            
        list_buttons = Buttons()
        
        for button,button_type in buttons.items():
            text = button
            if any(['http://'in button_type,'https://'in button_type]):
                link = button_type
                bu = Button(button_type=ButtonType.WEB_URL, title=text)
                bu.set_url(link)
                list_buttons.add_button(bu.get_content())
                
            elif button_type.startswith("+"):
                number = button_type
                bu = Button(button_type=ButtonType.PHONE_NUMPER,title=text)
                bu.set_phone_number(number)
                list_buttons.add_button(bu.get_content())
                    
            else :
                payload = button_type
                bu = Button(button_type=ButtonType.POSTBACK, title=text)
                bu.set_payload(payload)
                list_buttons.add_button(bu.get_content())
                
        return list_buttons.get_content()
    
    


