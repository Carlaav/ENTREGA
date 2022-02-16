from random import randint
cobro_por_hora= 10
total= 0
for i in range(51):
    horas_trabajadas= randint(35,50)
    salario_base=  horas_trabajadas*cobro_por_hora
    horas_extras= (horas_trabajadas-35)
    if horas_trabajadas==35:
        print(salario_base)
        total= total + salario_base
    elif horas_trabajadas>35 and horas_trabajadas<=43:
        salario_horas_extras= salario_base+ horas_extras*1.25
        total= total+ salario_horas_extras
    elif horas_trabajadas> 43:
        horas_extras_plus= horas_trabajadas-43
        salario_horas_extras_plus= salario_base+ horas_extras*1.25 + horas_extras_plus*1.5
        total= total+ salario_horas_extras_plus

print(total)



