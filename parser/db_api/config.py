from environs import Env

env = Env()
env.read_env()

# Postgres credentials
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
POSTGRES_IP = env.str("PG_IP")
POSTGRES_PORT = 5432

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@localhost:{POSTGRES_PORT}/{DATABASE}"