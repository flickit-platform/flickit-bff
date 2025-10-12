from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import assessment_kit_service
from rest_framework.permissions import AllowAny

class AssessmentKitStateApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.get_assessment_kit_state(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitInfoApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.get_assessment_kit_info(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitApi(APIView):
    authenticate()

    def patch(self, request, assessment_kit_id):
        result = assessment_kit_service.update_assessment_kit(request, assessment_kit_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, assessment_kit_id):
        result = assessment_kit_service.delete_assessment_kit(request, assessment_kit_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.get_assessment_kit_details(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsSubjectApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, subject_id):
        result = assessment_kit_service.get_assessment_kit_details_subjects(request, assessment_kit_id, subject_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsAttributesApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, attribute_id):
        result = assessment_kit_service.get_assessment_kit_details_attributes(request, assessment_kit_id, attribute_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsQuestionnairesApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, questionnaire_id):
        result = assessment_kit_service.get_assessment_kit_details_questionnaires(request,
                                                                                  assessment_kit_id,
                                                                                  questionnaire_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsQuestionApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, question_id):
        result = assessment_kit_service.get_assessment_kit_details_question(request,
                                                                            assessment_kit_id,
                                                                            question_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitDetailsMaturityLevelsAsAttributeApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, attribute_id, maturity_level_id):
        result = assessment_kit_service.get_assessment_kit_details_maturity_levels_as_attribute(request,
                                                                                                assessment_kit_id,
                                                                                                attribute_id,
                                                                                                maturity_level_id)
        return Response(data=result["body"], status=result["status_code"])
    
    
class AssessmentKitDetailsMeasureApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id, measure_id):
        result = assessment_kit_service.get_assessment_kit_details_measure(request,
                                                                            assessment_kit_id,
                                                                            measure_id)
        return Response(data=result["body"], status=result["status_code"])    


class AssessmentKitLikeApi(APIView):
    authenticate()

    def post(self, request, assessment_kit_id):
        result = assessment_kit_service.like_assessment_kit(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentKitsApi(APIView):
    authenticate()

    def get(self, request):
        result = assessment_kit_service.get_assessment_kits_list(request)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request):
        result = assessment_kit_service.create_assessment_kit(request)
        return Response(data=result["body"], status=result["status_code"])


class PublicAssessmentKitsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        result = assessment_kit_service.get_public_assessment_kits_list(request)
        return Response(data=result["body"], status=result["status_code"])

class PublicAssessmentKitApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.get_public_assessment_kit(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])

class AssessmentKitsSearchApi(APIView):
    authenticate()
    query_param = openapi.Parameter('query', openapi.IN_QUERY, description="search query param",
                                    type=openapi.TYPE_STRING)
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[query_param, size_param, page_param])
    def get(self, request):
        result = assessment_kit_service.assessment_kit_search(request)
        return Response(data=result["body"], status=result["status_code"])


class CloneAssessmentKitApi(APIView):
    authenticate()

    def post(self, request, assessment_kit_id):
        result = assessment_kit_service.clone_assessment_kit(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class CustomSubjectApi(APIView):
    authenticate()

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)
    kit_custom_id_param = openapi.Parameter('kitCustomId', openapi.IN_QUERY, description="kit_custom_id",
                                            type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param, kit_custom_id_param])
    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.load_custom_subject(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class KitLanguageApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_kit_id):
        result = assessment_kit_service.add_kit_language(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])