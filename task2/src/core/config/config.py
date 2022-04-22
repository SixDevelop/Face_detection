DATA_DIR = "./data"

ALL_METHODS = ["scale", "hist", "grad", "dft", "dct"]

METHODS_PARAM = {
    "scale": {"name": "l", "default": "2", "range": (2, 10)},
    "hist": {"name": "BIN", "default": "32", "range": (8, 65)},
    "grad": {"name": "W", "default": "10", "range": (4, 21)},
    "dft": {"name": "P", "default": "20", "range": (6, 31)},
    "dct": {"name": "P", "default": "20", "range": (6, 31)},
}

ALL_DATABASES = ["ORL"]

DATABASE_CONF = {
    "ORL": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "task2/data/ORL/s{g}/{im}.pgm",
    },
    "ORL_Cloaked": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "task2/data/ORL_Cloaked/s{g}/{im}.jpg"
    },
    "ORL_Masked": {
        "number_group": 40,
        "number_img": 10,
        "img_path": "task2/data/ORL_Masked/s{g}/{im}.jpg"
    }
}

RESEARCHES = ["1/N-1", "L/N-L"]

RESULT = "task2/data/results/{im}.jpg"
DATA_PATH = "task2/data/"