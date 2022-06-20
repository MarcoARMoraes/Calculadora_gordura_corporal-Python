from tkinter import *
import math

#JANELA
menu_inicial = Tk()
menu_inicial.title('CÁLCULO DE GORDURA CORPORAL')
menu_inicial.geometry("530x460")
menu_inicial.resizable(False, False)

#FUNÇÕES
#PARA OS CÁLCULOS
def gordura_corporal_homem():
        A = int(textbox_altura.get())
        C = int(textbox_cintura.get())
        P = int(textbox_pescoco.get())
        #label_resultado['text'] = (f'{A} \n {C} \n {P} \n {Q}') #como fiz antes para mostrar os dados no label resultado

        LOG_A = math.log10(A)
        LOG_C_P = math.log10(C - P)

        GC_H = (495 / (1.033 - 0.191 * (LOG_C_P) + 0.155 * (LOG_A))) - 450

        # HOMENS
        if GC_H < 3 and GC_H < 6:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nNível de COMPETIÇÃO')
        elif GC_H <= 9:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nNível ATLÉTICO')
        elif GC_H < 10 and GC_H < 14:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nVocê está EM BOA FORMA')
        elif GC_H < 15 and GC_H < 19:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nTaxa de gordura considerada NORMAL')
        elif GC_H < 20 and GC_H < 25:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nTaxa de gordura considerada ALTA')
        elif GC_H < 26 and GC_H < 30:
            label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_H:.1f}% \nTaxa de gordura considerada MUITO ALTA')

def gordura_corporal_mulher():
    A = int(textbox_altura.get())
    C = int(textbox_cintura.get())
    P = int(textbox_pescoco.get())
    Q = int(textbox_quadril.get())
    # label_resultado['text'] = (f'{A} \n {C} \n {P} \n {Q}') #como fiz antes para mostrar os dados no label resultado

    LOG_A = math.log10(A)
    LOG_Q_C_P = math.log10(Q + C - P)

    GC_M = (495 / (1.296 - 0.350 * (LOG_Q_C_P) + 0.221 * (LOG_A))) - 450

    #MULHERES
    if GC_M < 9 and GC_M < 12:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nNível de COMPETIÇÃO')
    elif GC_M <= 15:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nNível ATLÉTICO')
    elif GC_M > 16 and GC_M < 20:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nVocê está EM BOA FORMA')
    elif GC_M > 21 and GC_M < 25:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nTaxa de gordura considerada NORMAL')
    elif GC_M < 26 and GC_M < 30:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nTaxa de gordura considerada ALTA')
    elif GC_M > 31 and GC_M < 40:
        label_resultado['text'] = (f'\nSeu percentual de gordura corporal é {GC_M:.1f}% \nTaxa de gordura considerada MUITO ALTA')

#PARA VER OS RADIO BUTTONS FUNCIONAREM
def ver_radio():
    valor_funcao_radio = valor_botao_radio.get()
    if valor_funcao_radio == "masculino":
        #print("Sexo Masculino") #usei como teste de funcionalidade do RADIO
        label_quadril.grid_forget()
        label_vazia.grid(row=5, column=1)
        textbox_quadril.grid_forget()
        cmd_mulher.grid_forget()
        cmd_homem.grid(row=6, column=0)

    elif valor_funcao_radio == "feminino":
        #print("Sexo feminino") #usei como teste de funcionalidade do RADIO
        label_quadril.grid(row=5, column=0)
        textbox_quadril.grid(row=5, column=1)
        cmd_homem.grid_forget()
        cmd_mulher.grid(row=6, column=0)


def limpa_resultado():
    label_resultado['text'] = ""


#VARIÁVEL PARA DIFERENCIAR A SELEÇÃO DE GÊNERO
#valor_a = IntVar()
valor_botao_radio = StringVar()

#JANELA
frame0_janela = Frame(menu_inicial)
frame1_janela = Frame(menu_inicial)
frame2_janela = Frame(menu_inicial)
frame3_janela = Frame(menu_inicial)
frame4_janela = Frame(menu_inicial)

#label_generos
label_generos = Label(frame0_janela, text="Escolha o seu gênero a seguir: ", font="Arial 10 bold", bd=15)

#radio button mulher
ra_feminino = Radiobutton(frame1_janela, text="Feminino", variable=valor_botao_radio, value="feminino", bd=10,
                                  command=ver_radio)
ra_feminino.select()

#radiobutton homem
ra_masculino = Radiobutton(frame1_janela, text="Masculino", variable=valor_botao_radio, value="masculino", bd=10,
                           command=ver_radio)

#label1
label_altura = Label(frame2_janela, text="Insira a sua altura (cm): ", font="Arial 10 bold", bd=10)

#text1
textbox_altura = Entry(frame2_janela, bd=3)
textbox_altura.focus()

#label2
label_cintura = Label(frame2_janela, text="Insira a sua medida de cintura (cm): ", font="Arial 10 bold", bd=10)

#text2
textbox_cintura = Entry(frame2_janela, bd=3)

#label3
label_pescoco = Label(frame2_janela, text="Insira a medida do seu pescoço (cm): ", font="Arial 10 bold", bd=10)

#text3
textbox_pescoco = Entry(frame2_janela, bd=3)

#label4
label_quadril = Label(frame2_janela, text="Insira a medida do seu quadril (cm): ", font="Arial 10 bold", bd=10)

#label_vazia
label_vazia = Label(frame2_janela, font="Arial 10 bold", bd=10, width=0)

#text4
textbox_quadril = Entry(frame2_janela, bd=3)

#BOTÃO
cmd_homem = Button(frame3_janela, text="Calcular", bd=3, command=lambda: [gordura_corporal_homem(), ver_radio()])
cmd_mulher = Button(frame3_janela, text="Calcular", bd=3, command=lambda: [gordura_corporal_mulher(), ver_radio()])
cmd_limpar = Button(frame3_janela, text="Limpar", bd=3, command=limpa_resultado)

#LABEL RESULTADO
label_resultado = Label(frame4_janela, text="", width=60, height=8, padx=25, relief='groove',
                        font="Arial 10 bold")
label_resultado.place(x=10, y=10)

#ASSINATURA
label_assinatura = Label(frame4_janela, text="Desenvolvido por Marco Moraes", font="Arial 10 italic", bd=10)

#FECHAMENTO DE FRAMES
frame0_janela.grid()
frame1_janela.grid()
frame2_janela.grid()
frame3_janela.grid()
frame4_janela.grid()

#LAYOUT
label_generos.grid()
ra_feminino.grid(row=1, column=0)
ra_masculino.grid(row=1, column=1)
label_altura.grid(row=2, column=0)
textbox_altura.grid(row=2, column=1)
label_cintura.grid(row=3, column=0)
textbox_cintura.grid(row=3, column=1)
label_pescoco.grid(row=4, column=0)
textbox_pescoco.grid(row=4, column=1)
label_quadril.grid(row=5, column=0)
textbox_quadril.grid(row=5, column=1)
cmd_mulher.grid(row=6, column=0)
cmd_limpar.grid(row=6, column=1)
label_resultado.grid()
label_assinatura.grid()

#FIM
menu_inicial.mainloop()