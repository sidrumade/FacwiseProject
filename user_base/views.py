from django.shortcuts import render
from user_base.models import UserBase
from user_base.serializer import UserBaseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from team_base.serializer import TeamBaseSerializer



# Create your views here.


@api_view(['GET'])
def list_user(request):
    """
            :return: A json list with the response
            [
              {
                "name" : "<user_name>",
                "display_name" : "<display name>",
                "creation_time" : "<some date:time format>"
              }
            ]
            """
    users = UserBase.objects.all()
    serializer = UserBaseSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    """
            :param request: A json string with the user details
            {
              "name" : "<user_name>",
              "display_name" : "<display name>"
            }
            :return: A json string with the response {"id" : "<user_id>"}

            Constraint:
                * user name must be unique
                * name can be max 64 characters
                * display name can be max 64 characters
            """
    serializer = UserBaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def describe_user(request):
    """
    :param request: A json string with the user details
    {
      "id" : "<user_id>"
    }

    :return: A json string with the response

    {
      "name" : "<user_name>",
      "description" : "<some description>",
      "creation_time" : "<some date:time format>"
    }

    """
    try:
        user_id = request.data.get('id')
        user = UserBase.objects.get(pk=user_id)
    except UserBase.DoesNotExist as e:
        return Response({'Error':'USER_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserBaseSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['PUT'])
def update_user(request):
    """
            :param request: A json string with the user details
            {
              "id" : "<user_id>",
              "user" : {
                "name" : "<user_name>",
                "display_name" : "<display name>"
              }
            }

            :return:

            Constraint:
                * user name cannot be updated
                * name can be max 64 characters
                * display name can be max 128 characters
            """
    try:
        user_id = request.data.get('id')
        user_data = request.data.get('user')
        user = UserBase.objects.get(pk=user_id)
        user_serializer = UserBaseSerializer(user)

    except UserBase.DoesNotExist as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if user_serializer.data.get('name') != user_data.get('name'):  # * user name cannot be updated
        return Response({"Error":"user name cannot be updated"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserBaseSerializer(user, data=user_data)
    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_user_teams(request):
    """
            :param request:
            {
              "id" : "<user_id>"
            }

            :return: A json list with the response.
            [
              {
                "name" : "<team_name>",
                "description" : "<some description>",
                "creation_time" : "<some date:time format>"
              }
            ]
            """
    try:
        user_id = request.data.get('id')
        user = UserBase.objects.get(pk=user_id)
    except UserBase.DoesNotExist as e:
        return Response({'Error':'USER_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TeamBaseSerializer(user.team)
    return Response(serializer.data, status=status.HTTP_200_OK)


