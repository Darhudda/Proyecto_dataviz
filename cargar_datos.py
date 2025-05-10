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
engine = create_engine(os.environ.get("DATABASE_URL"))

# Insertar los datos
df.to_sql("fraude", engine, if_exists="replace", index=False)

print("Datos cargados correctamente.")

