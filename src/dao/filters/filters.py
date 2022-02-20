
def get_all(table):
    return table.select()


def filter_by(table, field, value):
    filter_dict = dict(
        manufacturer=filter_by_manufacturer,
        model=filter_by_model,
        color=filter_by_color,
        miniature_manufacturer=filter_by_mini_manufacturer,
        pos_x=filter_by_pos_x,
        pos_y=filter_by_pox_y,
        section=filter_by_section,
        rubber_tires=filter_by_rubber_tires
    )

    return filter_dict[field](table, value)


def filter_by_manufacturer(table, value):
    return table.select().filter(table.columns.manufacturer.like(f'%{value}%'))


def filter_by_model(table, value):
    return table.select().filter(table.columns.model.like(f'%{value}%'))


def filter_by_color(table, value):
    return table.select().filter(table.columns.color.like(f'%{value}%'))


def filter_by_mini_manufacturer(table, value):
    return table.select().filter(table.columns.miniature_manufacturer.like(f'%{value}%'))


def filter_by_pos_x(table, value):
    return table.select().filter(table.columns.pos_x == value)


def filter_by_pox_y(table, value):
    return table.select().filter(table.columns.pos_y == value)


def filter_by_section(table, value):
    return table.select().filter(table.columns.section == value)


def filter_by_rubber_tires(table, value):
    return table.select().filter(table.columns.rubber_tires == value)
