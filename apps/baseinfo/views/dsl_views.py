from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import FileResponse

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services.dsl_conversion.dsl_conversion_service import DSLConverterService
from baseinfo.serializers.dsl_serializers import ExcelFileUploadSerializer
from io import BytesIO
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from assessmentplatform.settings import EXCEL_SAMPLE_URL
from baseinfo.services import dsl_services
from baseinfo.services.dsl_export.kit_to_dsl_converter import KitToDSLConverterService
from baseinfo.services.dsl_export.model_converter import json_to_kit_model


class DSLConversionApi(APIView):
    authenticate()
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Convert Excel file to DSL and return as a zipped file",
        request_body=ExcelFileUploadSerializer,
        responses={
            200: openapi.Response(
                description="A zip file containing the DSL files",
                content_type='application/zip',
                schema=openapi.Schema(type=openapi.TYPE_FILE)
            ),
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        serializer = ExcelFileUploadSerializer(data=request.data)

        if serializer.is_valid():
            file = serializer.validated_data['file']
            try:
                # Create an instance of the conversion service
                converter_service = DSLConverterService(file)
                # Convert the Excel file to DSL and get the zip file as bytes
                zip_file_content = converter_service.convert_excel_to_dsl()

                # Create an in-memory file response
                response = FileResponse(BytesIO(zip_file_content), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=kit.zip'
                return response

            except ValueError as ve:
                return Response({"message": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
            except RuntimeError as re:
                return Response({"message": str(re)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": f"An unexpected error occurred: {str(e)}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            errors = serializer.errors
            # Extract the first error message from the error dictionary
            first_error_message = list(errors.values())[0][0] if errors else "Invalid input."
            return Response({"message": first_error_message}, status=status.HTTP_400_BAD_REQUEST)


class DSLConversionFileSampleApi(APIView):
    authenticate()

    def get(self, request):
        return Response({"url": EXCEL_SAMPLE_URL})


class KitToDSLExportApi(APIView):
    authenticate()

    @swagger_auto_schema(
        operation_description="Convert Kit JSON to DSL and return as a zipped file",
        responses={
            200: openapi.Response(
                description="A zip file containing the DSL files",
                content={'application/zip': {}},
            ),
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def get(self, request, assessment_kit_id):
        try:
            # 1) Call the microservice to get the DSL JSON
            result = dsl_services.get_dsl_json(request, assessment_kit_id)
            if result["status_code"] != 200:
                # If the microservice did not return a 200 OK, forward the error body and status code
                return Response(data=result["body"], status=result["status_code"])

            # 2) Convert the JSON to KitModel
            try:
                kit_model = json_to_kit_model(result["body"])
            except Exception as e:
                # Any validation or conversion error
                return Response(
                    {"message": f"Error converting JSON to KitModel: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # 3) Convert KitModel to DSL (ZIP bytes)
            converter = KitToDSLConverterService()
            try:
                dsl_zip_bytes = converter.convert_kit_to_dsl_zip(kit_model)
            except Exception as e:
                return Response(
                    {"message": f"Error generating DSL ZIP file: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # 4) Return the ZIP file
            response = FileResponse(BytesIO(dsl_zip_bytes), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=kit.zip'
            return response

        except Exception as e:
            # Catch any other unforeseen errors
            return Response(
                {"message": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )