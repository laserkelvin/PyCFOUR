
import yaml
from pathlib import Path


def read_yaml(filepath):
    """
    
    
    Parameters
    ----------
    filepath : [type]
        [description]
    
    Returns
    -------
    [type]
        [description]
    """
    path, check = check_filepath(filepath)
    if not check:
        raise FileNotFoundError(f"{filepath} not found!")
    yml_data = yaml.load(path.read_text(), Loader=yaml.FullLoader)
    return yml_data


def write_yaml(filepath, yml_dict):
    path, _ = check_filepath(filepath)
    path.with_suffix(".yml").write_text(
        yaml.dump(yml_dict)
        )
    

def check_filepath(filepath):
    path = Path(filepath)
    return (path, path.exists())
