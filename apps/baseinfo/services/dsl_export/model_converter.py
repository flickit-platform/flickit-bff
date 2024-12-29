from typing import Dict, List
from collections import defaultdict

from baseinfo.services.dsl_export.models.json_models import KitModel as JsonKit

from baseinfo.services.dsl_export.models.kit_models import (
    KitModel, SubjectModel, AttributeModel, QuestionnaireModel,
    QuestionModel, QuestionImpactModel, AnswerRangeModel, OptionModel,
    LevelModel
)


def map_json_to_kit(json_kit: JsonKit) -> KitModel:
    """
    Function to convert the old JSON-based model to the new KitModel.
    """

    # 1) Build AnswerRangeModels
    answer_range_dict: Dict[str, AnswerRangeModel] = {}
    new_answer_ranges: List[AnswerRangeModel] = []
    for rng in json_kit.answerRangeModels:
        new_ar = AnswerRangeModel(
            range_name=rng.code,
            index=rng.index if rng.index is not None else 0,
            title=rng.title,
            description=rng.description,
            options=[
                OptionModel(
                    index=o.index,
                    caption=o.caption,
                    value=o.value
                ) for o in rng.options
            ],
            values=None  # If needed, you can extract these values from JSON
        )
        new_answer_ranges.append(new_ar)
        answer_range_dict[rng.code] = new_ar

    # 2) Build LevelModels
    level_dict: Dict[str, LevelModel] = {}
    new_levels: List[LevelModel] = []
    for lvl in json_kit.levelModels:
        new_lvl = LevelModel(
            level_name=lvl.code,
            index=lvl.index if lvl.index is not None else 0,
            title=lvl.title,
            description=lvl.description,
            value=lvl.value if lvl.value is not None else 0,
            competence=lvl.levelCompetence or {}
        )
        new_levels.append(new_lvl)
        level_dict[lvl.code] = new_lvl  # Updated to use `lvl.code`

    # 3) Build AttributeModels
    attribute_dict: Dict[str, AttributeModel] = {}
    attribute_map = defaultdict(list)  # Used for grouping by subjectCode
    for attr in json_kit.attributeModels:
        new_attr = AttributeModel(
            attribute_name=attr.code,
            index=attr.index,
            weight=attr.weight,
            title=attr.title,
            description=attr.description
        )
        attribute_dict[attr.code] = new_attr
        # Grouping by subjectCode
        attribute_map[attr.subjectCode].append(new_attr)

    # 4) Build SubjectModels
    new_subjects: List[SubjectModel] = []
    for sub in json_kit.subjectModels:
        # Find the Attributes associated with this Subject
        sub_attrs = attribute_map[sub.code]
        new_sub = SubjectModel(
            subject_name=sub.code,
            index=sub.index,
            title=sub.title,
            description=sub.description,
            weight=sub.weight,
            attributes=sub_attrs
        )
        new_subjects.append(new_sub)

    # 5) Build QuestionnaireModels in a dictionary
    questionnaire_dict: Dict[str, QuestionnaireModel] = {}
    for qn in json_kit.questionnaireModels:
        new_qn = QuestionnaireModel(
            questionnaire_name=qn.code,
            index=qn.index,
            title=qn.title,
            description=qn.description,
            questions=[]  # Will fill later
        )
        questionnaire_dict[qn.code] = new_qn

    # 6) Group questions by questionnaireCode
    q_map = defaultdict(list)
    for q in json_kit.questionModels:
        q_map[q.questionnaireCode].append(q)

    # Build QuestionModels and attach them to Questionnaires
    for q_code, q_items in q_map.items():
        if q_code not in questionnaire_dict:
            continue  # If the questionnaire code is not in the dictionary, skip
        new_qn = questionnaire_dict[q_code]

        new_questions: List[QuestionModel] = []
        for ques in q_items:
            # Build impacts
            new_impacts: List[QuestionImpactModel] = []
            for imp in ques.questionImpacts:
                # Find the attribute by code
                at_obj = attribute_dict.get(imp.attributeCode)
                # Find the level by code
                lvl_obj = None
                if imp.level and imp.level.code in level_dict:
                    lvl_obj = level_dict[imp.level.code]

                new_impacts.append(
                    QuestionImpactModel(
                        attribute=at_obj,
                        level=lvl_obj,
                        weight=int(imp.weight),
                        optionValues=imp.optionValues
                    )
                )

            # The answerRange field
            ans_range_obj = answer_range_dict.get(ques.answerRangeCode)

            new_question = QuestionModel(
                question_code=ques.code,
                index=ques.index,
                title=ques.title or "",
                description=ques.description or "",
                mayNotBeApplicable=ques.mayNotBeApplicable,
                advisable=ques.advisable,
                answerRange=ans_range_obj,
                impacts=new_impacts
            )
            new_questions.append(new_question)

        # Attach the list of questions to the Questionnaire
        new_qn.questions = new_questions

    # Build the list of Questionnaires from the dictionary
    new_questionnaires = list(questionnaire_dict.values())

    # 7) Build the final KitModel
    new_kit = KitModel(
        subjects=new_subjects,
        questionnaires=new_questionnaires,
        levels=new_levels,
        answerRanges=new_answer_ranges
    )
    return new_kit


def json_to_kit_model(json: dict) -> KitModel:
    json_data = JsonKit(**json)
    return map_json_to_kit(json_data)
