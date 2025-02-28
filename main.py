from fastapi import FastAPI
import random 
import string

app = FastAPI()

# Генератор паролей
@app.get("/password")
def get_password(length: int):
    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+.,'
    password = ''
    for i in range(0, int(length), 1):
        password += random.choice(characters)

    return f"password: {password}"

# Гравитация
planets = {
    "Mars": {"mass": 6.417e23, "radius": 3389500},
    "Earth": {"mass": 5.972e24, "radius": 6371000},
    "Venus": {"mass": 4.867e24, "radius": 6051800}
}

G = 6.67430e-11

@app.get("/gravity")
def get_gravity(planet: str, height: float):
    if planet not in planets:
        return {"error": "Planet not found"}
    
    mass = planets[planet]["mass"]
    radius = planets[planet]["radius"]

    gravity = (G * mass) / ((radius + height) ** 2)

    return f"gravity: {gravity}"

# Штрафы
@app.get("/speeding-fine")
def get_fine(speed: int, limit: int):
    delta = speed - limit
    
    if delta <= 10:
        fine = 0
    elif 10 < delta <= 20:
        fine = 500
    elif 20 < delta <= 40:
        fine = 1500
    elif delta > 40:
        fine = 50 * delta

    return f"fine: {fine}"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)