from project_board_base.models import ProjectBoardBase,Task
from project_board_base.serializer import ProjectBoardBaseSerializer,TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from django.db.models import Q
# Create your views here.


# create a board
@api_view(['POST'])
def create_board(request):
    """
    :param request: A json string with the board details.
    {
        "name" : "<board_name>",
        "description" : "<description>",
        "team_id" : "<team id>"
        "creation_time" : "<date:time when board was created>"
    }
    :return: A json string with the response {"id" : "<board_id>"}

    Constraint:
     * board name must be unique for a team
     * board name can be max 64 characters
     * description can be max 128 characters
    """

    serializer = ProjectBoardBaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# list all open boards for a team
@api_view(['GET'])
def list_boards(request):
    """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
    """
    board = ProjectBoardBase.objects.all()
    serializer = ProjectBoardBaseSerializer(board,many=True)
    return Response(serializer.data,status = status.HTTP_200_OK)



# add task to board
@api_view(['POST'])
def add_task(request):
    """
        :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraint:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters

        Constraints:
        * Can only add task to an OPEN board
    """
    # user_id == team_id in create_board
    user_id = request.data.get('user_id')
    print('ggggggggg',user_id)
    QuerySet = ProjectBoardBase.objects.filter(team_id = user_id , status = 'OPEN')

    print('[[[[[[',len(QuerySet))
    if len(QuerySet) <= 0:
        return Response({'Error':'Team Board is invalid or closed'})


    print('======================================================')
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "id" : serializer.data.get('id')},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# update the status of a task
@api_view(['PUT'])
def update_task_status(request):
    """
        :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }
    """
    try:
        task_id = request.data.get('id')
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({'Error': 'Invalid Task id'},status = status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# close a board
@api_view(['POST'])
def close_board(request):
    """
        :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE
    """
    try:
        board = ProjectBoardBase.objects.get(pk = request.data.get("id"))
    except ProjectBoardBase.DoesNotExist:
        return Response({'Error':'Invalid board id'},status = status.HTTP_404_NOT_FOUND)

    #if board id is valid then chek all task under board are complete

    TaskQuerySet = Task.objects.filter(~Q(status='COMPLETE'),user_id=request.data.get("id"))

    if len(TaskQuerySet) >0:
        return Response({'Error':'Incomplete Tasks in board'},status= status.HTTP_400_BAD_REQUEST)
    else:
        board = ProjectBoardBase.objects.get(pk=request.data.get('id'))
        board.status = 'CLOSE'
        board.save()
        serelizer = ProjectBoardBaseSerializer(board)
        return Response(serelizer.data,status = status.HTTP_200_OK)

@api_view(['POST'])
def export_board(request):
    """
        Export a board in the out folder. The output will be a txt file.
        We want you to be creative. Output a presentable view of the board and its tasks with the available data.
        :param request:
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }
    """
    try:
        board = ProjectBoardBase.objects.get(pk=request.data.get('id'))
    except ProjectBoardBase.DoesNotExist:
        return Response({'Error':'Invalid board id'},status = status.HTTP_404_NOT_FOUND)
    board_serializer = ProjectBoardBaseSerializer(board)
    # take all tasks under boards
    TaskQuerySets = Task.objects.filter(user_id=board_serializer.data.get('team_id'))





    name = str(timezone.now())
    with open(f'./out/output_{name}.txt','w') as f:
        f.write('*************************ProjectBoardBase******************************'+'\n')
        f.write(f'Board Id: {board_serializer.data.get("id")}'+'\n')
        f.write(f'Board Name: {board_serializer.data.get("name")}'+'\n')
        f.write(f'Team Id: {board_serializer.data.get("team_id")}'+'\n')
        f.write('******************************Tasks************************************'+'\n')

        for query in TaskQuerySets:
            d = TaskSerializer(query).data
            f.write(f'Task id: {d.get("id")}'+'\n')
            f.write(f'Task title:  {d.get("title")}'+'\n')
            f.write(f'Task description:  {d.get("description")}'+'\n')
            f.write(f'Task Team_id:  {d.get("user_id")}'+'\n')
            f.write(f'Task creation_time:  {d.get("creation_time")}'+'\n')
            f.write(f'Task status:  {d.get("status")}'+'\n')
            f.write('--------------------------------------------------------------------'+'\n'+'\n')

    return Response({
          "out_file" : f"output_{name}.txt"
        },status = status.HTTP_201_CREATED)
