from flask import Flask, render_template, flash, request
from config import Config
import schedule
import time
import webbrowser, os, sys


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(Config)
from app import routes


if __name__ == "__main__":
    app.run()
    
 