<br />
<p align="center">
  <h3 align="center">NF-e Product Extractor</h3>

  <p align="center">
    Extrator de produtos de notas fiscais eletrônicas 4.0, utilizado para automatizar o cadastro de produtos no emissor de notas gratuito do Sebrae 4.01.
    <br />
	<br />
    <a href="https://github.com/xandao-dev/nfe-product-extractor"><strong>Explore a documentação »</strong></a>
    <br />
    <a href="https://github.com/xandao-dev/nfe-product-extractor/issue">Reporte um Bug</a>
    ·
    <a href="https://github.com/xandao-dev/nfe-product-extractor/issues">Peça um Recurso</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Conteúdo</summary>
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#instalação">Instalação</a></li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuição">Contribuição</a></li>
    <li><a href="#licença">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

## Sobre o Projeto

**NF-e Product Extractor** é um extrator de produtos de notas fiscais eletrônicas 4.0, ele é utilizado para automatizar o cadastro de produtos no emissor de notas gratuito do Sebrae 4.01.

Ele feito para funcionar com o emissor do Sebrae 4.01, que utiliza o layout de NF-e 4.0, porém ele pode facilmente ser adaptado para outras versões.

## Instalação

Instale o [python3.7.x](https://www.python.org/downloads/) para poder usar o script.

Todos os pré-requisitos já vem com o python 3.7.

## Uso

1. Insira as **notas ficais eletrônicas de produto 4.0 (NF-e 4.0)** no formato **.XML**. 
1. Escolha uma pasta para salvar os arquivos.
1. Será salvo na pasta escolhida arquivos chamados **"Products1.txt, Products2.txt, Products3.txt ..."**
1. Abra o **Emissor de NF-e gratuito do Sebrae** e selecione a sua empresa.
1. Agora vá em **Sistema** e depois em **Importar Arquivos**, como na imagem a seguir.![](./assets/images/img1.jpg)
1. Selecione no emissor a pasta que contém os aquivos **"Products1.txt, Products2.txt, Products3.txt ..."**
1. Clique em **Importar**
1. Pronto, os produtos foram importados! :clap::clap::clap:

OBS.: Caso tenha algum erro na importação você pode entrar no arquivo .TXT gerado e editar. Você também pode contactar o desenvolvedor com um print screen do erro para evitar problemas futuros.

## Roadmap

Veja as [issues abertas](https://github.com/xandao-dev/nfe-product-extractor/issues) para uma lista de recursos propostos (e problemas conhecidos).

## Contribuição

Contribuições são o que fazem a comunidade de código aberto um lugar incrível para aprender, se inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](./LICENSE.md) para mais informações.

Software livre =)

## Contato

Alexandre Calil - [Linkedin](https://www.linkedin.com/in/xandao-dev/) - [alexandre@xandao.dev](mailto:alexandre@xandao.dev)

Projeto: [https://github.com/xandao-dev/nfe-product-extractor](https://github.com/xandao-dev/nfe-product-extractor)
