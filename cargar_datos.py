import pandas as pd
from sqlalchemy import create_engine

# Cargar archivo CSV
df = pd.read_csv("dataset_final.csv", encoding='latin-1')
print("Primeros registros del archivo:")
print(df.head())

# Conexión a PostgreSQL
#usuario = "postgres"
#contraseña = "eliana20062004"  
#host = "localhost"
#puerto = "5432"
#base_datos = "dataviz_db"

# Crear conexión
engine = create_engine("postgresql://dataviz_db_user:RKGos4vhuLLTFGuikahmmS5Z2VXCmoBv@dpg-d0fm94q4d50c73f29660-a.oregon-postgres.render.com/dataviz_db")

# Insertar los datos
df.to_sql("fraude", engine, if_exists="replace", index=False)

print("Datos cargados correctamente.")

