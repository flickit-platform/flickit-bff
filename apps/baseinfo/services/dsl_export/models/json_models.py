from pydantic import BaseModel
from typing import List, Optional, Dict

class OptionModel(BaseModel):
    index: int
    caption: str
    value: float

class AnswerRangeModel(BaseModel):
    code: str
    index: Optional[int] = None
    title: str
    description: Optional[str] = None
    options: List[OptionModel]

class LevelModel(BaseModel):
    code: str
    index: Optional[int] = None
    title: str
    description: Optional[str] = None
    value: Optional[int] = None
    levelCompetence: Optional[Dict[str, int]] = None

class SubjectModel(BaseModel):
    code: str
    index: int
    title: str
    description: str
    weight: int
    questionnaireCodes: Optional[List[str]] = None

class AttributeModel(BaseModel):
    code: str
    index: int
    title: str
    description: str
    subjectCode: str
    weight: int

class QuestionImpactModel(BaseModel):
    attributeCode: str
    weight: float
    level: LevelModel
    optionValues: Dict[str, float]

class QuestionModel(BaseModel):
    code: str
    index: int
    title: str
    description: Optional[str] = None
    questionnaireCode: str
    questionImpacts: List[QuestionImpactModel]
    answerRangeCode: Optional[str] = None
    mayNotBeApplicable: bool
    advisable: bool
    answers: Optional[Dict] = None

class QuestionnaireModel(BaseModel):
    code: str
    index: int
    title: str
    description: str

class KitModel(BaseModel):
    questionnaireModels: List[QuestionnaireModel]
    attributeModels: List[AttributeModel]
    questionModels: List[QuestionModel]
    subjectModels: List[SubjectModel]
    levelModels: List[LevelModel]
    answerRangeModels: List[AnswerRangeModel] = []
    hasError: bool
