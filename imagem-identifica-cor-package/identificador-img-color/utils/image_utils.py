from skimage.io import imread, imsave

def read_image(path, is_gray=False):
    """Lê uma imagem a partir de um caminho especificado.
    
    Args:
        path (str): Caminho para a imagem.
        is_gray (bool): Se True, a imagem é lida em grayscale.
    
    Returns:
        ndarray: A imagem carregada.
    """
    image = imread(path, as_gray=is_gray)
    return image

def save_image(image, path):
    """Salva uma imagem em um caminho especificado.
    
    Args:
        image (ndarray): A imagem a ser salva.
        path (str): Caminho para salvar a imagem.
    """
    imsave(path, image)
