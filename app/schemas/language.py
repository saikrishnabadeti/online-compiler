##################################################################
################ This language by Rahul ##########################
##################################################################


from pydantic import BaseModel
from typing import Optional, List




class LanguageBase(BaseModel):
    lang_name: str
    description: Optional[str] = None
 
class LanguageCreate(LanguageBase):
    pass
 
class LanguageUpdate(BaseModel):
    lang_name: Optional[str] = None
    description: Optional[str] = None
 
class LanguageOut(LanguageBase):
    lang_id: int
 
class LanguagesBulkCreate(BaseModel):
    languages: List[LanguageCreate]
