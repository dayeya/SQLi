import pathlib as plib
import configparser as parser
from configparser import SectionProxy
from typing import Iterable

PARSER: parser.ConfigParser = None
ROOT_DIR = plib.Path(__file__).parent


class SectionDoesNotExist(Exception):
    pass


class ValueNotFound(Exception):
    pass


def chain_path(file: plib.Path) -> plib.Path:
    return ROOT_DIR.joinpath(file)


def set_global_parser() -> None:
    global PARSER

    if not PARSER:
        PARSER = parser.ConfigParser()


def get_configuration(section_name: str, file: plib.Path, keys: Iterable=None):
    try:
        section = get_section(section_name, file=file)
        return section if not keys else [section.get(item) for item in keys]
    except KeyError as _e:
        raise ValueNotFound(f"Some values of {keys} don't exit in the specified file object or {section_name}.")


def get_section(section_name: str, file: plib.Path) -> SectionProxy:
    global PARSER

    if not PARSER:
        set_global_parser()

    PARSER.read(chain_path(file))
    if not PARSER.has_section(section_name):
        raise SectionDoesNotExist(f"{file} does not contain {section_name} as a section.")

    return PARSER[section_name]

