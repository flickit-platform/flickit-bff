from typing import List, Optional, Dict
from pydantic import BaseModel

class OptionModel(BaseModel):
    index: int
    caption: str
    value: float

class AnswerRangeModel(BaseModel):
    range_name: str
    index: int
    title: str
    description: Optional[str] = None
    options: List[OptionModel]
    values: Optional[List[float]] = None

class LevelModel(BaseModel):
    level_name: str
    index: int
    title: str
    description: Optional[str] = None
    value: int
    competence: Dict[str, int]

class AttributeModel(BaseModel):
    attribute_name: str
    index: int
    title: str
    description: str
    weight : int

class QuestionImpactModel(BaseModel):
    attribute: Optional[AttributeModel] = None
    level: Optional[LevelModel] = None
    weight: int
    optionValues: Optional[Dict[str, float]] = None

class QuestionModel(BaseModel):
    question_code: str
    index: int
    title: str
    description: Optional[str] = None
    mayNotBeApplicable: bool
    advisable: bool
    answerRange: Optional[AnswerRangeModel] = None
    impacts: List[QuestionImpactModel]

class QuestionnaireModel(BaseModel):
    questionnaire_name: str
    index: int
    title: str
    description: str
    questions: List[QuestionModel]

class SubjectModel(BaseModel):
    subject_name: str
    index: int
    title: str
    description: str
    weight: int
    attributes: List[AttributeModel]

class KitModel(BaseModel):
    subjects: List[SubjectModel]
    questionnaires: List[QuestionnaireModel]
    levels: List[LevelModel]
    answerRanges: List[AnswerRangeModel]
