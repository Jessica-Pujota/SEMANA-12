#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
#Primera dimensión: Ciudades (Tabacundo, Cayambe, Ayora)
#Segunda dimensión: Días de la semana (7 días)
#Tercera dimensión: Semanas (4 semanas)

#Almacenar temperaturas diarias de las ciudades
temperaturas = [
    [   # Ciudad 1 "Tabacundo"
        [   # Semana 1
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 48},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 50},
            {"day": "Sábado", "temp": 46},
            {"day": "Domingo", "temp": 49}
       ],
        [   # Semana 2
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 53},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 57},
            {"day": "Sábado", "temp": 49},
            {"day": "Domingo", "temp": 53}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 48},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 52},
            {"day": "Jueves", "temp": 49},
            {"day": "Viernes", "temp": 51},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 49}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 48},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 49},
            {"day": "Domingo", "temp": 51}
        ]
    ],
    [   # Ciudad 2 "Cayambe"
        [   # Semana 1
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 48},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 49}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 43},
            {"day": "Martes", "temp": 46},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3 "Ayora"
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Tabacundo", "Cayambe", "Ayora"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")