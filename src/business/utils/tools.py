
def jsonify_object(obj):
    return dict(obj)


def paginate(obj, per_page):
    def split_list(l_obj, l_per_page): return [l_obj[i:i+l_per_page] for i in range(0, len(l_obj), l_per_page)]
    data = split_list(obj, per_page)

    paginated_data = dict()

    for i in range(len(data)):
        paginated_data[str(i)] = None

    for index, each in enumerate(data):
        paginated_data[str(index)] = each

    return paginated_data
