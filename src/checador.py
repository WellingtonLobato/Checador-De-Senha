#! /usr/bin/python env
# -*- coding: utf-8 -*-
__author__ = 'Jose Augusto'
'''
Script para checar se sua senha é segura! script em constate evolução! Contribua!
'''

senha = input('Digite a senha a ser testada: ')

if len(senha) < 15:
    print("Senha menor que 15 caracteres! não é segura!")

elif len(senha) > 15:
    print("Maior que 15 Senha boa!")

if senha.isdigit():
    print("Sua senha contem apenas numeros! não é segura!")
