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
    v1 =[1,"Legumbres, Hortalizas y Verduras","Platos de verduras"]
    v2 =[2,"Pastas","Platos a base de pastas "]
    v3 =[3,"Sopas","Sopas para servir como entradas"]
    v4 =[4,"Aperitivos y Entremeses","Aperitivos y entremeses para antes y despues de las comidas"]
    v5 =[5,"Postres"," Postres "]
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
    	
    	
    query = "INSERT INTO recetas(id_receta,nombre,fk_id_categoria,descripcion,preparacion,ingredientes,imagen,fk_id_pais) VALUES (?,?,?,?,?,?,?,?)"
   
    r1=["6","Sopa de miso con almejas","3","Sopa para servir como entrada",
        "Lavar y cocer las almejas luego agregar el miso pasandolo por un colador y retirar cuando se diluya en la sopa.",
        "350 gramos almejas , 150 gramos miso , Un trozo de puerro picado",
        "imagen1.jpeg",
        "161"]
    r2=["7","Sopa de cebolla","3","Sopa para servir como entrada",
        "Cortamos las cebollas en pedazos grandes y las papas con forma de cubitos. Sobre un poco de mantequilla y aceite sofreimos la cebolla, anadimos la harina fina y mezclamos luego sofreimos todo hasta obtener un color rosado. Despues anadimos un litro del agua fria y lo dejamos cocer hasta que haga ebullicion. Agregamos las papas al agua salada en la cual previamente les hemos cocido y anadimos azucar. En la leche mezclamos la yema y todo lo vertemos en la sopa. Despues de haber llevado la sopa hasta hacer hervor anadimos el vinagre. Asi esta lista, la Cibulaeka. ",
        "4 cebollas, 2 cucharadas de harina fina, 3 papas, 2,5 decilitros de leche, 1 yema de huevo, sal, mantequilla, 1 cucharada de azucar, vinagre, aceite.",
        "imagen2.jpeg",
        "39"]
    r3=["8","Bramboracka","3","Sopa para servir de como entrada",
       "Poner agua a calentar con la sal, la alcarabea, pimienta y un poco de manteca de cerdo.Mas tarde anadir todos los demas ingredientes cortados a cuadritos, menos el vinagre, que solo se anadira a la sopa una vez terminada si tiene un sabor demasiado dulce.",
       "4 Patatas,1 apio,1 puerro,1 nabo,1 chirivia(raiz de perejil),5 ajos, 2 zanahorias,150gr. de champinones,alcarabea,Sal,Pimienta,Un chorrito de vinagre,1 cucharada de manteca de cerdo.",
       "imagen3.jpeg",
       "11"]
    r4=["9","Carbonada","3","Plato de fondo",
        "Se corta la carne en cuadritos pequenos, se frie con aceite la cebolla cortada en pluma, la sal y los condimentos a gusto.Se le agrega la papa en plumas y se le agrega las verduras y la calabaza en plumas, se agregan los porotos verdes y se le agrega el litro de agua hervida.Cuando este todo cocido se le agrega las pastas chicas.Se espera que este cocida la pasta y se sirve.",
        "5 papas medianas,un trozo de calabaza,3 cucharadas soperas de aceite,150 gr de carne de vacuno,sal,verduras,150 gr de porotos verdes,1 litro de agua hervida,pasta ( unos dos punados ),una cebolla mediana,condimentos a gusto.",
        "imagen4.jpeg",
        "84"]
    r5=["10","Sopa de Tahin","3","Sopa para servir de entrada",
         "Anadir la pasta al caldo hervido,mezclar el tahin con un cucharon de caldo, el zumo de limon y anadir los huevos a la sopa fuera del fuego.",
         "2 litros caldo,150 gramos de fideos,120 gramos de de tahin,Zumo de 1 limon,Sal a gusto , 2 huevos.",
         "imagen5.jpeg",
         "19"]
    r6=["11","Albondigas","0","Plato de entrada",
         "Licuar 1/4 de cebolla 1/4 chile verde 2 ajos,agregarlo a la carne junto con el condimento y la cebolla chile y ajo licuados, mixar todo con el huevo y el pan molido,amasar y hacer bolitas de carne, ponerlas a cocinar a fuego lento por media hora en 2 tazas de agua,cuando esten cocinadas agregarle la salsa de tomate,y dejar hervir por 1 minuto con las hojas de laurel y el oregano.",
         "1 lb de carne, molida, 2 ajo, cebolla y chile verde,condimentos goya,pan molido, 1 taza y huevo, oregano 1 cda, 2 hojas de laurel, 2 latas de salsa de tomate. ",
         "imagen6.jpeg",
         "69"]
    r7=["12","Pytt i panna","0","Plato de fondo",
         "Se cortan los filetes y las patatas en cuadritos finos. Se pelan las cebollas y se pican.Se calienta la mantequilla en la sarten y se hechan los cuadritos de patatas y las cebollas picadas. Se frien a fuego lento durante 20 minutos. Se echa la mezcla en un plato y se calienta mas mantequilla en la sarten. Se frien los cuadritos de carne a fuego medio durante algunos minutos. Se echa la mezcla de cebolla y patatas en la sarten con la carne y se cuece todo durante cinco minutos. Se sirve con huevos fritos. ",
         "400 g de filetes de carne,500 g de patatas,3 cebollas,Mantequilla,Sal y pimienta,4 huevos.",
         "imagen7.jpeg",
         "41"]
    r8=["13","Alambres","0","Plato de entrada",
         "Se parten los ingredientes en cuadros pequenos. en una plancha o comal, se pone a dorar el tocino junto con el chile y la cebolla, ya que esten acitronados, se agrega la carne y se termina de cocinar con el resto de los ingredientes, se agrega pimienta y un poco de salsa de soya o salsa inglesa, se cubre todo con tortillas, mismas que se utilizan para hacerse sus tacos.",
         "Carne de res,tocino de puerco,cebolla,chile morron,sal a gusto,pimienta.",
         "imagen8.jpeg",
         "51"]
    r9=["14","Agato","0","Plato de fondo",
        "Pica repollo y agrega tinta de calamar a tu gusto,cuece a fuego bajo por 2 minutos.Muele el lomo echa la salsa picante y cuece por 25 minutos,espera que el lomo este frio y revuelve y sirve.",
        " 1 libra de lomo de puerco,1 libra de repollo,salsa picante,tinta de calamar ",
        "imagen9.jpeg",
        "75"]
    r10=["15","Milanesas","0","Plato que se puede servir como entrada.",
         "La carne la ponemos con huevo, y despues la echamos en el pan rallado, y cocinamos en la plancha llena de aceite.",
         "Carne de ternera muy fina, pan rallado, huevos,aceite. ",
         "imgen10.jpeg",
         "61"]
    r11=["16","Alfajores","5","Postre",
         "Las yemas y la clara se baten juntas, se les agregan manteca, harina mezclada con polvo de hornear, se mezcla todo, se estira finito, se cortan las tapas, se pinchan y se ponen en el horno 10 minutos, mas o menos. Se rellenan a gusto.",
         "5 yemas,1 clara,10 g de manteca,150 g de harina,1 cucharadita de polvo de hornear.",
         "imagen11.jpeg",
         "81"]
    r12=["17","Arroz Doce","5","Postre",
         "Ponga a coser arroz en una olla seguidamente la leche condensada y ya servidas en el plato hecha canela y dejar enfriar durante 30 minutos en la nevera.",
         "4 punados de arroz,1/2 canela en polvo,1/2 de leche condesada no disolvida.",
         "imagen12.jpeg",
         "129"]
    r13=["18","Atole de Guayaba","5","Postre",
         "Hervir un litro de agua, la leche evaporada y la raja de canela.Mezcla la masa en la taza de agua hasta que este todo disuelto.Pon la mezcla a hervir y mueve todo hasta que se cueza.Mezcla e elote molido con el azucar y sigue hirviendo.Deja en fuego bajo por 9 minutos y deja reposar.",
         "1 litro de jugo de guayaba,250 gramos de masa,1 1/2 tazas de agua,3 guayabas no semillas,canela,1 lata de leche evaporada,200 gramos de azucar.",
         "imagen13.jpeg",
         "52"]
    r14=["19","Postre Borracho","5","Postre",
         "Preparar el pudin o flan de chocolate en las dos tazas de leche, esperar a que espese.En una refractaria colocar una capa de pedazos pequenos de panque  y rociarlos con el brandy o aguardiente.Echar suavemente encima del panque una capa de pudin  de chocolate.Continuar colocando trozos de panque y tapar con lo que resta del pudin o flan de chocolate.Meter a la nevera hasta que cuaje.",
         "1 panque  de vainilla pequeno,1 pudin  de chocolate,2 tazas de leche,1 pocillo de aguardiente o brandy.",
         "imagen14.jpeg",
         "85"]
    r15=["20","Maskina","5","Postre",
         "Mezclar la harina con el azucar y la nata.Untar el molde con aceite, poner la mezcla igualando la superficie , untarla con aceite y esparcir los frutos secos.Meter en horno a temperatura mediana.Servir fria.",
         "2 vasos de harina,1 1/2 vaso de azucar en polvo,1 vaso de nata,frutos secos machacados.",
         "imagen15.jpeg",
         "110"]
    r16=["21","Colcannon","1","Plato de fondo",
         "Cortar las patatas en cuatro y hervirlas 15 minutos. Colarlas y aplastarlas con un tenedor.Cocer la col en agua durante 10 minutos y dejar escurrir.Derrretir la mantequilla en una sarten grande, anadir la col y la cebolla, rehogar dos minutos.Mezclar el sofrito con el pure de patatas y anadir la cantidad de leche necesaria para dar a la mezcla consistencia cremosa, anadir sal y pimenta a gusto y decorar con perejil.",
         "4 patatas medianas peladas,4 tazas de col troceada,60 gr. de mantequilla,1/2 taza de cabolleta picada,1/3 taza de leche caliente,pimienta molida,1 cucharada de perejil picado.",
         "imagen16.jpeg",
         "22"]
    r17=["22","Okroshka","1","Ensalada",
         "Cortar todos los ingredientes en trozos de 1 cm, anadir sal, azucar y la cebolla. Remover bien todos estos ingredientes. Dejarlo en el refrigerador durante 2 horas. Anadir kvas o cerveza, azucar, sal y la crema cortada al gusto. No utilice toda la cerveza o kvas, ni la crema cortada si no esta seguro de comerlo todo. El Okroshka se puede guardar en la nevera por algunos dias. Okroshka se sirve bien frio y con verduras como guisantes.",
         "3 huevos duros cocidos,4 tomates cocidos y pelados,2 Pepinos,300g de carne cocida,3 cebollas cortadas,1 taza de crema cortada,1 litro de Kvas o cerveza,Azucar,Sal y pimienta.",
         "imagen17.jpeg",
         "44"]
    r18=["23","El potaje de lentejas de paco","1","Plato de fondo",
          "Poner todos los ingredientes en un olla y cubrir de agua.Dejar cocer una hora aproximadamente, y listo para servir.",
          "1/4 kg de lentejas,1 cabeza de ajo sin pelar,1/8 l aceite de oliva,1 pimiento,1 hoja de laurel,1 cebolla grande(entera),1 chorizo,1 morcilla,1 patata,1 zanahoria,un poco de pimenton molido. ",
          "imagen18.jpeg",
          "1"]
    r19=["24","Salade cote cap verte","1","Ensalada",
          "En el cuenco de la ensalada combinar 2 o 3 vegetales como lechuga, espinaca, berros.Hacer monticulos en los 8 platos a servir. Cortar en rebanadas 4 huevos duros, esparcirlos luego encima de los platos. Ahora en una jarra combinar: 1 taza de aceite de Oliva, 1/2 taza de vinagre de estragon, una cucharadita de ajo en polvo o machacado, sal al gusto, sazonador para ensaladas una cucharada, una pizca de pimiento fresco y 2 cucharadas de miel. Agitar fuertemente la salsa y servir separadamente.",
          "Lechuga, espinaca, berros,huevos,aceite,vinagre tarragon,ajo en polvo (dientes de ajo),sal,pimienta fresca natural,condimento de ensalada a las hierbas,miel ",
          "imagen19.jpeg",
          "136"]
    r20=["25","Lentejas con pan y ajo","1","Plato de fondo",
          "Echar la sopa de lentejas caliente encima del pan en un plato hondo.Dejar reposar 5 minutos.Freir el ajo machacado, anadir el vinagre y dejar hervir 2 minutos.Echar el ajo con vinagre encima de las lentejas.Servir caliente.",
          "Sopa de lentejas amarillas,pan del dia anterior seco y cortado en trozos,2 dientes de ajo,2 cucharadas de vinagre,2 cucharadas de aceite ",
          "imagen20.jpeg",
          "97"]
    r21=["26","Codito ranchero","2","Plato de fondo",
          "Se cuece la pasta de codito como se hace normalmente y se escurre, en una cacerola se frien el ajo y la cebolla y una vez acitronados se agrega el chorizo hasta que este bien frito, se agrega el pure de tomate, se salpimenta y se incorpora la pasta en la mezcla, se agrega el queso desmoronado, se apaga la cacerola y se tapa hasta que se funda el queso.",
          "1 paquete de pasta de codito mediano,2 bolas de chorizo,1 diente de ajo picado,1/2 cebolla picada,1/2 taza de pure de tomate,1/2 queso ranchero,1 cucharadita de aceite,Sal y pimienta al gusto ",
          "imagen21.jpeg",
          "51"]
    r22=["27","Espaguetis a la Carbonara","2","Plato de fondo",
          "Cocer los espaguetis en abundante agua salada. Rallar el queso y cortar los ajos y el tocino. En una fuente batir los huevos con la nata liquida, el queso, la sal y la pimienta. Incorporar a la sarten la pasta y remover. Colocar la pasta en una fuente y mezclarla con el huevo batido, removiendo todo.",
          "35ccs de aceite, 4 dientes de ajo, 700grs. de espaguetis, 5,2 huevo, 7 cucharadas de nata liquida, 8grs de pimienta, 250grs de queso parmesano, 1 pizca de sal y 175grs de tocino ahumado. ",
          "imagen22.jpeg",
          "52"]
    r23=["28","Laevasan","2","Plato de fondo",
          "Hervir los macarrones unos 30 minutos a fuego lento anadir la sal y el vinagre y todo lo que te apezca, pasados 15 minutos meterlos al horno a 50 grados.",
          "Agua,aceite,vinagre,sal,macarrones ",
          "imagen23.jpeg",
          "210"]
    r24=["29","Lasagna a la Esther","2","Plato de fondo",
          "Para la carne:Sofreir la carne y agregarle los vegetales, luego de que estos esten medio fritos, echarle la pasta el caldo y una o dos tazas de agua, dejar esperar y listo.Mientras tanto aparte se sancocha la lasagna en pasta, se coloca agua a hervir y se introduce la pasta dejandola por 3 a 4 minutos, posteriormente sacar y escurrir.Cuando todo este listo empezamos a confeccionar la lasagna a la Esther; colocamos en un molde una cubierta de pasta, despues agregamos una cubierta de carne con salsa encima, luego aplicamos los diferentes quesos amarillo, chedar, mozarela, y parmesano, y por ultimo la rodaja de tocino; luego cubrimos con otra capa de pasta y seguimos el mismo procedimiento hasta que se halla llenado el molde. Se prende el horno y se coloca por unos 30 minutos hasta que se seque un poco la salsa. Y listo a disfrutar de una lasagna exquisita.",
          "Para la carne: 1 lb carne molida,1 zanahoria,2 cebollas,3 pimentones,apio,aceitunas,pasta de tomate,pimienta al gusto,ajo al gusto.Para la pasta: 1 cjta. de lasagna,1lb de queso amarillo,1lb de queso cheddar,1lb de queso mozarela,1lb de queso parmesano,1lb de tocino en rodajas",
          "imagen24.jpeg",
          "75"]
    r25=["30","Pudin aleman de fideos","2","Plato de fondo",
          "Engrase una fuente para el horno con un poco de mantequilla. Ponga a hervir agua en una cazuela, eche los fideos, deje que vuelva a hervir y cuezalos hasta que casi esten tiernos. Escurralos y reservelos.Bata el queso cremoso con el requeson y el azucar en un cuenco grande, hasta que la mezcla este suave. Vaya anadiendo el huevo poco a poco, y despues la nata agria, la vainilla, la canela, la ralladura de limon y, por ultimo, los fideos. Pase la mezcla a la fuente engrasada y alise la superficie.Derrita la mantequilla en una sarten a fuego lento y fria las almendras, sin dejar de remover, un par de  minutos o hasta que cojan un poco de color. Aparte la sarten del fuego y anada el pan rallado.Esparza la mezcla de almendra y pan rallado sobre el pudin y cuezalo en el horno precalentado a 180 grados, 35 o 45 minutos o hasta que cuaje. Espolvoreelo con un poco de azucar de lustre tamizado y sirvalo.",
          " 4 cucharadas de mantequilla y un poco mas para engrasar,175 g de fideos al huevo anchos,120 g de queso cremoso,225 g de requeson,85 g de azucar de granulado fino,2 huevos ligeramente batidos,125 ml de nata agria,1 cucharadita de esencia de vainilla,1 pizca de canela molida,1 cucharadita de ralladura de limon,25 g de almendras fileteadas,25 g de pan rallado blanco,azucar de lustre, para espolvorear ",
          "imagen25.jpeg",
          "17"]
    r26=["31","Aceitunas shock","4","Entremes",
          "Agregar las aceitunas con todo y el liquido que trae en la lata en un refractario. Anades el cilantro, la cebolla, el hielo y el jugo de los dos limones. Dejar reposar por 5 minutos para enfriar los ingredientes y servir.",
          "1 lata de aceitunas con anchoas,2 ramitas de Cilantro picado,1 rodaja de Cebolla picada,2 limones,Hielo.",
          "image26.jpeg",
          "51"]
    r27=["32","Bebida rapida de cafe","4","Aperitivo",
          "Disuelva el cafe(cafe en polvo)en media taza de agua caliente, luego se agrega azucar a gusto y se deja enfriar, anada el agua fria hasta completar un litro, sirva inmediatamente en vasos y si desea decorar con cascaras de limon.",
          "1 medida de ron,3 cucharadas de cafe (nescafe),1 cucharada de jugo de limon,2 tazas de hielo molido,cascara de limon, azucar a gusto.",
          "imagen27.jpg",
          "84"]
    r28=["33","Bola Magica","4","Entremes",
         "Triturar la jamonilla (se puede hacer con un tenedor).En un plato formar una montanita compresando la jamonilla.Suavizar el queso crema y untar por encima hasta cubrir toda la bola.Agregar por encima la jalea de pina.Servir con las galletas. ",
         "1 lata de jamonilla o SPAM,8 oz. de queso crema,1 taza de jalea de pina,1 paquete de galletas saladas (sugerencia: RITZ) ",
         "imagen28,jpeg",
         "76"]
    r29=["34","Jote","4","Aperitivo",
         "En un vaso mediano agregue 2/4 de vino luego incorpore 1/4 de coca cola revuelva y listo para beber,se recomienda la coca cola bien helada.",
         "Coca cola,vino chileno,hielo a gusto.",
         "imagen29.jpeg",
         "84"]
    r30=["35","Mangu cibaeno","4","Entremes",
         "Pelar los platanos y en un caldero de agua hirviendo,hecha los pedazos ya cortados,cuando esten blando hacerlo pure,para el escabeche,se echa en la cazuela un poco de aceite ,la cebolla el ajies y se deja sofreir hasta que esten blando luego coloque el caldo de pollo y el vinagre y hace una salsa riquisima y se le hecha a los platanos y a los huevos fritos",
         "6 platanos verde ,cebolla rojas ajies verdes,caldito de pollo,vinagre de manzana,aceite,queso blanco de freir o huevo y tambien salsa o pure de tomate",
         "imagen30,jpeg",
         "63"]
    
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r1)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r2)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r3)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r4)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r5)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r6)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r7)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r8)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r9)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r10)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r11)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r12)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r13)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r14)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r15)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r16)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r17)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r18)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r19)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r20)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r21)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r22)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r23)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r24)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r25)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r26)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r27)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r28)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r29)
    c.execute("INSERT INTO recetas VALUES (?,?,?,?,?,?,?,?)",r30)
    
    


    conn.commit()
