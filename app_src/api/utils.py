def update_object(instance, validated_data):
    for key, value in validated_data.items():
        setattr(instance, key, value)
    instance.save()
    return instance
