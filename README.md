# NFeProductExtractor

**NFeProductExtractor** é um extrator de produtos de notas fiscais eletrônicas 4.0, ele é utilizado para automatizar o cadastro de produtos no emissor de notas gratuito do Sebrae 4.01.

Ele feito para funcionar com o emissor do Sebrae 4.01, que utiliza o layout de NF-e 4.0, porém ele pode facilmente ser adaptado para outras versões.

## Installation

Instale o [python3.7.x](https://www.python.org/downloads/) para poder usar o script.

Agora, abra a pasta do projeto e instale os requisitos:

```bash
python3.7 -m pip install -r requirements.txt
```

## Usage

1. Insira uma **nota fical eletrônica de produto 4.0 (NF-e 4.0)** no formato **.XML**. Será produzido um arquivo chamado **"Products.txt"**
2. Abra o **Emissor de NF-e gratuito do Sebrae** e selecione a empresa.
1. Agora vá em **Sistema** e depois em **Importar Arquivos**, como na imagem a seguir.![](https://raw.githubusercontent.com/xandao6/NFeProductExtractor/master/imagesTutorial/img1.jpg?token=AFIVBVTFEFDUXZ66PFI6LM254BPIU)
1. Selecione no emissor o nosso arquivo **"Products.txt"**
1. Clique em **Importar**
1. Pronto, os produtos foram importados! :clap::clap::clap:

## Contributing

**Pull requests** são bem-vindos. Para grandes mudanças, abra **issue** para discutir o que você gostaria de modificar.

## License
[APACHE 2.0](https://github.com/xandao6/NFeProductExtractor/blob/master/LICENSE)
