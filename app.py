import streamlit as sl

sl.title(':red[Innomatics] Data Science App Internship Febuary 2023')
sl.header('My Projects App')
sl.text('Check for individual projects on the sidebar')
sl.subheader('A few illustration of streamlit.code()')
code = '''
def number_check(n):
    if n > 0:
        print('Its a positive number')
    else:
        print('Its a zero or negative number')
'''
sl.code(code,'python')
