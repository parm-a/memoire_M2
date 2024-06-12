"""
the process to apply to a given image
as a function for easier repeatability
"""

from pathlib import Path
from configparser import ConfigParser

import numpy as np
import cv2

# using the develop branch of pero-ocr
from pero_ocr.core.layout import PageLayout
from pero_ocr.document_ocr.page_parser import PageParser

import warnings
warnings.filterwarnings('ignore')

CONFIG = "config/config-mine.ini"

def process(filename, *, force=False, verbose=False, details=False):
    """
    process a given image and store results
    under the same name with different extensions

    if force is False, and the output files already exist,
    the function will not overwrite them and return immediately
    """

    # in case filename is a Path object
    filename = str(filename)
    # check input
    path = Path(filename)
    if not path.is_file():
        raise FileNotFoundError(f"File {path} does not exist")

    # load image to find size - discard non-image files
    try:
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        page_layout = PageLayout(id = filename, page_size = image.shape)
    except AttributeError:
        print(f"File {path} is not an image - skipping")
        return

    # compute output paths
    outpath = path.parent / "pero"
    outpath.mkdir(parents=True, exist_ok=True)
    outstem = outpath / path.stem
    f_xml = outstem.with_suffix(".out.xml")
    f_txt = outstem.with_suffix(".out.txt")
    f_alto = outstem.with_suffix(".out.alto.xml")
    f_rendered = outstem.with_suffix(".out.png")

    if not force and all([f.exists() for f in [f_xml, f_alto, f_rendered]]):
        if verbose:
            print(f"Skipping {path} - output files already exist")
        return

    # read config and create parser
    config = ConfigParser()
    config.read(CONFIG)
    page_parser = PageParser(
        config,
        config_path = str(Path(CONFIG).parent)
    )

    # compute
    page_layout2 = page_parser.process_page(image, page_layout)

    # store results
    if verbose:
        print(f"Writing results to\n  {f_xml}\n  {f_alto}\n  {f_rendered}")
    page_layout2.to_pagexml(str(f_xml))
    page_layout2.to_altoxml(str(f_alto))

    rendered_image = page_layout2.render_to_image(image)
    cv2.imwrite(str(f_rendered), rendered_image)

    # save cropped text lines
    for region in page_layout.regions:
        if verbose:
            print(f"{type(region)=} {region.id=}")
        # region is of type pero_ocr.core.layout.RegionLayout
        # which does not seem to have a method for saving the region as an image...
        # let's try to save the region as xml instead
        f_region = outstem.with_suffix(f".{region.id}.xml")
        if verbose:
            print(f"Writing region to {f_region}")
        # need to pass some already existing XML of some kind instead of a filename
        # def to_page_xml(self, page_element: ET.SubElement, validate_id: bool = False):
        # so this won't work
        # region.to_page_xml(str(f_region))
        #
        # store one image per line - it's a lot of noise
        # so we do it only if requested with details=True


	# Now we're saving the raw text in a .txt file, and the image with
	# the text region and baselines drawn on it in a .png file
        liste_lignes = []

        for line in region.lines:
            print(f"{line.id}: {line.transcription}")
            
            liste_lignes.append(line.transcription)

            if details:
                f_line = outstem.with_suffix(f".{line.id}.png")
                if verbose:
                    print(f"Writing line to {f_line}")
                cv2.imwrite(str(f_line), line.crop.astype(np.uint8))

        print(f"Writing results to\n  {f_txt}")
        
        with open(f_txt, 'a') as txt:
            for element in liste_lignes:
                txt.write(element + "\n")
