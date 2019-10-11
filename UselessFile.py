import functools
json = '{\n'
counter = 0
@functools.singledispatch
def json_generator(value):
    type_name = type(value).__name__
    raise TypeError("Unsupported type: " + type_name)

@json_generator.register(list)
def _(value):
    global counter
    counter += 1
    json = '"{}" : "{}"'.format(counter,value) + ',\n'
    return json
@json_generator.register(str)
def _(value):
    global counter
    counter += 1
    json = '"{}" : "{}"'.format(counter,value) + ',\n'
    return json

@json_generator.register(dict)
def _(value):
    global counter
    counter += 1
    value = str(value)
    value = value[:1] + '\n' + value[1:]
    value = value[:len(value)-1] + '\n' + value[len(value)-1:]
    value = value.replace('\'',"\"")
    json = '"{}" : {}'.format(counter,value) + ',\n'
    return json

json += json_generator([1,2])
json += json_generator("wefwef")
json += json_generator([1,7])
json += json_generator({"abn" :"eer"})
print(json[:len(json)-2] + json[len(json)-1:] + '}')
