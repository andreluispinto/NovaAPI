from rest_framework import serializers
from rest_framework import generics

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = movielist
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = movielist
        fields = min[('producer', 'interval', 'previousWin', 'followingWin')]
        max[('producer', 'interval', 'previousWin', 'followingWin')]

# Create views here.
class MovieList(generics.ListCreateAPIView):

    queryset = movielist.objects.all()
    serializer_class = MovieSerializer