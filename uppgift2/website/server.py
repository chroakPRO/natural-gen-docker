from flask import Flask
import psycopg2
app = Flask(__name__)


class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="host.docker.internal",
            database="postgres",
            user="postgres",
            password="postgres"
        )

    def close(self):
        self.conn.close()

    def count(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM public.results;")
            result = cur.fetchone()
            return str(result[0])
        finally:    
            cur.close()

    def largest(self):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT * FROM results WHERE original = (SELECT MAX(original) FROM results);"
            )
            result = cur.fetchone()
            return str(result[1]), str(result[2])
        finally:    
            cur.close()

 
@app.route('/')
def index():
    with open("index.html") as f:
        data = f.read()

    # try:
    conn = DatabaseConnection()
    number = conn.count()
    data = data.replace("NUMBER", number)
    largest_original, largest_factors = conn.largest()
    data = data.replace("LARGEST", f"{largest_original} = {largest_factors}")
    return data
    # except:
    #     return "Could not connect to database."
    # finally:
    #     conn.close()
 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')