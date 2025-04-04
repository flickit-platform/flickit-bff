import re
import pandas as pd
import zipfile
from io import BytesIO
from typing import Dict, List, Optional, Union
from . import constants


class DSLConverterService:
    def __init__(self, excel_file: Union[str, bytes]):
        self.excel_file = excel_file
        self.xls = self.load_excel()

    def load_excel(self) -> pd.ExcelFile:
        """Loads the Excel file."""
        try:
            return pd.ExcelFile(self.excel_file)
        except FileNotFoundError:
            raise FileNotFoundError("The provided Excel file was not found.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the Excel file: {str(e)}")

    def generate_subject_dsl(self, df: pd.DataFrame) -> str:
        """Generates DSL for subjects."""
        df.columns = df.columns.str.strip()
        dsl: List[str] = []
        try:
            subjects = df.dropna(subset=[constants.SHEET_QUALITY_ATTRIBUTES_SUBJECT_NAME])
            for _, row in subjects.iterrows():
                subject_name = row[constants.SHEET_QUALITY_ATTRIBUTES_SUBJECT_NAME]
                subject_title = row[constants.SHEET_QUALITY_ATTRIBUTES_SUBJECT_TITLE]
                subject_weight = row[constants.SHEET_SUBJECT_WEIGHT]
                subject_description = row[constants.SHEET_QUALITY_ATTRIBUTES_SUBJECT_DESCRIPTION]

                dsl_entry = (
                    f'subject {subject_name} {{\n'
                    f'    title: "{subject_title}"\n'
                    f'    description: "{subject_description}"\n'
                )

                if not pd.isna(subject_weight):
                    dsl_entry += f'    weight: {int(subject_weight)}\n'

                dsl_entry += '}'
                dsl.append(dsl_entry)
        except KeyError as e:
            raise ValueError(f"Error: Missing expected column in the sheet: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the sheet: {e}")
        return '\n\n'.join(dsl)

    def convert_maturity_levels(self, df: pd.DataFrame) -> str:
        """Converts maturity levels to DSL."""
        df.columns = df.columns.str.strip()
        levels = df.iloc[:, 0].dropna().tolist()  # Reading the levels from the first column
        dsl: List[str] = []
        try:
            for index, row in df.iterrows():
                title = row[constants.SHEET_MATURITY_LEVELS_TITLE]
                description = row[constants.SHEET_MATURITY_LEVELS_DESCRIPTION]
                value = index + 1
                competence_list: List[str] = []
                for level in levels:
                    if pd.notna(row.get(level)) and row[level] > 0:
                        competence_list.append(f"{level}:{row[level]}%")
                level_name = levels[index] if index < len(levels) else title
                competence_str = f"    competence: [{', '.join(competence_list)}]" if competence_list else ""
                dsl.append(
                    f'level {level_name} {{\n'
                    f'    title: "{title}"\n'
                    f'    description: "{description}"\n'
                    f'    value: {value}\n'
                    f'{competence_str}\n'
                    f'}}'
                )
        except KeyError as e:
            raise ValueError(f"Error: Missing expected column in MaturityLevels sheet: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing MaturityLevels: {e}")
        return '\n\n'.join(dsl)

    def convert_quality_attributes(self, df: pd.DataFrame) -> str:
        """Converts quality attributes to DSL."""
        df.columns = df.columns.str.strip()
        dsl: List[str] = []
        try:
            current_subject: Optional[str] = None
            for _, row in df.iterrows():
                subject_name = row[constants.SHEET_QUALITY_ATTRIBUTES_SUBJECT_NAME]
                if pd.notna(subject_name):
                    current_subject = subject_name
                attribute_name = row[constants.SHEET_ATTRIBUTES_ATTRIBUTE_NAME]
                attribute_title = row[constants.SHEET_ATTRIBUTES_ATTRIBUTE_TITLE]
                attribute_description = row[constants.SHEET_ATTRIBUTES_ATTRIBUTE_DESCRIPTION]
                attribute_weight = row[constants.SHEET_ATTRIBUTES_ATTRIBUTE_WEIGHT]
                if pd.notna(attribute_name):
                    dsl.append(
                        f'attribute {attribute_name} {{\n'
                        f'    title: "{attribute_title}"\n'
                        f'    description: "{attribute_description}"\n'
                        f'    subject: {current_subject}\n'
                        f'    weight: {attribute_weight}\n'
                        f'}}'
                    )
        except KeyError as e:
            raise ValueError(f"Error: Missing expected column in the sheet: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the sheet: {e}")
        return '\n\n'.join(dsl)

    def convert_questionnaires(self, df: pd.DataFrame) -> str:
        """Converts questionnaires to DSL."""
        dsl: List[str] = []
        try:
            for _, row in df.iterrows():
                name = row[constants.SHEET_QUESTIONNAIRES_NAME]
                title = row[constants.SHEET_QUESTIONNAIRES_TITLE]
                description = row[constants.SHEET_QUESTIONNAIRES_DESCRIPTION]
                dsl.append(
                    f'questionnaire {name} {{\n'
                    f'    title: "{title}"\n'
                    f'    description: "{description}"\n'
                    f'}}'
                )
        except KeyError as e:
            raise ValueError(f"Error: Missing expected column in the sheet: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the sheet: {e}")
        return '\n\n'.join(dsl)

    def generate_answer_ranges_dsl(self, answer_options_df: pd.DataFrame) -> str:
        """
        Generates DSL for answer ranges from the answer options DataFrame.
        """
        answer_ranges_dsl = []
        current_range_name = None
        range_options = []
        range_values = []

        for _, row in answer_options_df.iterrows():
            range_name = row[constants.SHEET_OPTIONS_RANGE_NAME]
            option_title = row[constants.SHEET_OPTIONS_TITLE]
            option_value = row[constants.SHEET_OPTIONS_VALUE]

            # If a new range starts, finalize the previous one
            if pd.notna(range_name):
                if current_range_name:
                    # Finalize current range DSL
                    dsl = (
                        f"answerRange {current_range_name} {{\n"
                        f'    title: "{current_range_name}"\n'
                        f'    options: {", ".join(range_options)}'
                    )
                    if range_values:
                        dsl += f" with values [{', '.join(map(str, range_values))}]"
                    dsl += "\n}"
                    answer_ranges_dsl.append(dsl)

                # Start a new range
                current_range_name = range_name
                range_options = []
                range_values = []

            # Add options and values for the current range
            range_options.append(f'"{option_title}"')
            range_values.append(option_value)

        # Finalize the last range
        if current_range_name:
            dsl = (
                f"answerRange {current_range_name} {{\n"
                f'    title: "{current_range_name}"\n'
                f'    options: {", ".join(range_options)}'
            )
            if range_values:
                dsl += f" with values [{', '.join(map(str, range_values))}]"
            dsl += "\n}"

            answer_ranges_dsl.append(dsl)

        return '\n\n'.join(answer_ranges_dsl)

    def convert_questions(self, questions_df: pd.DataFrame) -> Dict[str, List[str]]:
        """Converts questions to DSL grouped by questionnaire."""
        questions_by_questionnaire: Dict[str, List[str]] = {}

        for _, row in questions_df.iterrows():
            question_code = row[constants.SHEET_QUESTIONS_CODE]
            questionnaire_name = row[constants.SHEET_QUESTIONS_QUESTIONNAIRES]

            # Check for title presence before proceeding
            if pd.notna(row[constants.SHEET_QUESTIONS_TITLE]):
                title = row[constants.SHEET_QUESTIONS_TITLE].replace('"', '\\"')
                answer_range_name = row[constants.SHEET_QUESTIONS_OPTIONS]
                description = row[constants.SHEET_QUESTIONS_DESCRIPTION].replace('"', '\\"') if pd.notna(
                    row[constants.SHEET_QUESTIONS_DESCRIPTION]) else constants.DEFAULT_DESCRIPTION
                may_not_be_applicable = row[constants.SHEET_QUESTIONS_MAY_NOT_BE_APPLICABLE] == 1 if pd.notna(
                    row[constants.SHEET_QUESTIONS_MAY_NOT_BE_APPLICABLE]) else False
                advisable = row[constants.SHEET_QUESTIONS_ADVISABLE] == 0 if pd.notna(
                    row[constants.SHEET_QUESTIONS_ADVISABLE]) else True

                # Build the DSL for the question
                question_dsl = (
                    f'question {question_code} {{\n'
                    f'    questionnaire: {questionnaire_name}\n'
                    f'    hint: "{description}"\n'
                    f'    title: "{title}"\n'
                    f'    answerRange: {answer_range_name}\n'
                )

                # Add advisable if it's false
                if advisable:
                    question_dsl += f'        advisable: false\n'

                # Add the affects strings
                affects_str_list: List[str] = []
                for column in questions_df.columns[constants.SHEET_QUESTIONS_START_AFFECTS_COLUMN_INDEX:]:
                    if pd.notna(row[column]):
                        affects_str_list.append(
                            f'affects {column} on level {row[constants.SHEET_QUESTIONS_MATURITY]} with weight {int(row[column])}'
                        )
                affects_str = '\n    '.join(affects_str_list)
                question_dsl += f'    {affects_str}\n'

                # Add mayNotBeApplicable if applicable
                if may_not_be_applicable:
                    question_dsl += f'    mayNotBeApplicable: true\n'

                question_dsl += '}'

                # Group questions by questionnaire
                if questionnaire_name not in questions_by_questionnaire:
                    questions_by_questionnaire[questionnaire_name] = []
                questions_by_questionnaire[questionnaire_name].append(question_dsl)

        return questions_by_questionnaire

    def convert_questionnaire_name(self, name: str) -> str:
        """Converts CamelCase questionnaire name to snake_case."""
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
        return f"{constants.QUESTION_FILE_PREFIX}{name.lower()}"

    def convert_excel_to_dsl(self) -> bytes:
        """Converts an Excel file to DSL format and returns a zipped file as bytes."""
        try:
            # Load all sheets from Excel
            maturity_levels_df = pd.read_excel(self.xls, constants.SHEET_MATURITY_LEVELS,
                                               header=constants.HEADER_MATURITY_LEVELS)
            quality_attributes_df = pd.read_excel(self.xls, constants.SHEET_QUALITY_ATTRIBUTES,
                                                  header=constants.HEADER_QUALITY_ATTRIBUTES)
            questionnaires_df = pd.read_excel(self.xls, constants.SHEET_QUESTIONNAIRES,
                                              header=constants.HEADER_QUESTIONNAIRES)
            questions_df = pd.read_excel(self.xls, constants.SHEET_QUESTIONS, header=constants.HEADER_QUESTIONS)
            answer_options_df = pd.read_excel(self.xls, constants.SHEET_OPTIONS, header=constants.HEADER_OPTIONS)

        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the Excel sheets: {str(e)}")

        try:
            # Generate DSL for each component
            maturity_levels_dsl = self.convert_maturity_levels(maturity_levels_df)
            quality_attributes_dsl = self.convert_quality_attributes(quality_attributes_df)
            questionnaires_dsl = self.convert_questionnaires(questionnaires_df)
            answer_ranges_dsl = self.generate_answer_ranges_dsl(answer_options_df)
            questions_by_questionnaire = self.convert_questions(questions_df)
            subject_dsl = self.generate_subject_dsl(quality_attributes_df)
        except Exception as e:
            raise RuntimeError(f"An error occurred during the conversion process: {str(e)}")

        # Create a zip file in memory
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zipf:
            # Base folder name in the zip file
            base_folder = constants.DSL_FOLDER_NAME

            # Add each DSL component to the zip file
            zipf.writestr(f'{base_folder}/{constants.OUTPUT_FILE_LEVELS}', maturity_levels_dsl)
            zipf.writestr(f'{base_folder}/{constants.OUTPUT_FILE_QUALITY_ATTRIBUTES}', quality_attributes_dsl)
            zipf.writestr(f'{base_folder}/{constants.OUTPUT_FILE_QUESTIONNAIRES}', questionnaires_dsl)
            zipf.writestr(f'{base_folder}/{constants.OUTPUT_FILE_SUBJECTS}', subject_dsl)
            zipf.writestr(f'{base_folder}/{constants.OUTPUT_FILE_ANSWER_RANGES}', answer_ranges_dsl)

            for questionnaire_name, questions_dsl in questions_by_questionnaire.items():
                zipf.writestr(
                    f'{base_folder}/{self.convert_questionnaire_name(questionnaire_name)}{constants.DSL_FILE_EXT}',
                    '\n\n'.join(questions_dsl)
                )

        zip_buffer.seek(0)  # Reset the buffer's position to the beginning
        return zip_buffer.getvalue()
