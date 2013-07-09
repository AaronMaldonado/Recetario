# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
    conn = sqlite3.connect(db_name)
    c= conn.cursor()
    
    query = """CREATE TABLE categorias(id_categoria integer PRIMARY KEY AUTOINCREMENT,
									   nombre text,
									   descripcion text)"""
    c.execute(query)
    
    query = """CREATE TABLE paises (id_pais integer PRIMARY KEY AUTOINCREMENT,
                                    nombre text)"""
      
    c.execute(query)
    
    
    query1 = """CREATE TABLE recetas(id_receta integer primary key AUTOINCREMENT,
                                    nombre VARCHAR(45),
                                    fk_id_categoria integer,
                                    descripcion text,
                                    preparacion text,
                                    ingredientes text,
                                    imagen text,
                                    fk_id_pais integer,
			                        FOREIGN KEY (fk_id_categoria) REFERENCES categorias (id_categoria),
			                        FOREIGN KEY (fk_id_pais) REFERENCES paises (id_pais))"""
    c.execute(query1)
    
if __name__ == "__main__":
    db_name = 'base12.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO categorias (id_categoria,nombre,descripcion) VALUES (?,?,?)"	
    
    v0 =[0, "Carnes","Platos a base de carnes"]
    v1 =[1,"Ensaladas","Platos de verduras"]
    v2 =[2,"Pastas","Platos "]
    v3 =[3,"Sopas","Sopas XD"]
    v4 =[4,"Tragos","Aperitivos y Bajativos"]
    v5 =[5,"Postres","Ehhh Postres ? XDDD "]
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v0)
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v1)
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v2)
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v3)
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v4)	
    c.execute("INSERT INTO categorias VALUES (?,?,?)",v5)	
    conn.commit()


    query= "INSERT INTO paises(id_pais,nombre) VALUES (?,?)"
    
    p0=["151","Afganistan"]
    p1=["2","Albania"]
    p2=["17","Alemania"]
    p3=["3","Andorra"]
    p4=["98","Angola"]
    p5=["53","Anguilla"]
    p6=["54","Antigua y Barbuda"]
    p7=["73","Antillas Holandesas"]
    p8=["194","Arabia Saudi"]
    p9=["97","Argelia"]
    p10=["81","Argentina"]
    p11=["182","Armenia"]
    p12=["55","Aruba"]
    p13=["197","Australia"]
    p14=["4","Austria"]
    p15=["183","Azerbayan"]
    p16=["56","Bahamas"]
    p17=["184","Bahrain"]
    p18=["152","Bangladesh"]
    p19=["57","Barbados"]
    p20=["6","Belgica"]
    p21=["58","Belice"]
    p22=["99","Benin"]
    p23=["48","Bermudas"]
    p24=["5","Bielorrusia"]
    p25=["82","Bolivia"]
    p26=["7","Bosnia - Herzegovina"]
    p27=["100","Botswana"]
    p28=["83","Brasil"]
    p29=["154","Brunei"]
    p30=["8","Bulgaria"]
    p31=["101","Burkina Faso"]
    p32=["155","Burma (Myanmar)"]
    p33=["102","Burundi"]
    p34=["153","Butan"]
    p35=["104","Cabo Verde"]
    p36=["156","Camboya"]
    p37=["103","Camerun"]
    p38=["49","Canada"]
    p39=["106","Chad"]
    p40=["84","Chile"]
    p41=["157","China"]
    p42=["10","Chipre"]
    p43=["85","Colombia"]
    p44=["107","Comoros"]
    p45=["108","Congo"]
    p46=["170","Corea del Norte"]
    p47=["174","Corea del Sur"]
    p48=["217","Costa de Marfil"]
    p49=["60","Costa Rica"]
    p50=["9","Croacia"]
    p51=["61","Cuba"]
    p52=["12","Dinamarca"]
    p53=["62","Dominica"]
    p54=["86","Ecuador"]
    p55=["110","Egipto"]
    p56=["64","El Salvador"]
    p57=["195","Emiratos Arabes Unidos"]
    p58=["112","Eritrea"]
    p59=["39","Eslovaquia"]
    p60=["40","Eslovenia"]
    p61=["1","Espana"]
    p62=["52","Estados Unidos"]
    p63=["13","Estonia"]
    p64=["113","Etiopia"]
    p65=["199","Fiji"]
    p66=["172","Filipinas"]
    p67=["15","Finlandia"]
    p68=["16","Francia"]
    p69=["114","Gabon"]
    p70=["115","Gambia"]
    p71=["185","Georgia"]
    p72=["116","Ghana"]
    p73=["18","Gibraltar"]
    p74=["65","Granada"]
    p75=["19","Grecia"]
    p76=["50","Groenlandia"]
    p77=["66","Guadalupe"]
    p78=["201","Guam"]
    p79=["67","Guatemala"]
    p80=["90","Guayana"]
    p81=["88","Guayana Francesa"]
    p82=["117","Guinea"]
    p83=["111","Guinea Ecuatorial"]
    p84=["118","Guinea-Bissau"]
    p85=["68","Haiti"]
    p86=["32","Holanda"]
    p87=["69","Honduras"]
    p88=["158","Hong Kong"]
    p89=["20","Hungria"]
    p90=["59","I. Caiman"]
    p91=["219","I. Cocos (Keeling)"]
    p92=["198","I. Cook"]
    p93=["14","I. Feroe"]
    p94=["89","I. Galapagos"]
    p95=["87","I. Malvinas"]
    p96=["203","I. Marianas del Norte"]
    p97=["204","I. Marshall"]
    p98=["133","I. Reunion"]
    p99=["212","I. Salomon"]
    p100=["218","I. Virgenes Britanicas"]
    p101=["80","I. Virgenes EEUU"]
    p102=["216","I. Wallis y Futuna"]
    p103=["159","India"]
    p104=["160","Indonesia"]
    p105=["186","Iran"]
    p106=["187","Iraq"]
    p107=["22","Irlanda"]
    p108=["21","Islandia"]
    p109=["188","Israel"]
    p110=["23","Italia"]
    p111=["70","Jamaica"]
    p112=["161","Japon"]
    p113=["189","Jordania"]
    p114=["162","Kazajistan"]
    p115=["119","Kenia"]
    p116=["163","Kirguizistan"]
    p117=["202","Kiribati"]
    p118=["190","Kuwait"]
    p119=["164","Laos"]
    p120=["120","Lesotho"]
    p121=["24","Letonia"]
    p122=["191","Libano"]
    p123=["121","Liberia"]
    p124=["122","Libia"]
    p125=["25","Liechtenstein"]
    p126=["26","Lituania"]
    p127=["27","Luxemburgo"]
    p128=["165","Macao"]
    p129=["28","Macedonia"]
    p130=["123","Madagascar"]
    p131=["166","Malasia"]
    p132=["124","Malawi"]
    p133=["167","Maldivas"]
    p134=["125","Mali"]
    p135=["29","Malta"]
    p136=["128","Marruecos"]
    p137=["71","Martinica"]
    p138=["127","Mauricio"]
    p139=["126","Mauritania"]
    p140=["51","Mexico"]
    p141=["205","Micronesia"]
    p142=["30","Moldavia"]
    p143=["31","Monaco"]
    p144=["168","Mongolia"]
    p145=["72","Montserrat"]
    p146=["129","Mozambique"]
    p147=["130","Namibia"]
    p148=["206","Nauru"]
    p149=["169","Nepal"]
    p150=["74","Nicaragua"]
    p151=["131","Niger"]
    p152=["132","Nigeria"]
    p153=["33","Noruega"]
    p154=["207","Nueva Caledonia"]
    p155=["208","Nueva Zelanda"]
    p156=["192","Oman"]
    p157=["171","Pakistan"]
    p158=["209","Palau"]
    p159=["75","Panama"]
    p160=["210","Papua Nueva Guinea"]
    p161=["91","Paraguay"]
    p162=["92","Peru"]
    p163=["200","Polinesia Francesa"]
    p164=["34","Polonia"]
    p165=["35","Portugal"]
    p166=["76","Puerto Rico"]
    p167=["193","Qatar"]
    p168=["45","Reino Unido"]
    p169=["105","Rep. Centroafricana"]
    p170=["11","Rep. Checa"]
    p171=["63","Rep. Dominicana"]
    p172=["134","Ruanda"]
    p173=["36","Rumania"]
    p174=["37","Rusia"]
    p175=["147","Sahara Occidental"]
    p176=["211","Samoa"]
    p177=["38","San Marino"]
    p178=["135","Sao Tome y Principe"]
    p179=["136","Senegal"]
    p180=["137","Seychelles"]
    p181=["138","Sierra Leona"]
    p182=["173","Singapur"]
    p183=["220","Siria"]
    p184=["139","Somalia"]
    p185=["175","Sri Lanka"]
    p186=["78","St. Vicent y Grenadines"]
    p187=["77","St.Kitts & Nevis"]
    p188=["141","Sudan"]
    p189=["41","Suecia"]
    p190=["42","Suiza"]
    p191=["93","Sur Georgia e I. Sandwich"]
    p192=["140","Surafrica"]
    p193=["94","Surinam"]
    p194=["142","Swazilandia"]
    p195=["178","Tailandia"]
    p196=["176","Taiwan"]
    p197=["177","Tajikistan"]
    p198=["143","Tanzania"]
    p199=["144","Togo"]
    p200=["213","Tonga"]
    p201=["79","Trinidad y Tobago"]
    p202=["145","Tunez"]
    p203=["179","Turkmenistan"]
    p204=["43","Turquia"]
    p205=["214","Tuvalu"]
    p206=["44","Ucrania"]
    p207=["146","Uganda"]
    p208=["95","Uruguay"]
    p209=["180","Uzbekistan"]
    p210=["215","Vanuatu"]
    p211=["46","Vaticano"]
    p212=["96","Venezuela"]
    p213=["181","Vietnam"]
    p214=["196","Yemen"]
    p215=["109","Yibuti"]
    p216=["47","Yugoslavia"]
    p217=["148","Zaire"]
    p218=["149","Zambia"]
    p219=["150","Zimbabwe"]
    
    c.execute("INSERT INTO paises VALUES (?,?)",p0)
    c.execute("INSERT into paises VALUES (?,?)",p1)
    c.execute("INSERT into paises VALUES (?,?)",p2)
    c.execute("INSERT into paises VALUES (?,?)",p3)
    c.execute("INSERT into paises VALUES (?,?)",p4)	
    c.execute("INSERT into paises VALUES (?,?)",p5)
    c.execute("INSERT into paises VALUES (?,?)",p6)
    c.execute("INSERT into paises VALUES (?,?)",p7)
    c.execute("INSERT into paises VALUES (?,?)",p8)
    c.execute("INSERT into paises VALUES (?,?)",p9)	
    c.execute("INSERT into paises VALUES (?,?)",p10)
    c.execute("INSERT into paises VALUES (?,?)",p11)
    c.execute("INSERT into paises VALUES (?,?)",p12)
    c.execute("INSERT into paises VALUES (?,?)",p13)
    c.execute("INSERT into paises VALUES (?,?)",p14)	
    c.execute("INSERT into paises VALUES (?,?)",p15)
    c.execute("INSERT into paises VALUES (?,?)",p16)
    c.execute("INSERT into paises VALUES (?,?)",p17)
    c.execute("INSERT into paises VALUES (?,?)",p18)
    c.execute("INSERT into paises VALUES (?,?)",p19)	
    c.execute("INSERT into paises VALUES (?,?)",p20)
    c.execute("INSERT into paises VALUES (?,?)",p21)
    c.execute("INSERT into paises VALUES (?,?)",p22)
    c.execute("INSERT into paises VALUES (?,?)",p23)
    c.execute("INSERT into paises VALUES (?,?)",p24)	
    c.execute("INSERT into paises VALUES (?,?)",p25)
    c.execute("INSERT into paises VALUES (?,?)",p26)
    c.execute("INSERT into paises VALUES (?,?)",p27)
    c.execute("INSERT into paises VALUES (?,?)",p28)
    c.execute("INSERT into paises VALUES (?,?)",p29)	
    c.execute("INSERT into paises VALUES (?,?)",p30)
    c.execute("INSERT into paises VALUES (?,?)",p31)
    c.execute("INSERT into paises VALUES (?,?)",p32)
    c.execute("INSERT into paises VALUES (?,?)",p33)
    c.execute("INSERT into paises VALUES (?,?)",p34)	
    c.execute("INSERT into paises VALUES (?,?)",p35)
    c.execute("INSERT into paises VALUES (?,?)",p36)
    c.execute("INSERT into paises VALUES (?,?)",p37)
    c.execute("INSERT into paises VALUES (?,?)",p38)
    c.execute("INSERT into paises VALUES (?,?)",p39)	
    c.execute("INSERT into paises VALUES (?,?)",p40)
    c.execute("INSERT into paises VALUES (?,?)",p41)
    c.execute("INSERT into paises VALUES (?,?)",p42)
    c.execute("INSERT into paises VALUES (?,?)",p43)
    c.execute("INSERT into paises VALUES (?,?)",p44)	
    c.execute("INSERT into paises VALUES (?,?)",p45)
    c.execute("INSERT into paises VALUES (?,?)",p46)
    c.execute("INSERT into paises VALUES (?,?)",p47)
    c.execute("INSERT into paises VALUES (?,?)",p48)
    c.execute("INSERT into paises VALUES (?,?)",p49)
    c.execute("INSERT into paises VALUES (?,?)",p50)
    c.execute("INSERT into paises VALUES (?,?)",p51)
    c.execute("INSERT into paises VALUES (?,?)",p52)
    c.execute("INSERT into paises VALUES (?,?)",p53)
    c.execute("INSERT into paises VALUES (?,?)",p54)	
    c.execute("INSERT into paises VALUES (?,?)",p55)
    c.execute("INSERT into paises VALUES (?,?)",p56)
    c.execute("INSERT into paises VALUES (?,?)",p57)
    c.execute("INSERT into paises VALUES (?,?)",p58)
    c.execute("INSERT into paises VALUES (?,?)",p59)	
    c.execute("INSERT into paises VALUES (?,?)",p60)
    c.execute("INSERT into paises VALUES (?,?)",p61)
    c.execute("INSERT into paises VALUES (?,?)",p62)
    c.execute("INSERT into paises VALUES (?,?)",p63)
    c.execute("INSERT into paises VALUES (?,?)",p64)	
    c.execute("INSERT into paises VALUES (?,?)",p65)
    c.execute("INSERT into paises VALUES (?,?)",p66)
    c.execute("INSERT into paises VALUES (?,?)",p67)
    c.execute("INSERT into paises VALUES (?,?)",p68)
    c.execute("INSERT into paises VALUES (?,?)",p69)	
    c.execute("INSERT into paises VALUES (?,?)",p70)
    c.execute("INSERT into paises VALUES (?,?)",p71)
    c.execute("INSERT into paises VALUES (?,?)",p72)
    c.execute("INSERT into paises VALUES (?,?)",p73)
    c.execute("INSERT into paises VALUES (?,?)",p74)	
    c.execute("INSERT into paises VALUES (?,?)",p75)
    c.execute("INSERT into paises VALUES (?,?)",p76)
    c.execute("INSERT into paises VALUES (?,?)",p77)
    c.execute("INSERT into paises VALUES (?,?)",p78)
    c.execute("INSERT into paises VALUES (?,?)",p79)	
    c.execute("INSERT into paises VALUES (?,?)",p80)
    c.execute("INSERT into paises VALUES (?,?)",p81)
    c.execute("INSERT into paises VALUES (?,?)",p82)
    c.execute("INSERT into paises VALUES (?,?)",p83)
    c.execute("INSERT into paises VALUES (?,?)",p84)	
    c.execute("INSERT into paises VALUES (?,?)",p85)
    c.execute("INSERT into paises VALUES (?,?)",p86)
    c.execute("INSERT into paises VALUES (?,?)",p87)
    c.execute("INSERT into paises VALUES (?,?)",p88)
    c.execute("INSERT into paises VALUES (?,?)",p89)	
    c.execute("INSERT into paises VALUES (?,?)",p90)
    c.execute("INSERT into paises VALUES (?,?)",p91)
    c.execute("INSERT into paises VALUES (?,?)",p92)
    c.execute("INSERT into paises VALUES (?,?)",p93)
    c.execute("INSERT into paises VALUES (?,?)",p94)	
    c.execute("INSERT into paises VALUES (?,?)",p95)
    c.execute("INSERT into paises VALUES (?,?)",p96)
    c.execute("INSERT into paises VALUES (?,?)",p97)
    c.execute("INSERT into paises VALUES (?,?)",p98)
    c.execute("INSERT into paises VALUES (?,?)",p99)	
    c.execute("INSERT into paises VALUES (?,?)",p100)
    c.execute("INSERT into paises VALUES (?,?)",p101)
    c.execute("INSERT into paises VALUES (?,?)",p102)
    c.execute("INSERT into paises VALUES (?,?)",p103)
    c.execute("INSERT into paises VALUES (?,?)",p104)	
    c.execute("INSERT into paises VALUES (?,?)",p105)
    c.execute("INSERT into paises VALUES (?,?)",p106)
    c.execute("INSERT into paises VALUES (?,?)",p107)
    c.execute("INSERT into paises VALUES (?,?)",p108)
    c.execute("INSERT into paises VALUES (?,?)",p109)	
    c.execute("INSERT into paises VALUES (?,?)",p110)
    c.execute("INSERT into paises VALUES (?,?)",p111)
    c.execute("INSERT into paises VALUES (?,?)",p112)
    c.execute("INSERT into paises VALUES (?,?)",p113)
    c.execute("INSERT into paises VALUES (?,?)",p114)	
    c.execute("INSERT into paises VALUES (?,?)",p115)
    c.execute("INSERT into paises VALUES (?,?)",p116)
    c.execute("INSERT into paises VALUES (?,?)",p117)
    c.execute("INSERT into paises VALUES (?,?)",p118)
    c.execute("INSERT into paises VALUES (?,?)",p119)	
    c.execute("INSERT into paises VALUES (?,?)",p120)
    c.execute("INSERT into paises VALUES (?,?)",p121)
    c.execute("INSERT into paises VALUES (?,?)",p122)
    c.execute("INSERT into paises VALUES (?,?)",p123)
    c.execute("INSERT into paises VALUES (?,?)",p124)	
    c.execute("INSERT into paises VALUES (?,?)",p125)
    c.execute("INSERT into paises VALUES (?,?)",p126)
    c.execute("INSERT into paises VALUES (?,?)",p127)
    c.execute("INSERT into paises VALUES (?,?)",p128)
    c.execute("INSERT into paises VALUES (?,?)",p129)	
    c.execute("INSERT into paises VALUES (?,?)",p130)
    c.execute("INSERT into paises VALUES (?,?)",p131)
    c.execute("INSERT into paises VALUES (?,?)",p132)
    c.execute("INSERT into paises VALUES (?,?)",p133)
    c.execute("INSERT into paises VALUES (?,?)",p134)	
    c.execute("INSERT into paises VALUES (?,?)",p135)
    c.execute("INSERT into paises VALUES (?,?)",p136)
    c.execute("INSERT into paises VALUES (?,?)",p137)
    c.execute("INSERT into paises VALUES (?,?)",p138)
    c.execute("INSERT into paises VALUES (?,?)",p139)	
    c.execute("INSERT into paises VALUES (?,?)",p140)
    c.execute("INSERT into paises VALUES (?,?)",p141)
    c.execute("INSERT into paises VALUES (?,?)",p142)
    c.execute("INSERT into paises VALUES (?,?)",p143)
    c.execute("INSERT into paises VALUES (?,?)",p144)	
    c.execute("INSERT into paises VALUES (?,?)",p145)
    c.execute("INSERT into paises VALUES (?,?)",p146)
    c.execute("INSERT into paises VALUES (?,?)",p147)
    c.execute("INSERT into paises VALUES (?,?)",p148)
    c.execute("INSERT into paises VALUES (?,?)",p149)	
    c.execute("INSERT into paises VALUES (?,?)",p150)
    c.execute("INSERT into paises VALUES (?,?)",p151)
    c.execute("INSERT into paises VALUES (?,?)",p152)
    c.execute("INSERT into paises VALUES (?,?)",p153)
    c.execute("INSERT into paises VALUES (?,?)",p154)	
    c.execute("INSERT into paises VALUES (?,?)",p155)
    c.execute("INSERT into paises VALUES (?,?)",p156)
    c.execute("INSERT into paises VALUES (?,?)",p157)
    c.execute("INSERT into paises VALUES (?,?)",p158)
    c.execute("INSERT into paises VALUES (?,?)",p159)	
    c.execute("INSERT into paises VALUES (?,?)",p160)
    c.execute("INSERT into paises VALUES (?,?)",p161)
    c.execute("INSERT into paises VALUES (?,?)",p162)
    c.execute("INSERT into paises VALUES (?,?)",p163)
    c.execute("INSERT into paises VALUES (?,?)",p164)	
    c.execute("INSERT into paises VALUES (?,?)",p165)
    c.execute("INSERT into paises VALUES (?,?)",p166)
    c.execute("INSERT into paises VALUES (?,?)",p167)
    c.execute("INSERT into paises VALUES (?,?)",p168)
    c.execute("INSERT into paises VALUES (?,?)",p169)	
    c.execute("INSERT into paises VALUES (?,?)",p170)
    c.execute("INSERT into paises VALUES (?,?)",p171)
    c.execute("INSERT into paises VALUES (?,?)",p172)
    c.execute("INSERT into paises VALUES (?,?)",p173)
    c.execute("INSERT into paises VALUES (?,?)",p174)	
    c.execute("INSERT into paises VALUES (?,?)",p175)
    c.execute("INSERT into paises VALUES (?,?)",p176)
    c.execute("INSERT into paises VALUES (?,?)",p177)
    c.execute("INSERT into paises VALUES (?,?)",p178)
    c.execute("INSERT into paises VALUES (?,?)",p179)	
    c.execute("INSERT into paises VALUES (?,?)",p180)
    c.execute("INSERT into paises VALUES (?,?)",p181)
    c.execute("INSERT into paises VALUES (?,?)",p182)
    c.execute("INSERT into paises VALUES (?,?)",p183)
    c.execute("INSERT into paises VALUES (?,?)",p184)	
    c.execute("INSERT into paises VALUES (?,?)",p185)
    c.execute("INSERT into paises VALUES (?,?)",p186)
    c.execute("INSERT into paises VALUES (?,?)",p187)
    c.execute("INSERT into paises VALUES (?,?)",p188)
    c.execute("INSERT into paises VALUES (?,?)",p189)	
    c.execute("INSERT into paises VALUES (?,?)",p190)
    c.execute("INSERT into paises VALUES (?,?)",p191)
    c.execute("INSERT into paises VALUES (?,?)",p192)
    c.execute("INSERT into paises VALUES (?,?)",p193)
    c.execute("INSERT into paises VALUES (?,?)",p194)		
    c.execute("INSERT into paises VALUES (?,?)",p195)
    c.execute("INSERT into paises VALUES (?,?)",p196)
    c.execute("INSERT into paises VALUES (?,?)",p197)
    c.execute("INSERT into paises VALUES (?,?)",p198)
    c.execute("INSERT into paises VALUES (?,?)",p199)	
    c.execute("INSERT into paises VALUES (?,?)",p200)
    c.execute("INSERT into paises VALUES (?,?)",p201)
    c.execute("INSERT into paises VALUES (?,?)",p202)
    c.execute("INSERT into paises VALUES (?,?)",p203)
    c.execute("INSERT into paises VALUES (?,?)",p204)	
    c.execute("INSERT into paises VALUES (?,?)",p205)
    c.execute("INSERT into paises VALUES (?,?)",p206)
    c.execute("INSERT into paises VALUES (?,?)",p207)
    c.execute("INSERT into paises VALUES (?,?)",p208)
    c.execute("INSERT into paises VALUES (?,?)",p209)	
    c.execute("INSERT into paises VALUES (?,?)",p210)
    c.execute("INSERT into paises VALUES (?,?)",p211)
    c.execute("INSERT into paises VALUES (?,?)",p212)
    c.execute("INSERT into paises VALUES (?,?)",p213)
    c.execute("INSERT into paises VALUES (?,?)",p214)	
    c.execute("INSERT into paises VALUES (?,?)",p215)
    c.execute("INSERT into paises VALUES (?,?)",p216)
    c.execute("INSERT into paises VALUES (?,?)",p217)
    c.execute("INSERT into paises VALUES (?,?)",p218)
    c.execute("INSERT into paises VALUES (?,?)",p219)	
    conn.commit()
    	
    	
    query = "INSERT INTO recetas(id_receta,nombre,fk_id_categoria,descripcion,preparacion,ingredientes,imagen,fk_id_pais)"
   
    p1=["6","Carne al Jugo","0","Carne al vapor","",
    "1kg de tapapecho (vacuno) 200gr de mantequilla sin sal 2 cdas de Condimento para Carne Gourmet 2 cdas de mostaza dijon 2 hojas de Laurel Gourmet Agua necesaria 1 cda de maicena Pimienta Negra Molida Gourmet a gusto Sal a gusto",
    "tret","imagen1.png","84"]

    conn.commit()
