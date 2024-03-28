def funcion_colores_params(params, columnas_plot):
    # Define listas de columnas con nombres específicos
    lista_ataque = ['Asistencias', 'Goles para empatar', 'Regates en zona peligrosa', '% Regates en zona peligrosa con éxito','Regates en zona peligrosa con éxito',
    '% Regates con éxito',
    'Regates',
    'Regates con éxito',
    'Primeros goles',
    'Goles de falta',
    'Goles después de córner',
    'Goles después de falta',
    'Goles tras centro',
    'Goles desde fuera del área',
    'Goles',
    '% Efectividad',
    'Goles de cabeza',
    'Goles con la izquierda',
    'Goles de penalti',
    'Penaltis lanzados',
    'Penaltis provocados',
    'Pre-asistencias',
    'Goles con la derecha',
    'Progresiones con balón',
    '% Progresiones con balón con éxito',
    'Progresiones con balón con éxito',
    'Pases que acaban en tiro',
    'Pases previos a tiro (C-At)',
    'Tiros dentro del área',
    'Tiros tras centro',
    'Tiros fuera del área',
    'Pases que acaban en TP',
    'Goles (s.p.) por Disparo',
    'Tiros',
    'Tiros bloq. (ATA)',
    'Tiros a puerta',
    'Tiros por tiro a puerta',
    'Tiros por gol',
    'Tiros tras regate con éxito',
    'Toques en el área',
    'xA / Pases clave',
    'xA',
    'xG por disparo',
    'xG en contra (tiros a puerta)',
    'xG']

    lista_defensa = ['Tiros bloq. (DEF)',
    'Despejes',
    'Recuperaciones en últ. tercio',
    '1x1 Defensivos',
    '% 1x1 Defensivos con éxito',
    '1x1 Defensivos con éxito',
    'Recuperaciones en campo rival',
    'Penaltis cometidos',
    'Presiones defensivas (ind.)',
    'Intercepciones',
    'Recuperaciones',
    'Rec. rápidas tras pérdida',
    'Entradas']

    lista_duelos = ['Duelo defensivo por falta',
    '% Duelos aéreos ganados',
    'Duelos aéreos',
    'Duelos aéreos ganados',
    'Duelos defensivos',
    '% Duelos defensivos ganados',
    'Duelos defensivos ganados',
    'Duelos',
    '% Duelos ganados',
    'Duelos ganados',
    'Duelos en el suelo',
    '% Duelos en el suelo con éxito',
    'Duelos en el suelo con éxito',
    'Duelos ofensivos',
    '% Duelos ofensivos ganados',
    'Duelos ofensivos ganados']

    lista_distribucion = ['Pases hacia atrás',
    'Centros',
    '% Centros con éxito',
    'Centros con éxito',
    'Centros al área',
    '% Centros al área con éxito',
    'Centros al área con éxito',
    'Pases clave',
    '% Pases largos con éxito',
    '% Pases con éxito',
    'Pases intentados',
    'Pases previos a pérdida',
    'Pases con éxito',
    'Pases al último tercio',
    '% Pases al último tercio con éxito',
    'Pases al último tercio con éxito',
    'Pases al área',
    '% Pases al área con éxito',
    'Pases al área con éxito',
    'Pases progresivos',
    '% Pases progresivos con éxito',
    'Pases progresivos con éxito',
    'Pases verticales',
    'Pases profundos']

    lista_general = [ 'Aceleraciones',
    'Tarjetas provocadas',
    'Tarjetas',
    '% Porterías a cero',
    'Diferencial NPxG',
    'Diferencial xG',
    'Expulsiones',
    'Faltas',
    'NPxG',
    'NPxG por disparo',
    'Fueras de juego',
    'Goles en propia puerta',
    'Pérdidas en campo propio',
    'Pérdidas de balón',
    'Faltas recibidas',
    'Tarjetas rojas',
    'Goles para ganar',
    'Tarjetas amarillas']

    lista_porteros = ['Goles de falta concedidos',
    'Goles encajados',
    'Goles de cabeza concedidos',
    'Salidas por alto',
    'Goles lejanos concedidos',
    'Pases largos',
    'Pases largos con éxito',
    'Penaltis parados',
    'Goles de penalti concedidos',
    'Rechaces tras penalti',
    'Paradas por gol encajado',
    'Paradas',
    '% Paradas por tiros a puerta recibidos',
    'Tiros a puerta recibidos',
    'Superparadas',
    'Goles evitados']

    # Define colores correspondientes a cada lista de columnas
    color_lista_1 = '#01C52B'  # Verde
    color_lista_2 = '#A82AFF'  # Morado
    color_lista_3 = '#D70232'  # Rojo
    color_lista_4 = '#FF9300'  # Naranja
    color_lista_5 = '#1A78CF'  # Azul
    color_lista_6 = '#DDDBDE'  # Gris

    # Crea un diccionario que mapee los nombres de columna a sus colores correspondientes
    column_color_mapping = {}

    # Asigna colores a las columnas en cada lista
    for column in params:
        if column in lista_ataque:
            column_color_mapping[column] = color_lista_1
        elif column in lista_defensa:
            column_color_mapping[column] = color_lista_2
        elif column in lista_duelos:
            column_color_mapping[column] = color_lista_3
        elif column in lista_distribucion:
            column_color_mapping[column] = color_lista_4
        elif column in lista_general:
            column_color_mapping[column] = color_lista_5
        elif column in lista_porteros:
            column_color_mapping[column] = color_lista_6
        else:
            column_color_mapping[column] = 'lightblue'  # Color predeterminado para otras columnas

    # Crea la lista de colores de rebanadas usando el diccionario de mapeo de columnas a colores
    slice_colors = [column_color_mapping[column[:-10]] for column in columnas_plot]

    return slice_colors