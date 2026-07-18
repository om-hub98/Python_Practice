from pydantic import BaseModel, ValidationError, Field

class User(BaseModel):
    id: int
    name:str
    email:str
    age:int

user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)  

print(user)