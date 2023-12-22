"""
Esto es para leer el texto exportado de whatsapp y buscar gps mbds y drgs.

"""

import re
from datetime import datetime

ALIASES = {
    "antoni:": "Anton:",
    "Antoni:": "Anton:",
    "Sergowo Asterisco:": "Sergio:",
    "Sergio Acróbata:": "Sergio:",
    "Miden:": "Miranda:",
    "Netherlands:": "Miranda:",
    "Diego Smash:": "Diego:",
    "Paula Arcas:": "Paula:",
    "Laura Toro Diosdado:": "Laura:",
    "Jaoquien:": "Joaquin:",
    "Joaquín:": "Joaquin:",
    "aitor:": "Aitor:",
    "Miranda holanda:": "Miranda:"
}

# Formato: ['Profeta', 'fecha_inicio', 'fecha_fin']
PROFETAZGOS = [
    ['Pablo', '08/03/2022', '11/04/2023'],
    ['Laura', '18/04/2023', '10/06/2023'],
    ['Nerea', '20/06/2023', '']
]

VALID_GP_STRINGS = ['gp', 'GP', 'Gp', 'gP'] # no implementado
VALID_DRG_STRINGS = ['Drg', 'drg', 'DRG', 'Drg 🙏', 'drg 🙏', 'DRG 🙏']

# Mensajes hardcodeados para ser detectados aunque no tengan "Buenos días" en ellos. Incluye los mensajes clásicos además de algún otro random
HARDCODED_MBD_MESSAGES = [
    '¡Muy Buenos Días a Todos! Recuerden que para tener un día extraordinario es necesario hacer un gran esfuerzo ¡Que tengan una mañana tranquila y llena de oportunidades!',
    'Esta es la oportunidad para salir de tu zona de confort y tener un hermoso día, recuérdalo cuando las dificultades lleguen a ti y debas superarlas ¡Que tengan un buen día, amigos!',
    'Amigos míos, tengan presente que caemos para levantarnos, nunca se queden en el suelo ni se conformen con menos, este es un día para ser mejor que ayer. Que tengas el mejor día.',
    'Querida familia, oro para que este día sea asombroso para cada uno de ustedes, productivo y lleno de alegría y que en cada paso que den hoy nunca se apague la llama de sus sueños. Buenos días.',
    'Nos proponemos metas para cumplirlas, cada paso que damos es un nuevo objetivo, no dejes pasar un día sin trabajar por tus sueños. Es el amanecer de un nuevo día, reúne tus fuerzas para luchar, sonreír y experimentar la vida ¡Que tengas un gran día!',
    'Que tus sueños te mantengan fuerte y lleno de motivación, que sus metas hagan de esta una excelente mañana, no te olvides de celebrar y disfrutar de la vida, no te preocupes en exceso por el mañana, porque los cambios están a la orden del día.',
    'Cada nuevo día es una oportunidad para lograr más, para alcanzar nuevos sueños y perseguirlos sin cansancio. Mientras trabajas pueden practicar la gran sonrisa que tendrán en la cima ¡Disfruten de este día!',
    'Molt Bon dia a Tots! Recordin que per a tenir un dia extraordinari és necessari fer un gran esforç. Que tinguin un matí tranquil i ple d\'oportunitats!',
    'Aquesta és l\'oportunitat per a sortir de la teva zona de confort i tenir un bell dia, recorda\'l quan les dificultats arribin a tu i hagis de superar-les. Que tinguin un bon dia, amics!',
    'Amics meus, tinguin present que caiem per a aixecar-nos, mai es quedin en el sòl ni es conformin amb menys, aquest és un dia per a ser millor que ahir. Que tinguis el millor dia.',
    'Benvolguda família, or perquè aquest dia sigui sorprenent per a cadascun de vostès, productiu i ple d\'alegria i que en cada pas que donin avui mai s\'apagui la flama dels seus somnis. Bon dia.',
    'Ens proposem metes per a complir-les, cada pas que donem és un nou objectiu, no deixis passar un dia sense treballar pels teus somnis. És l\'alba d\'un nou dia, reuneix les teves forces per a lluitar, somriure i experimentar la vida. Que tinguis un gran dia!',
    'Que els teus somnis et mantinguin fort i ple de motivació, que les seves metes facin d\'aquesta un excel·lent matí, no t\'oblidis de celebrar i gaudir de la vida, no et preocupis en excés pel demà, perquè els canvis estan a l\'ordre del dia.',
    'Cada nou dia és una oportunitat per a aconseguir més, per a aconseguir nous somnis i perseguir-los sense cansament. Mentre treballes poden practicar el gran somriure que tindran en el cim. Gaudeixin d\'aquest dia!',
    'bondiarodalies😚😚\nA quina hora passa el tren de Sant Vicent de Calders🤨🤨 no puc esperar més😫😫\nNen, porto aquí mitja hora i això no ve saps😡😡'
]

# trozos de texto a buscar en un mbd. no implementado
HARCODED_MBD_STRINGS = [
    'buenos dias'
]

class WText:

    def __init__(self, text, start_date="", end_date="", use_range=False):
        self.start_date = start_date
        self.end_date = end_date
        self.use_range = use_range
        self.text = text

        self.aliases = ALIASES
        self.profetazgos = PROFETAZGOS
        self.hardcoded_messages = HARDCODED_MBD_MESSAGES
        
    def replace_with_aliases(self, text, aliases_dict):
        for alias, replacement in aliases_dict.items():
            text = text.replace(alias, replacement)
        return text
        
    def get_gps(self):
        """
            Devuelve una lista de tuples así:
            ('Fecha', 'Hora', 'Jugador', 'Mensaje gp')

        """
        pattern1 = r"(\d+/\d+/\d+), (\d+:\d+) - (\w+): (gp|Gp|GP)" 
        pattern2 = '(\d+/\d+/\d+, \d+:\d+\d+) - (.*?): (gp$|Gp$|GP$)'
        messages = re.findall(pattern1, self.replace_with_aliases(self.text, self.aliases), re.MULTILINE)

        if self.use_range == False:
            return messages
        else:
            start_date = datetime.strptime(start_date, "%y/%m/%d").date()
            end_date = datetime.strptime(end_date, "%y/%m/%d").date()

            matches = []
            for date_str, *rest in messages:
                date = datetime.strptime(date_str, "%d/%m/%y, %H:%M").date()
                if start_date <= date <= end_date:
                    matches.append((date_str, *rest))

            return [(date, time, name, message) for date, time, name, message in matches]

    def get_mbds(self):
        all_messages = []

        hardcoded_mbd_messages_string = '|'.join(HARDCODED_MBD_MESSAGES)
        for profetazgo in self.profetazgos:
            profeta_name = profetazgo[0]
            start_date = datetime.strptime(profetazgo[1], "%d/%m/%Y").date()

            end_date = profetazgo[2]
            if end_date == '':
                end_date = '01/01/2050' # increíbles hablilidades de programación para nada no tengo ni puta idea
                end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
            else:
                end_date = datetime.strptime(profetazgo[2], "%d/%m/%Y").date()

            pattern = fr"(\d+/\d+/\d+), (\d+:\d+) - ({profeta_name}): (.*buenas noches.*|.*Buenas noches.*|.*Feliz día.*|.*feliz día.*|.*bon dia.*|.*buenos días.*|.*buenos dias.*|.*bondiarodalies.*|{hardcoded_mbd_messages_string})" 
            aliases_replaced_text = self.replace_with_aliases(self.text, self.aliases)
            messages = re.findall(pattern, aliases_replaced_text, re.MULTILINE)

            matches = []
            for date_str, *rest in messages:
                date = datetime.strptime(date_str, "%d/%m/%y").date()
                if start_date <= date <= end_date:
                    matches.append((date_str, *rest))

            messages =  [(date, time, name, message) for date, time, name, message in matches]
            all_messages.append(messages)

        mbd_lists = []
        if self.use_range == False:
            mbd_lists = all_messages
        else:
            start_date = datetime.strptime(start_date, "%y/%m/%d").date()
            end_date = datetime.strptime(end_date, "%y/%m/%d").date()

            matches = []
            for date_str, *rest in messages:
                date = datetime.strptime(date_str, "%d/%m/%y, %H:%M").date()
                if start_date <= date <= end_date:
                    matches.append((date_str, *rest))

            mbd_lists = [(date, time, name, message) for date, time, name, message in matches]

        final_list = []

        for profetazgo_list in mbd_lists:
            for mbd_tuple in profetazgo_list:
                final_list.append(mbd_tuple)

        return final_list

    def get_drgs(self):
        all_messages = []

        valid_drg_strings = '|'.join(VALID_DRG_STRINGS)
        for profetazgo in self.profetazgos:
            profeta_name = profetazgo[0]
            start_date = datetime.strptime(profetazgo[1], "%d/%m/%Y").date()

            end_date = profetazgo[2]
            if end_date == '':
                end_date = '01/01/2050' # increíbles hablilidades de programación para nada no tengo ni puta idea
                end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
            else:
                end_date = datetime.strptime(profetazgo[2], "%d/%m/%Y").date()

            pattern = fr"(\d+/\d+/\d+), (\d+:\d+) - ({profeta_name}): ({valid_drg_strings})" 
            aliases_replaced_text = self.replace_with_aliases(self.text, self.aliases)
            messages = re.findall(pattern, aliases_replaced_text, re.MULTILINE)

            matches = []
            for date_str, *rest in messages:
                date = datetime.strptime(date_str, "%d/%m/%y").date()
                if start_date <= date <= end_date:
                    matches.append((date_str, *rest))

            messages =  [(date, time, name, message) for date, time, name, message in matches]
            all_messages.append(messages)

        drg_lists = []
        if self.use_range == False:
            drg_lists = all_messages
        else:
            start_date = datetime.strptime(start_date, "%y/%m/%d").date()
            end_date = datetime.strptime(end_date, "%y/%m/%d").date()

            matches = []
            for date_str, *rest in messages:
                date = datetime.strptime(date_str, "%d/%m/%y, %H:%M").date()
                if start_date <= date <= end_date:
                    matches.append((date_str, *rest))

            drg_lists = [(date, time, name, message) for date, time, name, message in matches]

        final_list = []

        for profetazgo_list in drg_lists:
            for drg_tuple in profetazgo_list:
                final_list.append(drg_tuple)

        return final_list


if __name__ == '__main__':
    with open("chat.txt", "r", encoding='utf-8') as f:
        text = f.read()
        
        wtext = WText(text=text, use_range=False)
        
        for drg in wtext.get_drgs():
            print(drg)
        