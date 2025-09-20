import flet as ft


def main(page: ft.Page):
    page.title = "Galeria"
    page.bgcolor = ft.Colors.BLACK12

    pinturas = [
        {
            "titulo": "La Gioconda",
            "autor": "Leonardo Davinci.",
            "año": 1503,
            "descripcion": (
                "La Gioconda: Enigmática sonrisa renacentista de Leonardo."
            ),
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/ProyectoBim1/refs/heads/main/gioconda.jpg",
        },
        {
            "titulo": "La noche estrellada",
            "autor": " Vincent van Gogh.",
            "año": 1889,
            "descripcion": (
                "La noche estrellada: Cielo vibrante y turbulento de Van Gogh."
            ),
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/ProyectoBim1/refs/heads/main/noche_estrellada.jpg",
        },
        {
            "titulo": "La persistencia de la memoria",
            "autor": " Salvador Dalí.",
            "año": 1931,
            "descripcion": (
                "La persistencia del tiempo: Relojes derretidos en un sueño "
                "surrealista."
            ),
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/ProyectoBim1/refs/heads/main/persistencias_de_la_memoria.webp",
        },
    ]

    indice_actual = [0]

    contenedor = ft.Container(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.GREY_300,
        alignment=ft.alignment.center,
        padding=20,
    )

    boton_siguiente = ft.ElevatedButton(text="Siguiente pintura")

    def mostrar_pintura():

        pintura = pinturas[indice_actual[0]]
        contenedor.content = ft.Column(
            [
                ft.Image(
                    src=pintura["imagen"],
                    width=300,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text(pintura["titulo"], size=20, weight=ft.FontWeight.BOLD),
                ft.Text(f"Autor:{pintura["autor"]}", size=16),
                ft.Text(f"Año: {pintura["año"]}", size=16),
                ft.Text(pintura["descripcion"], size=14, italic=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        if indice_actual[0] == len(pinturas) - 1:
            boton_siguiente.text = "Volver al inicio"
        else:
            boton_siguiente.text = "Siguiente pintura"
            page.update()

    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0] + 1) % len(pinturas)
        mostrar_pintura()

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    contenedor,
                    boton_siguiente
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

    mostrar_pintura()


ft.app(main)
