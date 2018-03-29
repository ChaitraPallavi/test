from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from service import *
import json
from utility import InputParser
from common_utils.error_handler import ErrorHandler
from common_utils.response_handler import SuccessResponse
from django.shortcuts import render


def default_view(request):
    return render(request, 'condenast/index.html', {
        'message': SuccesMessages.WELCOME_MESSAGE.value,
    })


class UpdateDataToDb(APIView):
    parser_classes = (InputParser,)

    @csrf_exempt
    def post(self, request):

        input_data = InputParser.parse(InputParser(), request.data)

        try:
            sys_fields = json.loads(input_data.body).get('sys')
            content_id = json.loads(input_data.body).get('sys').get('contentType').get('sys').get('id')
            input_request = json.loads(input_data.body).get('fields')
            response = None
            if content_id == 'places':
                response = AddOrEditPlace.add_edit_place(input_request, sys_fields.get('id'))

            elif content_id == 'feedTips':
                response = AddEditTips.add_edit_tips(input_request, sys_fields.get('id'))

            elif content_id == 'contributor':
                response = Contributor.add_edit_contributor(input_request, sys_fields.get('id'))

            elif content_id == 'noteworthy':
                response = Noteworthy.add_edit_noteworthy(input_request, sys_fields.get('id'))

            return SuccessResponse.get_response_obj(message=response)
        except Exception as exception:
            print exception
            return ErrorHandler.handle_exception(exception)


class DeleteData(APIView):
    parser_classes = (InputParser,)

    @csrf_exempt
    def post(self, request):
        try:
            input_data = InputParser.parse(InputParser(), request.data)
            sys_fields = json.loads(input_data.body).get('sys')
            content_id = json.loads(input_data.body).get('sys').get('contentType').get('sys').get('id')
            response = None
            if content_id == 'places':
                response = DeletePlace.delete_place(sys_fields.get('id'))

            if content_id == 'feedTips':
                response = DeleteTips.delete_tips(sys_fields.get('id'))

            if content_id == 'contributor':
                response = DeleteContributor.delete_contributor(sys_fields.get('id'))

            if content_id =='noteworthy':
                response = DeleteNoteworthy.delete_noteworthy_about(sys_fields.get('id'))

            return SuccessResponse.get_response_obj(message=response)
        except Exception as exception:
            return ErrorHandler.handle_exception(exception)
