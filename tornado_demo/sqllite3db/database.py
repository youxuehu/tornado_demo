# !/usr/bin/env python
# coding: UTF-8
"""A lightweight wrapper around SQLite3."""

import sqlite3
import copy
import itertools
import logging
import time


class Connection(object):

    """A lightweight wrapper around Sqlite3 connections.
    The main value we provide is wrapping rows in a dict/object so that
    columns can be accessed by name. Typical usage:
        sqllite3db = database_sqlite3.ConnectionSqlite3("/path/to/test.sqllite3db")
        for article in sqllite3db.query("SELECT * FROM articles"):
            print article.title
    Cursors are hidden by the implementation, but other than that, the methods
    are very similar to the sqlite3 API.
    We explicitly set the timezone to UTC and the character encoding to
    UTF-8 on all connections to avoid time zone and encoding errors.
    """

    def __init__(self, database=":memory:", host="localhost", user=None, password=None, max_idle_time=7 * 3600):
        self.host = host
        self.database = database
        self.max_idle_time = max_idle_time

        args = dict(db=database)
        self._db = None
        self._db_args = args
        self._last_use_time = time.time()
        try:
            self.reconnect()
        except:
            logging.error("Cannot connect to Sqlite3 on %s", self.host, exc_info=True)

    def __del__(self):
        self.close()

    def cursor(self):
        return self._cursor

    def close(self):
        """Closes this database connection."""
        if getattr(self, "_db", None) is not None:
            self._db.close()
            self._db = None

    def reconnect(self):
        """Closes the existing database connection and re-opens it."""
        self.close()
        self._db = sqlite3.connect(self.database)
        self.isolation_level = None  # similar to mysql self._db.autocommit(True)

    def iter(self, query, *parameters):
        """Returns an iterator for the given query and parameters."""
        self._ensure_connected()
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            for row in cursor:
                yield Row(zip(column_names, row))
        finally:
            cursor.close()

    def query(self, query, *parameters):
        """Returns a row list for the given query and parameters."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            column_names = [d[0] for d in cursor.description]
            return [Row(zip(column_names, row)) for row in cursor]
        finally:
            pass  # cursor.close()

    def get(self, query, *parameters):
        """Returns the first row returned for the given query."""
        rows = self.query(query, *parameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    def execute(self, query, *parameters):
        """Executes the given query, returning the lastrowid from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def executemany(self, query, parameters):
        """Executes the given query against all the given param sequences.
        We return the lastrowid from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def _ensure_connected(self):
        # if  coonection has been idle for too long (7 hours by default).
        # pre-emptive
        if self._db is None or (time.time() - self._last_use_time > self.max_idle_time):
            self.reconnect()
        self._last_use_time = time.time()

    def _cursor(self):
        self._ensure_connected()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters):
        try:
            cursor.execute(query, parameters)
            self._db.commit()
            return
        except OperationalError:
            logging.error("Error connecting to SQLite3 on %s", self.host)
            self.close()
            raise


class Row(dict):
    """A dict that allows for object-like property access syntax."""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


# Alias some common Sqlite3 exceptions
IntegrityError = sqlite3.IntegrityError
OperationalError = sqlite3.OperationalError


#
# Havent ported field-types over from Mysql to Sqlite3
#
# Fix the access conversions to properly recognize unicode/binary
# FIELD_TYPE = MySQLdb.constants.FIELD_TYPE
# FLAG = MySQLdb.constants.FLAG
# CONVERSIONS = copy.deepcopy(MySQLdb.converters.conversions)
#
# field_types = [FIELD_TYPE.BLOB, FIELD_TYPE.STRING, FIELD_TYPE.VAR_STRING]
# if 'VARCHAR' in vars(FIELD_TYPE):
#    field_types.append(FIELD_TYPE.VARCHAR)
# for field_type in field_types:
#    CONVERSIONS[field_type].insert(0, (FLAG.BINARY, str))
#
