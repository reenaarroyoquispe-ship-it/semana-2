print("=========================")
print("\tSISTEMA DE CONTROL DE NOTAS");
print("=========================")
suma_nota=0
cant_cursos=0
not_mayor=-1
not_menor=21
curso_mayor=""
curso_menor=""
continuar="s"
reporte_notas=""

while continuar.lower()=="s":
    print("Curso Nro:", (cant_cursos+1));
    curso=input("Ingresar curso:")
    nota=float(input("Ingresar nota [0-20]:"))
    if nota<0 or nota>20 or curso=="":
        print("Error:La nota es entre 0 y 20 y el curso no puede esatar vacia!!!")
    else:
        suma_nota+=nota
        cant_cursos+=1
        reporte_notas+=f"{curso}: {nota}\n"
        #nota maxima
        if nota>not_mayor:
            not_mayor=nota
            curso_mayor=curso
        #nota minima
        if nota<not_menor:
            not_menor=nota
            curso_menor=curso
        print("Registro Exitoso :)")
    continuar=input("Desea Continuar (s/n):")
    
print("********************")
print("\tReporte de Notas")
print("********************")
promedio=suma_nota/cant_cursos
print("Cursos:\n", reporte_notas)
print("Cursos Evaluados:", cant_cursos)
print("Promedios:", promedio)
print("La nota maxima:", curso_mayor, " ", not_mayor)
print("La nota menor:", curso_menor,"", not_menor)
if promedio<=13:
    print("Condicion academica: APROBADO");
elif promedio>=10.5:
    print("Condicion aacademica: RECUPERACION");
else:
    print("Condicion academica: DESAPROBADO");

