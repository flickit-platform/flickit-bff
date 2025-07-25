from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import kit_versions_services


class KitVersionsApi(APIView):
    authenticate()

    def get(self, request, kit_version_id):
        result = kit_versions_services.load_kit_with_version_id(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id):
        result = kit_versions_services.delete_kit_version(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class KitVersionSubjectsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_subject_kit_version(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_subjects_list(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class KitVersionSubjectApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, subject_id):
        result = kit_versions_services.update_subject(request, kit_version_id,
                                                      subject_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, subject_id):
        result = kit_versions_services.delete_subject_with_kit_version_id(request, kit_version_id,
                                                                          subject_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class SubjectChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_subject_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class KitVersionMaturityLevelsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_maturity_levels_with_kit_version(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_maturity_levels_with_kit_version(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class KitVersionMaturityLevelApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, maturity_level_id):
        result = kit_versions_services.update_maturity_level_with_kit_version(request, kit_version_id,
                                                                              maturity_level_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, maturity_level_id):
        result = kit_versions_services.delete_maturity_level_with_kit_version(request, kit_version_id,
                                                                              maturity_level_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class MaturityLevelsChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_maturity_levels_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class LevelCompetencesApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_level_competence(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_level_competences_list(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class LevelCompetenceApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, level_competence_id):
        result = kit_versions_services.update_level_competence(request, kit_version_id, level_competence_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, level_competence_id):
        result = kit_versions_services.delete_level_competence(request, kit_version_id, level_competence_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class KitActiveApi(APIView):
    authenticate()

    def post(self, request, kit_version_id):
        result = kit_versions_services.kit_active(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AttributesApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_attribute(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_attributes_list(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class AttributeApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, attribute_id):
        result = kit_versions_services.update_attribute(request, kit_version_id, attribute_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, attribute_id):
        result = kit_versions_services.delete_attribute(request, kit_version_id, attribute_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AttributeChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_attribute_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionnairesApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_questionnaire(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_questionnaires_list(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class QuestionnaireApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, questionnaire_id):
        result = kit_versions_services.update_questionnaire(request, kit_version_id, questionnaire_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, questionnaire_id):
        result = kit_versions_services.delete_questionnaire(request, kit_version_id, questionnaire_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionnaireChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_questionnaire_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_question(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class QuestionApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, question_id):
        result = kit_versions_services.update_question(request, kit_version_id, question_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, questionnaire_id):
        result = kit_versions_services.delete_question(request, kit_version_id, questionnaire_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionsChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_questions_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionImpactsApi(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_question_impact(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class QuestionImpactApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, question_impact_id):
        result = kit_versions_services.update_question_impact(request, kit_version_id, question_impact_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, question_impact_id):
        result = kit_versions_services.delete_question_impact(request, kit_version_id, question_impact_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionImpactListApi(APIView):
    authenticate()

    def get(self, request, kit_version_id, question_id):
        result = kit_versions_services.get_question_impacts_list(request, kit_version_id, question_id)
        return Response(data=result["body"], status=result["status_code"])


class AnswerOptionsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_answer_option(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class AnswerOptionApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, answer_option_id):
        result = kit_versions_services.update_answer_option(request, kit_version_id, answer_option_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, kit_version_id, answer_option_id):
        result = kit_versions_services.delete_answer_option(request, kit_version_id, answer_option_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class QuestionOptionsListApi(APIView):
    authenticate()

    def get(self, request, kit_version_id, question_id):
        result = kit_versions_services.get_question_options_list(request, kit_version_id, question_id)
        return Response(data=result["body"], status=result["status_code"])


class QuestionnaireListQuestionsApi(APIView):
    authenticate()
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id, questionnaire_id):
        result = kit_versions_services.get_questionnaire_questions_list(request, kit_version_id, questionnaire_id)
        return Response(data=result["body"], status=result["status_code"])


class AnswerRangesApi(APIView):
    authenticate()
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, kit_version_id):
        result = kit_versions_services.get_answer_ranges(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_answer_range(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class AnswerRangeApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, answer_range_id):
        result = kit_versions_services.update_answer_range(request, kit_version_id, answer_range_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AnswerOptionInAnswerRangeApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_answer_option_in_answer_range(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])


class KitVersionValidateApi(APIView):
    authenticate()

    def get(self, request, kit_version_id):
        result = kit_versions_services.load_kit_version_validate(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

class MeasuresApi(APIView):
    authenticate()

    def get(self, request, kit_version_id):
        result = kit_versions_services.get_measures_list(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id, measure_id):
        result = kit_versions_services.update_measures(request, kit_version_id, measure_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, kit_version_id):
        result = kit_versions_services.create_measures(request, kit_version_id)
        return Response(data=result["body"], status=result["status_code"])
class MeasureChangeOrderApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, kit_version_id):
        result = kit_versions_services.change_measure_order(request, kit_version_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])