import pandas as pd

Promedios = {}

meses = {0:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
root_dir = "SO2/"

for i in range(2010,2022):
    dir = root_dir+"SO2 "+str(i)+"/"

    año_median = {}
    año_mean = {}
    año_std = {}

    print(i)

    list = [inner for inner in range (13)]
    list.remove(1)

    for j in list:

        mes_median = []
        mes_mean = []
        mes_std = []

        print(j)

        file_name = "Promedio horarios de so2"
        if(j == 0):
            file_name += ".csv"
        else:
            file_name += "-"+str(j)+".csv"
        df = pd.read_csv(dir+file_name)

        for k in ["HGM", "MER", "CAM"]:
            if(k in df.keys()):
                print(k)

                mes_median.append(df[k].median())
                mes_mean.append(df[k].mean())
                mes_std.append(df[k].std())

        año_median[meses[j]] = mes_median
        año_mean[meses[j]] = mes_mean
        año_std[meses[j]] = mes_std


    #print(año)
    df = pd.DataFrame(año_median, index = [["HGM_Mediana","MER_Mediana","CAM_Mediana"]])
    df2 = pd.DataFrame(año_mean, index = [["HGM_Promedio","MER_Promedio","CAM_Promedio"]])
    df3 = pd.DataFrame(año_std, index = [["HGM_Desviacion_Estandar","MER_Desviacion_Estandar","CAM_Desviacion_Estandar"]])

    df = df.transpose()
    df2 = df2.transpose()
    df3 = df3.transpose()
    

    #Promedios[i] = df

    file_path = root_dir+"estadisticas_SO2_"+str(i)+".csv"

    pd.concat([df,df2,df3],axis=1).to_csv(file_path)

    


