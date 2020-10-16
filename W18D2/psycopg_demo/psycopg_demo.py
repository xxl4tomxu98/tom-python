import psycopg2
from pprint import pprint


CONNECTION_PARAMETERS = {
                          'dbname': 'psycopg_test_db',
                          'user': 'psycopg_test_user',
                          'password': 'password',
                          'host': 'localhost',
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    pprint(conn.get_dsn_parameters())

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute("SELECT USER;")
        result = curs.fetchone()
        pprint(result) # 'psycopg_test_user'

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute('SELECT manu_year, make, model FROM cars;')
        cars = curs.fetchall()
        for car in cars:
            pprint(car) # (1993, 'Mazda', 'Rx7')

def print_all_cars():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT manu_year, make, model, owner_id FROM cars;')
            cars = curs.fetchall()
            for car in cars:
                pprint(car)
            # alternate while print for each
            # car = curs.fetchone()
            # while car:
            #     pprint(car)
            #     car = curs.fetchone()

            # or this new way
            # while car:= curs.fetchone()
            #   pprint(car)


print_all_cars()
# Output:
# (1993, 'Mazda', 'Rx7', 1)
# ...additional cars

def get_owners_cars(owner_id):
    """
    Fetch and return all cars in the cars table
    :param owner_id: <int> the id of the owner who's cars to return
    :return: <list> the results of the query
    """
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         SELECT manu_year, make, model FROM cars
                         WHERE owner_id = %(owner_id)s
                         """,
                         {'owner_id': owner_id})
            results = curs.fetchall()
            return results

print(get_owners_cars(1)) # [(1993, 'Mazda', 'Rx7')]


def add_new_car(manu_year, make, model, owner_id):
    """
    Add the given car to the database
    :param manu_year: <int> the year the car was made
    :param make: <string> the manufacturer of the car
    :param model: <string> the model of the car
    :param owner_id: <int> the id number of the owner
    """
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            # curs.execute(f'INSERT INTO {table}{columns} VALUES{values};')
            curs.execute("""
                         INSERT INTO cars (manu_year, make, model, owner_id)
                         VALUES (%(manu_year)s, %(make)s,
                         %(model)s, %(owner_id)s)
                         """,
                         {'manu_year': manu_year,
                          'make': make,
                          'model': model,
                          'owner_id': owner_id})


add_new_car(2000, 'Ford', 'Lightning', 2)

add_new_car(1994, 'Toyota', 'Supra', 2)

print_all_cars()
# Output:
# ...additional cars
# (2000, 'Ford', 'Lightning', 2)
# (1994, 'Toyota', 'Supra', 2)

def change_car_owner(car_id, new_owner_id):
    """
    Update the owner of a car, both by record id
    :param car_id: <int> the id of the car to change
    :param new_owner_id: <int> the owner_id to give ownership to
    """
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         UPDATE cars SET owner_id = %(new_owner_id)s
                         WHERE id = %(car_id)s
                         """,
                         {'car_id': car_id,
                          'new_owner_id': new_owner_id})


change_car_owner(5, 1)

print_all_cars()
# Output:
# ...additional cars
# (1994, 'Toyota', 'Supra', 1) <- Owner is now 1


def delete_car(car_id):
    """
    Delete the record for a car given an id for that car
    :param car_id: <int> the id of the car record to remove
    """
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         DELETE FROM cars WHERE id = %(car_id)s
                         """,
                         {'car_id': car_id})


delete_car(2)

print_all_cars()
# Output:
# (1993, 'Mazda', 'Rx7', 1)
# (1994, 'Acura', 'Integra', 3)
# (2000, 'Ford', 'Lightning', 2)
# (1994, 'Toyota', 'Supra', 1)
