from _typeshed import Incomplete
from langchain.load.serializable import Serializable
from langchain.pydantic_v1 import BaseModel, FilePath as FilePath
from langchain.schema import Document
from langchain.text_splitter import TextSplitter as TextSplitter
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Literal, Optional, Protocol, Type, Union

class BaseLoader(Protocol):
    def load(self) -> List[Document]: ...
    def load_and_split(self, text_splitter: Optional[TextSplitter] = ...) -> List[Document]: ...
    def lazy_load(self) -> Iterator[Document]: ...

FORMAT_INSTRUCTION: str

class _FilePathLoader(Protocol):
    def __call__(self, file_path: str, **kwargs: Dict[str, Any]) -> BaseLoader: ...

class _FilePathLoaderProtocol(Protocol):
    def __init__(self, file_path: str, **kwargs: Dict[str, Any]) -> None: ...
    def load(self) -> List[Document]: ...

TYPE_CONV_MAPPING: Incomplete

class PromptTemplate(Protocol):
    input_variables: List[str]
    template: str
    def format(self, **kwargs: Any) -> str: ...

logger: Incomplete
SCOPES: List[str]

class _LRUCache:
    def __init__(self, capacity: int = ...) -> None: ...
    def get(self, key: str) -> Optional[str]: ...
    def put(self, key: str, value: str) -> None: ...

def default_conv_loader(mode: Literal['single', 'elements'] = ..., strategy: Literal['strategy', 'fast'] = ..., ocr_languages: str = ...) -> TYPE_CONV_MAPPING: ...

templates: Optional[Dict[str, PromptTemplate]]

def get_template(template: str) -> PromptTemplate: ...

class GoogleDriveUtilities(Serializable, BaseModel):
    class Config:
        extra: Incomplete
        underscore_attrs_are_private: bool
        arbitrary_types_allowed: bool
        allow_mutation: bool
    @property
    def files(self) -> Any: ...
    gdrive_api_file: Optional[FilePath]
    not_data: Incomplete
    def validate_api_file(cls, api_file: Optional[FilePath]) -> FilePath: ...
    def validate_template(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...
    def validate_file_loader_cls(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...
    gdrive_token_path: Optional[Path]
    num_results: int
    mode: str
    recursive: bool
    filter: Callable[[GoogleDriveUtilities, Dict], bool]
    link_field: Literal['webViewLink', 'webContentLink']
    follow_shortcut: bool
    return_link: bool
    conv_mapping: TYPE_CONV_MAPPING
    gslide_mode: Literal['single', 'elements', 'slide']
    gsheet_mode: Literal['single', 'elements']
    scopes: List[str]
    corpora: Optional[Literal['user', 'drive', 'domain', 'allDrives']]
    driveId: Optional[str]
    fields: str
    includeItemsFromAllDrives: Optional[bool]
    includeLabels: Optional[bool]
    includePermissionsForView: Optional[Literal['published']]
    orderBy: Optional[Literal['createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', 'viewedByMeTime']]
    pageSize: int
    spaces: Optional[Literal['drive', 'appDataFolder']]
    supportsAllDrives: bool
    file_loader_cls: Optional[Type]
    file_loader_kwargs: Optional[Dict[str, Any]]
    template: Union[PromptTemplate, Literal['gdrive-all-in-folder', 'gdrive-query', 'gdrive-by-name', 'gdrive-by-name-in-folder', 'gdrive-query-in-folder', 'gdrive-mime-type', 'gdrive-mime-type-in-folder', 'gdrive-query-with-mime-type', 'gdrive-query-with-mime-type-and-folder'], None]
    def orderBy_is_compatible_with_recursive(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...
    def __init__(self, **kwargs) -> None: ...
    def get_folder_name(self, file_id: str, **kwargs: Any) -> str: ...
    def lazy_get_relevant_documents(self, query: Optional[str] = ..., **kwargs: Any) -> Iterator[Document]: ...
    def __del__(self) -> None: ...
    def lazy_load_document_from_id(self, file_id: str) -> Iterator[Document]: ...
    def load_document_from_id(self, file_id: str) -> List[Document]: ...
    def load_slides_from_id(self, file_id: str) -> List[Document]: ...
    def load_sheets_from_id(self, file_id: str) -> List[Document]: ...
    def lazy_load_file_from_id(self, file_id: str) -> Iterator[Document]: ...
    def load_file_from_id(self, file_id: str) -> List[Document]: ...

class GoogleDriveAPIWrapper(GoogleDriveUtilities):
    class Config:
        extra: Incomplete
        underscore_attrs_are_private: bool
    mode: Literal['snippets', 'snippets-markdown', 'documents', 'documents-markdown']
    num_results: int
    template: Union[PromptTemplate, Literal['gdrive-all-in-folder', 'gdrive-query', 'gdrive-by-name', 'gdrive-by-name-in-folder', 'gdrive-query-in-folder', 'gdrive-mime-type', 'gdrive-mime-type-in-folder', 'gdrive-query-with-mime-type', 'gdrive-query-with-mime-type-and-folder'], None]
    def validate_template(cls, v: Dict[str, Any]) -> Dict[str, Any]: ...
    def run(self, query: str) -> str: ...
    def results(self, query: str, num_results: int) -> List[Dict]: ...
    def get_format_instructions(self) -> str: ...
