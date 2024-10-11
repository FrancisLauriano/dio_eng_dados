# identificador-img-color

Este pacote permite identificar se uma imagem é colorida ou em preto e branco. Ele utiliza a biblioteca `scikit-image` para manipulação de imagens, fornecendo funções para leitura, análise e salvamento de imagens. Este pacote é ideal para desenvolvedores e cientistas de dados que precisam processar imagens e identificar automaticamente o tipo de coloração.

## Funcionalidades

O pacote `identificador-img-color` é usado para:
- Ler imagens a partir de um caminho especificado.
- Determinar se a imagem é colorida ou em escala de cinza (preto e branco).
- Salvar imagens em formatos variados.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar `identificador-img-color`:

```bash
pip install identificador-img-color
```

## Usage

```python
from identificador_img_color.processing import is_color_image

# Caminho para a imagem a ser analisada
image_path = 'caminho/para/sua/imagem.jpg'

# Verificar se a imagem é colorida ou em preto e branco
resultado = is_color_image(image_path)
print(resultado)

```

## Author
Francis Lauriano

## License
[MIT](https://choosealicense.com/licenses/mit/)