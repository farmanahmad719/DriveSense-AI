import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        db_folder = Path("data")
        db_folder.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            db_folder / "drivesense.db"
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        # Driving Sessions
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            start_time TEXT,

            end_time TEXT,

            duration INTEGER,

            average_attention REAL,

            fatigue_score REAL

        )

        """)

        # Alerts
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS alerts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            timestamp TEXT,

            alert_type TEXT,

            severity TEXT,

            message TEXT

        )

        """)

        # Statistics
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS statistics(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            blinks INTEGER,

            yawns INTEGER,

            distractions INTEGER,

            average_ear REAL,

            average_mar REAL

        )

        """)

        self.connection.commit()

    def add_session(
            self,
            start_time,
            end_time,
            duration,
            average_attention,
            fatigue_score
    ):

            self.cursor.execute("""
                INSERT INTO sessions(
                    start_time,
                    end_time,
                    duration,
                    average_attention,
                    fatigue_score
                )

                VALUES (?, ?, ?, ?, ?)

            """, (
                start_time,
                end_time,
                duration,
                average_attention,
                fatigue_score
            ))

            self.connection.commit()

            return self.cursor.lastrowid
    
    def add_alert(
        self,
        session_id,
        timestamp,
        alert_type,
        severity,
        message
    ):
        self.cursor.execute("""

            INSERT INTO alerts(
                session_id,
                timestamp,
                alert_type,
                severity,
                message
            )

            VALUES (?, ?, ?, ?, ?)

        """, (
            session_id,
            timestamp,
            alert_type,
            severity,
            message
        ))

        self.connection.commit()

    def add_statistics(
        self,
        session_id,
        blinks,
        yawns,
        distractions,
        average_ear,
        average_mar
    ):

        self.cursor.execute("""

            INSERT INTO statistics(
                session_id,
                blinks,
                yawns,
                distractions,
                average_ear,
                average_mar
            )

            VALUES (?, ?, ?, ?, ?, ?)

        """, (
            session_id,
            blinks,
            yawns,
            distractions,
            average_ear,
            average_mar
        ))

        self.connection.commit()

    def get_sessions(self):
        self.cursor.execute("SELECT * FROM sessions")
        return self.cursor.fetchall()
    
    def get_alerts(self):
        self.cursor.execute("""
            SELECT *
            FROM alerts
            ORDER BY id DESC
        """)
        return self.cursor.fetchall()
    
    def get_statistics(self):
        self.cursor.execute("SELECT * FROM statistics")
        return self.cursor.fetchall()

    def close(self):

        self.connection.close()