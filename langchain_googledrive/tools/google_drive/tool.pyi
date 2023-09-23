from ...utilities.google_drive import FORMAT_INSTRUCTION as FORMAT_INSTRUCTION, GoogleDriveAPIWrapper as GoogleDriveAPIWrapper
from _typeshed import Incomplete
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun as AsyncCallbackManagerForToolRun, CallbackManagerForToolRun as CallbackManagerForToolRun
from langchain.tools import BaseTool

logger: Incomplete

class GoogleDriveSearchTool(BaseTool):
    name: str
    description: Incomplete
    api_wrapper: GoogleDriveAPIWrapper
