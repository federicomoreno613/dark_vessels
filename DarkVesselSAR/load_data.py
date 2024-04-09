import os
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw



def show_image_with_annotations(images_path, file_name, annotations):
    """
    Args:
        images_path (str): Directorio con las imágenes.
        file_name (str): Nombre del archivo de la imagen.
        annotations (dict): Diccionario con las anotaciones.

    output:
        Muestra la imagen con las anotaciones.
        """
    image_info = next((item for item in annotations['images'] if item['file_name'] == file_name), None)
    if not image_info:
        print("No se encontró la información de la imagen.")
        return

    image_path = os.path.join(images_path, file_name)
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    annotations_for_image = [anno for anno in annotations.get('annotations', []) if
                             anno['image_id'] == image_info['id']]
    categories = {category['id']: category['name'] for category in annotations['categories']}

    for anno in annotations_for_image:
        category_id = anno['category_id']
        category_name = categories.get(category_id, "Unknown")
        bbox = anno['bbox']

        # Dibujar bounding box
        draw.rectangle([(bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3])], outline="red", width=3)

        # Dibujar nombre de la categoría
        draw.text((bbox[0], bbox[1] - 10), category_name, fill="red")

        # Dibujar segmentación, si está disponible
        if 'segmentation' in anno:
            segmentation = anno['segmentation']
            if isinstance(segmentation, list):  # COCO Polygon format
                draw_polygon(draw, segmentation, "yellow")

    plt.figure(figsize=(12, 12))
    plt.imshow(image)
    plt.axis("off")
    plt.show()

def show_image(image_path, annotations=None):
    """Muestra una imagen con la opción de dibujar anotaciones."""
    image = Image.open(image_path)
    if annotations:
        draw = ImageDraw.Draw(image)
        for anno in annotations:
            # Asume que las anotaciones son bounding boxes en el formato [x,y,width,height]
            bbox = anno['bbox']
            draw.rectangle([bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]], outline ="red")
    plt.figure(figsize=(12, 12))
    plt.imshow(image)
    plt.axis('off')
    plt.show()


def draw_polygon(draw, polygon, color):
    for i in range(len(polygon)):
        for j in range(len(polygon[i])//2 - 1):
            x1, y1 = polygon[i][2*j], polygon[i][2*j+1]
            x2, y2 = polygon[i][2*(j+1)], polygon[i][2*(j+1)+1]
            draw.line([x1, y1, x2, y2], fill=color, width=2)