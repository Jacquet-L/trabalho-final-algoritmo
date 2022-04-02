from turtle import clear


prodict=dict()
listProd=[]
while True:
    prodict={}
    prodict["codigo"]=int(input("Entre o codigo:"))
    prodict["nome"]=str(input("Entre o nome:"))
    prodict["preco"]=float(input("Entre o preco:"))
    prodict["QdEmestoque"]=int(input("Entre a qantidade:"))
    listProd.append(prodict)
    while True:
        Question=str(input("deseja continuar? S/N")).upper()[0]
        if Question in "SN":
            break
        print("Erro!!! a sua resposta tem que ser S/N")
    if Question=="N":
        break
print(listProd)

vCod=int(input("digite o codigo do producto"))
verificador=False
for prd in listProd:
    if prd["codigo"]==vCod:
        preco=float(input("digite o preco:"))
        qdemstoque=int(input("digite a quantidade em estoque:"))
        prd["preco"]=preco
        prd["QdEmestoque"]=qdemstoque
        verificador=True
    if not verificador:
        print("Erro!!! o produto que voce digitou nao foi encontrado")
print(listProd)
while True:       
    codDacompra=int(input("Digite o codigo:"))
    preso=0
    for prd in listProd:
        if prd["codigo"]==codDacompra:
            QdAsercomprada=int(input("quantos produos12 que deseja comprar?:"))
            if QdAsercomprada<=prd["QdEmestoque"]:
                prd["QdEmestoque"]-=QdAsercomprada
                print("compra finalizada com successo!!!")
            else:
                print("ouppss! ocorreu um erro na sua compra voce digitou uma quantidade superior ao estoque!!!",prd["QdEmestoque"]) 
                break
        preso+=prd["preco"]       
print(listProd) 
print(preso)
    
seachforProd=int(input("digite o codigo do produto:"))
for prd in listProd:
    if prd["codigo"] == seachforProd:
        print(prd)
    else:
        print("o produto que voce digito nao foi cadastrado")
            