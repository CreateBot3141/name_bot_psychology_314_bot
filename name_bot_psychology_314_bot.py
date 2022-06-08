
def summ_p (emotional_exhaustion,depersonalization,reduction_of_professionalism):
    import math
    p = ((emotional_exhaustion/54)**2 +(depersonalization/30)**2+(1-(reduction_of_professionalism/48))**2)/3
    p = math.sqrt(p)
    return p


def null_all (message_in):
    message_out = message_in
    message_out = message_out.replace ("add_answer31_1_","")
    message_out = message_out.replace ("add_answer31_2_","")
    message_out = message_out.replace ("add_answer31_3_","")
    message_out = message_out.replace ("add_answer31_4_","")
    message_out = message_out.replace ("add_answer31_5_","")
    message_out = message_out.replace ("add_answer31_6_","")
    message_out = message_out.replace ("add_answer31_7_","")
    message_out = message_out.replace ("add_answer31_8_","")
    message_out = message_out.replace ("add_answer31_9_","")

    message_out = message_out.replace ("add_answer32_1_","")
    message_out = message_out.replace ("add_answer32_2_","")
    message_out = message_out.replace ("add_answer32_3_","")
    message_out = message_out.replace ("add_answer32_4_","")
    message_out = message_out.replace ("add_answer32_5_","")
    message_out = message_out.replace ("add_answer32_6_","")
    message_out = message_out.replace ("add_answer32_7_","")
    message_out = message_out.replace ("add_answer32_8_","")
    message_out = message_out.replace ("add_answer32_9_","")

    return message_out

def summ_emotions (namebot,user_id,points):
    emotional_exhaustion            = 0
    depersonalization               = 0
    reduction_of_professionalism    = 0
    emotional_exhaustion = points[0]+points[1]+points[2]+points[3]+points[7]+points[12]+points[13]+points[15]+points[19]
    ### 1, 2, 3, 6, 8, 13, 14, 16, 20
    depersonalization    = points[4]+points[9]+points[10]+points[14]+points[21]
    ### 5, 10, 11, 15, 22
    reduction_of_professionalism    = points[3]+points[6]+points[8]+points[11]+points[16]+points[17]+points[18]+points[20]
    ### 4, 7, 9, 12, 17, 18, 19, 21
    print ('[+] emotional_exhaustion:',emotional_exhaustion)
    print ('[+] depersonalization:',depersonalization)
    print ('[+] reduction_of_professionalism:',reduction_of_professionalism)
    return emotional_exhaustion,depersonalization,reduction_of_professionalism

def calculation_01_test (namebot,user_id):    
    print ('[+] Подсчет очков первого теста')
    import iz_telegram
    points = ['','','','','','','','','','','','','','','','','','','','','',''] 
    #answer = ['','','','','','','','','','','','','','','','','','','','','',''] 
    for number in range(22):
        answer = iz_telegram.load_variable (user_id,namebot,'answer'+str(number))
        if number == 5:            
            if answer == 'add_test_1_Никогда_'+str(number):
                points[number] = 6

            if answer == 'add_test_1_Очень  редко_'+str(number):
                points[number] = 5        
            if answer == 'add_test_1_Редко_'+str(number):
                points[number] = 4                
            if answer == 'add_test_1_Иногда_'+str(number):
                points[number] = 3                
            if answer == 'add_test_1_Часто_'+str(number):
                points[number] = 2                
            if answer == 'add_test_1_Очень часто_'+str(number):    
                points[number] = 1                
            if answer == 'add_test_1_Ежедневно_'+str(number): 
                points[number] = 0        
        else:
            if answer == 'add_test_1_Никогда_'+str(number):
                points[number] = 0
            if answer == 'add_test_1_Очень редко_'+str(number):
                points[number] = 1        
            if answer == 'add_test_1_Редко_'+str(number):
                points[number] = 2                
            if answer == 'add_test_1_Иногда_'+str(number):
                points[number] = 3                
            if answer == 'add_test_1_Часто_'+str(number):
                points[number] = 4                
            if answer == 'add_test_1_Очень часто_'+str(number):    
                points[number] = 5                
            if answer == 'add_test_1_Ежедневно_'+str(number): 
                points[number] = 6        
        print ('    [+]',number,answer,points[number])
    print ('[+] Список набранных балов:',points)
    return points

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram
    import time
    label = 'send'
    
    if message_in == '/start':  
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in == 'Пройти тест':
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ''

    if message_in == '/create':
        access_code = iz_telegram.create_access_code (namebot)
        message_out,menu = iz_telegram.get_message (user_id,'Генерация пароля',namebot)
        message_out = message_out.replace('%%Уникальный код%%',str(access_code))
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        active    = 'Активный'
        key_kod   = access_code 
        name      = 'Доступ на рассылку'
        plans     = 'Тариф пробный'
        quantity  = 1
        iz_telegram.save_access_code (active,key_kod,name,namebot,plans,quantity)

    if message_in == '/master':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Два пути','S',0) 

    if message_in == '/test01' or message_in == 'Выявление причин выгорания Старт':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Тест на профориентацию','S',0) 

    if message_in == '/test02' or message_in == 'Тест Старт':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Тест на организационные причины','S',0) 

    if message_in == '/test03' or message_in == 'Тест Старт3':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Тест Колесо баланса жизни','S',0) 

    if message_in == 'Тест Старт33':
        message_out,menu = iz_telegram.get_message (user_id,'Тест3_Вопрос_1',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        message_out,menu = iz_telegram.get_message (user_id,'Я сейчас',namebot)
        list = [['answer31_1_1','-1-'],
                ['answer31_1_2','-2-'],
                ['answer31_1_3','-3-'],
                ['answer31_1_4','-4-'],
                ['answer31_1_5','-5-'],
                ['answer31_1_6','-6-'],
                ['answer31_1_7','-7-'],
                ['answer31_1_8','-8-'],
                ['answer31_1_9','-9-'],
                ['answer31_1_10','-10-']                
               ]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
         
    if message_in.find ('answer31_') != -1:
        word = message_in
        word = word.replace('add_answer31_','')
        word = word.replace('_1','')
        word = word.replace('_2','')
        word = word.replace('_3','')
        word = word.replace('_4','')
        word = word.replace('_5','')
        word = word.replace('_6','')
        word = word.replace('_7','')
        word = word.replace('_8','')
        word = word.replace('_9','')
        word = word.replace('_10','')
        iz_telegram.save_variable (user_id,namebot,"Test_31_"+str(word),message_in)
        message_out,menu = iz_telegram.get_message (user_id,'Я хочу',namebot)
        list = [['answer32_'+str(word)+'_1','-1-'],
                ['answer32_'+str(word)+'_2','-2-'],
                ['answer32_'+str(word)+'_3','-3-'],
                ['answer32_'+str(word)+'_4','-4-'],
                ['answer32_'+str(word)+'_5','-5-'],
                ['answer32_'+str(word)+'_6','-6-'],
                ['answer32_'+str(word)+'_7','-7-'],
                ['answer32_'+str(word)+'_8','-8-'],
                ['answer32_'+str(word)+'_9','-9-'],
                ['answer32_'+str(word)+'_10','-10-']                
               ]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in.find ('add_answer32_')  != -1:
        word = message_in 
        word = word.replace('add_answer32_','')
        word = word.replace('_1','')
        word = word.replace('_2','')
        word = word.replace('_3','')
        word = word.replace('_4','')
        word = word.replace('_5','')
        word = word.replace('_6','')
        word = word.replace('_7','')
        word = word.replace('_8','')
        word = word.replace('_9','')
        word = word.replace('_10','')
        iz_telegram.save_variable (user_id,namebot,"Test_32_"+str(word),message_in)
        nomer = int (word)        
        nomer = nomer + 1
        if nomer < 9:
            message_out,menu = iz_telegram.get_message (user_id,'Тест3_Вопрос_'+str(nomer),namebot)
            markup = ''
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
            message_out,menu = iz_telegram.get_message (user_id,'Я сейчас',namebot)
            list = [['answer31_'+str(nomer)+'_1','-1-'],
                    ['answer31_'+str(nomer)+'_2','-2-'],
                    ['answer31_'+str(nomer)+'_3','-3-'],
                    ['answer31_'+str(nomer)+'_4','-4-'],
                    ['answer31_'+str(nomer)+'_5','-5-'],
                    ['answer31_'+str(nomer)+'_6','-6-'],
                    ['answer31_'+str(nomer)+'_7','-7-'],
                    ['answer31_'+str(nomer)+'_8','-8-'],
                    ['answer31_'+str(nomer)+'_9','-9-'],
                    ['answer31_'+str(nomer)+'_10','-10-']                
                   ]
            markup = iz_telegram.simple_menu (user_id,namebot,list)
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        else:
            #message_out,menu = iz_telegram.get_message (user_id,'Итоги теста 3',namebot)
            #list = [['next0033_','Продолжить']]
            #markup = iz_telegram.simple_menu (user_id,namebot,list)            
            #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Итоги теста 3','S',0)

    if message_in == 'Итоги теста 3 ответы':


        #message_out = message_out.replace("A","")
        #message_out = message_out.replace("A","")
        Test_31_1 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_1'))
        Test_31_2 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_2'))
        Test_31_3 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_3'))
        Test_31_4 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_4'))
        Test_31_5 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_5'))
        Test_31_6 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_6'))
        Test_31_7 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_7'))
        Test_31_8 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_8'))
        Test_31_9 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_31_9'))

        Test_32_1 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_1'))
        Test_32_2 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_2'))
        Test_32_3 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_3'))
        Test_32_4 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_4'))
        Test_32_5 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_5'))
        Test_32_6 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_6'))
        Test_32_7 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_7'))
        Test_32_8 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_8'))
        Test_32_9 = null_all (iz_telegram.load_variable (user_id,namebot,'Test_32_9'))




        message_out,menu = iz_telegram.get_message (user_id,'Колесо судьбы',namebot)
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Колесо судьбы','S',0)

        message_out = message_out.replace("%%Ответ11%%",str(Test_31_1))
        message_out = message_out.replace("%%Ответ12%%",str(Test_31_2))
        message_out = message_out.replace("%%Ответ13%%",str(Test_31_3))
        message_out = message_out.replace("%%Ответ14%%",str(Test_31_4))
        message_out = message_out.replace("%%Ответ15%%",str(Test_31_5))
        message_out = message_out.replace("%%Ответ16%%",str(Test_31_6))
        message_out = message_out.replace("%%Ответ17%%",str(Test_31_7))
        message_out = message_out.replace("%%Ответ18%%",str(Test_31_8))
        message_out = message_out.replace("%%Ответ19%%",str(Test_31_9))

        message_out = message_out.replace("%%Ответ21%%",str(Test_32_1))
        message_out = message_out.replace("%%Ответ22%%",str(Test_32_2))
        message_out = message_out.replace("%%Ответ23%%",str(Test_32_3))
        message_out = message_out.replace("%%Ответ24%%",str(Test_32_4))
        message_out = message_out.replace("%%Ответ25%%",str(Test_32_5))
        message_out = message_out.replace("%%Ответ26%%",str(Test_32_6))
        message_out = message_out.replace("%%Ответ27%%",str(Test_32_7))
        message_out = message_out.replace("%%Ответ28%%",str(Test_32_8))
        message_out = message_out.replace("%%Ответ29%%",str(Test_32_9))
        



        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
     
    if message_in == 'Готов2':
        message_out,menu = iz_telegram.get_message (user_id,'Тест2_Вопрос_1',namebot)
        list = [['answer2_Очень редко_1','Очень редко'],
                ['answer2_Никогда_1','Никогда'],
                ['answer2_Довольно_1 редко','Довольно редко'],
                ['answer2_Иногда_1','Иногда'],
                ['answer2_Довольно часто_1','Довольно часто'],
                ['answer2_Очень часто_1','Очень часто'],
                ['answer2_Всегда_1','Всегда']
               ]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 

    if message_in.find('add_answer2_') != -1:
        nm = message_in
        nm = nm.replace('add_answer2_Очень редко_',str(''))
        nm = nm.replace('add_answer2_Никогда_',str(''))
        nm = nm.replace('add_answer2_Довольно редко_',str(''))
        nm = nm.replace('add_answer2_Иногда_',str(''))
        nm = nm.replace('add_answer2_Довольно часто_',str(''))
        nm = nm.replace('add_answer2_Очень часто_',str(''))
        nm = nm.replace('add_answer2_Всегда_',str(''))
        iz_telegram.save_variable (user_id,namebot,'answer2'+str(nm),message_in)      
        print ('[+] nm',nm)
        nm = int(nm)+1
        message_out,menu = iz_telegram.get_message (user_id,'Тест2_Вопрос_'+str(nm),namebot)
        list = [['answer2_Очень редко_'+str(nm),'Очень редко'],
                ['answer2_Никогда_'+str(nm),'Никогда'],
                ['answer2_Довольно редко_'+str(nm),'Довольно редко'],
                ['answer2_Иногда_'+str(nm),'Иногда'],
                ['answer2_Довольно часто_'+str(nm),'Довольно часто'],
                ['answer2_Очень часто_'+str(nm),'Очень часто'],
                ['answer2_Всегда_'+str(nm),'Всегда']
               ]
        ### add_answer2_Довольно редко_6
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 

    if message_in.find('add_answer2_') != -1 and message_in.find('_31') != -1:
        message_out,menu = iz_telegram.get_message (user_id,'Подсчет итогов2',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        answer = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',0] 
        ask1 = [1,2,3,4,5,6,7,8,9,10,14,15,16]
        ball = 0
        for number in range(31):
            number = number + 1
            answer = iz_telegram.load_variable (user_id,namebot,'answer2'+str(number))
            ball = 0
            sl = answer
            sl = sl.replace('_10','')
            sl = sl.replace('_11','')
            sl = sl.replace('_12','')
            sl = sl.replace('_13','')
            sl = sl.replace('_14','')
            sl = sl.replace('_15','')
            sl = sl.replace('_16','')
            sl = sl.replace('_17','')
            sl = sl.replace('_18','')
            sl = sl.replace('_19','')
            sl = sl.replace('_20','')
            sl = sl.replace('_21','')
            sl = sl.replace('_22','')
            sl = sl.replace('_23','')
            sl = sl.replace('_24','')
            sl = sl.replace('_25','')
            sl = sl.replace('_26','')
            sl = sl.replace('_27','')
            sl = sl.replace('_28','')
            sl = sl.replace('_29','')
            sl = sl.replace('_30','')
            sl = sl.replace('_31','')
            sl = sl.replace('_1','')
            sl = sl.replace('_2','')
            sl = sl.replace('_3','')
            sl = sl.replace('_4','')
            sl = sl.replace('_5','')
            sl = sl.replace('_6','')
            sl = sl.replace('_7','')
            sl = sl.replace('_8','')
            sl = sl.replace('_9','')
             
            lb = 'No' 
            for k in ask1:
                if k == number:
                    lb = 'Yes'
            if lb == 'Yes':
                if sl == 'add_answer2_Очень редко':
                    ball = 1
                if sl == 'add_answer2_Никогда':
                    ball = 1
                if sl == 'add_answer2_Довольно редко':
                    ball = 2
                if sl == 'add_answer2_Иногда':
                    ball = 3
                if sl == 'add_answer2_Довольно часто':
                    ball = 4
                if sl == 'add_answer2_Очень часто':
                    ball = 5
                if sl == 'add_answer2_Всегда':
                    ball = 5 
            else:        
                if sl == 'add_answer2_Очень редко':
                    ball = 5
                if sl == 'add_answer2_Никогда':
                    ball = 5
                if sl == 'add_answer2_Довольно редко':
                    ball = 4
                if sl == 'add_answer2_Иногда':
                    ball = 3
                if sl == 'add_answer2_Довольно часто':
                    ball = 2
                if sl == 'add_answer2_Очень часто':
                    ball = 1
                if sl == 'add_answer2_Всегда':
                    ball = 1                 
            print ('[+]',number,sl,ball)
            points[number] = ball

        Job_loading                         = (points[1]+points[2]+points[3]+points[4])/20
        Decision_making                     = (points[5]+points[7]+points[6]+points[8])/20
        Complexity_of_the_work_performed    = (points[9]+points[10]+points[15])/15
        Clarity_of_responsibilities         = (points[11]+points[12]+points[13]+points[16])/20
        Freedom_of_choice                   = (points[14]+points[17]+points[18]+points[19]+points[20]+points[21]+points[22]+points[23]+points[24])/45
        Support_of_colleagues               = (points[28]+points[31]+points[32])/15
        Management_support                  = (points[29]+points[30])/10
        Satisfaction_with_the_results_of_work = (points[25]+points[26]+points[27])/15
        message_out,menu = iz_telegram.get_message (user_id,'Итог 02',namebot)
        markup = ''
        message_out = message_out.replace('%%Job_loading%%',str(Job_loading))
        message_out = message_out.replace('%%Decision_making%%',str(Decision_making))
        message_out = message_out.replace('%%Complexity_of_the_work_performed%%',str(Complexity_of_the_work_performed))
        message_out = message_out.replace('%%Clarity_of_responsibilities%%',str(Clarity_of_responsibilities))
        message_out = message_out.replace('%%Freedom_of_choice%%',str(Freedom_of_choice))
        message_out = message_out.replace('%%Support_of_colleagues%%',str(Support_of_colleagues))
        message_out = message_out.replace('%%Management_support%%',str(Management_support))
        message_out = message_out.replace('%%Satisfaction_with_the_results_of_work%%',str(Satisfaction_with_the_results_of_work))
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        message_out,menu = iz_telegram.get_message (user_id,'Запуск тест 3',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == 'Готов':
        message_out,menu = iz_telegram.get_message (user_id,'Выбор профессии',namebot)
        list = [['answer_A0','Инженер-технолог'],['answer_B0','Инженер-конструктор']]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 

    if message_in.find('add_answer_') != -1:
        word = message_in 
        word = word.replace("add_answer_","")
        word = word.replace("A","")
        word = word.replace("B","")
        message_out,menu = iz_telegram.get_message (user_id,'Выбор профессии',namebot)
        list = [['Электрорадиотехнолог','Врач-терапевт'],
                ['Авиаоператор','Программист-кодировщик'],
                ['Фотограф','Менеджер по продажам'],
                ['Спасатель МЧС','Дизайнер'],
                ['Политолог','Психиатр'],
                ['Ученый химик','Бухгалтер'],
                ['Философ','Частный предприниматель'],
                ['Лингвист-переводчик','Модельер'],
                ['Инспектор службы занятости населения','Системный аналитик'],
                ['Социальный педагог','Биржевой маклер'],
                ['Тренер','Искусствовед'],
                ['Нотариус','Руководитель компании'],
                ['Перфораторщик','Художник'],
                ['Лидер политической партии/общественной организации','Копирайтер'],
                ['Закройщик','Метеоролог'],
                ['Водитель','Журналист'],
                ['Чертежник','Риелтор'],
                ['Специалист по ремонту компьютеров и электронных приборов','Секретарь-референт'],
                ['Микробиолог','Психолог'],
                ['Видеооператор','Режиссер'],
                ['Экономист','Провизор'],
                ['Ветеринар','Инженер'],
                ['Программист-тестировщик','Архитектор'],
                ['Работник инспекции по делам несовершеннолетних','Торговый представитель'],
                ['Преподаватель','Биржевой брокер'],
                ['Воспитатель','Декоратор'],
                ['Реставратор','Зав. отделом предприятия'],
                ['Корректор','Литератор и кинокритик'],
                ['Фермер','Визажист'],
                ['Парикмахер','Социолог'],
                ['Экспедитор','Редактор'],
                ['Ветеринар','Финансовый директор'],
                ['Автомеханик','Стилист'],
                ['Археолог','Эксперт'],
                ['Библиограф','Корреспондент'],
                ['Эколог','Актер'],
                ['Логопед','Контроллер'],
                ['Адвокат','Директор ООО'],
                ['Кассир','Продюсер'],
                ['Поэт, писатель','Продавец'],
                ['Криминалист','Композитор'],
                ]
        if int(word) >= 0 and int(word) <= 40:
            #word    = 40
            A       = 'A'+str(int(word)+1)
            B       = 'B'+str(int(word)+1)
            nameA   = list[int(word)][0]
            nameB   = list[int(word)][1]
            list = [['answer_'+str(A),nameA],['answer_'+str(B),nameB]]
            markup = iz_telegram.simple_menu (user_id,namebot,list)
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
            iz_telegram.save_variable (user_id,namebot,"TEST_"+str(word),message_in)
        else:
            iz_telegram.save_variable (user_id,namebot,"TEST_"+str(word),message_in)
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Нет данных','S',0)  
            tab01 = ['1A','2A','3A','4A','5A','16A','17A','19A','21A','28A','31A','32A','33A','34A'] 
            tab02 = ['1B','6A','7A','8A','9A','16B','20A','22A','23A','24A','31B','35A','36A','37A']
            tab03 = ['2B','6B','10A','11A','12A','17B','20B','25A','26A','27A','36B','38A','39A','41B']
            tab04 = ['3B','7B','10B','13A','14A','18A','19B','22B','29A','32B','35B','38B','40A','42A']
            tab05 = ['4B','8B','11B','13B','15A','18B','23B','25B','26B','28B','30A','33B','39B','40B']
            tab06 = ['5B','9B','12B','14B','15B','21B','24B','27B','29B','30B','34B','37B','41A','42B']
            sum_tab01 = 0
            sum_tab02 = 0
            sum_tab03 = 0
            sum_tab04 = 0
            sum_tab05 = 0
            sum_tab06 = 0
            for number in range(40): 
                st = iz_telegram.load_variable (user_id,namebot,"TEST_"+str(number))
                st_liter = ''
                st_nomer = 0
                if st.find('add_answer_B') != -1:
                    st_liter = 'B'
                if st.find('add_answer_A') != -1:
                    st_liter = 'A'
                st_nomer = st
                st_nomer = st_nomer.replace("add_answer_A","")
                st_nomer = st_nomer.replace("add_answer_B","")
                sm = str(int(st_nomer)+1)+st_liter
                for line in tab01:
                    if line == sm:
                        sum_tab01 = sum_tab01 + 1
                for line in tab02:
                    if line == sm:
                        sum_tab02 = sum_tab02 + 1
                for line in tab03:
                    if line == sm:
                        sum_tab03 = sum_tab03 + 1
                for line in tab04:
                    if line == sm:
                        sum_tab04 = sum_tab04 + 1
                for line in tab05:
                    if line == sm:
                        sum_tab05 = sum_tab05 + 1
                for line in tab06:
                    if line == sm:
                        sum_tab06 = sum_tab06 + 1
            message_out,menu = iz_telegram.get_message (user_id,'Ответы на первый тест',namebot)
            markup = ''
            message_out = message_out.replace('%%Реалистический%%',str(sum_tab01))
            message_out = message_out.replace('%%Исследовательский%%',str(sum_tab02))
            message_out = message_out.replace('%%Социальный%%',str(sum_tab03))
            message_out = message_out.replace('%%Конвенциальный%%',str(sum_tab04))
            message_out = message_out.replace('%%Предпринимательский%%',str(sum_tab05))
            message_out = message_out.replace('%%Артистический%%',str(sum_tab06))
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 

    if message_in == 'Погнали дальше':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Погнали дальше сообщение','S',0) 

    if message_in == 'Я согласен' or message_in == '/fio':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Напиши свое ФИО','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Напиши свое ФИО')
        status = ''

    if status == 'Напиши свое ФИО' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Выбери свой пол','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Выбери свой пол')
        iz_telegram.save_active_user (namebot,user_id,FIO = message_in)

    if status == 'Выбери свой пол' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Напиши свой возраст','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Напиши свой возраст')
        iz_telegram.save_active_user (namebot,user_id,sex = message_in)

    if status == 'Напиши свой возраст' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Профессия / Роль в компании','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Профессия / Роль в компании')
        iz_telegram.save_active_user (namebot,user_id,age = message_in)

    if status == 'Профессия / Роль в компании' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Сфера деятельности компании','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Сфера деятельности компании')
        iz_telegram.save_active_user (namebot,user_id,profession = message_in)

    if status == 'Сфера деятельности компании' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Стаж на последнем месте работы','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Стаж на последнем месте работы')
        iz_telegram.save_active_user (namebot,user_id,company = message_in)

    if status == 'Стаж на последнем месте работы' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Часовой пояс','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'Часовой пояс')
        iz_telegram.save_active_user (namebot,user_id,experience = message_in)

    if status == 'Часовой пояс' :
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Приятно познакомиться','S',0) 
        iz_telegram.save_variable (user_id,namebot,"status",'')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Выявление причин выгорания','S',0) 
        iz_telegram.save_active_user (namebot,user_id,time_zone = message_in)

    if status == 'Ввод имени' :
        language  = ''
        login     = message_in
        project   = ''
        summ      = 0
        system    = ''
        wallet    = ''
        komment   = ''
        adress    = ''
        telefon   = ''
        iz_telegram.save_active_user (namebot,user_id)
        message_in = 'Укажите электронную почту'
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод почты')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,message_in,'S',0) 

    if status == 'Ввод почты' :
        language  = ''
        login     = ''
        project   = ''
        summ      = 0
        system    = ''
        wallet    = ''
        komment   = ''
        adress    = message_in
        telefon   = ''
        iz_telegram.save_active_user (namebot,user_id)        
        message_in = 'Спасибо за регистрацию'
        iz_telegram.save_variable (user_id,namebot,"status",'')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,message_in,'S',0) 

    if message_in == 'Начать' or message_in == '/test00':
        #message_out,menu = iz_telegram.get_message (user_id,'Начало теста',namebot)
        markup = ''
        nm     = 0
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        for number in range(22):
            iz_telegram.save_variable (user_id,namebot,'answer'+str(nm),'')        
            nm = int(nm)+1            
        message_out,menu = iz_telegram.get_message (user_id,'Вопрос № 0',namebot)
        list = [['test_1_Никогда_0','Никогда'],['test_1_Очень редко_0','Очень редко'],['test_1_Редко_0','Редко'],['test_1_Иногда_0','Иногда'],['test_1_Часто_0','Часто'],['test_1_Очень часто_0','Очень часто'],['test_1_Ежедневно_0','Ежедневно']]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in.find('add_test_1_') != -1:
        nm = message_in
        nm = nm.replace('add_test_1_Никогда_',str(''))
        nm = nm.replace('add_test_1_Очень редко_',str(''))
        nm = nm.replace('add_test_1_Редко_',str(''))
        nm = nm.replace('add_test_1_Иногда_',str(''))
        nm = nm.replace('add_test_1_Часто_',str(''))
        nm = nm.replace('add_test_1_Очень часто_',str(''))
        nm = nm.replace('add_test_1_Ежедневно_',str(''))
        iz_telegram.save_variable (user_id,namebot,'answer'+str(nm),message_in)        
        nm = int(nm)+1
        message_out,menu = iz_telegram.get_message (user_id,'Вопрос № '+str(nm),namebot)
        list = [['test_1_Никогда_'+str(nm),'Никогда'],['test_1_Очень редко_'+str(nm),'Очень редко'],['test_1_Редко_'+str(nm),'Редко'],['test_1_Иногда_'+str(nm),'Иногда'],['test_1_Часто_'+str(nm),'Часто'],['test_1_Очень часто_'+str(nm),'Очень часто'],['test_1_Ежедневно_'+str(nm),'Ежедневно']]
        markup = iz_telegram.simple_menu (user_id,namebot,list)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 

    if message_in.find('add_test_') != -1 and message_in.find('_21') != -1:
        message_out,menu = iz_telegram.get_message (user_id,'Подсчет итогов',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id) 
        iz_telegram.save_variable (user_id,namebot,'answer21',message_in)
        points = calculation_01_test (namebot,user_id)
        emotional_exhaustion,depersonalization,reduction_of_professionalism = summ_emotions (namebot,user_id,points)
        message_out,menu = iz_telegram.get_message (user_id,'Вывод итогов',namebot)
        message_out = message_out.replace('%%emotional_exhaustion%%',str(emotional_exhaustion))
        message_out = message_out.replace('%%depersonalization%%',str(depersonalization))
        message_out = message_out.replace('%%reduction_of_professionalism%%',str(reduction_of_professionalism))
        emotional_exhaustion_status         = ''
        depersonalization_status            = ''
        reduction_of_professionalism_status = ''

        if emotional_exhaustion >= 0 and emotional_exhaustion <= 15:
            emotional_exhaustion_status = 'Низкий уровень L'
        if emotional_exhaustion >= 16 and emotional_exhaustion <= 24:
            emotional_exhaustion_status = 'Средний уровень M'
        if emotional_exhaustion >= 25:
            emotional_exhaustion_status = 'Высокий уровень H'
        if depersonalization >= 0 and depersonalization <= 5:
            depersonalization_status            = 'Низкий уровень L'
        if depersonalization >= 6 and depersonalization <= 10:
            depersonalization_status            = 'Средний уровень M'
        if depersonalization >= 11:
            depersonalization_status            = 'Высокий уровень H'
        if reduction_of_professionalism >= 37:
            reduction_of_professionalism_status = 'Низкий уровень L'
        if reduction_of_professionalism >= 31 and reduction_of_professionalism <= 36:
            reduction_of_professionalism_status = 'Средний уровень M'
        if reduction_of_professionalism <= 30:
            reduction_of_professionalism_status = 'Высокий уровень H'
        message_out = message_out.replace('%%emotional_exhaustion_status%%',str(emotional_exhaustion_status))
        message_out = message_out.replace('%%depersonalization_status%%',str(depersonalization_status))
        message_out = message_out.replace('%%reduction_of_professionalism_status%%',str(reduction_of_professionalism_status))
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

        p = summ_p (emotional_exhaustion,depersonalization,reduction_of_professionalism)

        if p >= 0 and p <= 0.25:
            message_out,menu = iz_telegram.get_message (user_id,'Ответ 01',namebot)
            message_out = message_out.replace('%%TEST%%',str("TEST"))
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

        if p >= 0.25 and p <= 0.4:
            message_out,menu = iz_telegram.get_message (user_id,'Ответ 02',namebot)
            message_out = message_out.replace('%%TEST%%',str("TEST"))
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

        if p >= 0.4 and p <= 0.6:
            message_out,menu = iz_telegram.get_message (user_id,'Ответ 03',namebot)
            message_out = message_out.replace('%%TEST%%',str("TEST"))
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

        if p >= 0.6 and p <= 1:
            message_out,menu = iz_telegram.get_message (user_id,'Ответ 04',namebot)
            message_out = message_out.replace('%%TEST%%',str("TEST"))
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)

        time.sleep (10)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Два пути','S',0)   

    if message_in.find('@be_ballance_bot') != -1:
        iz_telegram.save_variable (user_id,namebot,"status",'')
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Проверка введенного кода','S',0) 
        answer = iz_telegram.check_access_code (user_id,namebot,message_in)
        if answer != 0:
            iz_telegram.save_variable (user_id,namebot,"status",'Ввод имени')
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Активировать код','S',0) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Укажите имя','S',0)             
            iz_telegram.activate_access_code (user_id,namebot,message_in)
        else: 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Код не активирован','S',0)   

    if message_in.find('answer_ask_') != -1:
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос защитан",'S',0)

        if message_in.find('_A1_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 01',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 01 защитан",'S',0)
        if message_in.find('_A2_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 02',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 02 защитан",'S',0)
        if message_in.find('_A3_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 03',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 03 защитан",'S',0)
        if message_in.find('_A4_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 04',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 04 защитан",'S',0)
        if message_in.find('_A5_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 05',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 05 защитан",'S',0)
        if message_in.find('_A6_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 06',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 06 защитан",'S',0)
        if message_in.find('_A7_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 07',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 07 защитан",'S',0)
        if message_in.find('_A8_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 08',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 08 защитан",'S',0)
        if message_in.find('_A9_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 09',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 09 защитан",'S',0)
        if message_in.find('_A10_') != -1:
            iz_telegram.save_variable (user_id,namebot,'Задание 10',message_in) 
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Вопрос 10 защитан",'S',0)
