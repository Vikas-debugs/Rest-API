class my(serializers.Serializer):
    zip = serializers.CharField(max_lenght=10)
    city = serializers.CharField(max_lenght=10)
    def __str__(self):
        return 'serializers'