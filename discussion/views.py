from django.shortcuts import render
from .models import QA, Answer
from .serializers import QASerializer, AnswerSerializer
from account.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets


class QAViewSet(viewsets.ModelViewSet):
    serializer_class = QASerializer
    queryset = QA.objects.all()

   # def retrieve(self, request, pk=None):
    #    queryset = Image.objects.all()
     #   image = get_object_or_404(queryset, pk=pk)
     #   serializer = ImageSerializer(image)
     #   total_views = r.incr(f'image:{image.id}:views')
     #   r.zincrby('image_ranking', 1, image.id)
     #   return Response(serializer.data)
        
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)
      #  create_action(self.request.user, 'post image', serializer)

    
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = QA.objects.all()
        if self.action == 'list':
            username = self.request.query_params.get('username', None)
            tag = self.request.query_params.get('tag', None)

            if username is not None:
                userID = User.objects.get(username=username)
                queryset = queryset.filter(user=userID)
            elif tag is not None:
                queryset = queryset.filter(tags__name__in=[tag])

        #elif self.action == 'detail':
#            total_views = r.incr(f'image:{image.id}:views')
 #           r.zincrby('image_ranking', 1, image.id)
        return queryset

    


#class LikeView(viewsets.ViewSet):
 #   queryset = Image.objects.all()

  #  def like(self, request, pk):
   #     image = Image.objects.get(id=pk)
    #    image.users_like.add(request.user)
     #   return Response({'message': 'now you like the image'}, status=status.HTTP_200_OK)
        
    
    #def dislike(self, request, pk):
     #   image = Image.objects.get(id=pk)
      #  image.users_like.remove(request.user)
       # return Response({'message': 'now you don\t like the image'}, status=status.HTTP_200_OK)

   

 

    
#class ExplorerView(APIView):
 #   queryset = Image.objects.all()
  #  serializer_class = ImageSerializer

   # def get(self, request, *args, **kwargs):
        
           # get image ranking dictionary
    #    image_ranking = r.zrange('image_ranking', 0, -1, desc=True)
     #   image_ranking_ids = [int(id) for id in image_ranking]
        # get most viewed images
      #  most_viewed = list(Image.objects.filter(
       #                    id__in=image_ranking_ids))
        #most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
        #x = ImageSerializer(most_viewed, many=True)
        #return Response(x.data, status=status.HTTP_200_OK)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    
 
    def perform_create(self, serializer):
        user=self.request.user
        serializer =serializer.save(user=user)

        
    def get_permissions(self):        
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
   