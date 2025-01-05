import re
import zipfile
from io import BytesIO
from typing import Dict, List, Optional
from jinja2 import Environment, FileSystemLoader, select_autoescape
from baseinfo.services.dsl_export import constants
from baseinfo.services.dsl_export.models.kit_models import KitModel


class KitToDSLConverterService:
    def __init__(self):
        # Configure the Jinja2 Environment
        self.env = Environment(
            loader=FileSystemLoader('baseinfo/services/dsl_export/templates'),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=select_autoescape(['html', 'xml']))

    def escape_quotes(self, text: Optional[str], default: str = "") -> str:
        """
        Escape double quotes in a given text by replacing " with \\".
        If the text is None or empty, return the default value.
        """
        if not text:
            return default
        return text.replace('"', '\\"')

    def generate_dsl_from_kit(self, kit: KitModel) -> Dict[str, str]:
        """
        Generate DSL strings from a KitModel.
        Returns a dictionary with file names as keys and DSL content as values.
        """
        dsl_files: Dict[str, str] = {}

        # 1. Generate DSL for Subjects
        subject_dsl = []
        subject_template = self.env.get_template('subject_template.txt')
        for subject in sorted(kit.subjects, key=lambda x: x.index):
            rendered = subject_template.render(
                subject_name=subject.subject_name,
                title=subject.title,
                description=self.escape_quotes(subject.description)
            )
            subject_dsl.append(rendered)
        dsl_files[constants.OUTPUT_FILE_SUBJECTS] = '\n\n'.join(subject_dsl)

        # 2. Generate DSL for Levels
        levels_dsl = []
        level_template = self.env.get_template('level_template.txt')
        for level in sorted(kit.levels, key=lambda x: x.index):
            rendered = level_template.render(
                level_name=level.level_name,
                title=level.title,
                description=self.escape_quotes(level.description),
                value=level.value,
                competence=level.competence if level.competence else {}
            )
            levels_dsl.append(rendered)
        dsl_files[constants.OUTPUT_FILE_LEVELS] = '\n\n'.join(levels_dsl)

        # 3. Generate DSL for AnswerRanges
        answer_ranges_dsl = []
        answer_range_template = self.env.get_template('answer_range_template.txt')
        for answer_range in sorted(kit.answerRanges, key=lambda x: x.index):
            options_sorted = sorted(answer_range.options, key=lambda x: x.index)
            if answer_range.values and len(answer_range.values) > 0:
                values_str = answer_range.values
            else:
                # Extract the value from options if values are not set
                values_str = [option.value for option in options_sorted]
            rendered = answer_range_template.render(
                range_name=answer_range.range_name,
                title=self.escape_quotes(answer_range.title),
                options=options_sorted,  # list of OptionModel
                values=values_str
            )
            answer_ranges_dsl.append(rendered)
        dsl_files[constants.OUTPUT_FILE_ANSWER_RANGES] = '\n\n'.join(answer_ranges_dsl)

        # 4. Generate DSL for Questionnaires and Questions
        questionnaires_dsl = []
        questions_dsl_files: Dict[str, str] = {}
        questionnaire_template = self.env.get_template('questionnaire_template.txt')
        question_template = self.env.get_template('question_template.txt')

        for questionnaire in sorted(kit.questionnaires, key=lambda x: x.index):
            # Render Questionnaire
            rendered_questionnaire = questionnaire_template.render(
                questionnaire_name=questionnaire.questionnaire_name,
                title=questionnaire.title,
                description=self.escape_quotes(questionnaire.description)
            )
            questionnaires_dsl.append(rendered_questionnaire)

            # Render Questions
            questions_dsl = []
            for question in sorted(questionnaire.questions, key=lambda x: x.index):
                impacts = []
                for impact in question.impacts:
                    if impact.attribute and impact.level:
                        impacts.append({
                            'attribute': impact.attribute.attribute_name,
                            'level': impact.level.level_name,
                            'weight': impact.weight
                        })

                # Convert values to boolean and manage default values
                may_not_be_applicable = question.mayNotBeApplicable if question.mayNotBeApplicable is not None else False
                advisable = question.advisable if question.advisable is not None else True

                rendered_question = question_template.render(
                    question_code=question.question_code,
                    questionnaire_name=questionnaire.questionnaire_name,
                    hint=self.escape_quotes(question.description, default=" "),
                    title=self.escape_quotes(question.title),
                    answer_range=question.answerRange.range_name if question.answerRange else "",
                    may_not_be_applicable=may_not_be_applicable,
                    advisable=advisable,
                    impacts=impacts if impacts else []
                )
                questions_dsl.append(rendered_question)

            # Save DSL questions as a separate file
            questionnaire_file_name = self.convert_questionnaire_name(
                questionnaire.questionnaire_name) + constants.DSL_FILE_EXT
            questions_dsl_files[questionnaire_file_name] = '\n\n'.join(questions_dsl)

        dsl_files[constants.OUTPUT_FILE_QUESTIONNAIRES] = '\n\n'.join(questionnaires_dsl)
        # Add question files to the DSL dictionary
        dsl_files.update(questions_dsl_files)

        # 5. Generate DSL for Attributes
        attributes_dsl = []
        attribute_template = self.env.get_template('attribute_template.txt')
        for subject in sorted(kit.subjects, key=lambda x: x.index):
            for attribute in sorted(subject.attributes, key=lambda x: x.index):
                rendered = attribute_template.render(
                    attribute_name=attribute.attribute_name,
                    title=attribute.title,
                    description=self.escape_quotes(attribute.description),
                    subject_name=subject.subject_name,
                    index=attribute.index,
                    weight=attribute.weight
                )
                attributes_dsl.append(rendered)
        dsl_files[constants.OUTPUT_FILE_QUALITY_ATTRIBUTES] = '\n\n'.join(attributes_dsl)

        return dsl_files

    def convert_questionnaire_name(self, name: str) -> str:
        """
        Convert the questionnaire name from CamelCase to snake_case.
        """
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
        return f"{constants.QUESTION_FILE_PREFIX}_{name.lower()}"

    def convert_kit_to_dsl_zip(self, kit: KitModel) -> bytes:
        """
        Convert KitModel to a zipped DSL file.
        Returns the ZIP file as bytes.
        """
        try:
            # Generate DSL from KitModel
            dsl_files = self.generate_dsl_from_kit(kit)

            # Create an in-memory ZIP file
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Base folder name in the ZIP file
                base_folder = constants.DSL_FOLDER_NAME

                # Add each DSL file to the ZIP file
                for file_name, dsl_content in dsl_files.items():
                    zipf.writestr(f'{base_folder}/{file_name}', dsl_content)

            zip_buffer.seek(0)  # Reset the reading pointer to the beginning of the buffer
            return zip_buffer.getvalue()

        except Exception as e:
            raise RuntimeError(f"An error occurred during the DSL generation process: {str(e)}")
