import pyautogui
import time

# pyautogui.click => clicar em algo
# pyautogui.write => escrever um texto
# pyautogui.press => precionar uma tecla
#pyautogui => .hotkey("ctrl", "v")

pyautogui.PAUSE = 0.5

# entrar na página
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# preencher o formulário

# pyautogui.click(x=714, y=465)
pyautogui.press('tab')
pyautogui.write('lelele')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')

#importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

#cadastrar um dado na tabela

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.press('tab')
    pyautogui.write(codigo)

    marca = tabela.loc[linha, "marca"]

    pyautogui.press('tab')
    pyautogui.write(marca)

    tipo = tabela.loc[linha, "tipo"]

    pyautogui.press('tab')
    pyautogui.write(tipo)

    categoria = tabela.loc[linha, "categoria"]

    pyautogui.press('tab')
    pyautogui.write(str(categoria))

    preco = tabela.loc[linha, "preco_unitario"]

    pyautogui.press('tab')
    pyautogui.write(str(preco))

    custo = tabela.loc[linha, "custo"]

    pyautogui.press('tab')
    pyautogui.write(str(custo))

    obs = tabela.loc[linha, "obs"]

    if pandas.isna(obs):
        pyautogui.press('tab')  
        
    pyautogui.press('tab')
    pyautogui.press("enter")
    pyautogui.press("f5")