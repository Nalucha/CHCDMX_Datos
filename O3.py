import pandas as pd

Promedios = {}

meses = {0:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
root_dir = "Ozono/"

for i in range(2010,2022):
    dir = root_dir+str(i)+" O3/"

    año = {}

    print(i)

    list = [inner for inner in range (13)]
    list.remove(1)

    for j in list:

        mes = []

        print(j)

        file_name = "Promedio horarios de o3"
        if(j == 0):
            file_name += ".csv"
        else:
            file_name += "-"+str(j)+".csv"
        df = pd.read_csv(dir+file_name)

        for k in ["HGM", "MER", "CAM"]:
            if(k in df.keys()):
                print(k)

                mes.append(df[k].median())

        año[meses[j]] = mes


    #print(año)
    df = pd.DataFrame(año, index = [["HGM","MER","CAM"]])

    df = df.transpose()
    print(df)

    #Promedios[i] = df

    file_path = root_dir+"mediana_O3_"+str(i)+".csv"

    df.to_csv(file_path)

    


