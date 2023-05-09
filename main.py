# Import packages
from dash import Dash
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP

import os
from dotenv import load_dotenv
import mysql.connector



def main() -> None:

    # Load environment variables
    load_dotenv("/home/javier/Universidad/Master/2º Semestre/Biological databases/.env")

    # Get MySQL username and password from environment variables
    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")

    db = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="master_app"
    )

    

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Master app"
    app.layout = create_layout(app,db)
    app.run()
    db.close()


if __name__ == "__main__":
    main()