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
            {"day": "Lunes", "temp": 41},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 48},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 46},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp":44},
            {"day": "Martes", "temp": 47},
            {"day": "Miércoles", "temp": 49},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 44},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # Ciudad 3 "Ayora"
        [   # Semana 1
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 44},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 40},
            {"day": "Domingo", "temp": 39}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
i=0;
for ciudad in temperaturas:
    i=i+1
    print(f'Ciudad No. {i}')
    j=0
    for semana in ciudad:
        j=j+1
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = round(suma / 7,2)
        promedio_celsius = round((promedio - 32 ) * (5/9),2)
        print(f'El promedio de de la semana No. {j} es: {promedio_celsius}')