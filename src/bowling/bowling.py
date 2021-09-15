class Bowling:
    def __init__(self):
        self.score_acum = 0
        self.score_anterior = 0
        self.score_turnos = [0]
        self.numero_tiros = 1
        self.spare = False
        self.strike = False
        self.turnos = [[] for _ in range(11)]
        self.scores = []
        self.nro_turno_actual = 0
        self.juego_perfecto = True
    def Tirar(self, pinos):
        self.turnos[self.nro_turno_actual].append(pinos)
        if len(self.turnos[self.nro_turno_actual]) == 2:
            self.nro_turno_actual += 1

        if pinos == 10:
            self.nro_turno_actual += 1


    def Score(self):
        # primer elemento
        score = 0
        i = 0
        turno_actual = self.turnos[0]
        turno_siguiente = self.turnos[i+1]

        if turno_actual[0] == 10: # strike
            if len(turno_siguiente) == 2:
                score += turno_siguiente[0] + turno_siguiente[1]
            else:
                score += 10
            score += 10
        elif turno_actual[0] + turno_actual[1] == 10: # spare
            score += turno_siguiente[0]
            score += 10
        else:
            score += turno_actual[0] + turno_actual[1]

        self.scores.append(score)

        # intermedios
        for i in range(1, len(self.turnos)-2):
            turno_actual = self.turnos[i]
            turno_siguiente = self.turnos[i+1]
            score = self.scores[i-1]

            if turno_actual[0] == 10: # strike
                if len(turno_siguiente) == 2:
                    score += turno_siguiente[0] + turno_siguiente[1]
                else:
                    score += 10
                score += 10
            elif turno_actual[0] + turno_actual[1] == 10: # spare
                score += turno_siguiente[0]
                score += 10
            else:
                score += turno_actual[0] + turno_actual[1]

            self.scores.append(score)

        # turno 10
        score = self.scores[-1]
        self.turno_actual = self.turnos[9]
        if len(turno_actual) == 1 or turno_actual[0] + turno_actual[1] == 10: # --> strike o spare
            score += 10 + self.turnos[10][0]
        else:
            score += turno_actual[0] + turno_actual[1]

        self.scores.append(score)

        for turno in self.turnos:
            if len(turno) != 1:
                self.juego_perfecto = False

        if self.juego_perfecto:
            return 300
        return self.scores[-1]
