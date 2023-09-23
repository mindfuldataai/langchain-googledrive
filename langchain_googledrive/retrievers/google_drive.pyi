from ..utilities.google_drive import GoogleDriveUtilities as GoogleDriveUtilities, get_template as get_template
from _typeshed import Incomplete
from langchain.callbacks.manager import AsyncCallbackManagerForRetrieverRun as AsyncCallbackManagerForRetrieverRun, CallbackManagerForRetrieverRun as CallbackManagerForRetrieverRun
from langchain.schema import BaseRetriever, Document as Document
from typing import Any, Dict, Literal

class GoogleDriveRetriever(GoogleDriveUtilities, BaseRetriever):
    class Config:
        extra: Incomplete
        allow_mutation: bool
        underscore_attrs_are_private: bool
    mode: Literal['snippets', 'snippets-markdown', 'documents', 'documents-markdown']
    def validate_template(cls, v: Dict[str, Any]) -> Dict[str, Any]: ...
