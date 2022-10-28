from pydantic import BaseModel


class ExternalPhoto(BaseModel):
    """
    Model used to validate external photo data
    Since we do not always need to set up whole project
    """
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str
