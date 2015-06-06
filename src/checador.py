#! /usr/bin/python env
# -*- coding: utf-8 -*-
__author__ = 'Jose Augusto'
'''
Script para checar se sua senha é segura! script em constate evolução! Contribua!
'''

#Função para checar a senha digitada pelo usuario
def Checador(senha):
    if len(senha) < 15:
        print("Senha menor que 15 caracteres! não é segura!")
        
    elif len(senha) > 15:
        print("Maior que 15 Senha boa!")

    if senha.isdigit(): #Estava com elif, mas não seria possivel alcançar essa condição(Ou ela é menor que 15, ou maior que quinze, ou tem só digito). Se colocar um if, ele verifica o tamanho e se a string é composta só por numeros 
        print("Sua senha contem apenas numeros! não é segura!")
        
    elif senha.isalpha(): #Verifica se só tem letras na senha
        print("Sua senha contem apenas letras! não é segura!")
        
    else:
        print("Sua senha contem letras e numeros! Senha boa")
        

if __name__ == "__main__":
    senha = input('Digite a senha a ser testada: ')
    Checador(senha)

