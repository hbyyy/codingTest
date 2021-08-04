from pydantic import BaseModel


class Shirt(BaseModel):
    color: str
    size: str


colors = ["black", "white"]
sizes = ["S", "M", "R"]

for tshirt in (Shirt(color=c, size=s) for c in colors for s in sizes):
    print(tshirt)
