from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def main():

    conn = psycopg2.connect(database = "test", 
                            user = "hubba", 
                            host= '10.45.80.3',
                            password = "hubba",
                            port = 5432)
    cur = conn.cursor()

    cur.execute("""CREATE TABLE test(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR (26) NOT NULL);
            """)

    cur.execute("INSERT INTO test(name) VALUES('eddie');")

    cur.execute('SELECT * FROM test;')
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    conn.close()

    return "Hello World"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
