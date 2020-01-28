__version__ = '1.1'
__author__ = 'Alexandre Calil Martins Fonseca'

import xml.etree.ElementTree as ElementTree
import os
import platform
from typing import Type, List, TextIO, Tuple
from pathlib import Path
import tkinter
from tkinter import filedialog

# CONSTANTS
separator: str = '|'
separator2x: str = '||'
separator3x: str = '|||'
lineBreak: str = '\n'
produtoTAG: str = 'PRODUTO'
groupA: str = 'A'
version: str = '1.02'
groupI: str = 'I'
portal: str = '{http://www.portalfiscal.inf.br/nfe}'

# LISTS
nfe_elements_names: List[str] = [
    'cProd', 'xProd', 'cEAN', 'NCM', 'CEST', 'indEscala',
    'CFOP', 'uCom', 'qCom', 'vUnCom', 'vProd', 'cEANTrib',
    'uTrib', 'qTrib', 'vUnTrib', 'indTot',
]

cProd, xProd, cEAN, NCM, CEST, indEscala, CFOP, uCom, qCom, vUnCom, vProd,  \
    cEANTrib, uTrib, qTrib, vUnTrib, indTot = (
        [] for i in range(len(nfe_elements_names)))

nfe_elements: List[str] = [
    cProd, xProd, cEAN, NCM, CEST, indEscala, CFOP, uCom, qCom,
    vUnCom, vProd, cEANTrib, uTrib, qTrib, vUnTrib, indTot,
]

# platform.system() return 'Windows', 'Linux' or 'Darwin' for Mac
operating_system = platform.system()


def main():
    root_window = tkinter.Tk()
    root_window.withdraw()

    xml_files_path = ask_where_are_xml_files()
    xml_filenames = get_filenames_from_paths(xml_files_path)
    output_files_directory = ask_dictory_to_save_output_files()

    for file_index, xml_file_path in enumerate(xml_files_path):
        output_files_path = generate_output_files_path(True,
                                                       output_files_directory,
                                                       xml_filenames,
                                                       file_index)
        output_file = open(output_files_path, 'w')
        process_file(xml_file_path, output_file)

    output_file.close()
    say_good_bye_to_user()


def process_file(xml_file_path: str, output_file: TextIO) -> None:
    tree = ElementTree.parse(xml_file_path)
    root_element = tree.getroot()
    n_products = count_products(root_element)
    iterate_over_xml(root_element)
    make_sure_the_lists_is_not_empty(n_products)
    format_lists(n_products)
    #generate_output_file_simple_mode(output_file, n_products)
    generate_output_file_full_mode(output_file, n_products)
    print_products(n_products)
    reset_lists()


def ask_where_are_xml_files() -> Tuple[str]:
    print('Escolha as notas fiscais (XML) dos seus fornecedores: ')
    xml_files_path = filedialog.askopenfilenames(
        title='Escolha as NF-e dos fornecedos',
        filetypes=[('XML document', ('.XML', '.xml')), ('all files', '.*')])
    if xml_files_path == ():
        print("Erro! Você não escolheu nenhuma NF-e.")
        exit()
    return xml_files_path


def get_filenames_from_paths(paths: Tuple[str]) -> Tuple[str]:
    filenames = []
    for file_index in range(len(paths)):
        parts_from_path = Path(paths[file_index]).parts
        filename_and_extension = os.path.splitext(parts_from_path[-1])
        filenames.append(filename_and_extension[0])
    return filenames


def generate_output_files_path(use_filename_name: bool,
                               output_files_directory: Type[Path],
                               xml_filenames: Tuple[str],
                               file_index: int) -> Tuple[Type[Path]]:
    if use_filename_name == True and operating_system != 'Windows':
        # Only work on linux
        output_files_path = output_files_directory / \
            'Products: {0}.txt'.format(xml_filenames[file_index])
    else:
        output_files_path = output_files_directory / \
            'Products{0}.txt'.format(file_index)
    return output_files_path


def ask_dictory_to_save_output_files() -> Type[Path]:
    print('Escolha um local para salvar os aquivos de produtos (TXT): ')
    try:
        output_files_directory = Path(filedialog.askdirectory(
            title='Escolha um diretorio para salvar'))
    except:
        print("Erro!")
        exit()
    return output_files_directory


def count_products(root_element: Type[ElementTree.Element]) -> int:
    n_products = 0
    for _ in root_element.iter('{0}prod'.format(portal)):
        n_products += 1
    return n_products


def iterate_over_xml(root_element: Type[ElementTree.Element]) -> None:
    for product in root_element.iter('{0}prod'.format(portal)):
        for product_element in list(product):
            for i in range(len(nfe_elements_names)):
                if product_element.tag == '{0}{1}'.format(
                        portal, nfe_elements_names[i]):
                    if product_element.text is not None:
                        nfe_elements[i].append(product_element.text)


def make_sure_the_lists_is_not_empty(n_products: int) -> None:
    for i in range(n_products):
        for j in range(len(nfe_elements_names)):
            if not nfe_elements[j]:
                nfe_elements[j].append('')
            try:
                if not nfe_elements[j][i]:
                    nfe_elements[j].append('')
            except IndexError:
                nfe_elements[j].append('')


def format_lists(n_products: int) -> None:
    for n_product in range(n_products):
        if not vUnCom[n_product] == '':
            vUnCom[n_product] = ("{0:.4f}".format(float(vUnCom[n_product])))
        if not vUnTrib[n_product] == '':
            vUnTrib[n_product] = ("{0:.4f}".format(float(vUnTrib[n_product])))
        if cEAN[n_product] == 'SEM GTIN':
            cEAN[n_product] = ''
        if cEANTrib[n_product] == 'SEM GTIN':
            cEANTrib[n_product] = ''


def generate_output_file_simple_mode(output_file: TextIO,
                                     n_products: int) -> None:
    # I|cProd|xProd||NCM|||uCom|vUnCom||uTrib|vUnTrib|indTot|

    output_file.write(produtoTAG + separator + str(n_products) + lineBreak)
    for n_product in range(n_products):
        output_file.write(groupA + separator + version + lineBreak)
        output_file.write(
            groupI + separator + cProd[n_product] + separator +
            xProd[n_product] + separator2x + NCM[n_product] +
            separator3x + uCom[n_product] + separator +
            vUnCom[n_product] + separator2x + uTrib[n_product] +
            separator + vUnTrib[n_product] + separator +
            indTot[n_product] + separator + lineBreak)


def generate_output_file_full_mode(output_file: TextIO,
                                   n_products: int) -> None:
    # I|cProd|xProd|cEAN|NCM|*opc*EXTIPI|*opc*genero|uCom|vUnCom|cEANTrib|
    # uTrib|vUnTrib|indTot|CEST

    output_file.write(produtoTAG + separator + str(n_products) + lineBreak)
    for n_product in range(n_products):
        output_file.write(groupA + separator + version + lineBreak)
        output_file.write(
            groupI + separator + cProd[n_product] + separator +
            xProd[n_product] + separator + cEAN[n_product] +
            separator + NCM[n_product] + separator3x +
            uCom[n_product] + separator + vUnCom[n_product] +
            separator + cEANTrib[n_product] + separator +
            uTrib[n_product] + separator + vUnTrib[n_product] +
            separator + indTot[n_product] + separator +
            CEST[n_product] + separator + lineBreak)


def print_products(n_products: int) -> None:
    print(lineBreak + 'Arquivo gerado com os seguintes produtos:')
    for n_product in range(n_products):
        print('Produto ' + str(n_product + 1) + ': ' + str(xProd[n_product]))


def reset_lists() -> None:
    for i in range(len(nfe_elements)):
        nfe_elements[i].clear()


def say_good_bye_to_user() -> None:
    print(lineBreak + 'Caso encontre problemas abra o arquivo txt e edite.')
    input(lineBreak + 'Pressione \'Enter\' para sair.')


if __name__ == '__main__':
    main()
