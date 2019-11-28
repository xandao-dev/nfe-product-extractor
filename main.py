import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import filedialog

nItems = 0
fixedTextA = 'PRODUTO|'
fixedTextB = 'A|1.02\n'
fixedTextC = 'I'
cProd = []
xProd = []
cEAN = []
NCM = []
CEST = []
indEscala = []
CFOP = []
uCom = []
qCom = []
vUnCom = []
vProd = []
cEANTrib = []
uTrib = []
qTrib = []
vUnTrib = []
indTot = []


def main():
    rootTK = tk.Tk()
    rootTK.withdraw()
    print('Escolha a nota fiscal (XML) do seu fornecedor: ')
    file_path = filedialog.askopenfilename()
    
    output_file_path = 'Products.txt'
    outputFile = open(output_file_path, 'w')

    tree = ET.parse(file_path)
    rootET = tree.getroot()
    print('Aguarde um instante...\n')

    nItems = iterateOverXml(rootET)
    generateOutputFileFirstMode(outputFile, nItems)
    #generateOutputFileSecondMode(outputFile, nItems)
    #generateOutputFileThirdMode(outputFile, nItems)
    printProducts(nItems)

    outputFile.close()
    


def iterateOverXml(rootET):
    nItems = 0
    for det in rootET.iter('{http://www.portalfiscal.inf.br/nfe}prod'):
        nItems += 1
        for detList in list(det):
            for cProdITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}cProd'):
                cProd.append(cProdITER.text)
            for xProdITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}xProd'):
                xProd.append(xProdITER.text)
            for cEANITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}cEAN'):
                cEAN.append(cEANITER.text)
            for NCMITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}NCM'):
                NCM.append(NCMITER.text)
            for CESTITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}CEST'):
                CEST.append(CESTITER.text)
            for indEscalaITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}indEscala'):
                indEscala.append(indEscalaITER.text)
            for CFOPITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}CFOP'):
                CFOP.append(CFOPITER.text)
            for uComITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}uCom'):
                uCom.append(uComITER.text)
            for qComITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}qCom'):
                qCom.append(qComITER.text)
            for vUnComITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}vUnCom'):
                vUnCom.append(vUnComITER.text)
            for vProdITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}vProd'):
                vProd.append(vProdITER.text)
            for cEANTribITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}cEANTrib'):
                cEANTrib.append(cEANTribITER.text)
            for uTribITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}uTrib'):
                uTrib.append(uTribITER.text)
            for qTribITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}qTrib'):
                qTrib.append(qTribITER.text)
            for vUnTribITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}vUnTrib'):
                vUnTrib.append(vUnTribITER.text)
            for indTotITER in detList.iter('{http://www.portalfiscal.inf.br/nfe}indTot'):
                indTot.append(indTotITER.text)
    return nItems

def generateOutputFileFirstMode(outputFile, nItems):
    # I|cProd|xProd|cEAN|NCM|||uCom|vUnCom||uCom(uTrib)|vUnCom(vUnTrib)|1.000|

    outputFile.write(fixedTextA + str(nItems) + '\n')
    for nItem in range(0, nItems):
        outputFile.write(fixedTextB)
        outputFile.write(fixedTextC + '|' + str(cProd[nItem]) +
                         '|' + str(xProd[nItem]) + '|' + str(cEAN[nItem]) +
                         '|' + str(NCM[nItem]) + '|||' + str(uCom[nItem]) +
                         '|' + str(vUnCom[nItem]) + '||' + str(uCom[nItem]) +
                         '|' + str(vUnCom[nItem]) + '|' + '1.000' + '|' + '\n')


def generateOutputFileSecondMode(outputFile, nItems):
    # I|cProd|cEAN|xProd|NCM|*cBenef|*EXTIPI|CFOP|uCom|qCom|vUnCom|vProd|cEANTrib|
    # uTrib|qTrib|vUnTrib|*vFrete|*vSeg|*vDesc|*vOutro|indTot|*xPed|*nItemPed|*nFCI|

    outputFile.write(fixedTextA + str(nItems) + '\n')
    for nItem in range(0, nItems):
        outputFile.write(fixedTextB)
        outputFile.write(fixedTextC + '|' + str(cProd[nItem]) +
                         '|' + str(cEAN[nItem]) + '|' + str(xProd[nItem]) +
                         '|' + str(NCM[nItem]) + '|||' + str(CFOP[nItem]) +
                         '|' + str(uCom[nItem]) + '|' + str(qCom[nItem]) +
                         '|' + str(vUnCom[nItem]) + '|' + str(vProd[nItem]) +
                         '|' + str(cEANTrib[nItem]) + '|' + str(uTrib[nItem]) +
                         '|' + str(qTrib[nItem]) + '|' + str(vUnTrib[nItem]) +
                         '|||||' + str(indTot[nItem]) + '||||' + '\n')


def generateOutputFileThirdMode(outputFile, nItems):
    #Mude como quiser

    outputFile.write(fixedTextA + str(nItems) + '\n')
    for nItem in range(0, nItems):
        outputFile.write(fixedTextB)
        outputFile.write(fixedTextC + '|' + str(cProd[nItem]) +
                         '|' + str(cEAN[nItem]) + '|' + str(xProd[nItem]) +
                         '|' + str(NCM[nItem]) + '|||' + str(CFOP[nItem]) +
                         '|' + str(uCom[nItem]) + '|' + str(qCom[nItem]) +
                         '|' + str(vUnCom[nItem]) + '|' + str(vProd[nItem]) +
                         '|' + str(cEANTrib[nItem]) + '|' + str(uTrib[nItem]) +
                         '|' + str(qTrib[nItem]) + '|' + str(vUnTrib[nItem]) +
                         '|||||' + str(indTot[nItem]) + '||||' + '\n')

def printProducts(nItems):
    i = 0
    print('Arquivo gerado com os seguintes produtos:\n')
    for nItem in range(0, nItems):
        i += 1
        print('Produto ' + str(i) + ': ' + str(xProd[nItem]))
    print('\nCaso identifique algum problema abra o arquivo txt e edite.')

if __name__ == '__main__':
    main()
