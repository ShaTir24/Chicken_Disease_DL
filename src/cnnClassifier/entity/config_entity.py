from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:  #dataclass class
    root_dir: Path      #specifies the return type of the class as a collection of all the fields
    source_URL: str
    local_data_file: Path
    unzip_dir: Path