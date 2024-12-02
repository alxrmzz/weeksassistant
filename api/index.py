import json

def handler(request):
    from datetime import datetime
import pytz

gdl = pytz.timezone('America/Mexico_City')
hoy = datetime.now(gdl)
hoy_str = hoy.strftime("%d %m %Y")
hoy_int = datetime.strptime(hoy_str, "%d %m %Y").date()
born = datetime(2009, 3, 15)
born_str = born.strftime("%d %m %Y")
born_int = datetime.strptime(born_str, "%d %m %Y").date()
diff = hoy_int - born_int
weeks = diff.days / 7
round_weeks = int(weeks)
dayweek_now = weeks - round_weeks
def solomon_grundy(today):
    if today < 0.05:
      return 0 
    elif today < 0.15:
      today = 1
    elif today < 0.30:
      today = 2
    elif today < 0.45:
      today = 3
    elif today < 0.60:
      today = 4
    elif today < 0.75:
      today = 5
    elif today < 0.90:
      today = 6
    else:
      today = 0
    return today

dayweek_now = solomon_grundy(dayweek_now)
result = f"{round_weeks}.{dayweek_now}"
print("Hoy es: " + hoy_str)
print(f"Tienes {result} semanas, Alex")
    

    # Retorna una respuesta HTTP
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Script ejecutado exitosamente"})
    }
