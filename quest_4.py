sao_paulo = 67836.43
rio = 36678.66
minas_gerais = 29229.88
espirito_santo = 27165.48
outros = 19849.53

total = sao_paulo + rio + minas_gerais + espirito_santo + outros
percentual_sp = (sao_paulo*100)/total
percentual_rj = (rio*100)/total
percentual_mg = (minas_gerais*100)/total
percentual_es = (espirito_santo*100)/total
percentual_outros = (outros*100)/total

print(f"""
A representação percentual de cada estado é de:
    - SP = {format(percentual_sp, '.2f')}%
    - RJ = {format(percentual_rj, '.2f')}%
    - MG = {format(percentual_mg, '.2f')}%
    - ES = {format(percentual_es, '.2f')}%
    - Outros = {format(percentual_outros, '.2f')}%
""")