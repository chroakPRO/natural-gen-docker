import os
import time
import psycopg2

# ==================================================
# Allt som behövs för att kommunicera med databasen


class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="host.docker.internal",
            database="postgres",
            user="postgres",
            password="postgres",
        )

    def exists(self, number):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM public.results WHERE original = " + str(number))
            result = cur.fetchall()
            return len(result) > 0
        finally:
            cur.close()

    def add(self, original, factors):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO public.results (original, factors) VALUES (%s, %s)",
                (str(original), factors),
            )
            self.conn.commit()
        finally:
            cur.close()


# ==================================================

# ==================================================
# (LÅNGSAM) ALGORITM FÖR ATT PRIMTALSFAKTORISERA


def factorize(tal):
    factors = []

    factor = 2
    while factor < tal:
        if tal % factor == 0:
            # time.sleep(0.1)
            factors.append(str(factor))
            tal = int(tal / factor)
        else:
            factor += 1
    if factor > 1:
        factors.append(str(factor))

    return "*".join(factors) if factors else str(tal)


# ==================================================

# ==================================================
# HÄR ÄR APPLIKATIONEN

# Koppla upp mot databasen och läs ENV-variabel "START_NUMBER"
database = DatabaseConnection()
START_NUMBER = int(os.environ["START_NUMBER"])
number = START_NUMBER

while True:
    # Kontrollera först om detta tal redan räknats ut, hoppa över isåfall
    if database.exists(number):
        number += 1
        continue

    # Faktorisera detta tal
    result = factorize(number)

    # Spara i databasen
    database.add(number, result)

    # Gå vidare till nästa tal
    number += 1

# ==================================================
