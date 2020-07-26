def tallest_people(**peoples):
    max_value = max(peoples.values())
    result = []
    for key, value in peoples.items():
        if value == max_value:
            result.append(key)
    result.sort()
    # print(result)
    for res in result:
        print(f"{res} : {max_value}")


# print(tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169))