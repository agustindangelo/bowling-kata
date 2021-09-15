import pytest
from bowling.bowling import Bowling

def test_peor_juego():
    bowling = Bowling()
    for turno in range(10):
        for tiro in range(2):
            bowling.Tirar(0)
    score = bowling.Score()
    assert score == 0

def test_tire_todos_1():
    bowling = Bowling()
    for turno in range(10):
        bowling.Tirar(1)
        bowling.Tirar(1)
    score = bowling.Score()
    assert score == 20

def test_al_menos_un_spare():
    bowling = Bowling()
    # Turno 1
    bowling.Tirar(3)
    bowling.Tirar(7)
    # Turno 2
    bowling.Tirar(2)
    bowling.Tirar(2)
    for turno in range(8):
        for tiro in range(2):
            bowling.Tirar(0)
    score = bowling.Score()
    assert score == 16

def test_al_menos_un_strike():
    bowling = Bowling()
    # Turno 1
    bowling.Tirar(10)
    # Turno 2
    bowling.Tirar(2)
    bowling.Tirar(2)
    for turno in range(8):
        for tiro in range(2):
            bowling.Tirar(0)
    score = bowling.Score()
    assert score == 18

def test_un_spare_un_strike():
    bowling = Bowling()
    # Turno 1
    bowling.Tirar(2) # --> 20
    bowling.Tirar(8)
    # Turno 2
    bowling.Tirar(10) # --> 20+10+2 = 32
    for turno in range(8):
        for tiro in range(2):
            bowling.Tirar(1)
    score = bowling.Score() # --> 32 + 8*2 = 48
    assert score == 48

def test_todos_spare():
    bowling = Bowling()
    for turno in range(10):
        bowling.Tirar(5)
        bowling.Tirar(5)
    bowling.Tirar(5)
    score = bowling.Score()
    assert score == 150

def test_todos_strike():
    bowling = Bowling()
    for turno in range(10):
        bowling.Tirar(10)
    bowling.Tirar(10)
    score = bowling.Score()
    assert score == 300
