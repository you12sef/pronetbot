from templates.element import Menu
from messengerapi.components import QuickReplies,QuickReply
from messengerapi.constants import QuickReplyType
from data import data 

class response():
    
    def __init__(self):
        self.__data__ = data
        self.__imageshost = 'https://iili.io/'
        self.__locationshost = 'https://maps.app.goo.gl/'

                    
    def __image_urls__(self):
        ihost = self.__imageshost
        return dict(
                    MENU = dict( 
                        TOWER = f'{ihost}JBZQwHG.jpg',
                        PROFILES = f'{ihost}JBZQhSs.jpg',
                        SUBSCRIBE = f'{ihost}JBZQNRf.jpg',
                        CONTACT = f'{ihost}JnvWUzJ.jpg',
                        SERVICE = f'{ihost}JBZQXln.jpg'),
                    
                    TOWERS = dict(
                        SOQ_ALJOMA = f'{ihost}JBtBlOQ.jpg',
                        MONEDER = f'{ihost}JnvX1rN.jpg',
                        FORNAJ = f'{ihost}JBtB7Ub.jpg',
                        AIN_ZARA = f'{ihost}JBtBaJj.jpg',
                        ZAWIA = f'{ihost}JBtBc5x.jpg'
                        ),
                    
                    PROFILES = dict(
                        LIMIT = f'{ihost}JnvL3PV.jpg',
                        UNLIMIT = f'{ihost}JnvL2MQ.jpg',
                        
                        LIMIT_ = dict(
                            PRO4 = f'{ihost}JCdYnIf.md.jpg',
                            PRO6 = f'{ihost}JCdS0Zv.jpg',
                            PRO8 = f'{ihost}JCdSGGp.md.jpg',
                            PRO10 = f'{ihost}JCdSEnR.md.jpg',
                            PRO12= f'{ihost}JCdSlwJ.jpg'
                         
                            ),
                        UNLIMIT_ = dict(
                            PRO06 = f'{ihost}Jn4qTF4.jpg',
                            PRO08 = f'{ihost}Jn4qxMG.jpg',
                            PRO010 = f'{ihost}Jn4qzPf.jpg',
                            PRO012 = f'{ihost}Jn4qucl.jpg'
                            )
                         ),
                    SUBSCRIBES = dict(
                        LITE = f'{ihost}Jn4Q1Q1.md.jpg',
                        POWERAC = f'{ihost}Jn4NXDl.jpg',
                        POWERM5 = f'{ihost}Jn4weyv.md.jpg'
                    ),
                    
                    icons = dict(
                        BACK = f'{ihost}JBt5zP4.jpg',
                        test = 'https://cpmr-islands.org/wp-content/uploads/sites/4/2019/07/test.png',
                    )
        )
        
    def ___towers_locations__(self):
        lhost = self.__locationshost
        return dict(
                    SOQ_ALJOMA = f'{lhost}6BF6oC9y5wsJ9CxN9',
                    MONEDER = f'{lhost}JMsPwVUBzexTKj3W7',
                    FORNAJ = f'{lhost}m8FnqbTQYQYrdbor6',
                    AIN_ZARA = f'{lhost}yRYSDZBcBacurCuE7',
                    ZAWIA = f'{lhost}WVcdTBmvKbjUuoXB9'
        )
        
        
    def txt_msg(self,text: str) -> str:
        match text:
            case text if text in self.__data__.__greetingone__():
                return "وعليكم السلام"

            case text if text in self.__data__.__greetingtwo__():
                return "مرحبا ,تفضل"


    def postback_msg(self,payload) -> dict:
        icons = response.__image_urls__(self)['icons']
        menu = response.__image_urls__(self)['MENU']
        towers = response.__image_urls__(self)['TOWERS']
        profiles = response.__image_urls__(self)['PROFILES']
        subs = response.__image_urls__(self)['SUBSCRIBES']
        limit = response.__image_urls__(self)['PROFILES']['LIMIT_']
        unlimit = response.__image_urls__(self)['PROFILES']['UNLIMIT_']
        
        locations = response.___towers_locations__(self)
        
        
        match payload:
                    
            case '<start_button>':
                return ['سنحاول الرد عليك في أقرب وقت ممكن ,في الؤقت الحالي سيساعدك الرد الألي في الاستفسار عن أبرز الأشياء',
                        
                    Menu.get_button({'عرض القوائم':'<MENUs>'})
                        
                        ]
            
            case '<MENUs>':
                return Menu.list_menu([
                    
                {('مواقع الأبراج','أعرف الأبراج القريبة منك',menu['TOWER']):{'عرض المواقع':'<maps>','أقرب برج ليك':'<location>'}}, 
                {('أسعار الباقات','أعرف أسعار الباقات اللي تناسبك',menu['PROFILES']):{'عرض الأسعار':'<profiles>'}},
                {('الاشتراك مع برونت',' أسعار الاشتراكات',menu['SUBSCRIBE']):{'عرض':'<sub>'}},
                {('اتصل بنا',' ',menu['CONTACT']):{'اتصل بالرقم الأول':'+218929368000','اتصل بالرقم الثاني':'+218929378000'}},
                {('للمشتركين','عرض خدمات المشتركين',menu['SERVICE']):{'عرض':'<user_button>'}}
                
            ])
            
            case '<maps>':
                return Menu.list_menu([

                {('برج سوق الجمعة','سيمافرو ولاد الحاج بجانب سوق العاشوري',towers['SOQ_ALJOMA']):{'أعرض على الخريطة':locations['SOQ_ALJOMA']}}, 
                {('برج سيدي منيذر','وسط البلاد',towers['MONEDER']):{'أعرض على الخريطة':locations['MONEDER']}},
                {('برج الفرناح','نهاية شارع الغاز',towers['FORNAJ']):{'أعرض على الخريطة':locations['FORNAJ']}},
                {('برج عين زارة','بالقرب من مدرسة بن حيان',towers['AIN_ZARA']):{'أعرض على الخريطة':locations['AIN_ZARA']}},
                {('برج الزاوبة','شارع جمال عبدالناصر',towers['ZAWIA']):{'أعرض على الخريطة':locations['ZAWIA']}},

            ]),[QuickReply('الرجوع','<MENUs>',icons['BACK'],QuickReplyType.TEXT).get_content()]
                
                
            case '<profiles>':
                return Menu.list_menu([

                {('الباقات المحدودة','',profiles['LIMIT']):{'عرض':'<limit>'}},
                {('الباقات الغير محدودة','',profiles['UNLIMIT']):{'عرض':'<unlimit>'}},
            ]),[QuickReply('الرجوع','<MENUs>',icons['BACK'],QuickReplyType.TEXT).get_content()]
                
            case '<unlimit>':
                return Menu.list_menu([

                {(' ','باقة 4 ميقا',limit['PRO4']):{'التفاصيل':'<l_button4>'}},
                {(' ','باقة 6 ميقا',limit['PRO6']):{'التفاصيل':'<l_button6>'}},
                {(' ','باقة 8 ميقا',limit['PRO8']):{'التفاصيل':'<l_button8>'}},
                {(' ','باقة 10 ميقا',limit['PRO10']):{'التفاصيل':'<l_button10>'}},
                {(' ','باقة 12 ميقا',limit['PRO12']):{'التفاصيل':'<l_button12>'}},
            ]),[QuickReply('الرجوع','<profiles>',icons['BACK'],QuickReplyType.TEXT).get_content()]

            case '<limit>':
                return Menu.list_menu([
                {(' ','باقة 45 جيجا',unlimit['PRO06']):{'التفاصيل':'<l_button06>'}},
                {(' ','باقة 90 جيجا',unlimit['PRO08']):{'التفاصيل':'<l_button08>'}},
                {(' ','باقة 150 جيجا',unlimit['PRO010']):{'التفاصيل':'<l_button010>'}},
                {(' ','باقة 400 جيجا',unlimit['PRO012']):{'التفاصيل':'<l_button012>'}},                    
            ]),[QuickReply('الرجوع','<profiles>',icons['BACK'],QuickReplyType.TEXT).get_content()]
                
            
            case '<l_button4>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 4Mb
سرعة الرفع : 4Mb
سعر الباقة : 50 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button6>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 6Mb
سرعة الرفع : 6Mb
سعر الباقة : 75 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button8>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 8Mb
سرعة الرفع : 8Mb
سعر الباقة : 95 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button10>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 10Mb
سرعة الرفع : 10Mb
سعر الباقة : 120 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button12>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 12Mb
سرعة الرفع : 12Mb
سعر الباقة : 150 دينار''',Menu.get_button({'الرجوع':'<limit>'})

################################################################
            case '<l_button06>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 6Mb
سرعة الرفع : 6Mb
سعة الباقة : 45GB
سعر الباقة : 30 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button08>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 8Mb
سرعة الرفع : 8Mb
سعة الباقة : 90GB
سعر الباقة : 60 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button010>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 10Mb
سرعة الرفع : 10Mb
سعة الباقة : 150GB
سعر الباقة : 110 دينار''',Menu.get_button({'الرجوع':'<limit>'})

            case '<l_button012>':
                return '''مدة الباقة : 30 يوم
سرعة التحميل : 12Mb
سرعة الرفع : 12Mb
سعة الباقة : 400GB
سعر الباقة : 130 دينار''',Menu.get_button({'الرجوع':'<limit>'})


            case '<sub>':
                return Menu.get_menu([
                
                {('LiteBeam 5AC','السعر غير متوفر في الوقت الحالي',subs['LITE']):None},
                {('PowerBeam M5','السعر غير متوفر في الوقت الحالي',subs['POWERAC']):None},
                {('PowerBeam 5AC','السعر غير متوفر في الوقت الحالي',subs['POWERM5']):None},
                
            ]),[QuickReply('الرجوع','<MENUs>',icons['BACK'],QuickReplyType.TEXT).get_content()]

            
            case '<user_button>':
                return 'خدمات المشتركين',Menu.get_button({'صفحة تعبئة الرصيد':'http://my.pro-net.ly',
                                            'الرجوع':'<MENUs>'})


