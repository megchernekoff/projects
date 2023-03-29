import pandas as pd
import sqlite3

df = pd.read_excel('Contestants.xlsx')
tuples_list = list(df.itertuples(index=False, name=None))


if __name__ == '__main__':
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    for tup in tuples_list:
        cursor.execute("""INSERT INTO WEBSITE_CONTESTANTS (NAME, AGE, HOMETOWN, CYCLE, ELIM) VALUES {};""".format(tup))

    conn.commit()
