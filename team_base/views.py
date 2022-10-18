from django.shortcuts import render
from team_base.models import TeamBase
from team_base.serializer import TeamBaseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from user_base.models import UserBase
from user_base.serializer import UserBaseSerializer
# Create your views here.


# list all teams
@api_view(['GET'])
def list_teams(requests):
    """
    :return: A json list with the response.
    [
      {
        "name" : "<team_name>",
        "description" : "<some description>",
        "creation_time" : "<some date:time format>",
        "admin": "<id of a user>"
      }
    ]
    """
    teams = TeamBase.objects.all()
    serializer = TeamBaseSerializer(teams,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# add users to team
@api_view(['POST'])
def add_users_to_team(request):
    """
            :param request: A json string with the team details
            {
              "id" : "<team_id>",
              "users" : ["user_id 1", "user_id2"]
            }

            :return:

            Constraint:
            * Cap the max users that can be added to 50
    """
    try:
        team_id = request.data.get('id')
        team = TeamBase.objects.get(pk=team_id)
    except TeamBase.DoesNotExist:
        return Response({'Error':'TEAM_NOT_FOUND'},status = status.HTTP_404_NOT_FOUND)

    T = UserBase.objects.filter(team=team)
    cap = len(T)  # * Cap the max users that can be added to 50

    try:
        user_ids = request.data.get("users")
        for uid in user_ids:
            try:
                user = UserBase.objects.get(pk=uid)
            except UserBase.DoesNotExist:
                return Response({'Error': 'USER_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

            user.team = team
            user.save()
            cap+=1
            if cap >= 50 :
                return Response({'Error': 'MEMBER_LIMIT_EXCEDED'}, status=status.HTTP_201_CREATED)
        return Response({},status = status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'Error': 'Service Unavailable'}, status=status.HTTP_400_BAD_REQUEST)

# remove user from team
@api_view(['POST'])
def remove_users_from_team(request):
    """
            :param request: A json string with the team details
            {
              "id" : "<team_id>",
              "users" : ["user_id 1", "user_id2"]
            }

            :return:

            Constraint:
            * Cap the max users that can be added to 50
    """

    try:
        team_id = request.data.get('id')
        team = TeamBase.objects.get(pk=team_id)
    except TeamBase.DoesNotExist:
        return Response({'Error': 'TEAM_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    T = UserBase.objects.filter(team=team)
    cap = len(T)  # * Cap the max users that can be added to 50

    try:
        user_ids = request.data.get("users")
        for uid in user_ids:
            try:
                user = UserBase.objects.get(pk=uid)
            except UserBase.DoesNotExist:
                return Response({'Error': 'USER_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

            user.team = None
            user.save()
            cap -= 1
            if cap <= 0:
                return Response({'Error': 'MEMBER_LIMIT_EXCEDED'}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'Error': 'Service Unavailable'}, status=status.HTTP_400_BAD_REQUEST)


# list users of a team
@api_view(['POST'])
def list_team_users(request):
    """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<user_id>",
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        ]
    """
    try:
        team_id = request.data.get('id')
        team = TeamBase.objects.get(pk=team_id)
    except TeamBase.DoesNotExist:
        return Response({'Error': 'TEAM_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    try:
        usersQSet = UserBase.objects.filter(team=team)
    except UserBase.DoesNotExist:
        return Response({'Error': 'TEAM_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    if len(usersQSet) > 0:
        serializer = UserBaseSerializer(usersQSet,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({},status= status.HTTP_200_OK)


# update team
@csrf_exempt
@api_view(['PUT'])
def update_team(request):
    """
    :param request: A json string with the team details
    {
      "id" : "<team_id>",
      "team" : {
        "name" : "<team_name>",
        "description" : "<team_description>",
        "admin": "<id of a user>"
      }
    }

    :return:

    Constraint:
        * Team name must be unique
        * Name can be max 64 characters
        * Description can be max 128 characters
    """

    try:
        team_id = request.data.get('id')
        team = TeamBase.objects.get(pk=team_id)
    except TeamBase.DoesNotExist:
        return Response({'Error': 'TEAM_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    team_details = request.data.get('team')

    serializer = TeamBaseSerializer(team,data=team_details)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    else:
        return Response({'Error':'Invalid Input'},status = status.HTTP_400_BAD_REQUEST)

# describe team
@api_view(['POST'])
def describe_team(request):
    """
            :param request: A json string with the team details
            {
              "id" : "<team_id>"
            }

            :return: A json string with the response

            {
              "name" : "<team_name>",
              "description" : "<some description>",
              "creation_time" : "<some date:time format>",
              "admin": "<id of a user>"
            }

            """
    try:
        team_id = request.data.get('id')
        team = TeamBase.objects.get(pk=team_id)
    except TeamBase.DoesNotExist as e:
        return Response({'Error':'Team_NOT_FOUND'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TeamBaseSerializer(team)
    return Response(serializer.data, status=status.HTTP_200_OK)

# create a team

@api_view(['POST'])
def create_team(request):
    """
        :param request: A json string with the team details
        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "admin": "<id of a user>"
        }
        :return: A json string with the response {"id" : "<team_id>"}

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters
    """
    serializer = TeamBaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


