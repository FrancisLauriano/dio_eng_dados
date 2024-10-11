from utils.image_utils import read_image

def is_color_image(image_path):
    """Verifica se uma imagem é colorida ou em preto e branco.
    
    Args:
        image_path (str): Caminho para a imagem.
    
    Returns:
        str: Descrição do tipo da imagem.
    """
    image = read_image(image_path)
    
    if len(image.shape) == 3 and image.shape[2] == 3:
        return "A imagem é colorida."
    elif len(image.shape) == 2:
        return "A imagem é em preto e branco."
    else:
        return "Não foi possível determinar o tipo de imagem."
