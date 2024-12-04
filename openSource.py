opensource = {'ArcGIS': False, 'LibreOffice': True, 'MSOffice': False, 'Matlab': False, 'QGIS': True, 'R': True}

antwoorden = {key: value for key, value in opensource.items() if value == True}
print(list(antwoorden.keys()))
