from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from assessment.services import assessment_services, assessment_permission_services
from baseinfo.services import custom_kit_services


class AssessmentApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def put(self, request, assessment_id):
        result = assessment_services.edit_assessment(request, assessment_id)
        return Response(result["body"], result["status_code"])


class AssessmentsApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request):
        result = assessment_services.create_assessment(request)
        return Response(result["body"], result["status_code"])


class AssessmentsComparableApi(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, assessment_id):
        result = assessment_services.assessments_invite_user(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class InviteesAssessmentsApi(APIView):
    permission_classes = [IsAuthenticated]

    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, assessment_id):
        result = assessment_services.assessment_invitees(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentInvitesApi(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def post(self, request, assessment_id):
        result = assessment_services.assessment_migrate_kit_version(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentAssignCustomKitApi(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        result = assessment_permission_services.get_assessment_permissions_list(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class GrantReportAccessApi(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_id):
        result = assessment_services.access_assessment_report_grant(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class UsersWithReportAccessApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        result = assessment_services.get_report_users_access(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class ReportMetadataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        result = assessment_services.get_report_metadata(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])

    def patch(self, request, assessment_id):
        result = assessment_services.update_report_metadata(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])