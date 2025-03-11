from pydantic import BaseModel as Base


class Live(Base):
    live: bool
    title: str
