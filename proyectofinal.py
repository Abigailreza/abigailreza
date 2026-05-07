import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("550x550")
    reg.resizable(False, False)
    reg.configure(bg="#ffe4ec")

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="REGISTRO DE PRODUCTOS",
        font=("Arial", 20, "bold"),
        bg="#ffe4ec",
        fg="#c2185b"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame = tk.Frame(
        reg,
        bg="white",
        bd=3,
        relief="ridge"
    )
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # -------------------------
    # ESTILOS
    # -------------------------
    fuente_label = ("Arial", 12, "bold")
    fuente_entry = ("Arial", 12)

    color_label = "#d63384"
    color_entry = "#fff0f5"

    # -------------------------
    # ID PRODUCTO
    # -------------------------
    lbl_id = tk.Label(
        frame,
        text="ID del Producto",
        font=fuente_label,
        bg="white",
        fg=color_label
    )
    lbl_id.pack(pady=(20,5))

    txt_id = tk.Entry(
        frame,
        font=fuente_entry,
        bg=color_entry,
        width=35,
        relief="flat"
    )
    txt_id.pack(ipady=6)

    # -------------------------
    # DESCRIPCIÓN
    # -------------------------
    lbl_desc = tk.Label(
        frame,
        text="Descripción",
        font=fuente_label,
        bg="white",
        fg=color_label
    )
    lbl_desc.pack(pady=(15,5))

    txt_desc = tk.Entry(
        frame,
        font=fuente_entry,
        bg=color_entry,
        width=35,
        relief="flat"
    )
    txt_desc.pack(ipady=6)

    # -------------------------
    # PRECIO
    # -------------------------
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        font=fuente_label,
        bg="white",
        fg=color_label
    )
    lbl_precio.pack(pady=(15,5))

    txt_precio = tk.Entry(
        frame,
        font=fuente_entry,
        bg=color_entry,
        width=35,
        relief="flat"
    )
    txt_precio.pack(ipady=6)

    # -------------------------
    # CATEGORÍA
    # -------------------------
    lbl_categoria = tk.Label(
        frame,
        text="Categoría",
        font=fuente_label,
        bg="white",
        fg=color_label
    )
    lbl_categoria.pack(pady=(15,5))

    txt_categoria = tk.Entry(
        frame,
        font=fuente_entry,
        bg=color_entry,
        width=35,
        relief="flat"
    )
    txt_categoria.pack(ipady=6)

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validar campos vacíos
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            precio_float = float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser numérico."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as file:
            file.write(
                f"{id_prod}|{descripcion}|{precio_float}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        frame,
        text="GUARDAR PRODUCTO",
        command=guardar_producto,
        bg="#ff69b4",
        fg="white",
        activebackground="#ff1493",
        activeforeground="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="flat",
        cursor="hand2"
    )
    btn_guardar.pack(pady=30)


def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de registro de ventas."
    )


def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes."
    )


def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - AbigailReza v1")
ventana.geometry("500x650")
ventana.resizable(False, False)
ventana.configure(bg="#ffe4ec")

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))
    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="#ffe4ec"
    )
    lbl_logo.pack(pady=20)

except:
    lbl_sin_logo = tk.Label(
        ventana,
        text="(Aquí va el logo del sistema)",
        font=("Arial", 14),
        bg="#ffe4ec"
    )
    lbl_sin_logo.pack(pady=40)

# -------------------------
# TÍTULO PRINCIPAL
# -------------------------
titulo_principal = tk.Label(
    ventana,
    text="PUNTO DE VENTA",
    font=("Arial", 22, "bold"),
    bg="#ffe4ec",
    fg="#c2185b"
)
titulo_principal.pack(pady=10)

# -------------------------
# ESTILO BOTONES
# -------------------------
color_boton = "#ff69b4"
color_texto = "white"

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = tk.Button(
    ventana,
    text="Registro de Productos",
    command=abrir_registro_productos,
    bg=color_boton,
    fg=color_texto,
    activebackground="#ff1493",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=28,
    height=2,
    relief="flat",
    cursor="hand2"
)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(
    ventana,
    text="Registro de Ventas",
    command=abrir_registro_ventas,
    bg=color_boton,
    fg=color_texto,
    activebackground="#ff1493",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=28,
    height=2,
    relief="flat",
    cursor="hand2"
)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(
    ventana,
    text="Reportes",
    command=abrir_reportes,
    bg=color_boton,
    fg=color_texto,
    activebackground="#ff1493",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=28,
    height=2,
    relief="flat",
    cursor="hand2"
)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(
    ventana,
    text="Acerca de",
    command=abrir_acerca_de,
    bg=color_boton,
    fg=color_texto,
    activebackground="#ff1493",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=28,
    height=2,
    relief="flat",
    cursor="hand2"
)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO APP
# -------------------------
ventana.mainloop()