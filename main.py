import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import tkinter
from tkinter import filedialog

# CONSTANTS
separator = '|'
separator2x = '||'
separator3x = '|||'
lineBreak = '\n'
produtoTAG = 'PRODUTO'
groupA = 'A'
version = '1.02'
groupI = 'I'
portal = '{http://www.portalfiscal.inf.br/nfe}'
n_elements = 16

# LISTS
cProd, xProd, cEAN, NCM, CEST, indEscala, CFOP, uCom, qCom, vUnCom, vProd, \
    cEANTrib, uTrib, qTrib, vUnTrib, indTot = ([] for i in range(n_elements))

nfe_elements = [cProd, xProd, cEAN, NCM, CEST, indEscala, CFOP, uCom, qCom,
                vUnCom, vProd, cEANTrib, uTrib, qTrib, vUnTrib, indTot]


def main():
    rootTK = tkinter.Tk()
    rootTK.withdraw()

    print('Escolha as notas fiscais (XML) dos seus fornecedores: ')
    xml_files_path = filedialog.askopenfilenames(
        title='Escolha as NF-e dos fornecedos',
        filetypes=[('XML document', ('.XML', '.xml')), ('all files', '.*')])

    print('Escolha um local para salvar os aquivos de produtos (TXT): ')
    output_files_directory = Path(filedialog.askdirectory(
        title='Escolha um diretorio para salvar'))

    product_index = 0
    for xml_file in xml_files_path:
        output_files_path = output_files_directory / \
            'Products{0}.txt'.format(product_index)
        outputFiles = open(output_files_path, 'w')
        tree = ET.parse(xml_file)
        rootET = tree.getroot()
        nItems = iterate_over_xml(rootET)
        making_sure_the_lists_is_not_empty(nItems)
        formating_lists(nItems)
        #generate_output_file_simple_mode(outputFiles, nItems)
        generate_output_file_full_mode(outputFiles, nItems)
        print_products(nItems)
        reset_lists()
        product_index += 1

    print(lineBreak + 'Caso identifique algum problema abra o arquivo txt e edite.')
    outputFiles.close()
    input(lineBreak + 'Pressione \'Enter\' para sair.')


def iterate_over_xml(rootET):
    nItems = 0
    for det in rootET.iter('{0}prod'.format(portal)):
        nItems += 1
        for detList in list(det):
            for cProdITER in detList.iter('{0}cProd'.format(portal)):
                cProd.append(cProdITER.text)
            for xProdITER in detList.iter('{0}xProd'.format(portal)):
                xProd.append(xProdITER.text)
            for cEANITER in detList.iter('{0}cEAN'.format(portal)):
                cEAN.append(cEANITER.text)
            for NCMITER in detList.iter('{0}NCM'.format(portal)):
                NCM.append(NCMITER.text)
            for CESTITER in detList.iter('{0}CEST'.format(portal)):
                CEST.append(CESTITER.text)
            for indEscalaITER in detList.iter('{0}indEscala'.format(portal)):
                indEscala.append(indEscalaITER.text)
            for CFOPITER in detList.iter('{0}CFOP'.format(portal)):
                CFOP.append(CFOPITER.text)
            for uComITER in detList.iter('{0}uCom'.format(portal)):
                uCom.append(uComITER.text)
            for qComITER in detList.iter('{0}qCom'.format(portal)):
                qCom.append(qComITER.text)
            for vUnComITER in detList.iter('{0}vUnCom'.format(portal)):
                vUnCom.append(vUnComITER.text)
            for vProdITER in detList.iter('{0}vProd'.format(portal)):
                vProd.append(vProdITER.text)
            for cEANTribITER in detList.iter('{0}cEANTrib'.format(portal)):
                cEANTrib.append(cEANTribITER.text)
            for uTribITER in detList.iter('{0}uTrib'.format(portal)):
                uTrib.append(uTribITER.text)
            for qTribITER in detList.iter('{0}qTrib'.format(portal)):
                qTrib.append(qTribITER.text)
            for vUnTribITER in detList.iter('{0}vUnTrib'.format(portal)):
                vUnTrib.append(vUnTribITER.text)
            for indTotITER in detList.iter('{0}indTot'.format(portal)):
                indTot.append(indTotITER.text)
    return nItems


def making_sure_the_lists_is_not_empty(nItems):
    for i in range(nItems):
        for j in range(len(nfe_elements)):
            if not nfe_elements[j]:
                nfe_elements[j].append('')
            if not nfe_elements[j][i]:
                nfe_elements[j].append('')


def formating_lists(nItems):
    # cEAN e cEANTrib -> Verificar se eh numero (SEM GTIN = "")
    # vUnCom e vUnTrib -> max 4 decimais ex: 4.5000
    for nItem in range(nItems):
        vUnCom[nItem] = ("{0:.4f}".format(float(vUnCom[nItem])))
        vUnTrib[nItem] = ("{0:.4f}".format(float(vUnTrib[nItem])))
        if cEAN[nItem] == 'SEM GTIN':
            cEAN[nItem] = ''
        if cEANTrib[nItem] == 'SEM GTIN':
            cEANTrib[nItem] = ''


def generate_output_file_simple_mode(outputFile, nItems):
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


def reset_lists():
    for i in range(len(nfe_elements)):
        nfe_elements[i].clear()


if __name__ == '__main__':
    main()
