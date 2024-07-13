from datetime import datetime, date

from django.urls.converters import StringConverter


class DateConverter(StringConverter):
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)
