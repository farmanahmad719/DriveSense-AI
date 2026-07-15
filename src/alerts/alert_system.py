from datetime import datetime


class AlertSystem:

    def __init__(self, max_alerts=50):

        self.max_alerts = max_alerts
        self.alerts = []

    def add_alert(self, severity, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        alert = {
            "time": timestamp,
            "severity": severity,
            "message": message
        }

        self.alerts.insert(0, alert)

        if len(self.alerts) > self.max_alerts:
            self.alerts.pop()

    def get_alerts(self):
        return self.alerts

    def clear(self):
        self.alerts.clear()