import pandas as pd

Promedios = {}

meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

for i in range(2010,2022):
    dir = str(i)+"/CO/"

    año = {}

    print(i)

    for j in range(12):

        mes = []

        print(j)

        file_name = "Promedio horarios de co"
        if(j == 0):
            file_name += ".csv"
        else:
            file_name += "("+str(j)+").csv"
        df = pd.read_csv(dir+file_name)

        for k in ["HGM","MER","CAM"]:
            if(k in df.keys()):
                print(k)
                mes.append(df[k].median())

        año[meses[j]] = mes


    #print(año)
    df = pd.DataFrame(año, index = [["HGM","MER","CAM"]])

    df = df.transpose()
    print(df)

    #Promedios[i] = df

    file_path = "mediana_CO_"+str(i)+".csv"

    df.to_csv(file_path)

    


