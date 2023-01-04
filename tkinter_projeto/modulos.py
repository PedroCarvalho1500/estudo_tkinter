import re
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter.constants import *
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate
import webbrowser
import sqlite3
from tkinter import filedialog 
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import base64
from tkcalendar import Calendar