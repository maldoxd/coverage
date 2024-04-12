from pydantic import BaseModel


class Coverage(BaseModel):
    oop_max: int
    remaining_oop_max: int
    copay: int