from datetime import datetime
from pydantic import BaseModel

class Event(BaseModel):
    name: str
    time: datetime

event = Event(name="Release", time=datetime(2026, 6, 1, 12, 0, 0))

# Returns - python dict: {'name': 'Release', 'time': datetime.datetime(2026, 6, 1, 12, 0)}
print(event.model_dump())

# Returns - json string: {"name":"Release","time":"2026-06-01T12:00:00"}
print(event.model_dump_json())

schema = Event.model_json_schema()

print(schema)
