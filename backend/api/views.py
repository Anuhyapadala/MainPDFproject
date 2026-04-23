from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.utils.ocr_engine import extract_text
from api.utils.aggregator import build_final_output


class UploadPDFView(APIView):

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            file.seek(0)

            print("FILE:", file.name)

            # STEP 1: OCR
            text = extract_text(file)

            print("TEXT TYPE:", type(text))
            print("TEXT:", text[:500])  # avoid huge logs

            # STEP 2: AI parsing
            result = build_final_output(text)
            print("PARSED DATA:", result)

            print("RESULT TYPE:", type(result))
            print("RESULT:", result)

            return Response({
                "filename": file.name,
                "raw_text": text,
                "structured_data": result
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )
        
