from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

from .utils import extract_text, extract_table_data

logger = logging.getLogger(__name__)


class UploadPDFView(APIView):

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            file.seek(0)  # safe reset

            # extract text
            text = extract_text(file)

            # extract structured data
            table_data = extract_table_data(text)

            return Response({
                "filename": file.name,
                "raw_text": text,
                "table_data": table_data
            })

        except Exception as e:
            logger.error(f"PDF upload failed: {str(e)}")

            return Response({
                "error": str(e),
                "type": type(e).__name__
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)