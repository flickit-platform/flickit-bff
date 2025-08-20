from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from assessment.services import assessment_services, assessment_permission_services
from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import custom_kit_services


class AssessmentApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def put(self, request, assessment_id):
        result = assessment_services.edit_assessment(request, assessment_id)
        return Response(result["body"], result["status_code"])


class AssessmentsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request):
        result = assessment_services.create_assessment(request)
        return Response(result["body"], result["status_code"])


class AssessmentsComparableApi(APIView):
    authenticate()
    kit_id_param = openapi.Parameter('kitId', openapi.IN_QUERY, description="kit id param",
                                     type=openapi.TYPE_INTEGER)
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[kit_id_param, size_param, page_param])
    def get(self, request):
        result = assessment_services.assessments_comparable_list(request)
        return Response(result["body"], result["status_code"])


class InviteUsersAssessmentsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, assessment_id):
        result = assessment_services.assessments_invite_user(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class InviteesAssessmentsApi(APIView):
    authenticate()

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, assessment_id):
        result = assessment_services.assessment_invitees(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentInvitesApi(APIView):
    authenticate()

    def delete(self, request, invite_id):
        result = assessment_services.assessment_invite_delete(request, invite_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, invite_id):
        result = assessment_services.assessment_invite_edit(request, invite_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentMigrateKitVersionApi(APIView):
    authenticate()

    def post(self, request, assessment_id):
        result = assessment_services.assessment_migrate_kit_version(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentAssignCustomKitApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_id):
        assessments_details = assessment_services.load_assessment(request, assessment_id)
        if assessments_details["status_code"] != 200:
            return Response(assessments_details["body"], assessments_details["status_code"])
        custom_kit = custom_kit_services.create_custom_kit(request, assessments_details["body"]["kit"]["id"])
        if custom_kit["status_code"] != 201:
            return Response(custom_kit["body"], custom_kit["status_code"])
        result = assessment_services.assign_custom_kit(request, assessment_id, custom_kit["body"]["kitCustomId"])
        if result["Success"]:
            return Response(data=custom_kit["body"], status=201)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentPermissionsListApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_permission_services.get_assessment_permissions_list(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class GrantReportAccessApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_id):
        result = assessment_services.access_assessment_report_grant(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class UsersWithReportAccessApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_services.get_report_users_access(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class ReportMetadataAPI(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_services.get_report_metadata(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body = openapi.Schema(type = openapi.TYPE_OBJECT), response = 201)
    def patch(self, request, assessment_id):
        result = assessment_services.update_report_metadata(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

class QuestionIssuesApi(APIView):
    authenticate()

    def get(self, request, assessment_id, question_id):
        result = assessment_services.get_question_issues(request, assessment_id, question_id)
        return Response(data=result["body"], status=result["status_code"])


class PreAdviceInfoApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_services.get_pre_advice_info(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class ApproveAnswerApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, assessment_id):
        result = assessment_services.approve_answer(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class ApproveAssessmentAnswersApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_services.approve_assessment_answers(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

class AssessmentModeApi(APIView):
    authenticate()
    mode_param = openapi.Parameter('mode', openapi.IN_QUERY, description="mode",
                                    type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(request_body = openapi.Schema(type = openapi.TYPE_OBJECT), response = 200)
    def put(self, request, assessment_id):
        result = assessment_services.update_assessment_mode(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

class AssessmentSpaceApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body = openapi.Schema(type = openapi.TYPE_OBJECT), response = 200)
    def put(self, request, assessment_id):
        result = assessment_services.update_assessment_space(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

class MoveTargetsApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_services.get_move_targets(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])