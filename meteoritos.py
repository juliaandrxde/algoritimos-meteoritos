#MARIA CLARA PONTES RAMALHO, TIA 42337771, SALA 01G11

import math

print("-:: Sistema para Análise de Chuva de Meteoros ::-")
print("1. Definir perímetro da propriedade e da edificação de interesse")
print("2. Unificar sistemas de coordenadas de referência")
print("3. Processar registros de chuva de meteoros")
print("4. Apresentar estatísticas")
print("5. Sair")

fim = False

# Inicialize as coordenadas da propriedade e da sede
px1, py1, px2, py2 = 0.0, 0.0, 0.0, 0.0
sx1, sy1, sx2, sy2 = 0.0, 0.0, 0.0, 0.0  

registros = []

opcao = int(input("Opção: "))

while not fim:
    if opcao == 1:
        # DEFINIR PERÍMETRO FAZENDA E SEDE
        print("Defina o perímetro da fazenda: ") 
        p = input()
        print("Defina o perímetro da sede: ") 
        s = input()
        # Divida as coordenadas em variáveis individuais
        px1, py1, px2, py2 = map(float, p.split())   #VERIFICAR 
        sx1, sy1, sx2, sy2 = map(float, s.split())

        print("Perímetro da propriedade:", (px1, py1, px2, py2))
        print("Perímetro da sede:", (sx1, sy1, sx2, sy2))

    elif opcao == 2:
        # UNIFICAR SISTEMAS DE COORDENADAS DE REFERÊNCIA
        coo = input("Insira as coordenadas: ")
        x, y = map(float, coo.split())
        distancia = math.sqrt(x * 2 + y * 2)  # RETANGULAR PARA POLAR
        angulo = math.degrees(math.atan2(y, x))
        print(distancia, angulo)
      
    elif opcao == 3:
        # PROCESSAR REGISTROS DE CHUVA DE METEOROS
        registros = []  # Limpar registros anteriores

        while True:
            try:
                distancia = float(input("Informe a distância do meteorito (em metros, negativo para sair): "))
                if distancia < 0:
                    break
                angulo = float(input("Informe o ângulo do meteorito (em graus): "))

                # Calcular as coordenadas (x, y) com base na distância e no ângulo
                x = distancia * math.cos(math.radians(angulo))
                y = distancia * math.sin(math.radians(angulo))

                # Verificar se a queda está dentro do perímetro da fazenda
                if (
                    px1 <= x <= px2 and
                    py1 <= y <= py2
                ):
                    print("A queda está dentro da propriedade da fazenda.")
                else:
                    print("A queda está fora da propriedade da fazenda.")

                registros.append((distancia, angulo))
            except ValueError:
                print("Entrada inválida. Por favor, insira valores numéricos.")

    elif opcao == 4:
        # APRESENTAR ESTATÍSTICAS
        totalQuedas = len(registros)
        quedasFazenda = 0
        atingiuSede = False

        for queda in registros:
            distancia, angulo = queda
            x = distancia * math.cos(math.radians(angulo))
            y = distancia * math.sin(math.radians(angulo))

            # Verifique se a queda está dentro do perímetro da fazenda
            if (
                px1 <= x <= px2 and
                py1 <= y <= py2
            ):
                quedasFazenda += 1

                # Verifique se a queda atingiu a sede da fazenda
                if (
                    sx1 <= x <= sx2 and
                    sy1 <= y <= sy2
                ):
                    atingiu_sede = True

        print(f"Total de quedas registradas: {totalQuedas}")
        print(f"Quedas dentro da propriedade: {quedasFazenda}({(quedasFazenda/totalQuedas) * 100:.2f}%)")

        if atingiuSede:
            print("A edificação principal foi atingida? SIM")
        else:
            print("A edificação principal foi atingida? NÃO")

    elif opcao == 5:
        fim = True
        print("Sessão encerrada")
    else:
        print("Opção inválida. Tente novamente.")
    opcao = int(input("Opção: "))