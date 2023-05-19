from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def increase_points_api(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Authentication credentials were not provided.")

    user = request.user
    user.points += 10000
    user.save()
    return Response({'points':user.points})


# @csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def reduce_points_api(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("Authentication credentials were not provided.")

    user = request.user
    points_to_reduce = int(request.POST.get('points', 0))
    if points_to_reduce >= 0 and points_to_reduce <= user.points:
        user.points -= points_to_reduce
        user.save()
    # data = {
    #     'points': user.points
    # }
    # return JsonResponse(data)
    return Response({'points':user.points})

@csrf_exempt
# @permission_classes([AllowAny])
def upload_badge_api(request):
    user = request.user
    badge_image = request.FILES.get('badge')

    if badge_image:
        user.badge = badge_image
        user.save()

    data = {
        'badge' : user.badge.url if user.badge else None
    }
    return JsonResponse(data)




# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import User
# from rest_framework.decorators import permission_classes
# from django.http import HttpResponse


# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def increase_points_api(request):
#     user = request.user
#     user.points += 10000
#     user.save()
#     data = {
#         'points' : user.points
#     }
#     return JsonResponse(data)

# # @csrf_exempt
# # @permission_classes([IsAuthenticated])
# # def increase_points_api(request):
# #     user = request.user
# #     user.points += 10000
# #     user.save()
# #     return HttpResponse(user.points)

# # @csrf_exempt
# # @permission_classes([IsAuthenticated])
# # def reduce_points_api(request):
# #     user = request.user
# #     points_to_reduce = int(request.POST.get('points', 0))
# #     if points_to_reduce > 0 and points_to_reduce <= user.points:
# #         user.points -= points_to_reduce
# #         user.save()
# #     return HttpResponse(user.points)

# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def reduce_points_api(request):
#     user = request.user
#     points_to_reduce = int(request.POST.get('points', 0))
#     if points_to_reduce > 0 and points_to_reduce <= user.points:
#         user.points -= points_to_reduce
#         user.save()
#     data = {
#         'points' : user.points
#     }
#     return JsonResponse(data)

# @csrf_exempt
# def upload_mark_api(request):
#     user = request.user
#     mark_image = request.FILES.get('mark')

#     if mark_image:
#         user.mark = mark_image
#         user.save()

#     data = {
#         'mark' : user.mark.url if user.mark else None
#     }
#     return JsonResponse(data)