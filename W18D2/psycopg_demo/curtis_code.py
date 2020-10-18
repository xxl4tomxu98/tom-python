import psycopg2
from pprint import pprint


CONNECTION_PARAMETERS = {
                          'dbname': 'sqlalchemy_petrack',
                          'user': 'petrack_app',
                          'password': 'password',
                          'host': 'localhost',
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
  with conn.cursor() as cursor:
    cursor.execute("""
        SELECT id, first_name, last_name, email
        FROM owners
        ORDER BY last_name
    """)
    print("owners")
    # row = cursor.fetchone()
    # while row:
    #   pprint(row)
    #   row = cursor.fetchone()

    while row := cursor.fetchone():
      pprint(row)
    #pprint(cursor.fetchall())


    cursor.execute("""
        SELECT id, first_name, last_name, email
        FROM owners
        WHERE last_name like %(filter)s
        ORDER BY last_name
    """, {'filter': 'M%'})
    print("\owners M%")
    pprint(cursor.fetchall())


    # cursor.execute("""
    #     INSERT INTO owners(first_name, last_name, email)
    #     VALUES
    #     (%(first_name)s, %(last_name)s, %(email)s)
    # """, {
    #     'first_name': 'Carlsbad',
    #     "last_name": 'Koch',
    #     "email": 'carl@Koch.com'
    # })
    # cursor.execute("""
    #     SELECT id, first_name, last_name, email
    #     FROM owners
    #     ORDER BY last_name
    # """)
    # print("\owners after insert")
    # pprint(cursor.fetchall())


    #joint table example
    cursor.execute("""
        SELECT p.id, p.name, pt.type, p.age, p.has_microchip
        FROM pets p
        JOIN pet_types pt ON (p.pet_type_id = pt.id)
        ORDER BY name
    """)
    print("\npets")
    pprint(cursor.fetchall())
