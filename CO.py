import pandas as pd

Promedios = {}

meses = {0:'Enero',1:'Febrero',2:'Marzo',3:'Abril',4:'Mayo',5:'Junio',6:'Julio',7:'Agosto',8:'Septiembre',9:'Octubre',10:'Noviembre',11:'Diciembre'}
root_dir = "CO/"

for i in range(2010,2022):
    dir = root_dir+str(i)+"/"

    año_median = {}
    año_mean = {}
    año_std = {}

    print(i)

    for j in range(12):

        mes_median = []
        mes_mean = []
        mes_std = []

        print(j)

        file_name = "Promedio horarios de co"
        if(j == 0):
            file_name += ".csv"
        else:
            file_name += "("+str(j)+").csv"
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
    print(df2)
    

    #Promedios[i] = df

    file_path = root_dir+"estadistica_CO_"+str(i)+".csv"

    pd.concat([df,df2,df3],axis=1).to_csv(file_path)

    


