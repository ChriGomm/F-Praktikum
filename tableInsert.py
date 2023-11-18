
def writeTable(filename,data):
    rows = len(data)
    try:
        columns = len(data[0])
    except:
        columns = rows
        rows =1
    
    with open(filename,'r+') as file:
        for line in file:
            if (line=='%#insert table here#\n'):
                file.write('\\begin{table}[H]\\begin{tabular}{|'+'c|'*columns+'}\\hline\n'+'&'*(columns-1)+'\\\\\\hline\\hline\n')
                try:
                    for row in range(rows):
                        file.write(str(data[row,0]))
                        for column in range(1,columns):
                            
                            file.write('&'+str(data[row,column]))
                        file.write('\\\\\\hline\n')
                except:
                    for row in range(rows):
                        file.write(str(data[row][0]))
                        for column in range(1,columns):
                            
                            file.write('&'+str(data[row][column]))
                        file.write('\\\\\\hline\n')
                    

                file.write('\\end{tabular}\\caption{}\\end{table}\n')
                break

