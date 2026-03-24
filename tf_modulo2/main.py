from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load
from tabulate import tabulate

def main():
    data = extract()
    
    data_transform = transform(data)
    cabeceras = ['nombre','capital','region','poblacion']
    print(tabulate(data_transform,headers=cabeceras,tablefmt='grid'))
    
    resultado = load(data_transform)
    print(f' Se insertaron {resultado} registros en la base de datos')
  
    
if __name__ == "__main__":
    main()