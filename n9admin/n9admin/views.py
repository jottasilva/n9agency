from .models import Welcome, Idea, Portfolio, ClientArchives
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
#create config welcome
@swagger_auto_schema(
    method='post',
    tags=["Welcome"],
    operation_description="Cria configurações de boas-vindas para o site.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phrase': openapi.Schema(type=openapi.TYPE_STRING, description='Frase principal'),
            'sub_phrase': openapi.Schema(type=openapi.TYPE_STRING, description='Subfrase'),
            'middle_phrase': openapi.Schema(type=openapi.TYPE_STRING, description='Frase intermediária'),
            'desc_phrase': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição da frase'),
            'img': openapi.Schema(type=openapi.TYPE_FILE, description='Imagem do Welcome'),
        },
        required=['phrase', 'sub_phrase', 'middle_phrase', 'desc_phrase', 'img'],
    ),
    responses={
        200: openapi.Response('Welcome criado com sucesso.', examples={"application/json": {"message": "Welcome criado com sucesso!", "id": 1}}),
        400: openapi.Response('Erro de validação.'),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['POST'])
@csrf_exempt
def create_welcome(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    try:
        data = request.POST
        img = request.FILES.get('img')
        required_fields = ['phrase', 'sub_phrase', 'middle_phrase', 'desc_phrase']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'O campo {field} é obrigatório!'}, status=400)
        if not img:
            return JsonResponse({'error': 'O campo img é obrigatório e deve ser um arquivo!'}, status=400)
        welcome = Welcome(
            phrase=data['phrase'],
            sub_phrase=data['sub_phrase'],
            middle_phrase=data['middle_phrase'],
            desc_phrase=data['desc_phrase'],
            img=img
        )
        welcome.save()
        return JsonResponse({'message': 'Welcome criado com sucesso!', 'id': welcome.id}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#create ideia informations
@swagger_auto_schema(
    method='post',
    tags=["Ideia"],
    operation_description="Cria uma nova ideia.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Título da ideia'),
            'msg': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem da ideia'),
            'desc': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição detalhada da ideia'),
        },
        required=['title', 'msg', 'desc'],
    ),
    responses={
        200: openapi.Response('Ideia criada com sucesso.', examples={"application/json": {"message": "Criado com sucesso!", "id": 1}}),
        400: openapi.Response('Erro de validação.'),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['POST'])
@csrf_exempt
def create_idea(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    try:
        data = request.POST
        required_fields = ['title', 'msg', 'desc']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'O campo {field} é obrigatório!'}, status=400)
        idea = Idea(
            title=data['title'],
            msg=data['msg'],
            desc=data['desc'],
        )
        idea.save()
        return JsonResponse({'message': 'Criado com sucesso!', 'id': idea.id}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# get idea informations
@swagger_auto_schema(
    method='get',
    tags=["Ideia"],
    operation_description="Obtém todas as ideias cadastradas.",
    responses={
        200: openapi.Response('Lista de ideias.', examples={"application/json": [{"id": 1, "title": "Ideia A", "msg": "Mensagem A", "desc": "Descrição A"}]}),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['GET'])
def get_ideas(request):
    try:
        ideas = Idea.objects.all().values('id','title','msg','desc')
        ideas_list = list(ideas)
        return JsonResponse(ideas_list, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 
    
#create Porfolio
@swagger_auto_schema(
    method='post',
    tags=["Clients"],
    operation_description="Cria um novo cliente/portfolio.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Título do portfolio'),
            'desc': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição do portfolio'),
            'specs': openapi.Schema(type=openapi.TYPE_STRING, description='Especificações'),
            'img': openapi.Schema(type=openapi.TYPE_FILE, description='Imagem do cliente'),
        },
        required=['title', 'desc', 'specs', 'img'],
    ),
    responses={
        200: openapi.Response('Cliente criado com sucesso.', examples={"application/json": {"message": "Criado com sucesso!", "id": 1}}),
        400: openapi.Response('Erro de validação.'),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['POST'])
@csrf_exempt
def create_client(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    try:
        data = request.POST
        img = request.FILES.get('img')
        required_fields = ['title','desc','specs']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'O campo {field} é obrigatório!'}, status=400)
        portfolio =Portfolio(
            title=data['title'],
            specs=data['specs'],
            img=img,
            desc=data['desc'],
        )
        portfolio.save()
        return JsonResponse({'message': 'Criado com sucesso!', 'id': portfolio.id}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# get clients
@swagger_auto_schema(
    method='get',
    tags=["Clients"],
    operation_description="Obtém a lista de clientes/portfolios cadastrados.",
    responses={
        200: openapi.Response('Lista de portfolios.', examples={"application/json": [{"id": 1, "title": "Cliente A", "desc": "Descrição A", "specs": "Specs A"}]}),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['GET'])
def get_clients(request):
    try:
        clients = Portfolio.objects.all().values('id','title','img','desc','created_at','specs')
        clients_list = list(clients)
        return JsonResponse(clients_list, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 
            
# get welcome informations
@swagger_auto_schema(
    method='get',
    tags=["Welcome"],
    operation_description="Obtém as configurações de boas-vindas cadastradas.",
    responses={
        200: openapi.Response('Lista de boas-vindas.', examples={"application/json": [{"id": 1, "phrase": "Bem-vindo", "sub_phrase": "Olá"}]}),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['GET'])
def get_welcome(request):
    try:
        welcomes = Welcome.objects.all().values('id','phrase', 'sub_phrase', 'middle_phrase','img','desc_phrase','created_at')
        welcomes_list = list(welcomes)
        return JsonResponse( welcomes_list,safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# get images media
@swagger_auto_schema(
    method='get',
    operation_description="Serve arquivos de mídia estáticos.",
    manual_parameters=[
        openapi.Parameter('path', openapi.IN_PATH, description='Caminho do arquivo de mídia', type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response('Arquivo encontrado e retornado.'),
        404: openapi.Response('Arquivo não encontrado.')
    }
)
@api_view(['GET'])
def serve_media(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg, image/svg")  
    else:
        return HttpResponse("Imagem não encontrada", status=404)

#create client paste
@swagger_auto_schema(
    method='post',
    tags=["Clients"],
    operation_description="Cria um novo cliente",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Título do arquivo'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição do arquivo'),
            'specifications': openapi.Schema(type=openapi.TYPE_STRING, description='Especificações'),
            'email': openapi.Schema(type=openapi.TYPE_FILE, description='Imagem do cliente'),
            'archive': openapi.Schema(type=openapi.TYPE_FILE, description='Arquivo do cliente'),
        },
        required=['title', 'description', 'specifications', 'email','archive'],
    ),
    responses={
        200: openapi.Response('Arquivo criado com sucesso.', examples={"application/json": {"message": "Criado com sucesso!", "id": 1}}),
        400: openapi.Response('Erro de validação.'),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['POST'])
@csrf_exempt
def create_archive(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    try:
        data = request.POST
        required_fields = ['title', 'description', 'specifications', 'email','archive']
        for field in required_fields:
            if field not in data:
                return JsonResponse({'error': f'O campo {field} é obrigatório!'}, status=400)
        archive = ClientArchives(
            title=data['title'],
            specifications=data['specifications'],
            description=data['description'],
            email=data['email'],
            archive=data['archive']
        )
        archive.save()
        return JsonResponse({'message': 'Criado com sucesso!', 'id': archive.id}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# get client archives
@swagger_auto_schema(
    method='get',
    tags=["Clients"],
    operation_description="Obtém os arquivos de usuario especifico.",
    responses={
        200: openapi.Response('Lista de arquivos.', examples={"application/json": [{"id": 1, "phrase": "Bem-vindo", "sub_phrase": "Olá"}]}),
        500: openapi.Response('Erro interno do servidor.')
    }
)
@api_view(['GET'])
def get_archives(request):
    try:
        email = request.GET.get('email') 
        if not email:
            return JsonResponse({'error': 'O campo email é obrigatório!'}, status=400)
        archives = ClientArchives.objects.filter(email=email).values('id', 'title', 'description', 'specifications', 'created_at', 'archive', 'email')
        archives_list = list(archives)
        return JsonResponse(archives_list, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)