from flask import Blueprint, render_template, redirect, url_for
import os
import psycopg2
from app.forms import AppointmentForm
from datetime import datetime, timedelta

bp = Blueprint("main", __name__, "")

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route("/")
def main():
    d = datetime.now()
    return redirect(url_for(".daily", year=d.year, month=d.month, day=d.day))


@bp.route("/<int:year>/<int:month>/<int:day>", methods=["GET", "POST"])
def daily(year, month, day):
    form = AppointmentForm()

    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
            'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
            'description': form.description.data,
            'private': form.private.data
            }
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute('''
                INSERT INTO appointments (
                    name,
                    start_datetime,
                    end_datetime,
                    description,
                    private
                )
                VALUES (
                    %(name)s,
                    %(start_datetime)s,
                    %(end_datetime)s,
                    %(description)s,
                    %(private)s
                );
                ''', (
                    params
                ))


        return redirect("/")

    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            day = datetime(year, month, day)
            next_day = day + timedelta(days=1)
            sql = """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
                ORDER BY start_datetime
            """
            curs.execute(sql, {'day': day, 'next_day': next_day})
            rows = curs.fetchall()
            timeslots = [{'time': slot(day, slot_index, 8), 'open': True}
                         for slot_index in range(12 * 4)]
            overriden = 0
            for timeslot in timeslots:
                for id, name, start, end in rows:
                    if start == timeslot['time']:
                        timeslot['appointment'] = {
                            'units': int((end-start).seconds / 60 // 15),
                            'name': name,
                        }
                        overriden = timeslot['appointment']['units']
                if overriden > 0:
                    overriden -= 1
                    timeslot['open'] = False
            from pprint import pprint
            pprint(rows)
            return render_template("main.html",
                                   day=day,
                                   timeslots=timeslots,
                                   form=form)


def round_time(time):
    return time - timedelta(minutes=time.minute % 15,
                            seconds=time.second)


def slot(day, index, hours=0):
    day = datetime(day.year, day.month, day.day)
    day = day + timedelta(hours=hours)
    return day + timedelta(minutes=15 * index)
