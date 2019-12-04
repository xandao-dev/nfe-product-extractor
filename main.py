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


#IMPLEMENTAR TRY EXCEPT
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

    file_index = 1
    for xml_file in xml_files_path:
        output_files_path = output_files_directory / \
            'Products{0}.txt'.format(file_index)
        outputFiles = open(output_files_path, 'w')
        tree = ET.parse(xml_file)
        rootET = tree.getroot()
        n_products = count_products(rootET)
        iterate_over_xml(rootET)
        making_sure_the_lists_is_not_empty(n_products)
        formating_lists(n_products)
        #generate_output_file_simple_mode(outputFiles, n_products)
        generate_output_file_full_mode(outputFiles, n_products)
        print_products(n_products)
        reset_lists()
        file_index += 1

    print(lineBreak + 'Caso identifique algum problema abra o arquivo txt e edite.')
    outputFiles.close()
    input(lineBreak + 'Pressione \'Enter\' para sair.')


def count_products(rootET):
    n_products = 0
    for product in rootET.iter('{0}prod'.format(portal)):
        n_products += 1
    return n_products


def iterate_over_xml(rootET):
    for product in rootET.iter('{0}prod'.format(portal)):
        for product_element in list(product):
            for i in range(n_elements):
                if product_element.tag == '{0}{1}'.format(portal, nfe_elements_names[i]):
                    if not product_element.text == None:
                        nfe_elements[i].append(product_element.text)


def making_sure_the_lists_is_not_empty(n_products):
    for i in range(n_products):
        for j in range(n_elements):
            if not nfe_elements[j]:
                nfe_elements[j].append('')
            if not nfe_elements[j][i]:
                nfe_elements[j].append('')


def formating_lists(n_products):
    # cEAN e cEANTrib -> Verificar se eh numero (SEM GTIN = "")
    # vUnCom e vUnTrib -> max 4 decimais ex: 4.5000
    for n_product in range(n_products):
        if not vUnCom[n_product] == '': 
            vUnCom[n_product] = ("{0:.4f}".format(float(vUnCom[n_product])))
        if not vUnTrib[n_product] == '':
            vUnTrib[n_product] = ("{0:.4f}".format(float(vUnTrib[n_product])))
        if cEAN[n_product] == 'SEM GTIN':
            cEAN[n_product] = ''
        if cEANTrib[n_product] == 'SEM GTIN':
            cEANTrib[n_product] = ''


def generate_output_file_simple_mode(outputFile, n_products):
    # I|cProd|xProd||NCM|||uCom|vUnCom||uTrib|vUnTrib|indTot|  -> Minimo Funcional
    outputFile.write(produtoTAG + separator + str(n_products) + lineBreak)
    for n_product in range(n_products):
        outputFile.write(groupA + separator + version + lineBreak)
        outputFile.write(groupI + separator + cProd[n_product] +
                         separator + xProd[n_product] + separator2x +
                         NCM[n_product] + separator3x + uCom[n_product] +
                         separator + vUnCom[n_product] + separator2x + uTrib[n_product] +
                         separator + vUnTrib[n_product] + separator + indTot[n_product] +
                         separator + lineBreak)


def generate_output_file_full_mode(outputFile, n_products):
    # I|cProd|xProd|cEAN|NCM|*opc*EXTIPI|*opc*genero|uCom|vUnCom|cEANTrib|
    # uTrib|vUnTrib|indTot|CEST

    outputFile.write(produtoTAG + separator + str(n_products) + lineBreak)
    for n_product in range(n_products):
        outputFile.write(groupA + separator + version + lineBreak)
        outputFile.write(groupI + separator + cProd[n_product] +
                         separator + xProd[n_product] + separator + cEAN[n_product] +
                         separator + NCM[n_product] + separator3x + uCom[n_product] +
                         separator + vUnCom[n_product] + separator + cEANTrib[n_product] +
                         separator + uTrib[n_product] + separator + vUnTrib[n_product] +
                         separator + indTot[n_product] + separator + CEST[n_product] +
                         separator + lineBreak)


def print_products(n_products):
    i = 0
    print(lineBreak + 'Arquivo gerado com os seguintes produtos:')
    for n_product in range(n_products):
        i += 1
        print('Produto ' + str(i) + ': ' + str(xProd[n_product]))


def reset_lists():
    for i in range(len(nfe_elements)):
        nfe_elements[i].clear()


if __name__ == '__main__':
    main()
