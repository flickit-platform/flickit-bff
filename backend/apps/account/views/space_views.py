from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from account.services import space_services


class SpacesApi(APIView):
    permission_classes = [IsAuthenticated]
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    def post(self, request):
        result = space_services.create_spacer(request)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request):
        result = space_services.get_spaces_list(request)
        return Response(data=result["body"], status=result["status_code"])


class MembersSpaceApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, space_id):
        result = space_services.get_list_members_in_space(request, space_id)
        return Response(data=result["body"], status=result["status_code"])

    def post(self, request, space_id):
        result = space_services.add_member_in_space(request, space_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class MemberSpaceApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, space_id, user_id):
        result = space_services.delete_member_space(request, space_id, user_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class InviteMembersSpaceApi(APIView):
    permission_classes = [IsAuthenticated]
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param])
    def get(self, request, space_id):
        result = space_services.space_invites_list(request, space_id)
        return Response(data=result["body"], status=result["status_code"])


class InviteMemberInSpaceApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, space_id):
        result = space_services.invite_member_in_space(request, space_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class SpaceSeenApi(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, space_id):
        result = space_services.space_seen_service(request, space_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class SpaceApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, space_id):
        result = space_services.get_space(request, space_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, space_id):
        result = space_services.update_space(request, space_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])
