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

nfe_elements_names = ['cProd', 'xProd', 'cEAN', 'NCM', 'CEST', 'indEscala', \
                      'CFOP', 'uCom', 'qCom','vUnCom', 'vProd', 'cEANTrib', \
                      'uTrib', 'qTrib', 'vUnTrib', 'indTot']

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
    for product in rootET.iter('{0}prod'.format(portal)):
        nItems += 1
        for product_element in list(product):
            for i in range(n_elements):
                if product_element.tag == '{0}{1}'.format(portal, nfe_elements_names[i]):
                    nfe_elements[i].append(product_element.text)
    return nItems


def making_sure_the_lists_is_not_empty(nItems):
    for i in range(nItems):
        for j in range(n_elements):
            if not nfe_elements[j]:
                nfe_elements[j].append('')
            if not nfe_elements[j][i]:
                nfe_elements[j].append('')

#TRY EXCEPT NA CONVERSAO
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

#BUG EM ALGUNS ARQUIVOS(LN 122)
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
