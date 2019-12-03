import xml.etree.ElementTree as ET
from pathlib import Path
import tkinter
from tkinter import filedialog

nItems = 0
separator = '|'
separator2x = '||'
separator3x = '|||'
lineBreak = '\n'
produtoTAG = 'PRODUTO'
groupA = 'A'
version = '1.02'
groupI = 'I'
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
    rootTK = tkinter.Tk()
    rootTK.withdraw()

    print('Escolha as notas fiscais (XML) dos seus fornecedores: ')
    xml_files_path = filedialog.askopenfilenames(
        title='Escolha as NF-e dos fornecedos',
        filetypes=[('XML document', ('.XML', '.xml')), ('all files', '.*')])

    print('Escolha um local para salvar os aquivos de produtos (TXT): ')
    output_files_directory = Path(filedialog.askdirectory(
        title='Salvando os produtos'))

    product_index = 0
    for xml_file in xml_files_path:
        output_files_path = output_files_directory / \
            'Products{0}.txt'.format(product_index)
        outputFiles = open(output_files_path, 'w')
        tree = ET.parse(xml_file)
        rootET = tree.getroot()
        nItems = iterate_over_xml(rootET)
        check_if_item_exists(nItems)
        #generate_output_file_simple_mode(outputFiles, nItems)
        generate_output_file_full_mode(outputFiles, nItems)
        print_products(nItems)
        product_index += 1

    print(lineBreak + 'Caso identifique algum problema abra o arquivo txt e edite.')
    outputFiles.close()
    input(lineBreak + 'Pressione \'Enter\' para sair.')


def iterate_over_xml(rootET):
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


def check_if_item_exists(nItems):
    for i in range(nItems):
        if not cProd:
            cProd.append('')
        if not cProd[i]:
            cProd.append('')

        if not xProd:
            xProd.append('')
        if not xProd[i]:
            xProd.append('')

        if not cEAN:
            cEAN.append('')
        if not cEAN[i]:
            cEAN.append('')

        if not NCM:
            NCM.append('')
        if not NCM[i]:
            NCM.append('')

        if not CEST:
            CEST.append('')
        if not CEST[i]:
            CEST.append('')

        if not indEscala:
            indEscala.append('')
        if not indEscala[i]:
            indEscala.append('')

        if not CFOP:
            CFOP.append('')
        if not CFOP[i]:
            CFOP.append('')

        if not uCom:
            uCom.append('')
        if not uCom[i]:
            uCom.append('')

        if not qCom:
            qCom.append('')
        if not qCom[i]:
            qCom.append('')

        if not vUnCom:
            vUnCom.append('')
        if not vUnCom[i]:
            vUnCom.append('')

        if not vProd:
            vProd.append('')
        if not vProd[i]:
            vProd.append('')

        if not cEANTrib:
            cEANTrib.append('')
        if not cEANTrib[i]:
            cEANTrib.append('')

        if not uTrib:
            uTrib.append('')
        if not uTrib[i]:
            uTrib.append('')

        if not qTrib:
            qTrib.append('')
        if not qTrib[i]:
            qTrib.append('')

        if not vUnTrib:
            vUnTrib.append('')
        if not vUnTrib[i]:
            vUnTrib.append('')

        if not indTot:
            indTot.append('')
        if not indTot[i]:
            indTot.append('')


def generate_output_file_simple_mode(outputFile, nItems):
    # cEAN e cEANTrib -> Verificar se eh numero (SEM GTIN = "")
    # vUnCom e vUnTrib -> max 4 decimais ex: 4.5000
    # I|cProd|xProd||NCM|||uCom|vUnCom||uTrib|vUnTrib|indTot|  -> Minimo Funcional
    outputFile.write(produtoTAG + separator + str(nItems) + lineBreak)
    for nItem in range(0, nItems):
        outputFile.write(groupA + separator + version + lineBreak)
        outputFile.write(groupI + separator + cProd[nItem] +
                         separator + xProd[nItem] + separator2x +
                         NCM[nItem] + separator3x + uCom[nItem] +
                         separator + vUnCom[nItem] + separator2x + uTrib[nItem] +
                         separator + vUnTrib[nItem] + separator + indTot[nItem] +
                         separator + lineBreak)


def generate_output_file_full_mode(outputFile, nItems):
    # cEAN e cEANTrib -> Verificar se eh numero (SEM GTIN = "")
    # vUnCom e vUnTrib -> max 4 decimais ex: 4.5000

    # I|cProd|xProd|cEAN|NCM|*opc*EXTIPI|*opc*genero|uCom|vUnCom|cEANTrib|
    # uTrib|vUnTrib|indTot|CEST

    outputFile.write(produtoTAG + separator + str(nItems) + lineBreak)
    for nItem in range(0, nItems):
        outputFile.write(groupA + separator + version + lineBreak)
        outputFile.write(groupI + separator + cProd[nItem] +
                         separator + xProd[nItem] + separator + cEAN[nItem] +
                         separator + NCM[nItem] + separator3x + uCom[nItem] +
                         separator + vUnCom[nItem] + separator + cEANTrib[nItem] +
                         separator + uTrib[nItem] + separator + vUnTrib[nItem] +
                         separator + indTot[nItem] + separator + CEST[nItem] +
                         separator + lineBreak)


def print_products(nItems):
    i = 0
    print(lineBreak + 'Arquivo gerado com os seguintes produtos:')
    for nItem in range(0, nItems):
        i += 1
        print('Produto ' + str(i) + ': ' + str(xProd[nItem]))


if __name__ == '__main__':
    main()
