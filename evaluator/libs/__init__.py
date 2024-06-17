from pathlib import Path


libs = Path(__name__).parent.absolute()

LIBRARIES = {
    'fstream': libs / 'fstream.h'
}
