import requests
from rest_framework import status

from account.services.oauth_service import get_user_by_email
from assessmentplatform.settings import ASSESSMENT_URL


def user_info(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/users/me',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def load_user_profile(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/user-profile',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def edit_user_profile(request):
    response = requests.put(
        ASSESSMENT_URL + 'assessment-core/api/user-profile',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def get_user_id_by_email(email):
    result = get_user_by_email(email)
    if result["Success"] is True:
        return {"Success": True, "body": {"id": result["body"]["id"]}, "status_code": status.HTTP_200_OK}
    elif result["body"]["code"] == "NOT_FOUND":
        return {"Success": False, "body": {"id": ""}, "status_code": status.HTTP_200_OK}
    return result


def update_user_profile_picture(request):
    file = request.data.get('pictureFile')
    response = requests.put(
        ASSESSMENT_URL + 'assessment-core/api/user-profile/picture',
        files={'pictureFile': (file.name, file, file.content_type)},
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
