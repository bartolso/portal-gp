from datetime import time

V1 = {
    1: 100,
    2: 95,
    3: 90,
    4: 85,
    5: 80,
    6: 75,
    7: 70,
    8: 65,
    9: 60,
    10: 55,
    12: 50,
    14: 47,
    18: 45,
    25: 43,
    35: 40,
    45: 37,
    55: 35,
    70: 33,
    90: 30,
    110: 27,
    140: 25,
    180: 23,
    540: 20,
    300: 17,
    420: 15,
    540: 13,
    660: 10,
    780: 7,
    900: 5,
    1020: 3,
    1200: 2,
    1380: 1,
    1440: 0,
}

# PUESTO
V2 = {
    1: 100,
    2: 75,
    3: 65,
    4: 45,
    5: 30,
    6: 20,
    7: 10,
    8: 5,
    9: 5,
    10: 0,
}

# RACHA
V3 = {
    1: 0,
    2: 3,
    3: 5,
    4: 7,
    5: 10,
    6: 13,
    7: 15,
    8: 17,
    9: 20,
    10: 23,
    11: 25,
    12: 27,
    13: 30,
    14: 33,
    15: 35,
    16: 37,
    17: 40,
    18: 43,
    19: 45,
    20: 47,
    21: 50,
    22: 55,
    23: 60,
    24: 65,
    25: 70,
    26: 75,
    27: 80,
    28: 85,
    29: 90,
    30: 95,
    31: 100,
}
# DIFICULTAD TIEMPO ENTRE MBD Y DRG
D1 = {
    0: 100,
    1: 100,
    2: 95,
    3: 93,
    4: 90,
    5: 80,
    7: 70,
    10: 67,
    12: 65,
    14: 63,
    18: 60,
    25: 50,
    35: 45,
    45: 40,
    55: 35,
    70: 30,
    90: 25,
    110: 20,
    140: 15,
    180: 10,
    240: 7,
    300: 5,
    420: 3,
    540: 1,
    660: 0,
    1440: 0,
}

# DIFICULTAD HORA DEL MBD
D2 = {
    0: 10,
    60: 40,
    120: 60,
    180: 75,
    240: 100,
    300: 90,
    360: 80,
    420: 60,
    480: 50,
    540: 40,
    600: 35,
    660: 30,
    720: 30,
    780: 20,
    840: 20,
    900: 20,
    960: 20,
    1020: 10,
    1080: 10,
    1140: 0,
    1200: 0,
    1260: 0,
    1320: 0,
    1380: 10,
    1140: 10,
}

# MULTIPLICADORES
mV1 = 11
mV2 = 15
mV3 = 15
mD1 = 11
mD2 = 8

max_points = (100 * mV1) + (100 * mV2) + (100 * mV3) + (100 * mD1) + (100 * mD2)

def hour_to_minutes(t):
        return t.hour * 60 + t.minute

class GPV:
    def __init__(self, hora_mbd, hora_gp, hora_drg, puesto, racha):
        if __name__ == "__main__":
            self.hora_mbd = hora_mbd
            self.hora_gp = hora_gp
            self.hora_drg = hora_drg
        else:
            if hora_drg == None:
                self.hora_drg == time(23, 59) #si no hay drg se pone a las 23:59, mínima dificultad... no sé si es lo mejor
            else:
                self.hora_drg = hour_to_minutes(hora_drg)

            self.hora_mbd = hour_to_minutes(hora_mbd)
            self.hora_gp = hour_to_minutes(hora_gp)
            
            
        self.puesto = puesto
        self.racha = racha

    def find_closest_value(self, my_value, values):
        closest_value = min(values, key=lambda x: abs(x - my_value))

        return closest_value
    
    def get_tiempo_respuesta_points(self):
        # hora mbd, hora gp
        response_time = self.hora_gp - self.hora_mbd

        indexes_list = list(V1.keys())
        response_time_closest = self.find_closest_value(response_time, indexes_list)
        points = V1[response_time_closest]

        return points * mV1

    def get_puesto_points(self):
        # puesto
        puesto = self.puesto

        indexes_list = list(V2.keys())
        puesto_closest = self.find_closest_value(puesto, indexes_list)
        points = V2[puesto_closest]

        return points * mV2

    def get_racha_points(self):
        # racha
        racha = self.racha

        indexes_list = list(V3.keys())
        racha_closest = self.find_closest_value(racha, indexes_list)
        points = V3[racha_closest]

        return points * mV3

    def get_mbd_drg_difficulty(self):
        # hora_mbd, hora_drg

        legal_time = self.hora_drg - self.hora_mbd

        indexes_list = list(D1.keys())
        mbd_drg_difficulty_closest = self.find_closest_value(legal_time, indexes_list)
        points = D1[mbd_drg_difficulty_closest]

        return points * mD1
    
    def get_mbd_time_difficulty(self):
        # hora_mbd

        hora_mbd = self.hora_mbd

        indexes_list = list(D2.keys())
        mbd_time_difficulty_closest = self.find_closest_value(hora_mbd, indexes_list)
        points = D2[mbd_time_difficulty_closest]

        return points * mD2

    def get_gpv(self):
        gpv = self.get_tiempo_respuesta_points() + self.get_puesto_points() + self.get_racha_points() + self.get_mbd_time_difficulty() + self.get_mbd_drg_difficulty()

        return gpv
    
def main():
    # VALORES
    # hayque pasar un datetime.time, no string!!!
    hora_mbd_str = "8:00"
    hora_gp_str = "8:00"
    hora_drg_str = "9:00"
    puesto = 5
    racha = 10

    hora_mbd = hour_to_minutes(hora_mbd_str)
    hora_gp = hour_to_minutes(hora_gp_str)
    hora_drg = hour_to_minutes(hora_drg_str)

    gp = GPV(hora_mbd, hora_gp, hora_drg, puesto, racha)

    print("-----------------------")
    print("DATOS DEL GP")
    print()
    print("Hora del G.P.: " + str(hora_gp_str))
    print("Hora del M.B.D.: " + str(hora_mbd_str))
    print("Hora del Drg: " + str(hora_drg_str))
    print("Puesto: " + str(puesto))
    print("Racha: " + str(racha))
    print("-----------------------")
    print("PUNTOS")
    print()
    print("V1 Tiempo de respuesta: " + str(gp.get_tiempo_respuesta_points()) + " (x" + str(mV1) + ")")
    print("V2 Puesto: " + str(gp.get_puesto_points()) + " (x" + str(mV2) + ")")
    print("V3 Racha: " + str(gp.get_racha_points()) + " (x" + str(mV3) + ")")
    print("D1 Tiempo entre M.B.D. y Drg: " + str(gp.get_mbd_drg_difficulty()) + " (x" + str(mD1) + ")")
    print("D2 Hora del M.B.D.: " + str(gp.get_mbd_time_difficulty()) + " (x" + str(mD2) + ")")
    print("-----------------------")
    print("GPV: " + str(gp.get_gpv()))
    print("-----------------------")

if __name__ == '__main__':
    main()