

def magic (dia, mes, ano):
    if dia * mes == ano % 100:
        return True
    else:
        return False





for dia in range(1, 32):
    for mes in range (1 ,13):
        for ano in range (1901, 2001):
            ano_magico = magic(dia, mes, ano)
            if ano_magico == True:
                print(f"Data mágica: {dia}/{mes}/{ano}")
    
    
    
            
                
                
        
    
    